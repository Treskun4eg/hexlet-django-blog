from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    temp = [
        {'name': 'Yoda', 'position': 'CEO'},
        {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
        {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
        {'name': 'Jar Jar Binks', 'position': 'Trainee'},
    ]
    temp_new = {user.get('name'): user for user in temp}
    print(temp_new)
    return render(request, 'articles/index.html', context={'temp_new': temp_new},)
