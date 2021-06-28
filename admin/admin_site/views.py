from django.shortcuts import render, redirect
from .models import *
from .forms import *

def main(request):
    return render(request, 'admin_site/main.html')

def user_list(request):
    list = User.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'admin_site/user_list.html', context)

def user_detail(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'admin_site/user_detail.html', context)

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
    
    return render(request, 'admin_site/user_new.html', {'form': form})

def user_update(request, id):
    user = User.objects.get(id=id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user.id)
    else:
        form = UserForm(instance=user)

    return render(request, 'admin_site/user_update.html', {'user':user, 'form':form})

def vegan_store_list(request):
    list = Vegan_Store.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'admin_site/vegan_store_list.html', context)

def vegan_store_detail(request, id):
    store = Vegan_Store.objects.get(id=id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            reviews = review_form.save()
    
    review_form = ReviewForm()
    reviews = store.reviews.all()

    return render(request, 'admin_site/vegan_store_detail.html', {
        'store': store, 'review_form': review_form, 'reviews': reviews,
    })

def review_create(request, id):
    store = Vegan_Store.objects.get(id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.store_id = id
            review.save()
            return redirect('vegan_store_detail', id)
    else:
        form = ReviewForm()
    context = {'form': form, 'id': id, 'store': store}
    return render(request, 'admin_site/review_create.html', context)


def vegan_store_delete(request, id):
    store = Vegan_Store.objects.get(id=id)
    store.delete()
    return redirect('vegan_store_list')

def vegan_store_new(request):
    if request.method == "POST":
        form = VeganStoreForm(request.POST)
        if form.is_valid():
            store = form.save()
        return redirect('vegan_store_detail', store.id)
    else:
        form = VeganStoreForm()
    
    return render(request, 'admin_site/vegan_store_new.html', {'form': form})

def vegan_store_update(request, id):
    store = Vegan_Store.objects.get(id=id)

    if request.method == "POST":
        form = VeganStoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('vegan_store_detail', store.id)
    else:
        form = VeganStoreForm(instance=store)

    return render(request, 'admin_site/vegan_store_update.html', {'store':store, 'form':form})

def food_list(request):
    list = Food.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'admin_site/food_list.html', context)

def food_detail(request, id):
    food = Food.objects.get(id=id)
    context = {
        'food': food,
    }
    return render(request, 'admin_site/food_detail.html', context)

def food_delete(request, id):
    food = Food.objects.get(id=id)
    food.delete()
    return redirect('food_list')

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
        return redirect('food_detail', food.id)
    else:
        form = FoodForm()
    
    return render(request, 'admin_site/food_new.html', {'form': form})

def food_update(request, id):
    food = Food.objects.get(id=id)

    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food.id)
    else:
        form = FoodForm(instance=food)

    return render(request, 'admin_site/food_update.html', {'food':food, 'form':form})

def good_list(request):
    list = Market_Goods.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'admin_site/goods_list.html', context)

def good_detail(request, id):
    good = Market_Goods.objects.get(id=id)
    context = {
        'good': good,
    }
    return render(request, 'admin_site/goods_detail.html', context)

def good_delete(request, id):
    good = Market_Goods.objects.get(id=id)
    good.delete()
    return redirect('good_list')

def good_new(request):
    if request.method == "GET":
        form = GoodForm()
    else:
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            good = form.save()
        return redirect('good_detail', good.id)
            
    return render(request, 'admin_site/goods_new.html', {'form': form})

def good_update(request, id):
    good = Market_Goods.objects.get(id=id)

    if request.method == "POST":
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return redirect('good_detail', good.id)
    else:
        form = GoodForm(instance=good)

    return render(request, 'admin_site/goods_update.html', {'good':good, 'form':form})