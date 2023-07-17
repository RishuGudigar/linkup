from django import forms
from .models import fProfile


class fProfileForm(forms.ModelForm):
    class Meta:
        model=fProfile
        fields=['name','category','phone_number','operation_commenced','city','franchise_commenced','LOGO','about_us','mission','vision','category','investment','brand_fee','royalty','anticipated_return_on_investment','likely_payback_period','floor_area_required','employees_requires','standard_agreement','franchise_term','term_renewable']



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient_email = forms.EmailField()