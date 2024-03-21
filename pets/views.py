from django.shortcuts import render
from pets.models import Cat, Student


def index(request):
    context_dict = {}

    context_dict['students'] = Student.objects.all()
    context_dict['cats'] = Cat.objects.all()

    return render(request, 'pets/index.html', context=context_dict)


def pets(request):
    context_dict = {'cats': Cat.objects.all()}

    return render(request, 'pets/pets.html', context=context_dict)


def guess_that_cat(request):
    context_dict = {'random_cat': Cat.objects.order_by('?').first()}

    return render(request, 'pets/guess.html', context=context_dict)