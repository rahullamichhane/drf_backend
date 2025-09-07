from django.urls import path
from . import views

urlpatterns = [
    # Notes
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    
    # Students
    path("students/", views.StudentListCreateView.as_view(), name="student-list-create"),
    path("students/<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name="student-detail"),
    
    # Books
    path("books/", views.BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", views.BookRetrieveUpdateDestroyView.as_view(), name="book-detail"),
    
    # Contact
    path("contacts/", views.ContactListCreateView.as_view(), name="contact-list-create"),
]
