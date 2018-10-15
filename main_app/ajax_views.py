from django.views.generic import View
from django.http import HttpResponse

from models import QuotationLine, Quotation

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class QuotationLineFieldEditView(View):
    def post(self, request, id, field_name, **kwargs):
        line = QuotationLine.objects.get(id= id)
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
class QuotationLineCreateView(View):
    pass
