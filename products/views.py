from django.shortcuts import redirect, render
from products.models import Product , SizeVariant
from account.models import Cart , CartItems,Profile
from django.http import HttpResponseRedirect


def get_product(request , slug):
    print('******')
    print(request.user)
    print('******')

    print(request.user.profile.get_cart_count)
    try:
        product = Product.objects.get(slug =slug)
        context = {'product' : product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)

            # This context is just define or assign for product.html
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)

        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)
    
def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)
    cart_item = CartItems.objects.create(cart = cart , product = product)

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'account/category.html', {'categories': categories})

# def category_products(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     return render(request, 'category_products.html', {'category': category, 'products': products})
