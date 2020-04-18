from django import forms
from .models import Data


class DataForm(forms.ModelForm):
	class Meta():
		model = Data
		fields = (
			"plentific_job_number",
			"commission_pre_vat",
			"payments",
			"wo_number",
			"invoice_number",
			"customer_name",
			"job_description",
		)


class SearchAndUpdateForm(forms.Form):
	plentific_job_number = forms.CharField(
		max_length=7,
		widget=forms.TextInput(
			attrs={'name': 'plentific_job_number',
		}))
	commission_pre_vat = forms.FloatField(
		widget=forms.TextInput(
			attrs={'name': 'commission_pre_vat',
		}))
	payments = forms.FloatField(
		widget=forms.TextInput(
			attrs={'name': 'payments',
		}))
