from django.contrib.auth import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import frontpage, shop, signup, myaccount, order, edit_myaccount, about, help, contact2, newcontact
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('order/', order, name='order'),
    path('about/', about ,name='about'),
    path('help/', help ,name='help'),
    path('contact/', contact2 ,name='contact'),
    path('help/shop/', help ,name='helpshop'),
    path('newcontent/', newcontact, name='newcontent')
]

urlpatterns += staticfiles_urlpatterns()