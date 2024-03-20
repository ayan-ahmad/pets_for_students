from django.shortcuts import render
from pets.models import Cat, Student


def index(request):
    context_dict = {}

    context_dict['students'] = Student.objects.all()
    context_dict['cats'] = Cat.objects.all()

    return render(request, 'pets/index.html', context=context_dict)


def pets(request):
    context_dict = {}

    context_dict['cats'] = Cat.objects.all()

    return render(request, 'pets/pets.html', context=context_dict)