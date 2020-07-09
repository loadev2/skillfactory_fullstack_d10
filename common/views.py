from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from common.models import Car

from .forms import FormFilter

# Create your views here.
@csrf_exempt
def index(request):

    cars = {}
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        param = request.GET.get('searchText')

        #val = request.GET.get('searchText')
        #val = 'Black'
        #cars = Car.objects.filter(color__containes=val)
        if param:
            cars = Car.objects.filter(Q(release_year=param))
        else:
            cars = Car.objects.all()
    else:
        cars = Car.objects.all()
    form = FormFilter()
    return render(request, 'index.html', {'form': form, "cars": cars})


class ListCar(ListView):
    model = Car
    context_object_name = "cars"
    template_name = "index.html"
