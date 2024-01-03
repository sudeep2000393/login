# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.contrib.auth.decorators import login_required

@csrf_exempt 



def add_employee(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or wherever you want
    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})

def success(request):
    return render(request, 'success.html')

@csrf_exempt 
def user(request):
    return render(request, 'user.html')

@login_required
def login(request):
    student_id = request.user.student.id  # Assuming a one-to-one relationship between User and Student
    return render(request, 'student_details.html', {'student_id': student_id})

# views.py

from django.shortcuts import render, get_object_or_404
from .models import Student

def display_marks(request, student_id):
    # Retrieve the student object or return a 404 error if not found
    student = get_object_or_404(Student, id=student_id)

    # Assuming you have a 'marks' attribute in your Student model
    marks = student.marks.all()

    # You can modify the above query based on your actual model structure

    context = {
        'student': student,
        'marks': marks,
    }

    return render(request, 'display_marks.html', context)
