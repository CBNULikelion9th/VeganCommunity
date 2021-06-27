from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm #CommentForm

def market_home(request):
    return render(request, 'market/home.html')

def farmer_notice(request):
    return render(request, 'market/farmer_notice.html')

def market_list(request):
    market_list = Post.objects.all()
    context = {
        'market_list': market_list,
    }
    return render(request, 'market/market_list.html', context)

def market_detail(request, post_id ):
    post = Post.objects.get(id=post_id)

    context = {
            'post': 'post',
        
    }
    return render(request, 'market/market_detail.html', context)

def market_new(request):
    if request.method == 'GET':
        form = PostForm()

    elif request.method == 'POST':
        #포스트 : 사용자가 입력한 데이터를 저장하는 부분
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #post = form.save(ommit=true) user가 없어서 error
            # post = form.save(commit=False)
            # print(post)
            # post.user = request.user
             #post.id가 생성됨
            
            post_after_commit = post.save()
            print(post_after_comit)
        return redirect('market_detail', post_id = post_after_commit.id)
            
    return render(request, 'market/market_new.html', {
        
    })
    

# def market_new(request):
#     if request.method == 'GET':
#         form = PostForm()

#     elif request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('market_detail', post_id =post.id)
#     return render(request, 'market/market_new.html', {
#         'form' : form,
#     })

#2
# def market_detail(request, post_id ):
#     post = Post.objects.get(id=post_id)

#     context = {
#             'post': post,
#         # 'post_id': 1,
#         # 'post': post,
#     }
#     return render(request, 'market/market_detail.html', context)


# def market_new(request):
#     if request.method == 'GET':
#         form = PostForm()

#     elif request.method == 'POST':
#         #포스트 : 사용자가 입력한 데이터를 저장하는 부분
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #post = form.save(ommit=true) user가 없어서 error
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save() #post.id가 생성됨

            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # image = form.cleaned_data['image']
            # post = Post.objects.create(title=title, content=content, image=image)

            # post = Post.objects.create(title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # title, content=content, image=image)
            # return redirect('market_detail', post_id=post.id)



def market_comment(request,  post_id):
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(id=post.id)#(post_id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('visit_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment2.html',{
        'form': form,
    })





# def detail(request, post_id) :
#     post_detail = get_object_or_404(Post, pk=post_id)
#     comment_form = ComentForm()
#     return render(request, 'comment2.html', {'post_detail':post_detail, 'comment_form':comment_form})

# def new_comment(request, post_id) :
#     filled_form = CommentForm(request.POST)
#     if filled_form.is_valid() :
#         finished_form = filled_form.save(commit=False)
#         finished_form.post = get_object_or_404(Post, pk=post_id)
#         finished_form.save()
#     return redirect('visit_detail', post_id)



# def new_comment(request, post_id) :
#     filled_form = CommentForm(request.POST)
#     if filled_form.is_valid() :
#         finished_form = filled_form.save(commit=False)
#         finished_form.post = get_object_or_404(Post, pk=post_id)
#         finished_form.save()
#     # return redirect('visit_detail', post_id)
#     return render(request, 'comment2.html',{
#         'form':form,
#     })