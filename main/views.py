from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views import View
from .models import Car, Note
from django.views.generic import CreateView

from main.models import Car


class IndexView(View):
    def get(self, request, **kwargs):
        if request.user is not None:
            if request.user.is_authenticated:
                cars = Car.objects.filter(user=request.user).all()
                print(cars)
                return render(request, 'mainPage/index.html', context={'login': False, 'cars': cars})
        return render(request, 'mainPage/index.html', context={'login': True})

    def post(self, request, **kwargs):
        return redirect(
            'shop_info',
            shop_id=request.POST.get("select")
        )


class CarView(View):
    def get(self, request, id):
        object = Car.objects.filter(id=id).first()

        return render(request, 'journal/jornal.html', {'records': object})


class CarCreateView(CreateView):
    model = Car
    fields = ['name', 'manufacturer', 'model', 'issue_year', 'cost', 'mileage', 'registration_number',
              'fuel_type']
    template_name = 'create_car.html'

    def form_valid(self, form):
        self.object = Car(user_id=self.kwargs['user'], **form.cleaned_data)
        self.object.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('car', args=[self.object.user_id])
