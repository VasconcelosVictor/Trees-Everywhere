from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *

class SetupTestData(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criar usuários
        cls.user1 = CustomUser.objects.create_user(username='user1', password='test')
        cls.user2 = CustomUser.objects.create_user(username='user2', password='test')
        cls.user3 = CustomUser.objects.create_user(username='user3', password='test')

        # Criar contas e associar usuários
        cls.account1 = Account.objects.create(name='Account 1', active=True)
        cls.account1.users.add(cls.user1, cls.user2)

        cls.account2 = Account.objects.create(name='Account 2', active=True)
        cls.account2.users.add(cls.user3)

        # Criar plantas
        cls.plant1 = Plant.objects.create(name='Plant 1')
        cls.plant2 = Plant.objects.create(name='Plant 2')

        # Criar árvores plantadas
        cls.tree1 = PlantedTree.objects.create(user=cls.user1, plant=cls.plant1)
        cls.tree2 = PlantedTree.objects.create(user=cls.user1, plant=cls.plant2)
        cls.tree3 = PlantedTree.objects.create(user=cls.user2, plant=cls.plant1)
        cls.tree4 = PlantedTree.objects.create(user=cls.user3, plant=cls.plant2)

class TemplateViewTests(SetupTestData):
    def test_planted_trees_view(self):
        self.client.login(username='user1', password='test')
        response = self.client.get(reverse('planted_trees'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planted_trees.html')
        self.assertContains(response, 'Plant 1')
        self.assertContains(response, 'Plant 2')



