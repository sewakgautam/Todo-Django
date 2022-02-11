from pipes import Template
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import TemplateView, FormView , CreateView , ListView, DeleteView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import login_form
import datetime
from . models import Todo
# Create your views here.

class Login(FormView):
    template_name = 'todo/login.html'
    redirect_authenticated_user = True
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo')
        return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'todo/todo.html')
            return HttpResponse('Invalid login details supplied.')
    def get(self, request, *args, **kwargs):
        form = login_form()
        return render(request, 'todo/login.html', {'form': form})

def Logout_view(request):
    logout(request)
    return HttpResponse('You Gyz successfully logout')

class index(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    model = Todo
    fields = ['title', 'text']
    template_name = 'todo/index.html'
    success_url = '/todo/'
    
    #if user is login redirect to todo page
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo')
        return super(index, self).dispatch(request, *args, **kwargs)
class todo(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'todo/todo.html'
    model = Todo
    context_object_name = 'todos'


    def post(self, request , *args, **kwargs):
        if request.method == 'POST':
            todo = Todo.objects.get(id=request.POST['id'])
            todo.delete()
            return redirect('todo')
        return render(request, 'todo/todo.html')

class todo_add(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Todo
    fields = ['title', 'text']
    template_name = 'todo/add_todo.html'
    success_url = '/todo/'

class Delete_todo(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todo/'
    template_name = 'todo/todo.html'

    
