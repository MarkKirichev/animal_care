from django.shortcuts import render, redirect

from app.forms import AnimalForm
from app.models import Animal


def add_animal(request):
    if request.method == 'GET':
        context = {
            'form': AnimalForm(),
        }

        return render(request, 'app/create.html', context)
    else:
        form = AnimalForm(request.POST, initial={'priority': 'low'})
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'app/create.html', context)


def edit_animal(request, pk):
    animal = Animal.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'animal': animal,
            'form': AnimalForm(instance=animal),
        }

        return render(request, 'app/edit.html', context)
    else:
        form = AnimalForm(request.POST, instance=animal)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'animal': animal,
            'form': form,
        }

        return render(request, 'app/edit.html', context)


def delete_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.delete()
    return redirect('index')


def details_animal(request, pk):
    animal = Animal.objects.ger(pk=pk)

    context = {
        'animal': animal
    }

    return render(request, 'app/details.html', context)


def cure_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.is_cured = True

    return redirect('index')
