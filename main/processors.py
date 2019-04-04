from main.models import Car


def processor(request):
    cars = []
    try:
        cars = Car.objects.filter(user=request.user).all()
    except:
        cars = []
    return {'CARS': cars}
