from django.db import models
from django.contrib.auth.models import User
from students.models import Student
from books.models import Book
from django.utils import timezone

class NoteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=7, default='#007bff')  # Hex color code
    
    class Meta:
        verbose_name_plural = "Note Categories"
    
    def __str__(self):
        return self.name

class Note(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_public = models.BooleanField(default=False)
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['priority']),
            models.Index(fields=['category']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.category.name}"
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

class Attachment(models.Model):
    note = models.ForeignKey(Note, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='note_attachments/')
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(default=timezone.now)
    file_size = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.filename} - {self.note.title}"
