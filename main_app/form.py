from extra_views import FormSetView
from extra_views import ModelFormSetView


class quotaionLineFormSetView(ModelFormSetView):
    model = QuotationLine
    template_name = 'quotation_line_formset.html'
    fields = '__all__'


class QuotationFormSet(FormSetView):
    form_class = QuotationForm
    template_name = 'quotation_formset.html'
