from django.contrib import admin

from django.forms import ModelForm
from .models import Product, Customer, Quotation, QuotationLine, BillLine, Bill

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    model = Product


class CustomerAdmin(admin.ModelAdmin):
    model = Customer


# ////////////////////////////////////////////////////
class QuotationAdminForm(ModelForm):
    class Meta:
        model = Quotation
        fields = "__all__"


class QuotationLineInLine(admin.TabularInline):
    model = QuotationLine


class QuotationAdmin(admin.ModelAdmin):
    form = QuotationAdminForm
    inlines = (QuotationLineInLine, )


class BillLineInLine(admin.TabularInline):
    model = BillLine


class BillAdminForm(ModelForm):
    model = Bill


class BillAdmin(admin.ModelAdmin):
    form = BillAdminForm


admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Product)
admin.site.register(Customer)
