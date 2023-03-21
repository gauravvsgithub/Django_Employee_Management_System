from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        department = int(request.POST['department'])
        role = int(request.POST['role'])

        new_emp = Employee(first_name=fname, last_name=lname, salary=salary, bonus=bonus, phone=phone,
                           dept_id=department, role_id=role,
                           hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully!')
    else:
        print('No')
    return render(request, 'add_emp.html')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            employee_to_be_removed = Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse('Employee removed successfully!')
        except:
            return HttpResponse('Enter valid Employee Id')
    emps = Employee.objects.all();
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    return render(request, 'filter_emp.html')
