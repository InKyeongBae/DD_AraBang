from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, School, Community, Comment
from django.core.paginator import Paginator
from user.models import User
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Count


# Create your views here.

def community_list(request, school_list):
    communities = Community.objects.all()
    school = School.objects.get(pk=school_list)

    return render(request, 'community/community_list.html', {
        'communities': communities,
        'school': school})


def post_list(request, school_list, community_list):

    page = request.GET.get("page")

    all_post = Post.objects.all()
    # 학교로 필터링 
    my_school = School.objects.get(pk=school_list)
    posts_School = all_post.filter(School=my_school)
    # 커뮤니티 링크 및 현재 커뮤니티 
    communities = Community.objects.all()
    my_community = Community.objects.get(pk=community_list)
    # # 학교 #게시판 게시물 
    posts_community = posts_School.filter(community=my_community)
    # 페이지 작업 
    paginator = Paginator(posts_community, 5)
    posts = paginator.get_page(page)
    # 실시간인기글
    hot_posts = Post.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at')

    return render(request, "community/post_list.html", {
        "posts" : posts,
        "posts_community": posts_community,
        'communities': communities,
        'my_community': my_community,
        'my_school': my_school,
        'hot_posts': hot_posts})


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

    return render(request, 'community/post_detail.html', {'post': post, "comments":comments, "comment_form":comment_form})


def delete(request, delete):
    post = Post.objects.get(pk=delete)
    rtn_school = post.School.id
    rtn_community = post.community.id 
    post.delete()
    return redirect('/community/{}/{}'.format(rtn_school, rtn_community))

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


def my_page(request):
    user_id = request.user.id
    user_info = User.objects.get(pk=user_id)
    return render(request, 'community/my_page.html', { 'user_info' : user_info })


def create_comment(request ,content_id):
    is_ajax = request.POST.get('is_ajax')

    content = get_object_or_404(Post, pk=content_id)

    comment_form = CommentForm(request.POST)
    comment_form.instance.user_id = request.user.id
    comment_form.instance.content_id = content_id
    if comment_form.is_valid():
        comment = comment_form.save()

    if is_ajax:
        # 데이터 만들어서 던져주기
        html = render_to_string('community/comment_list.html',{'comments':comment})
        return JsonResponse({'html':html})
    return redirect(reverse('community:detail', args=[content_id]))


def comment_update(request, comment_id):
    is_ajax, data = (request.GET.get('is_ajax'), request.GET) if 'is_ajax' in request.GET else (request.POST.get('is_ajax', False), request.POST)

    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.content.id

    if request.user != comment.user:
        messages.warning(request, "권한 없음")
        return redirect('community:post_detail', post)

    if is_ajax:
        form = CommentForm(data, instance=comment)

        if form.is_valid():
            form.save()
            return JsonResponse({'works':True})

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('community:post_detail', post)
    
    else:
        form = CommentForm(instance=comment)
        return render(request, 'community/comment_update.html', {'form':form})


def comment_delete(request, comment_id):
    is_ajax = request.GET.get('is_ajax') if 'is_ajax' in request.GET else request.POST.get('is_ajax',False)
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.content.id

    if request.user != comment.user and not request.user.is_staff and request.user != post.user:
        messages.warning(request, "권한 없음")
        return redirect('community:post_detail', post)

    if is_ajax:
        comment.delete()
        return JsonResponse({"works":True})

    if request.method == "POST":
        del_post = post 
        comment.delete()
        return redirect('community:post_detail', del_post)

    else:
        return render(request, 'community/comment_delete.html', {'comment': comment})


def post_i_like(request):
    like_posts = Post.objects.filter(like_users=request.user)
    return render(request, 'community/post_i_like.html', {'like_posts': like_posts})
    

