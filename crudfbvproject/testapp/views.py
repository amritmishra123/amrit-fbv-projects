from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def retrieve_view(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/index.html', {'employees': employees})


def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():

            form.save()
        return redirect('/')
    return render(request, 'testapp/create.html', {'form': form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    print('Do you want to delete!!!')
    employee.delete()
    return redirect('/')
    #return render(request,'testapp/delete.html')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'employee':employee})

