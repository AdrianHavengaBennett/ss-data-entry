from django.db import models

# Create your models here.
class Data(models.Model):
	plentific_job_number = models.CharField(max_length=7, blank=False)
	commission_pre_vat = models.FloatField(blank=True, null=True)
	payments = models.FloatField(blank=False)
	wo_number = models.IntegerField(blank=False)
	invoice_number = models.IntegerField(blank=True, null=True)
	customer_name = models.CharField(max_length=30, blank=False)
	job_description = models.TextField()

	def __str__(self):
		return self.name
