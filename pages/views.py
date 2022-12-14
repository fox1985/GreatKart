from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from carts.models import CartItem
from carts.views import _cart_id
from  pages.models import Category, Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def home(reguest):
    products = Product.objects.all().filter(is_available=True)
    context = {"products": products,}
    return render(reguest, 'pages/home.html', context)


def store(request, category_slug=None):
    category = None
    categoris = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.order_by('created_date').filter(category=category, is_available=True)
        # количесто продуктов на одной страници
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_cout = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        #количесто продуктов на одной страници
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_cout = products.count()

    context = {
        'products': paged_products,
        'product_cout': product_cout,
        'category': category,
        'categories':categoris,
    }
    return  render(request, 'store/store.html', context)



def product_detail(reguest, category_slug,  product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(reguest), product = single_product).exists()

    except Exception as e:
        raise e

    context = {'single_product': single_product, 'in_cart' : in_cart}

    return  render(reguest, 'store/product_detail.html', context)

#-----------------------------------------------------------------------------------------------------------------------

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_cout = products.count()

    context = {
        'products': products,
        'product_cout': product_cout,
    }
    return render(request, 'store/store.html', context)