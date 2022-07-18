from django.urls import path
from experiment_csr import views

app_name = 'experiment_csr'

urlpatterns = [
    path('csr/',views.CSRView,name='csr'),
    path('certreq/',views.RequestView, name='certreq')
]
