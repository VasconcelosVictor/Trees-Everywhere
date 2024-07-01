from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .decotetor import *


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            account = form.cleaned_data.get('account')
            request.session['active_account_id'] = account.id
            request.session.save()
            login(request, user)
            
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request) 
    return redirect('login') 

@login_required
@permission_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            accounts = form.cleaned_data['account']
           
            for account in accounts:    
                account.users.add(user)  # add user in account
            # Profile create
            profile = Profile()
            profile.user = user
            profile.bio = form.cleaned_data['bio']
            profile.save()
            user.save()
            
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(error)

    else:
        form = CustomUserCreationForm()
    return render(request, 'adm_register.html', {'form': form})

@login_required
@permission_required
def users_list(request):
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'adm_users_list.html', {'users': users})

@login_required
@permission_required
def delete_user(request,id):
    user = get_object_or_404(CustomUser, pk=id)
    user.delete()
    return redirect('users_list')


@login_required
@permission_required
def create_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect('account_list') 
    else:
        form = AccountCreationForm() 
    return render(request, 'adm_create_account.html', {'form': form})

@login_required
@permission_required
def edit_account(request, id):
    account = get_object_or_404(Account, pk=id)

    if request.method == 'POST':
        form = AccountCreationForm(request.POST, account=account)
        if form.is_valid():
            account.name = form.cleaned_data['name']
            users = form.cleaned_data['users']
            account.users.set(users)
            account.save()
            return redirect('account_list') 
    else:
        form = AccountCreationForm(account=account) 
    return render(request, 'adm_create_account.html', {'form': form, 'account': account})


@login_required
@permission_required
def account_list(request):
    accounts = Account.objects.all().order_by('id')
    
    return render(request, 'adm_account_list.html', {'accounts' :accounts,})

@login_required
@permission_required
def account_detail(request, id):
    account = get_object_or_404(Account, pk=id)
    users = account.users.all()

    return render(request, 'adm_account_detail.html', {'account' : account, 'users': users})

@login_required
@permission_required
def update_status(request,id):
    account = get_object_or_404(Account, pk=id)
    if account.active:
        account.active = False
    else:
        account.active = True
    account.save()
    return redirect('account_list')

@login_required
@permission_required    
def account_delete(request,id):
    account = get_object_or_404(Account, pk=id)
    account.delete()
    return redirect('account_list')

def change_account(request):
    account = request.GET.get('account')
    account = Account.objects.get(id=int(account))
    request.session['active_account_id'] = account.id
    print(account)

    return JsonResponse({'success': True}, status=200)


# PROFILE
@login_required
@permission_required
def profile(request):

    user = request.user
    account  = Account.objects.get(id=int(request.session['active_account_id']))
    profile = user.get_profile()
    trees = PlantedTree.objects.filter(user=user)
    count = trees.count()
    
    return render(request, 'profile.html' , {'user':user, 'profile': profile,'count': count, 'account': account})

@login_required
@permission_required
def edit_profile(request,id=None):
    user = get_object_or_404(CustomUser, pk=id)
    account  = Account.objects.get(id=int(request.session['active_account_id']))
    
    if request.method == "POST":
        form = ProfileForm(request.POST, user=user)
        if form.is_valid():
            profile = user.get_profile()
            if profile == None:
                profile = Profile()
                profile.user = user
            profile.bio = form.cleaned_data['bio']
            profile.save()
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            accounts = form.cleaned_data['accounts']
            user.accounts.set(accounts)
            user.save()
            return redirect(reverse('profile'))
        else:
            for error in list(form.errors.values()):
                print(error)
    else:
        form = ProfileForm(user=user)       

    return render(request, 'edit_profile.html', {'form': form, 'user': user, 'account' : account})

@login_required
@permission_required
def create_profile(request,id,id_profile=None ):
    user = get_object_or_404(CustomUser, pk=id)
    profile = get_object_or_404(Profile, pk=id_profile)
    if request.method == "POST":
        form = ''
        if form.is_valid():
            if profile == None:
                profile = Profile()

            profile.user = user
            profile.bio = ''
            profile.save()

    return render(request, 'adm_profile.html', {})

#  Trees views 
@login_required
@permission_required
def home(request):
    
    account  = Account.objects.get(id=int(request.session['active_account_id']))
    trees = PlantedTree.objects.filter(user=request.user ).order_by('plant')
    count = trees.count()


    paginator = Paginator(trees, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)

    return render(request, 'user_trees.html', {'page_obj': page_obj,'count': count})

@login_required
@permission_required
def add_plant(request):
    name = request.GET.get('name')
    scientific_name = request.GET.get('scientific_name')
    plant = Plant.objects.create(name=name, scientific_name= scientific_name)
    plant.save()

    return JsonResponse({'success':'success'})


@login_required
@permission_required
def add_tree(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            tree = form.cleaned_data['name']
            latitude = float(form.cleaned_data['latitude'])
            longiture = float(form.cleaned_data['longiture'])
            user = request.user
            account = Account.objects.get(id=int(request.session['active_account_id']))
            planted_tree = user.plant_tree(tree,(latitude,longiture), account)
            planted_tree.age = form.cleaned_data['age']
           
            planted_tree.save()
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(error)

    else:
        form = PlantForm()
    return render(request, 'add_tree.html', {'form': form})

@login_required
@permission_required
def user_trees(request):
    user = request.user
    account = Account.objects.get(id=int(request.session['active_account_id']))
    
    if user.is_superuser:
        trees = PlantedTree.objects.all()
    else:
        trees = PlantedTree.objects.filter(account__in=user.accounts.all()).order_by('plant') 
        
    count = trees.count()
    paginator = Paginator(trees, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)

    return render(request, 'all_trees.html', {"user": user, "page_obj":page_obj,'count': count, 'account': account })

@login_required
@permission_required
def tree_detail(request, pk):
    user = request.user
    acccount = Account.objects.get(id=int(request.session['active_account_id']))
    tree = get_object_or_404(PlantedTree, pk=pk)
    planted_tree = PlantedTree.objects.filter(plant=tree.plant, account__in=user.accounts.all()).order_by('-planted_at')

    if tree.user.id != user.id:
        return render(request, '403_template.html', status=403)
    
    count = planted_tree.count()
    paginator = Paginator(planted_tree, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)

    return render(request, 'tree_detail.html', {'tree': tree, 'page_obj': page_obj, 'count': count})

@login_required
@permission_required
def edit_tree(request,id):
    tree = get_object_or_404(PlantedTree, pk=id)
    if request.method == "POST":
        form = PlantForm(request.POST, tree=tree)
        if form.is_valid():

            tree.age = form.cleaned_data['age']
            tree.latitude = form.cleaned_data['latitude']
            tree.longiture = form.cleaned_data['longiture']
            tree.save()

            return redirect( reverse('tree_detail',args=[tree.id]))
    else:
        form = PlantForm( tree=tree)

    return render(request, 'edit_tree.html', {'form': form, 'tree': tree})


@login_required
def delete_tree(request,id):
    tree = PlantedTree.objects.get(id=id)

    tree.delete()
    return redirect('home')





