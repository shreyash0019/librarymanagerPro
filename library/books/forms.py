from django import forms
from django.contrib.auth.models import User
from .models import Book, Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'quantity']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    student_id = forms.CharField(max_length=20)
    department = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Student.objects.create(user=user, student_id=self.cleaned_data['student_id'], department=self.cleaned_data['department'])
        return user
