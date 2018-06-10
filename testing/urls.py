from django.urls import path

from . import views

app_name = 'testing'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('new_driver/', views.New_Driver.as_view(), name='new_driver'),
    path('drivers/', views.Drivers.as_view(), name='drivers'),
    path('new_testing/', views.New_Testing.as_view(), name='new_testing'),
    path('acceleration/', views.AccelerationV.as_view(), name='acceleration'),
    path('skidpad/', views.SKV.as_view(), name='skid_pad'),
    path('autocross/', views.AutoXV.as_view(), name='autocross'),
    path('endurance/', views.EnduranceV.as_view(), name='endurance'),
    path('old_testing/<slug:event>', views.Old_Testing.as_view(), name='old_testing'),
    path('old_test/<str:event>', views.Old_Testing.as_view(), name='old_test')
]
