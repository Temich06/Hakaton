from django.shortcuts import render


# Create your views here.
menu = [
    {'title': 'ГЛАВНАЯ', 'url': '/'},
    {'title': 'ПРОЕКТЫ', 'url': '/project'},
    {'title': 'ВОЛОНТЁРСКАЯ ПОМОЩЬ', 'url': '/volunteerhelp'},
    {'title': 'ВОЛОНТЁРАМ', 'url': '/volunteer'},
    {'title': 'КОНТАКТЫ', 'url': '/contacts'}
]


def main(request):
    array = {'menu': menu}
    return render(request, 'main/index.html', context=array)


def project(request):
    array = {'menu': menu}
    return render(request, 'main/project.html', context=array)


def volunteer(request):
    array = {'menu': menu}
    return render(request, 'main/volunteer.html', context=array)


def volunteerhelp(request):
    array = {'menu': menu}
    return render(request, 'main/volunteerhelp.html', context=array)


def contacts(request):
    array = {'menu': menu}
    return render(request, 'main/contacts.html', context=array)