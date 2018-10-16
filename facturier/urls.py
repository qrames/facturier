from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views

from main_app.views import IndexView

from main_app.views import ListCustomerView, CreateCustomerView, DetailCustomerView, UpdateCustomerView, DeleteCustomerView

from main_app.views import ListProductView, CreateProductView, DetailProductView, UpdateProductView, DeleteProductView

from main_app.views import QuotationFormSetView, ListQuotationView, DetailQuotationView, DeleteQuotationView

from main_app.ajax_views import QuotationFieldEditView, QuotationLineFieldEditView, CreateQuotationLineView

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
    url(r'^quotation/$', ListQuotationView.as_view(), name="quotation"),
    url(r'^quotation/(?P<pk>[\d]+)/$',
        DetailQuotationView.as_view(),
        name="detail-quotation"),
    url(r'^quotation/delete/(?P<pk>[\d]+)/$',
        DeleteQuotationView.as_view(),
        name="delete-quotation"),
    url(r'^quotation-line/add/(?P<id>[\d]+)/(?P<code>[\d]+)$',
        CreateQuotationLineView.as_view(),
        name="create-field-line-quotation"),
    url(r'^quotation-line/(?P<id>[\d]+)/(?P<field_name>[-\w]+)$',
        QuotationLineFieldEditView.as_view(),
        name="edit-field-line-quotation"),
    url(r'^quotation/(?P<pk>[\d]+)/(?P<field_name>[-\w]+)$',
        QuotationFieldEditView.as_view(),
        name="edit-field-quotation"),

    # ////////////////////////////////////////
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(next_page='/'),
        name="logout"),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
