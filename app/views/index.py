from django.shortcuts import render

from app.models import Animal


def index(request):
    if Animal.objects.exists():
        context = {
            'cured_animals': Animal.objects.filter(is_cured=True),
            'sick_animals': Animal.objects.all(is_cured=False)
        }

        return render(request, 'app/home_with_sick_and_cured.html', context)
    else:
        return render(request, 'app/home_with_no_animals.html')
