from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from .models import Account, Plant, PlantedTree

CustomUser = get_user_model()

class TreesEverywhereTestCase(TestCase):
    def setUp(self):
       
        self.account1 = Account.objects.create(name="Account 1")
        self.account2 = Account.objects.create(name="Account 2")

        # 
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass')
        self.user3 = CustomUser.objects.create_user(username='user3', password='pass')

        # 
        self.account1.users.add(self.user1, self.user2)
        self.account2.users.add(self.user2, self.user3)

        #
        self.plant1 = Plant.objects.create(name="Plant 1", scientific_name="Plantus One")
        self.plant2 = Plant.objects.create(name="Plant 2", scientific_name="Plantus Two")

        # 
        self.tree1 = PlantedTree.objects.create(user=self.user1, plant=self.plant1, latitude=10.0, longiture=20.0, account=self.account1)
        self.tree2 = PlantedTree.objects.create(user=self.user2, plant=self.plant2, latitude=15.0, longiture=25.0, account=self.account1)
        self.tree3 = PlantedTree.objects.create(user=self.user3, plant=self.plant1, latitude=20.0, longiture=30.0, account=self.account2)
        self.all_trees = PlantedTree.objects.filter(account__in=self.user2.accounts.all())
        
        # Session Config
        session = self.client.session
        session['active_account_id'] = self.account1.id
        session.save()



    def test_user_tree_listing_template(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_trees.html')
        self.assertContains(response, self.tree1.plant.name)
        self.assertNotContains(response, self.tree2.plant.name)

    def test_access_another_user_trees_forbidden(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tree_detail', kwargs={'pk': self.tree3.pk}))
        self.assertEqual(response.status_code, 403)

    def test_account_trees_listing_template(self):
        self.client.force_login(self.user2)
        session = self.client.session
        session['active_account_id'] = self.account2.id
        session.save()
        
        response = self.client.get(reverse('user_trees'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_trees.html')
        self.assertContains(response, self.tree1.plant.name)
        self.assertContains(response, self.tree2.plant.name)
        self.assertContains(response, self.tree3.plant.name)

    def test_plant_tree_method(self):
        user = CustomUser.objects.create_user(username='testuser', password='pass')
        account = Account.objects.create(name="Test Account")
        account.users.add(user)
        plant = Plant.objects.create(name="Test Plant", scientific_name="Plantus Testus")
        tree = user.plant_tree(plant, (30.0, 40.0), account)
        self.assertIsInstance(tree, PlantedTree)
        self.assertEqual(tree.user, user)
        self.assertEqual(tree.plant, plant)
        self.assertEqual(tree.account, account)
        self.assertEqual(tree.latitude, 30.0)
        self.assertEqual(tree.longiture, 40.0)

    def test_plant_trees_method(self):
        user = CustomUser.objects.create_user(username='testuser2', password='pass')
        account = Account.objects.create(name="Test Account 2")
        account.users.add(user)
        plant = Plant.objects.create(name="Test Plant 2", scientific_name="Plantus Testus 2")
        plantings = [(plant, (30.0, 40.0)), (plant, (35.0, 45.0))]
        user.plant_trees(plantings, account)
        self.assertEqual(PlantedTree.objects.filter(user=user).count(), 2)
        tree1 = PlantedTree.objects.get(user=user, latitude=30.0, longiture=40.0)
        tree2 = PlantedTree.objects.get(user=user, latitude=35.0, longiture=45.0)
        self.assertEqual(tree1.plant, plant)
        self.assertEqual(tree2.plant, plant)
        self.assertEqual(tree1.account, account)
        self.assertEqual(tree2.account, account)
