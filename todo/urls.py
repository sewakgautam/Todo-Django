from django.contrib import admin
from django.urls import path, include
from . views import index , Logout_view, Login, todo , todo_add

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('todo/', todo.as_view(), name='todo'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout_view, name='logout'),
    path('todo_add/', todo_add.as_view(), name='todo_add'),
    
]
