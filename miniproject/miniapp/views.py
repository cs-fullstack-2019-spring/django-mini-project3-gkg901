from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TeacherModel
from .forms import NewTeacherForm


# ===================SUPERUSER: ADMIN   PASS:test4321============================
# Create your views here.

# GRABS ALL OBJECTS WITHIN TEACHERMODEL AND INJECTS THEM INTO INDEX.HTML
def index(request):
    allTeachers = TeacherModel.objects.all()
    return render(request, 'miniapp/index.html', {'teacherlist': allTeachers})


# USES FORM TO CREATE ENTRIES
def create(request):
    newForm = NewTeacherForm(request.POST or None)
    if newForm.is_valid():
        newForm.save()
        return redirect('index')
    return render(request, 'miniapp/create.html', {'teacherform': newForm})


# EDITS AN ENTRY USING ID PASSED FROM URL
def edit(request, id):
    print('+++++++++++++++++++++++++')
    teacher = get_object_or_404(TeacherModel, pk=id)
    print(teacher.id)
    edit_teacher = NewTeacherForm(request.POST or None, instance=teacher)
    if edit_teacher.is_valid():
        edit_teacher.save()
        return redirect('index')
    return render(request, 'miniapp/create.html', {'teacherform': edit_teacher})


# DELETES AN ENTRY USING ID PASSED FROM URL
def delete(request, id):
    teacher = get_object_or_404(TeacherModel, pk=id)
    if request.method == "POST":
        teacher.delete()
        return redirect('index')
    return render(request, 'miniapp/delete.html', {'selectedteacher': teacher})

# FAILED FILTER ATTEMPT :((
# def teacher(request, id):
#     teacher = TeacherModel.objects.filter(name=)
