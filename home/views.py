from django.shortcuts import render
from home.forms import HouseForm
from home.models import House
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import ListView

import os
import pickle
from sklearn import linear_model, metrics, model_selection
from sklearn.model_selection import train_test_split
from datetime import datetime
import numpy as np
import pandas as pd

# Create your views here.
class HouseList(ListView):
	model = House
	template_name = 'house_list.html'
	context_object_name = 'house_list'

def get_prediction(request):
	form = HouseForm()
	if request.method == 'POST':
		form = HouseForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
			filename = 'static/home/house_model.sav'
			loaded_model = pickle.load(open( os.path.join(os.path.dirname(os.path.dirname(__file__)),filename), 'rb'))
			xnew = []
			l = []
			for key, value in form.cleaned_data.items():
				if key != 'transaction_date':
					l.append(value)
			xnew.append(l)
			ynew = loaded_model.predict(xnew)
			obj = House.objects.latest('id')
			obj.price = ynew[0]
			obj.save()
			data = float("{:.2f}".format(ynew[0]))
			return render(request, 'show_prediction.html', {'data': data})
		else:
			print(form.errors)
	return render(request, 'add_house.html', {'form': form})
