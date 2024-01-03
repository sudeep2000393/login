# myapp/urls.py

from django.urls import path
from . import views  # Correct the import statement
from .views import login, display_marks

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    path('success/', views.success, name='success'),
    path('user/', views.user, name='user'),
    path('login/', login, name='login'),
    path('display_marks/<int:student_id>/', display_marks, name='display_marks'),


    
]






