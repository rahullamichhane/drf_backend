from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Science", "Fiction"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    publish_year = models.IntegerField()
    publication_name = models.CharField(max_length=100)
    for_class = models.CharField(max_length=10, default='10')
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return f"{self.title} ({self.author.name})"
