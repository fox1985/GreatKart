from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from carts import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


