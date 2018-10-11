"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views

from main_app.views import IndexView
from main_app.views import  ListCustomerView, CreateCustomerView, DetailCustomerView, UpdateCustomerView, DeleteCustomerView
from main_app.views import ListProductView, CreateProductView, DetailProductView, UpdateProductView, DeleteProductView
from main_app.views import QuotationFormSetView, ListQuotationView
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),

    # ////////////////////////////////////////
    url(r'^products/$', ListProductView.as_view(), name='products'),
    url(r'^product/add/$', CreateProductView.as_view(), name="add-product"),
    url(r'^product/(?P<code>[-\w]+)/$',
        DetailProductView.as_view(),
        name="detail-product"),
    url(r'^product/edit/(?P<code>[-\w]+)/$',
        UpdateProductView.as_view(),
        name="edit-product"),
    url(r'^product/delete/(?P<code>[-\w]+)/$',
        DeleteProductView.as_view(),
        name="delete-product"),
    # ////////////////////////////////////////
    url(r'^customers/$', ListCustomerView.as_view(), name='customers'),
    url(r'^customer/add/$', CreateCustomerView.as_view(), name="add-customer"),
    url(r'^customer/(?P<slug>[-\w]+)/$',
        DetailCustomerView.as_view(),
        name="detail-customer"),
    url(r'^customer/edit/(?P<slug>[-\w]+)/$',
        UpdateCustomerView.as_view(),
        name="edit-customer"),
    url(r'^customer/delete/(?P<slug>[-\w]+)/$',
        DeleteCustomerView.as_view(),
        name="delete-customer"),
    # ////////////////////////////////////////
    url(r'^quotation/add/$',
        QuotationFormSetView.as_view(),
        name="add-quotation"),
    url(r'^quotation/$',
        ListQuotationView.as_view(),
        name="quotation"),

    # ////////////////////////////////////////
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(next_page='/'),
        name="logout"),
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
