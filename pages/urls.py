from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages import views




urlpatterns = [
    # выводит все на галовной странице
    path('', views.home, name='home'),

    # выводи ссылку магазин
    path('store/', views.store, name='store'),

    #выбор катигории
    path('store/category/<slug:category_slug>/', views.store, name='category'),

    # страница товара
    path('store/category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    #поиск
    path('store/search/', views.search, name='search'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



