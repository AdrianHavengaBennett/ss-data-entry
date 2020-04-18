"""data_entry_ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (
    all_data,
    add_data,
    edit_data,
    search_update_feedback,
    edit_specific,
    data_entry,
    export_job_info_report,
    search_data,
    clear_report_info
)

urlpatterns = [
    path("", data_entry, name="data_entry"),
	path("add_data/", add_data, name="add_data"),
    path("all_data/", all_data, name="all_data"),
	path("edit_data/<id>/", edit_data, name="edit_data"),
	path("search_data/", search_data, name="search_data"),
	path("search/", search_update_feedback, name="search_update_feedback"),
	path("export_job_info_report/", export_job_info_report, name="export_job_info_report"),
	path("clear_report_info/", clear_report_info, name="clear_report_info"),
    path("edit_specific/<id>/<commission_pre_vat>/<payments>/", edit_specific, name="edit_specific"),
    path('admin/', admin.site.urls),
]
