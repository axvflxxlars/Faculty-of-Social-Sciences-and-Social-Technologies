from django.shortcuts import render, get_object_or_404
from .models import Specialty, Department, HomePageContent, ExchangeProgram

def home(request):
    content = HomePageContent.objects.first()
    return render(request, "faculty/home.html", {'content': content})

def program_list(request):
    bachelors = Specialty.objects.filter(degree='bachelor')
    masters = Specialty.objects.filter(degree='master')
    phds = Specialty.objects.filter(degree='phd')
    return render(request, 'faculty/program_list.html', {
        'bachelors': bachelors,
        'masters': masters,
        'phds': phds
    })

def program_detail(request, pk):
    program = get_object_or_404(Specialty, pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': program})

def department_list(request):
    departments = Department.objects.prefetch_related('specialties').all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'faculty/department_detail.html', {'department': department})

def exchange_list(request):
    programs = ExchangeProgram.objects.all().order_by('deadline')
    return render(request, 'faculty/exchange_list.html', {'programs': programs})
