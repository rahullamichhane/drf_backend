from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password"]
        extra_kwargs = {"password":{"write_only": True}}
        
    def create(self,validated_date):
        print(validated_date)
        user = User.objects.create_user(**validated_date)
        return user
    
    
# Note
class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","tittle","content","created_at","author"]
        extra_kwargs = {"author":{"read_only":True}}

# Student and Book serializers
from students.models import Student, ClassCategory
from books.models import Book, Author, BookCategory
from registration.models import Contact

class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
