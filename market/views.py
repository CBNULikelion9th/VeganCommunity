from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm #CommentForm
from django.utils import timezone

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
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    return render(request, 'market/market_detail.html', {
        'post':post,
    })

# def market_new(request):
#     form = PostForm()
#     return render(request, 'market/market_new.html',{'form':form })

def market_new(request):
    
    form = Post(request.POST, request.FILES )
    if request.method == 'GET':
        form = Post()
    
    elif request.method == 'POST':
        form = Post(request.POST, request.FILES)

        if form.is_valid():
            form.title = request.POST['title']
            form.writer = request.POST['writer']
            form.content = request.POST['content']
            form.image = request.POST['image']
            form.check = request.POST.getlist('check[]')
            # form.organic = request.getlist('organic')
            # form.nature = request.getlist('nature')
            # form.nature = request.getlist('usual')

            market_new = Post.objects.create(
                title=title, writer=writer, content=content, image=image,
                )
            print(market_new)
            return redirect('market_detail', post_id=post.id)
            
    return render(request, 'market/market_new.html',{'form':form })

def market_create(request):
    new_post= Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.content = request.POST['content']

    # new_post.organic = request.getlist['organic']
    # new_post.nature = request.getlist['nature']
    # new_post.nature = request.getlist['usual']
    new_post.check = request.POST.getlist('check[]')

    new_post.image = request.FILES['image']
    new_post.pub_date = timezone.now()
    new_post.save()
    print(new_post.check)
    return redirect('market_detail', new_post.id)

def market_edit(request, post_id):
    market_edit = Post.objects.get(id=post_id)
    
    if request.method == "POST":
        form = Post(request.POST, request.FILES, request.checkbox)
        if form.is_valid():
            form.title = request.POST['title']
            form.writer = request.POST['writer']
            form.content = request.POST['content']
            
            # form.organic = request.checkbox['organic']
            # form.nature = request.checkbox['nature']
            # form.usual = request.checkbox['usual']

            # form.image = request.POST['image']
            market_edit = form.save()
            market_edit = Post.objects.get(
                title=title, writer=writer, content=content, image=image, organic=organic, nature=nature, usual=usual
                )
            print(market_new)
            return redirect('market_detail', post_id=post.id)
    else:
        form = Post()            
        print(market_edit)
        return render(request, 'market/market_edit.html', {
            'form':form,
            'post':market_edit,
        })

def market_update(request, post_id) :
    market_update = Post.objects.get(id = post_id)
    market_update.title = request.POST['title']
    market_update.writer = request.POST['writer']
    market_update.content = request.POST['content']
    # market_update.image = request.FILES['image']

    # market_update.organic = request.checkbox['organic']
    # market_update.nature = request.checkbox['nature']
    # market_update.nature = request.checkbox['usual']

    market_update.pub_date = timezone.now()
    market_update.save()
    return redirect('market_detail', market_update.id)

def market_delete(request, post_id) :
    post = Post.objects.get (id=post_id)
    post.delete()
    return redirect('market_list')

    
    # post = Post.objects.create(title=title, content=content, image=image)



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
            return redirect('market_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'market/comment.html',{
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