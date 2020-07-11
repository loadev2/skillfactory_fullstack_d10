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
        query_list = str(param).split()
        query_list_num = [int(x) for x in query_list if x.isdigit()]
        query_list.append(param) # for cases like Model X
        query_list_trans = [x[0] for x in Car.TRANS_TYPE if x[1] in query_list]

        if param:
            cars = Car.objects.filter(Q(release_year__in=query_list_num) |
                                      Q(color__in=query_list) |
                                      Q(model__title__in=query_list) |
                                      Q(model__brand__title__in=query_list) |
                                      Q(transmission__in=query_list_trans))
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
