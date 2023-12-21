import uuid
from django.shortcuts import render,redirect
from django.views import View
from eshop.models import Customer,Order,Product
from datetime import date, timedelta
from django.core.files.storage import FileSystemStorage
from .forms import ProductFormWidget

# Create your views here.
class OrderedProducts(View):
    def get(self, request, customer_id):
        filter_last_week = date.today() - timedelta(days=7)
        filter_last_month = date.today() - timedelta(days=30)
        filter_last_year = date.today() - timedelta(days=365)

        customer = Customer.objects.filter(pk=customer_id).first()
        last_week_orders = Order.objects.filter(customer_id=customer_id,created_at__gt=filter_last_week).order_by('-created_at')
        last_month_orders = Order.objects.filter(customer_id=customer_id,created_at__gt=filter_last_month).order_by('-created_at')
        last_year_orders = Order.objects.filter(customer_id=customer_id,created_at__gt=filter_last_year).order_by('-created_at')

        products = {
            "week": OrderedProducts.get_products(last_week_orders),
            "month": OrderedProducts.get_products(last_month_orders),
            "year": OrderedProducts.get_products(last_year_orders),
        }

        previous_customer_id = customer_id - 1 if customer_id > 1 else 0
        next_customer_id = customer_id + 1

        context = {
            "customer": customer,
            "products": products,
            "previous_product_id": previous_customer_id, 
            "next_product_id":next_customer_id
        }

        return render(request, "eshop/customer_orders.html", context)
    
    @staticmethod
    def get_products(orders):
        products_set = set()
        products = []
        for order in orders:
            if order.product.exists():
                for p in order.product.all():
                    if p.pk in products_set:
                        continue
                    products.append((p.pk, p.name, order.created_at))
                    products_set.add(p.pk)
        return products


class CreateProduct(View):
    def get(self, request):
        form = ProductFormWidget()
        return render(request, 'eshop/create_product.html', {'form': form})
    
    def post(self, request):
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            image_name = CreateProduct.save_img(img)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            qty = form.cleaned_data['qty']
            
            product = Product(name=name, description=description, price=price, qty=qty, img=image_name)
            product.save()
            return redirect(f'/product/{product.pk}')
        
        return render(request, 'eshop/create_product.html', {'form': form})
    
    @staticmethod
    def save_img(image):
        name = '.'.join((str(uuid.uuid4()), image.name.split('.')[-1]))
        fs = FileSystemStorage()
        fs.save(name, image)
        return name

class ReadProduct(View):
    def get(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        previous_product_id = product_id - 1 if product_id > 1 else 0
        next_product_id = product_id + 1
        context = {
            "product": product,
            "product_id": product_id,
            "previous_product_id": previous_product_id, 
            "next_product_id":next_product_id
        }
        return render(request, "eshop/read_product.html", context, status=200 if product else 404)

class Index(View):
    def get(self, request):
        return render(request, "eshop/index.html")
