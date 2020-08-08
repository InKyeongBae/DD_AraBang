from django.http import Http404
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, School, Community
from django.core.paginator import Paginator


# Create your views here.

def community_list(request, pk_1):
    community = Community.objects.all()
    school = School.objects.get(pk=pk_1)
    return render(request, 'community/community_list.html', {
        'communities': community,
        'school': school})


def post_list(request, pk_1, pk):

    page = request.GET.get("page")
    post = Post.objects.all()
    school = School.objects.get(pk=pk_1)
    community = Community.objects.all()
    community_1 = Community.objects.get(pk=pk)
    post_1 = post.filter(School=school)
    post_2 = post_1.filter(community=community_1)
    paginator = Paginator(post_2, 5)
    posts = paginator.get_page(page)

    return render(request, "community/post_list.html", {
        "posts": posts,
        "post_2": post_2,
        'communities': community,
        'community_1': community_1,
        'school': school})


def post_write(request, pk_1, pk):
    # if not request.session.get('user'):
    #    return redirect('/users/login')
    if request.method == "GET":
        form = PostForm()

    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # user_id = request.session.get('user')
            # user = Users.objects.get(pk=user_id)
            new_post = Post(
                School=School.objects.get(pk=pk_1),
                community=Community.objects.get(pk=pk),
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                # writer=user
            )
            new_post.save()
            return redirect('/community/{}/{}'.format(pk_1, pk))

    return render(request, 'community/post_write.html', {'form': form})


def post_detail(request, pk_1, pk, pk_3):
    try:
        post = Post.objects.get(pk=pk_3)
    except Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'community/post_detail.html', {'post': post})


def delete(request, pk_1, pk, pk_3):
    post = Post.objects.get(pk=pk_3)
    post.delete()
    return redirect('/community/{}/{}'.format(pk_1, pk))
