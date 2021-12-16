from django.shortcuts import render

# Create your views here.

from .models import Role, Image_name, Page_Number, Person, Manumission, Gender, Birth_Place, Death_Place, Age_Listed, Age_Freed, Year_Manumitted, Place_Freed, Monthly_Meeting, Call_Number

def about(request):

    # Render the HTML template index.html with the data in the context variable
    return render(
        request, 
        'about.html')

def visualizations(request):
    return render(
        request,
        'visualizations.html')

def essays(request):
    return render(
        request,
        'essays.html')

def glossary(request):
    return render(
        request,
        'glossary.html')

def allmanumitted(request):
    return render(
        request,
        'allmanumitted.html')

def allslaveholders(request):
    return render(
        request,
        'allslaveholders.html')

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_manumissions = Manumission.objects.all().count()
    num_roles = Role.objects.all().count()
    num_persons = Person.objects.count()
    num_image_names = Image_name.objects.count()
    num_birth_places = Birth_Place.objects.count()
    num_death_places = Death_Place.objects.count()
    num_age_listeds = Age_Listed.objects.count()
    num_age_freeds = Age_Freed.objects.count()
    num_year_manumitteds = Year_Manumitted.objects.count()
    num_place_freeds = Place_Freed.objects.count()
    num_monthly_meetings = Monthly_Meeting.objects.count()
    num_call_numbers = Call_Number.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request, 
        'index.html',
        context = {
        'num_manumissions': num_manumissions,
        'num_roles': num_roles,
        'num_persons': num_persons,
        'num_image_names': num_image_names,
        'num_birth_places': num_birth_places,
        'num_death_places': num_death_places,
        'num_age_listeds': num_age_listeds,
        'num_age_freeds': num_age_freeds,
        'num_year_manumitteds': num_year_manumitteds,
        'num_place_freeds': num_place_freeds,
        'num_monthly_meetings': num_monthly_meetings,
        'num_call_numbers': num_call_numbers,
        'num_visits': num_visits
        }
    )


from django.views import generic

class ManumissionListView(generic.ListView):
    model = Manumission
    paginate_by = 30
    
class ManumissionDetailView(generic.DetailView):
    model = Manumission

class PersonListView(generic.ListView):
    model = Person
    paginate_by = 30

class PersonDetailView(generic.DetailView):
    model = Person

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Person, Manumission

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    initial = {'date_of_death': '05/01/1775'}

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')

class ManumissionCreate(CreateView):
    model = Manumission
    fields = '__all__'
    initial = {'date_of_death': '05/01/1775'}

class ManumissionUpdate(UpdateView):
    model = Manumission
    fields = '__all__'

class ManumissionDelete(DeleteView):
    model = Manumission
    success_url = reverse_lazy('manumissions')
