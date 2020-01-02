from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path('borrowed/', views.AllLoanedBooksListView.as_view(), name='all-borrowed'),
]

urlpatterns +=[
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew_bymodelform/', views.renew_book_librarian_modelform, name='renew-book-librarian-modelform'),
]

#modelform實做範例
#Author資料利用modelform快速建立create, update, delete功能
#modelform的快速建立功能相當類似asp.net mvc的skeleton
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
]