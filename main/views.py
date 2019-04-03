from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request, **kwargs):
        return render(request, 'mainPage/index.html', context={})

    def post(self, request, **kwargs):
        return redirect(
            'shop_info',
            shop_id=request.POST.get("select")
        )