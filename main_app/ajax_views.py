from django.views.generic import View, CreateView, DeleteView
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, reverse

from form import QuotationLineForm

import json

from models import QuotationLine, Quotation, Product

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class QuotationLineFieldEditView(View):
    def post(self, request, id, field_name, **kwargs):
        line = QuotationLine.objects.get(id=id)
        value = request.POST.get("value")
        setattr(line, field_name, value)
        line.save()

        return HttpResponse("success:", line.id)


@method_decorator(csrf_exempt, name='dispatch')
class QuotationFieldEditView(View):
    def post(self, request, pk, field_name, **kwargs):
        quotation = Quotation.objects.get(pk=pk)
        value = request.POST.get("value")

        setattr(quotation, field_name, value)
        quotation.save()

        return HttpResponse("success:", quotation.pk)


@method_decorator(csrf_exempt, name='dispatch')
class CreateQuotationLineView(CreateView):
    model = QuotationLine
    form_class = QuotationLineForm

    def post(self, request, *args, **kwargs):

        data = request.body
        quotationId = json.loads(data)['quotationId']
        productId = json.loads(data)['productId']
        quantity = json.loads(data)['quantity']

        product = Product.objects.get(id=productId)
        quotation = Quotation.objects.get(id=quotationId)

        # CreateView.post(self, request, kwargs)
        line = QuotationLine.objects.create(
            quotation=quotation, product=product, quantity=quantity)
        return JsonResponse({
            "data_url_quantity":
            reverse("edit-field-line-quotation", args=[line.id, 'quantity']),
            "name":
            line.product.name,
            "quantity":
            line.quantity,
            "price":
            line.product.price,
            "id":
            line.id,
            "code":
            line.product.code,
        })

    def get_success_url(self):
        return reverse("detail-quotation", args=[self.object.quotation.id])


@method_decorator(csrf_exempt, name='dispatch')
class DeleteQuotationLineView(DeleteView):
    model = QuotationLine

    def get_success_url(self):
        return reverse("detail-quotation", args=[self.object.quotation.id])
