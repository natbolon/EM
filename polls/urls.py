from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('home/', views.home, name='home'),
    path('new_driver/', views.new_driver.as_view(), name='new_driver'),
    path('new_testing/', views.new_testing, name='new_testing'),
    path('acceleration/', views.acceleration.as_view(), name='acceleration'),
    path('drivers/', views.Drivers, name='drivers')
]
