from django.urls import path,include
from . import views
from rest_framework.routers import  DefaultRouter


router = DefaultRouter()

router.register('subjectapi',views.SubjectModelViewSet)
router.register('courseapi',views.CourseModelViewSet)
router.register('enrollmentapi',views.EnrollmentModelViewSet)




# Course App URLS


urlpatterns = [
    path('',include(router.urls)),
    path('sublist/', views.subject_list, name = 'Subject_list'),
    path('subadd/', views.add_subject, name='Add_Subject'),
    path('subject_edit/<id>', views.edit_subject, name='Edit_Subject'),
    path('subject_delete/<id>', views.delete_subject, name='Delete_Subject'),

    # Enrollment Table URLS

    path('enrollment_list/', views.enrollment_list, name = 'Enrollment_list'),
    path('enrollment_add/', views.add_enrollment, name='Add_Enrollment'),
    path('enrollment_edit/<id>', views.edit_enrollment, name='Edit_Enrollment'),
    path('enrollment_delete/<id>', views.delete_enrollment, name='Delete_Enrollment'),
    ]