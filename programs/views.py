from django.shortcuts import render, redirect
from .models import ProgrammingLanguage


def language_list(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'programs/language_list.html', {'languages': languages})

def add_language(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if title is not None and description is not None:
        ProgrammingLanguage.objects.create(
            title=title,
            description=description
        )
        return redirect('language_list')
    return render(request, 'programs/add_language.html')