from django.urls import path
from experiment import views

app_name = 'experiment'

urlpatterns = [
    path('ca',views.RootCAView,name='ca'),
]
