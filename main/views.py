from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views import View
from .models import Car, Note
from django.views.generic import CreateView, UpdateView, DeleteView

from main.models import Car


class IndexView(View):
    def get(self, request, **kwargs):
        if request.user is not None:
            if request.user.is_authenticated:
                cars = Car.objects.filter(user=request.user).all()
                return render(request, 'mainPage/index.html', context={'login': False, 'cars': cars})
        return render(request, 'mainPage/index.html', context={'login': True})

    def post(self, request, **kwargs):
        return redirect(
            'car',
            pk=request.POST.get("select")
        )


class CarView(LoginRequiredMixin, View):
    def get(self, request, pk):
        car = Car.objects.filter(id=pk).first()
        notes = Note.objects.filter(car_id=pk).all()

        return render(request, 'journal/jornal.html', {'records': notes, 'car': car})


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['name', 'manufacturer', 'model', 'issue_year', 'cost', 'mileage', 'registration_number',
              'fuel_type']
    template_name = 'create_car.html'

    def form_valid(self, form):
        self.object = Car(user_id=self.request.user.id, **form.cleaned_data)
        self.object.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('index')


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['name', 'manufacturer', 'model', 'issue_year', 'cost', 'mileage', 'registration_number',
              'fuel_type']
    template_name = 'update_car.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('car', args=[self.object.id])


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'delete_car.html'

    def get_success_url(self):
        return reverse_lazy('index')


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["odometer", "fuel_volume", "cost", "date", "fuel_type"]
    template_name = 'create_note.html'

    def form_valid(self, form):
        print(self.kwargs)
        self.object = Note(car_id=self.kwargs["pk"], **form.cleaned_data)
        self.object.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('car', args=[self.kwargs["pk"]])


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ["odometer", "fuel_volume", "cost", "date", "fuel_type"]
    template_name = 'update_note.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('car', args=[self.kwargs["car_id"]])


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'delete_note.html'

    def get_success_url(self):
        return reverse_lazy('car', args=[self.kwargs["car_id"]])
