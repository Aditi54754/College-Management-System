from django.shortcuts import render,redirect
from .models import Attendance
from .forms import AttendanceForm
from .serializers import AttendanceSerializer
from rest_framework import viewsets



class AttendanceModelViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Create your views here.

# ATTENDANCE TABLE VIEW

def attendance_list(request):
    attendance = Attendance.objects.all()
    return render (request,'attendance_list.html',{'attendance':attendance})


def add_attendance(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Attendance_list')
    return render(request,'add_attendance.html',{'form':form})



def edit_attendance(request,id):
    attendance = Attendance.objects.get(id=id)
    form = AttendanceForm(request.POST or None,instance=attendance)
    if form.is_valid():
        form.save()
        return redirect('Attendance_list')
    return render(request,'attendance_list.html',{'form':form})

def delete_attendance(request,id):
    attendance = Attendance.objects.get(id=id)
    attendance.delete()
    return redirect('Attendance_list')
    


