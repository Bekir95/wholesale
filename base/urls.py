from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name="home"),
    path('products',views.products, name="products"),
    path('us/<str:pk>/',views.modal_view, name="modal"),
    path('adminImportUpdate',views.adminImportUpdate),
  


]