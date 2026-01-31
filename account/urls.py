from django.urls import path
from account import views
from account.views import *
from products.views import *

urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/' , cart , name="cart"),
   path('add_to_cart/<uid>/' , add_to_cart , name="add_to_cart"),
   path('remove-cart/<cart_item_uid>/', remove_cart, name="remove_cart"),
    path('product/<slug:slug>/', views.product_view, name='product'),
    # path('make-purchase', make_purchase , name="make_purchase" )
   path('category/', category_list, name='category_list'), 
    # path('category/<slug:category_slug>/', category_products, name='category_products'),
]