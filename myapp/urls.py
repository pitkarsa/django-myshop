from django.urls import path
from myapp import views

urlpatterns = [
   # path('index', views.home),
   path('index2',views.index2), 
   # path('register', views.register)  ,# GET - empty form, #POST submit the form
   path('signup',views.signup),
   path('addcat',views.addCategory),
   path('addproduct',views.addProduct)
]
