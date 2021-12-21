from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.LaptopCreateView.as_view(),name='create_lap'),
    path('list/',views.LaptopListView.as_view(),name='list_lap'),
    path('delete/<int:pk>/',views.LaptopDeleteView.as_view(),name='delete_lap'),
    path('update/<int:pk>/',views.LaptopUpdateView.as_view(),name='update_lap'),
]