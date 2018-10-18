from django.views.generic import View, CreateView
from django.http import HttpResponse

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

    # def post(self, request, *args, **kwargs):
    #
    #     data = request.body
    #     quotationId = json.loads(data)['quotationId']
    #     productId = json.loads(data)['productId']
    #     quantity = json.loads(data)['quantity']
    #
    #     product = Product.objects.get(id=productId)
    #     quotation = Quotation.objects.get(id=quotationId)
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>><>>>>>>>>>>>>>>>>>>>")
    #     print(quotation)
    #     print(product)
    #     print(quantity)
    #     print(">>>>>>>>>>>>>>>>>>>>>><>>>>>>>>>>>>>>>>>>>>>>>")
    #
    #     return HttpResponse("success")

    def get_success_url(self):
        return reverse("detail-quotation", args=[self.object.quotation.id])
