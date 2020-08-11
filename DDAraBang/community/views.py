from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, School, Community, All_Community, All_Post
from django.core.paginator import Paginator
from user.models import User


# Create your views here.

def community_list(request, school_list):
    communities = Community.objects.all()
    school = School.objects.get(pk=school_list)

    return render(request, 'community/community_list.html', {
        'communities': communities,
        'school': school})

def all_community_list(request):
    all_communities = All_Community.objects.all()

    return render(request, 'community/all_community_list.html', {
        'all_communities': all_communities,
        })

def post_list(request, school_list, community_list):

    page = request.GET.get("page")

    all_post = Post.objects.all()

    # 학교로 필터링 
    my_school = School.objects.get(pk=school_list)
    posts_School = all_post.filter(School=my_school)

    # 커뮤니티 링크 및 현재 커뮤니티 
    communities = Community.objects.all()
    my_community = Community.objects.get(pk=community_list)

    # 학교 #게시판 게시물 
    posts_community = posts_School.filter(community=my_community)

    # 페이지 작업 
    paginator = Paginator(posts_community, 5)
    posts = paginator.get_page(page)

    return render(request, "community/post_list.html", {
        "posts" : posts,
        "posts_community": posts_community,
        'communities': communities,
        'my_community': my_community,
        'my_school': my_school})

def all_post_list(request, all_community_list):

    page = request.GET.get("page")

    all_post = All_Post.objects.all()

    #전체 커뮤니티 링크 및 현재 커뮤니티
    all_communities = All_Community.objects.all()
    all_my_community = All_Community.objects.get(pk=all_community_list)

    #게시판 게시물 
    all_posts_community = all_post.filter(all_community=all_my_community)

    # 페이지 작업 
    paginator = Paginator(all_posts_community, 5)
    posts = paginator.get_page(page)

    return render(request, "community/all_post_list.html", {
        "posts" : posts,
        'all_communities': all_communities,
        'all_posts_community' : all_posts_community,
        'all_my_community': all_my_community,
        })


def post_write(request, my_school, my_community):
    # if not request.session.get('user'):
    #    return redirect('/users/login')
    if request.method == "GET":
        form = PostForm()

    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(
                user = request.user,
                School= School.objects.get(pk=my_school),
                community= Community.objects.get(pk=my_community),
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                photo=form.cleaned_data['photo'],)
                # writer=user
            new_post.save()

            return redirect('/community/{}/{}'.format(my_school, my_community))

    return render(request, 'community/post_write.html', {'form': form})


def all_post_write(request, all_my_community):
    # if not request.session.get('user'):
    #    return redirect('/users/login')
    if request.method == "GET":
        form = PostForm()

    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = All_Post(
                user = request.user,
                all_community= All_Community.objects.get(pk=all_my_community),
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                photo=form.cleaned_data['photo'],)
                # writer=user
            new_post.save()

            return redirect('/community/all/{}'.format(all_my_community))

    return render(request, 'community/all_post_write.html', {'form': form})



def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    
    except Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'community/post_detail.html', {'post': post})

def all_post_detail(request, post_id):
    try:
        post = All_Post.objects.get(pk=post_id)
    
    except All_Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'community/all_post_detail.html', {'post': post})


def delete(request, delete):
    post = Post.objects.get(pk=delete)
    rtn_school = post.School.id
    rtn_community = post.community.id 
    post.delete()
    return redirect('/community/{}/{}'.format(rtn_school, rtn_community))

def all_delete(request, delete):
    post = All_Post.objects.get(pk=delete)
    rtn_school = post.School.id
    rtn_community = post.all_community.id 
    post.delete()
    return redirect('/community/{}'.format(rtn_community))

def update(request, update):
    post = Post.objects.get(pk=update)
    if request.method == "GET":
        form = PostForm(instance=post)

    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.photo = form.cleaned_data['photo']
        # post.pub_date = timezone.datetime.now()
        post.save()
        
        return redirect('/community/detail/{}'.format(post.id))


    return render(request, 'community/update.html', {'form': form})

def all_update(request, update):
    post = All_Post.objects.get(pk=update)
    if request.method == "GET":
        form = PostForm(instance=post)

    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.photo = form.cleaned_data['photo']
        # post.pub_date = timezone.datetime.now()
        post.save()
        
        return redirect('/community/detail/{}'.format(post.id))


    return render(request, 'community/update.html', {'form': form})

def my_write(request):
    all_posts = Post.objects.all()
    posts = all_posts.filter(user=request.user.id)
    return render(request, 'community/my_write.html', {'posts':posts})

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():
        #좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('community:post_detail', post_id)

def all_like(request, post_id):
    post = get_object_or_404(All_Post, id=post_id)
    
    if request.user in post.like_users.all():
        #좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('community:all_post_detail', post_id)

def my_page(request):
    user_id = request.user.id
    user_info = User.objects.get(pk=user_id)
    return render(request, 'community/my_page.html', { 'user_info' : user_info })
