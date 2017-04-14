from tastypie.resources import ModelResource
from services.models import Product, Order
import os
#from django.conf.settings import PROJECT_ROOT
from django.conf import settings
class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        allowed_methods = ['get']
    def dehydrate(self, bundle):
        p=bundle.request.GET
        print(p['lol'])
        file_ = open(os.path.join(settings.PROJECT_ROOT, 'lol.txt'))
        with file_ as f:
            s = f.read()
        bundle.data['text_field'] = s
        return bundle

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get', 'post', 'put']
    def dehydrate(self, bundle):
        bundle.data['custom_field'] = "Whatever you want"
        return bundle
