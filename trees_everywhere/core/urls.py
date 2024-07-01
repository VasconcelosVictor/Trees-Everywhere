
from django.urls import path
from . import views, viewsets

urlpatterns = [
    # User
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('users_list/', views.users_list, name='users_list'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    # account
    path('create_account/', views.create_account, name='create_account'),
    path('account_list/', views.account_list, name='account_list'),
    path('account_detail/<int:id>/', views.account_detail, name='account_detail'),
    path('account_delete/<int:id>/', views.account_delete, name='account_delete'),
    path('edit_account/<int:id>/', views.edit_account, name='edit_account'),
    path('update_status/<int:id>/', views.update_status, name='update_status'),
    path('ajax_change_account/', views.change_account, name='change_account'),
    # Profile
    
    path('profile/', views.profile, name='profile'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),

    # Tree
    path('home/', views.home , name='home'),
    path('trees/', views.user_trees, name='user_trees'),
    path('edit_tree/<int:id>/', views.edit_tree, name='edit_tree'),
    path('tree_detail/<int:pk>/', views.tree_detail, name='tree_detail'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('add_tree/', views.add_tree, name='add_tree'),
    path('delete_tree/<int:id>/', views.delete_tree, name='delete_tree'),

    # API METHODS
    path('api/v1/trees/', viewsets.UserPlantedTreesList.as_view(), name='user_planted_trees_api'),
]
