from django.db import models


class Data(models.Model):
	plentific_job_number = models.CharField(max_length=7, blank=False)
	commission_pre_vat = models.FloatField(blank=True, null=True)
	payments = models.FloatField(blank=False)
	wo_number = models.IntegerField(blank=False)
	invoice_number = models.IntegerField(blank=True, null=True)
	customer_name = models.CharField(max_length=30, blank=False)
	job_description = models.TextField()

	def __str__(self):
		return self.plentific_job_number


# class JobInfoReport(models.Model):
# 	"""The following are prefixed with 'r' to represent report"""

# 	r_plentific_job_number = models.CharField(max_length=7)
# 	r_wo_number = models.IntegerField()
# 	r_invoice_number_found = models.IntegerField()
# 	r_payments = models.FloatField()
# 	r_job_number_exists = models.CharField(max_length=3)

# 	def __str__(self):
# 		return self.r_plentific_job_number
