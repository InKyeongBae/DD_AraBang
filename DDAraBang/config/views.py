from django.shortcuts import render, Http404
from community.models import School
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.paginator import Paginator


def main_html(request):
    schools = School.objects.all()
    paginator = Paginator(schools, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'DDmainpage.html', {
        'schools' : schools,
        'posts' : posts,
        })


    

