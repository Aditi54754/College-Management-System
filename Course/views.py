from django.shortcuts import render,redirect
from .models import Subject,Course,Enrollment
from .forms import SubjectForm,EnrollmentForm
from .serializers import SubjectSerializer,CourseSerializer,EnrollmentSerializer
from rest_framework import viewsets



class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentModelViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer




# Create your views here.

def subject_list(request):
    subject = Subject.objects.all()
    return render(request,'subject_list.html',{'subject':subject})

def add_subject(request):
    form = SubjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Subject_list')
    
    return render(request,'add_subject.html',{'form':form})

def edit_subject(request,id):
    subject = Subject.objects.get(id=id)
    form = SubjectForm(request.POST or None,instance=subject)

    if form.is_valid():
        form.save()
        return redirect('Subject_list')
    
    return render(request,'add_subject.html',{'form':form})

def delete_subject(request,id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect('Subject_list')


# Enrollment Table Views Inherit Table Course And Student

def enrollment_list(request):
    enrollment = Enrollment.objects.all()
    return render(request,'Enrollment_list.html',{'enrollment':enrollment})


def add_enrollment(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Enrollment_list')
    return render(request,'Enrollment.html',{'form':form})


def edit_enrollment(request,id):
    enrollment = Enrollment.objects.get(id=id)
    form = EnrollmentForm(request.POST or None,instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect('Enrollment_list')
    return render(request,'Enrollment.html',{'form':form})

def delete_enrollment(request,id):
    enrollment = Enrollment.objects.get(id=id)
    enrollment.delete()
    return redirect('Enrollment_list')







    
    



