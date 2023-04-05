from django.urls import path, re_path

from . import views
# app_name="books"
urlpatterns = [
    path('',views.BookList.as_view(), name="books"),
    path('book/<slug:pk>', views.ShowPost.as_view(), name="book"),    
    path('authors/', views.authors, name="authors"),
    path('publishers/', views.publishers, name="publishers"),
    path('edit_project/<str:pk>', views.editProject, name='edit_project'), 
    path('create_project/', views.CreateProject.as_view(), name="create_project"),
    path('create_publisher/', views.CreatePublisher.as_view(), name='create_publisher'), 
    path('create_author/', views.CreateAuthor.as_view(), name="create_author"), 
    path('edit_publisher/<str:pk>', views.editPublisher, name='edit_publisher'), 
    path('edit_author/<str:pk>', views.editAuthor, name='edit_author'), 
    path('delete_book/<str:pk>', views.deleteBook, name='delete_book'), 
    path('delete_author/<str:pk>', views.deleteAuthor, name='delete_author'), 
    path('delete_publisher/<str:pk>', views.deletePublisher, name='delete_publisher'),
    path('login/', views.LoginUser.as_view(), name='login'), 
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.RegisterUser.as_view(), name='register')


    ]
 
