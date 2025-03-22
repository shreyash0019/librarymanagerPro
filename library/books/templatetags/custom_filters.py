from django import template
from books.models import Student

register = template.Library()

@register.filter
def get_student_id(user):
    student = Student.objects.filter(user=user).first()
    return student.id if student else None
