from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import *
from books.form import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

posts = Books.objects.all()


class BookList(DataMixin, ListView):
    model=Books
    template_name = 'books/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list =None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return context | c_def


# def index(request):
#     posts = Books.objects.all()
#     con = {
#         'posts': posts,
#         'title': 'Главная страница'
#     }
#     return render(request, 'books/index.html', context=con)


def books(request):
    posts = Books.objects.all()
    return render(request, 'books/index.html', {'posts': posts})

 
# def show_book(request, book_id):
#     book = Books.objects.get(pk=book_id)
#     return render(request, 'books/single_project.html', {'book':book})

class ShowPost(DataMixin, DetailView):
    model = Books
    template_name = 'books/single_project.html'
    int_url_kwarg = 'pk'
    context_object_name = 'book'

    def get_context_data(self, *, object_list =None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['book'])
        return context | c_def
    

def authors(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.html', {'posts': authors})

def publishers(request):
    posts = Publisher.objects.all()
    return render(request, 'books/publishers.html', {'posts': posts})

@login_required(login_url='/admin/')
def editProject(request, pk):
    project = Books.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method=="POST":
        print(request.POST)
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('books')
            
    context = {'form': form}
    return render(request, 'books/project_form.html', context)

# def createProject(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('books')
#     context = {'form': form}
#     return render(request, 'books/project_form.html', context)

class CreateProject(LoginRequiredMixin, DataMixin, CreateView):
    form_class = ProjectForm
    template_name = 'books/project_form.html'
    success_url = reverse_lazy('books')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Create New Book")
        return context | c_def

# def createPublisher(request):
#     form = PublisherForm()
#     if request.method=="POST":
#         print(request.POST)
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('publishers')
#     context = {'form': form}
#     return render(request, 'books/publisher_form.html', context)

class CreatePublisher(LoginRequiredMixin, DataMixin, CreateView):
    form_class = PublisherForm
    template_name = 'books/publisher_form.html'
    success_url = reverse_lazy('publishers')
    login_url = reverse_lazy('login')
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Create New Publisher")
        return context | c_def


@login_required(login_url='login')
def editPublisher(request, pk):
    project = Publisher.objects.get(id=pk)
    form = PublisherForm(instance=project)
    if request.method=="POST":
        print(request.POST)
        form = PublisherForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('publishers')
            
    context = {'form': form}
    return render(request, 'books/publisher_form.html', context)



# def createAuthor(request):
#     form = AuthorForm()
#     if request.method=="POST":
#         print(request.POST)
#         form = AuthorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('authors')
#     context = {'form': form}
#     return render(request, 'books/author_form.html', context)


class CreateAuthor(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('authors')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Create New Author")
        return context | c_def
    
    
@login_required(login_url='login')
def editAuthor(request, pk):
    project = Author.objects.get(id=pk)
    form = AuthorForm(instance=project)
    if request.method=="POST":
        print(request.POST)
        form = AuthorForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('authors')
            
    context = {'form': form}
    return render(request, 'books/author_form.html', context)


@login_required(login_url='login')
def deleteBook(request, pk):
    project = Books.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('books')
    context = {'project':project}
    return render(request, 'books/delete.html',context)


@login_required(login_url='login')
def deleteAuthor(request, pk):
    project = Author.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('authors')
    context = {'project':project}
    return render(request, 'books/delete_author.html',context)


@login_required(login_url='login')
def deletePublisher(request, pk):
    project = Publisher.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('publishers')
    context = {'project':project}
    return render(request, 'books/delete_publisher.html',context)

# def login(request):
#     return HttpResponse('LOGIN')

def register(request):
    return HttpResponse('REGISTER')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')


    def get_context_data(self, *, object_list =None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Register')
        return context | c_def
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('books')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'books/login.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list =None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Authentication')
        return context | c_def

    def get_success_url(self) -> str:
        return reverse_lazy('books')
    

def logout_user(request):
    logout(request)
    return redirect('login')