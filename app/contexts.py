from .models import Data
from .forms import SearchAndUpdateForm


def get_form_data(request):
	"""Provides data for use in URL arguments"""

	form_data = SearchAndUpdateForm(request.POST)

	return {"form_data": form_data}
