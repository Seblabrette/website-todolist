from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('login/', views.userLogin, name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('register/', views.userRegister, name='userRegister'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('detail/<int:list_id>/', views.detailView, name='detailview'),
    path('createlist/', views.createlist, name='createlist'),
    path('delete-list/', views.delete_list, name='delete-list'),
    path('rename-list/<int:list_id>/', views.rename_list, name='rename-list'),
    path('delete-item/', views.delete_item, name='delete-item'),
    path('create-item/', views.create_item, name='create-item'),
    path('modify-item/', views.modify_item, name='modify-item'),
]
