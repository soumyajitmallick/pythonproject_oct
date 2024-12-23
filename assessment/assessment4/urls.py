from django.urls import path
from .views import product_list, edit_or_delete_product

# FOR ASSESSMENT 4
urlpatterns=[
    path('product_list/',product_list,name="product_list"),
    path('edit_or_delete_product/<int:product_id>/',edit_or_delete_product,name="edit_or_delete_product"),
]