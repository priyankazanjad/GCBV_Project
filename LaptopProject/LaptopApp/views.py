from django.shortcuts import render
from .models import Laptop
from django.views.generic import CreateView,ListView,DeleteView,UpdateView

class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/lap/list/'

class LaptopListView(ListView):
    model = Laptop

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/lap/list/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/lap/list/'