from django.shortcuts import render
from community.models import School

# def DDmainpage(request):
#     return render(request, 'DDmainpage.html', context={})

def main_html(request):
    schools = School.objects.all()
    return render(request, 'DDmainpage.html', {
        'schools': schools
    })