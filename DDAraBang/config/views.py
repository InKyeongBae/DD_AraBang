from django.shortcuts import render


def DDmainpage(request):
    return render(request, 'DDmainpage.html', context={})