from django.urls import path
from . import views

urlpatterns = [
    path("",views.getRoutes),
    path('items/',views.getItems),
    path('category/',views.getCategory),
    path('item/<int:pk>/',views.getItem)
]