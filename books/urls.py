from django.urls import path
from .views import book_list, book_add, book_edit, book_delete

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', book_add, name='book_add'),
    path('edit/<int:pk>/', book_edit, name='book_edit'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
]
