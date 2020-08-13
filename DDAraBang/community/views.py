# from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, School, Community, All_Community, All_Post, Comment
from django.core.paginator import Paginator
from user.models import User
from django.template.loader import render_to_string
from django.contrib import messages


# Create your views here.

# def get_point(request):
#     user = User.objects.get(username=request.user)
#     user.point +=10

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


<<<<<<< Updated upstream
def post_list(request, school_list, community_list):
=======
>>>>>>> Stashed changes
    page = request.GET.get("page", 1)

    all_post = Post.objects.all()

<<<<<<< Updated upstream
    # 학교로 필터링
=======

    # 학교로 필터링 
>>>>>>> Stashed changes
    my_school = School.objects.get(pk=school_list)
    posts_School = all_post.filter(School=my_school)

    # 커뮤니티 링크 및 현재 커뮤니티
    communities = Community.objects.all()
    my_community = Community.objects.get(pk=community_list)
    community_desc = my_communinty.description

    # 학교 #게시판 게시물
    posts_community = posts_School.filter(community=my_community)

<<<<<<< Updated upstream
    # 페이지 작업
=======
    # 페이지 작업 
>>>>>>> Stashed changes
    paginator = Paginator(posts_community, 10)
    posts = paginator.page(int(page))

    return render(request, "community/post_list.html", {
<<<<<<< Updated upstream
        "page": posts,
=======
        "page" : posts,
>>>>>>> Stashed changes
        "posts_community": posts_community,
        'communities': communities,
        'my_community': my_community,
        'my_school': my_school,
        'community_desc': community_desc,})


<<<<<<< Updated upstream
def all_post_list(request, all_community_list):
    page = request.GET.get("page")
=======
    page = request.GET.get("page", 1)
>>>>>>> Stashed changes

    all_post = All_Post.objects.all()

    # 전체 커뮤니티 링크 및 현재 커뮤니티
    all_communities = All_Community.objects.all()
    all_my_community = All_Community.objects.get(pk=all_community_list)

    # 게시판 게시물
    all_posts_community = all_post.filter(all_community=all_my_community)

    # 페이지 작업
    paginator = Paginator(all_posts_community, 5)
    posts = paginator.page(int(page))

    return render(request, "community/all_post_list.html", {
<<<<<<< Updated upstream
        "posts": posts,
=======
        "page" : posts,
>>>>>>> Stashed changes
        'all_communities': all_communities,
        'all_posts_community': all_posts_community,
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
                user=request.user,
                School=School.objects.get(pk=my_school),
                community=Community.objects.get(pk=my_community),
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
<<<<<<< Updated upstream
                photo=form.cleaned_data['photo'], )
            # writer=user
=======
                photo=form.cleaned_data['photo'],)

>>>>>>> Stashed changes
            new_post.save()

            user = User.objects.get(username=request.user)
            user.point +=10
            user.save()
            
            return redirect('/community/{}/{}'.format(my_school, my_community))

    return render(request, 'community/post_write.html', {'form': form})


def all_post_write(request, all_my_community):

    if request.method == "GET":
        form = PostForm()

    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = All_Post(
                user=request.user,
                all_community=All_Community.objects.get(pk=all_my_community),
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
<<<<<<< Updated upstream
                photo=form.cleaned_data['photo'], )
            # writer=user
            new_post.save()

=======
                photo=form.cleaned_data['photo'],)
>>>>>>> Stashed changes
            return redirect('/community/all/{}'.format(all_my_community))

    return render(request, 'community/all_post_write.html', {'form': form})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

    except Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    else:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            comment_form.instance.user_id = request.user.id
            comment_form.instance.content_id = post_id
            if comment_form.is_valid():
                comment = comment_form.save()

        comment_form = CommentForm()
        comments = post.comments.all()

    return render(request, 'community/post_detail.html',
                  {'post': post, "comments": comments, "comment_form": comment_form})


def all_post_detail(request, post_id):
    try:
        post = All_Post.objects.get(pk=post_id)

    except All_Post.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    else:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            comment_form.instance.user_id = request.user.id
            comment_form.instance.all_content_id = post_id
            if comment_form.is_valid():
                comment = comment_form.save()

        comment_form = CommentForm()
        comments = post.comments.all()

    return render(request, 'community/all_post_detail.html',
                  {"comments": comments, 'post': post, "comment_form": comment_form})


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
<<<<<<< Updated upstream
=======
    
        
        return redirect('/community/detail/{}'.format(post.id))
>>>>>>> Stashed changes

        return redirect('/community/detail/{}'.format(post.id))

    return render(request, 'community/update.html', {'form': form})


def my_write(request):
    all_posts = Post.objects.all()
    posts = all_posts.filter(user=request.user.id)
    return render(request, 'community/my_write.html', {'posts': posts})


def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.like_users.all():
        # 좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)

    return redirect('community:post_detail', post_id)


def all_like(request, post_id):
    post = get_object_or_404(All_Post, id=post_id)

    if request.user in post.like_users.all():
        # 좋아요 취소
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)

    return redirect('community:all_post_detail', post_id)


def my_page(request):
    user_id = request.user.id
    user_info = User.objects.get(pk=user_id)
    return render(request, 'community/my_page.html', {'user_info': user_info})


def create_comment(request, content_id):
    is_ajax = request.POST.get('is_ajax')

    content = get_object_or_404(Post, pk=content_id)
    all_content = get_object_or_404(All_Post, pk=content_id)

    comment_form = CommentForm(request.POST)

    comment_form.instance.user_id = request.user.id
    comment_form.instance.content_id = content_id

    if comment_form.is_valid():
        comment = comment_form.save()

    if is_ajax:
        # 데이터 만들어서 던져주기
        html = render_to_string('community/comment_list.html', {'comments': comment})
        return JsonResponse({'html': html})
    if all_content == 0:
        return redirect(reverse('community:detail', args=[content_id]))
    else:
        return redirect(reverse('community:all_detail', args=[content_id]))


def comment_update(request, comment_id):
    is_ajax, data = (request.GET.get('is_ajax'), request.GET) if 'is_ajax' in request.GET else (
    request.POST.get('is_ajax', False), request.POST)

    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.all_content is None:
        post = comment.content.id
    else: 
        all_post = comment.all_content.id

    if request.user != comment.user:
        messages.warning(request, "권한 없음")
        if comment.all_content == 0:
            return redirect('community:post_detail', post)
<<<<<<< Updated upstream
        else:
            return redirect('community:all_post_detail', post)
=======
        else: 
            return redirect('community:all_post_detail', all_post)
>>>>>>> Stashed changes

    if is_ajax:
        form = CommentForm(data, instance=comment)

        if form.is_valid():
            form.save()
            return JsonResponse({'works': True})

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            if comment.all_content is None:
                return redirect('community:post_detail', post)
<<<<<<< Updated upstream
            else:
                return redirect('community:all_post_detail', post)

    else:
        form = CommentForm(instance=comment)
        return render(request, 'community/comment_update.html', {'form': form})

=======
            else: 
                return redirect('community:all_post_detail', all_post)
    
    # else:
    #     form = CommentForm(instance=comment)
    #     return render(request, 'community/comment_update.html', {'form':form})
    else:
        if comment.all_content is None:
            form = CommentForm(instance=comment)
            return render(request, 'community/comment_update.html', {'form':form})
        else: 
            form = CommentForm(instance=comment)
            return render(request, 'community/comment_update.html', {'form':form})
    
>>>>>>> Stashed changes

def comment_delete(request, comment_id):
    is_ajax = request.GET.get('is_ajax') if 'is_ajax' in request.GET else request.POST.get('is_ajax', False)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.all_content is None:
        post = comment.content.id
    else: 
        all_post = comment.all_content.id

    if request.user != comment.user and not request.user.is_staff and request.user != post.user:
        messages.warning(request, "권한 없음")
        if comment.all_content is None:
            return redirect('community:post_detail', post)
<<<<<<< Updated upstream
        else:
            return redirect('community:all_post_detail', post)
=======
        else: 
            return redirect('community:all_post_detail', all_post)
>>>>>>> Stashed changes

    if is_ajax:
        comment.delete()
        return JsonResponse({"works": True})

<<<<<<< Updated upstream
    if request.method == "POST":
        del_post = post
        comment.delete()
        if all_content == 0:
            return redirect('community:post_detail', del_post)
        else:
            return redirect('community:all_post_detail', del_post)
=======
    else:
        comment.delete()
        if comment.all_content is None:
            return redirect('community:post_detail', post)
        else: 
            return redirect('community:all_post_detail', all_post)
>>>>>>> Stashed changes

