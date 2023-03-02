from django.urls import path
from . import views

urlpatterns = [

    
#    path("<str:nome>", views.greet, name="greet")
    path("<str:nome>", views.bomdia, name="greet")    
    
]

