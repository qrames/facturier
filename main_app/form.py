from models import QuotationLine

from django.forms import ModelForm


class QuotationLineForm(ModelForm):
    class Meta:
        model = QuotationLine
        fields = '__all__'
