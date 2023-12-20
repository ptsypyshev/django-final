from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import OrderedProducts,CreateProduct,ReadProduct,Index

urlpatterns = [
    path('ordered-products/<int:customer_id>/', OrderedProducts.as_view(), name='ordered_products'),
    path('create-product/', CreateProduct.as_view(), name='create_product'),
    path('product/<int:product_id>/', ReadProduct.as_view(), name='read_product'),
    path('', Index.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
