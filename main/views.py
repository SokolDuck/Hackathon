from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

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