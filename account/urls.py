from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('accountapi',views.ProfileModelViewSet)


urlpatterns = [

    
   # ACCOUNT VIEWS
   path('',include(router.urls)),
   path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),
   path('main/', views.main_page, name='main_page'),

]