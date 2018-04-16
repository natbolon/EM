from django.urls import path

from . import views

app_name = 'testing'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('home/', views.home, name='home'),
    path('new_driver/', views.new_driver.as_view(), name='new_driver'),
    path('new_testing/', views.New_Testing.as_view(), name='new_testing'),
    path('acceleration/', views.AccelerationV.as_view(), name='acceleration'),
    path('drivers/', views.Drivers, name='drivers'),
    path('event/', views.event, name='event'),
    path('skidpad/', views.SKV.as_view(), name='skid_pad'),
    path('autocross/', views.AutoXV.as_view(), name='autocross'),
    path('old_testing/<slug:event>', views.Old_Testing, name='old_testing'),
]
