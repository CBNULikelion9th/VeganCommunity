from django.shortcuts import render, redirect
from .models import Post, Market_Post, Market_Comment
from signup.models import User, UserManager
from .forms import UserForm, PostForm, MarketPostForm, MarketCommentForm

def main(request):
    return render(request, 'vegan_admin/main.html')

def user_list(request):
    list = User.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'vegan_admin/user_list.html', context)

def user_detail(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'vegan_admin/user_detail.html', context)

def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user_list')

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect('user_detail', user.id)
    else:
        form = UserForm()
    
    return render(request, 'vegan_admin/user_new.html', {'form': form})

def user_update(request, id):
    user = User.objects.get(id=id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user.id)
    else:
        form = UserForm(instance=user)

    return render(request, 'vegan_admin/user_update.html', {'user':user, 'form':form})

def custom_store_list(request):
    list = Post.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'vegan_admin/custom_store_list.html', context)

def custom_store_detail(request, id):
    store = Post.objects.get(id=id)
    context = {
        'store': store,
    }
    return render(request, 'vegan_admin/custom_store_detail.html', context)

def custom_store_delete(request, id):
    store = Post.objects.get(id=id)
    store.delete()
    return redirect('custom_store_list')

def custom_store_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            store = form.save()
        return redirect('custom_store_detail', store.id)
    else:
        form = PostForm()
    
    return render(request, 'vegan_admin/custom_store_new.html', {'form': form})

def custom_store_update(request, id):
    store = Post.objects.get(id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('custom_store_detail', store.id)
    else:
        form = PostForm(instance=store)

    return render(request, 'vegan_admin/custom_store_update.html', {'store':store, 'form':form})

def goods_list(request):
    list = Market_Post.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'vegan_admin/goods_list.html', context)

def goods_detail(request, id):
    good = Market_Post.objects.get(id=id)
    if request.method == "POST":
        comment_form = MarketCommentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save()
    
    comment_form = MarketCommentForm()
    comments = good.comment.all()

    return render(request, 'vegan_admin/goods_detail.html', {
        'good': good, 'comment_form': comment_form, 'comments': comments,
    })

def comment_create(request, id):
    good = Market_Post.objects.get(id=id)
    if request.method == "POST":
        form = MarketPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.goods_id = id
            comment.save()
            return redirect('goods_detail', id)
    else:
        form = MarketCommentForm()
    context = {'form': form, 'id': id, 'good': good}
    return render(request, 'vegan_admin/comment_create.html', context)

def comment_list(request):
    list = Market_Comment.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'vegan_admin/comment_list.html', context)

def goods_delete(request, id):
    good = Market_Post.objects.get(id=id)
    good.delete()
    return redirect('goods_list')

def goods_new(request):
    if request.method == "GET":
        form = MarketPostForm()
    else:
        form = MarketPostForm(request.POST, request.FILES)
        if form.is_valid():
            good = form.save()
        return redirect('goods_detail', good.id)
            
    return render(request, 'vegan_admin/goods_new.html', {'form': form})

def goods_update(request, id):
    good = Market_Post.objects.get(id=id)

    if request.method == "POST":
        form = MarketPostForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return redirect('goods_detail', good.id)
    else:
        form = MarketPostForm(instance=good)

    return render(request, 'vegan_admin/goods_update.html', {'good':good, 'form':form})