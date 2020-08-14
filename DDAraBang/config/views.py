from django.shortcuts import render, Http404
from community.models import School
from django.db.models import Q
from django.template.loader import render_to_string
from .forms import SearchForm



def main_html(request):
    schools = School.objects.all()


    return render(request, 'DDmainpage.html', {
        'schools': schools,
    })
