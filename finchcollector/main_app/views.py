from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Import the FeedingForm
from .forms import FeedingForm

from .models import Finch, Toy

# views.py

# finches = [
#   {'name': 'Australian Finches', 'size': '10-16 cm', 'habitation': 'widely spread across Australia shrubby forests and grasslands'},
#   {'name': 'Double-barred Finch', 'size': '11 cm', 'habitation': 'Across northern and eastern Australia in grassy woodlands and forests'},
# ]

# Create your views here.

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

# Add new view
def finches_index(request):
    finches= Finch.objects.all()# Retrieve all finches
    
    return render(request, 'finches/index.html', {
    'finches': finches,
  })
    
def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.toys.all().values_list('id')
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 
     'finch': finch,
     'feeding_form': feeding_form,
     'toys': toys_finch_doesnt_have
     })

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['name', 'size', 'habitation']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
   
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
  return f"{self.get_meal_display()} on {self.date}"

  # change the default sort
class Meta:
    ordering = ['-date']
    
    
def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'