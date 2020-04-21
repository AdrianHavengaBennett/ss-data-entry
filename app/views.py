from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Data, JobInfoReport
from .forms import DataForm, SearchAndUpdateForm
from io import BytesIO
import pandas as pd
import xlsxwriter


def do_update_and_collect_job_info(request, obj, commission_pre_vat=0, payments=0):
	"""
	Helper function to do heavy lifting
	A new job_info report instance is created each time
	"""

	job_info = JobInfoReport()

	job_info.r_plentific_job_number = obj.plentific_job_number
	job_info.r_wo_number = obj.wo_number
	job_info.r_job_number_exists = "Yes"

	if not request.GET.get("commission_pre_vat"):
		obj.commission_pre_vat = commission_pre_vat
	else:
		obj.commission_pre_vat = request.GET.get("commission_pre_vat")

	obj.save()

	if obj.invoice_number:
		job_info.r_invoice_number_found = obj.invoice_number
	else:
		job_info.r_invoice_number_found = "None"

	if not request.GET.get("payments"):
		inputted_payment = float(payments)
	else:
		inputted_payment = float(request.GET.get("payments"))

	if inputted_payment != obj.payments:
		job_info.r_payments = "don't match: expected £{}, received £{}".format(
			obj.payments, inputted_payment)
	else:
		job_info.r_payments = "match"

	job_info.save()

	return request


def all_data(request):
	"""Retrieves all data and renders to html page"""

	obj = Data.objects.all()

	return render(request, "all_data.html", {"obj": obj})


def add_data(request):
	"""
	Loads form and saves data to database
	Redirects to render all data on html page
	"""

	if request.method == "POST":
		form = DataForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect(reverse(all_data))
	else:
		form = DataForm()

	return render(request, "add_data.html", {"form": form})


def data_entry(request):
	"""
	Creates new instance of data entry form and renders it on html page
	along with a report table, which updates with each data entry input
	"""

	form = SearchAndUpdateForm()

	# df = pd.DataFrame(JOB_INFO,
	# 	columns=[
	# 		"Plentific Job Number",
	# 		"WorkOrder Number",
	# 		"Invoice Number Found",
	# 		"Payments",
	# 		"Job Number Exists",
	# 	])

	# if not df.empty:
	# 	df_html = df.to_html(classes="table table-striped table-hover")
	# 	return render(request, "data_entry.html", {
	# 		"form": form, "df_html": df_html})
	# else:

	job_info = JobInfoReport.objects.all()

	return render(request, "data_entry.html", {
		"form": form, "job_info": job_info})


def edit_data(request, id):
	"""
	Loads form with contents for editing, and saves data
	to database when complete.
	Redirects to render all data on html page
	"""

	item = get_object_or_404(Data, pk=id)

	if request.method == "POST":
		form = DataForm(request.POST, instance=item)
		if form.is_valid():
			form.save()

		return redirect(reverse(all_data))
	else:
		form = DataForm(instance=item)

	return render(request, "add_data.html", {"form": form})


def search_data(request):
	"""
	Searches data and returns job info if found
	Handles 2 exceptions:
	1. Job number not found
	2. Multiples of a job number found
	"""

	inputted_job_number = request.GET["plentific_job_number"]
	if "#" not in inputted_job_number:
		inputted_job_number = "#{}".format(inputted_job_number)

	try:
		obj = Data.objects.filter(plentific_job_number=inputted_job_number)

		return render(request, "searched_data.html", {"obj": obj,
			"inputted_job_number": inputted_job_number})

	except ObjectDoesNotExist:
		
		return render(request, "not_found.html", {
			"inputted_job_number": inputted_job_number})

	except MultipleObjectsReturned:
		obj = Data.objects.filter(plentific_job_number=inputted_job_number)

		return render(request, "multiples_search.html", {"obj": obj})


def search_update_feedback(request):
	"""
	Entry point for data entry. Searches database for job number,
	updates file with inputted data, and adds to report.
	Handles 2 exceptions:
	1. Job number not found
	2. Multiples of a job number found
	"""

	try:
		inputted_job_number = request.GET["plentific_job_number"]
		if "#" not in inputted_job_number:
			inputted_job_number = "#{}".format(inputted_job_number)

		obj = Data.objects.get(plentific_job_number__exact=inputted_job_number)

		do_update_and_collect_job_info(request, obj)

		return redirect(reverse(data_entry))

	except ObjectDoesNotExist:
		job_info = JobInfoReport()

		job_info.r_plentific_job_number = "N/A"
		job_info.r_wo_number = "N/A"
		job_info.r_job_number_exists = "Plentific Job Number {} not found".format(inputted_job_number)
		job_info.r_invoice_number_found = "N/A"
		job_info.r_payments = "N/A"

		job_info.save()

		return redirect(reverse(data_entry))

	except MultipleObjectsReturned:
		obj = Data.objects.filter(plentific_job_number=inputted_job_number)

		inputted_payment = float(request.GET["payments"])

		return render(request, "multiples_update.html", {
			"obj": obj, "commission_pre_vat": request.GET["commission_pre_vat"],
			"payments": inputted_payment})


def edit_specific(request, id, commission_pre_vat, payments):
	"""
	Returns all matching objects for user to choose which
	to update. Calls upon helper function to do heavy lifting.
	Redirects to data entry html page
	"""

	obj = Data.objects.get(pk=id)

	do_update_and_collect_job_info(request, obj, commission_pre_vat, payments)

	return redirect(reverse(data_entry))


def export_job_info_report(request):
	"""
	Exports the job_info list as an Excel spreadsheet
	and saves it to user's local directory
	"""
	df = pd.DataFrame.from_records(JobInfoReport.objects.all().values())

	output = BytesIO()
	writer = pd.ExcelWriter(output, engine='xlsxwriter')
	df.to_excel(writer, sheet_name='report', index=False)
	writer.save()
	output.seek(0)
	response = HttpResponse(output,
		content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename=%s.xlsx' % 'Download'

	return response


def clear_report_info(request):
	"""Empties the job_info dictionary"""

	JobInfoReport.objects.all().delete()

	return redirect(reverse(data_entry))
