from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<int:pk>', views.get_product_detail, name='detail'),
]