from django.urls import path,include
from . import views
from rest_framework.routers import  DefaultRouter


router = DefaultRouter()

router.register('attendanceapi',views.AttendanceModelViewSet)

urlpatterns = [

    
    # ATTENDACE TABLE URLS
    path('',include(router.urls)),
    path('attendance_list/', views.attendance_list, name = 'Attendance_list'),
    path('attendance_add/', views.add_attendance, name='Add_Attendance'),
    path('attendance_edit/<id>', views.edit_attendance, name='Edit_Attendance'),
    path('attendance_delete/<id>', views.delete_attendance, name='Delete_Attendance'),
     
]