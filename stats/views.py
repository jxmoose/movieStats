from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests
from . import util
import logging
import csv

# Create your views here.
def index(request):
	#util.process([])
	return render(request, "stats/index.html")

def imdb(request):
	if request.method=="GET":
		return render(request, "stats/imdb.html")
	try:
		link = imdb_link(request.POST)
		if not link.is_valid():
			messages.error(request,'Link not valid')
			return HttpResponseRedirect(reverse('imdb'))
		list_id = link.split('/')[-2]
		try:
			url = "https://imdb-api.com/API/IMDbList/k_nvwbbfzq/" + list_id
			response = requests.GET(url)
		except:
			messages.error(request, "Your URL did not work. Either your list is private or you entered a wrong URL. Please try again")
			return HttpResponseRedirect(reverse('imdb'))

	except Exception as E:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
	
	return HttpResponseRedirect(reverse('imdb'))	

def about(request):
	return render(request, "stats/about.html")

def letterboxd(request):
	return render(request, "stats/letterboxd.html")

def import_csv(request):
	if request.method=="GET":
		return render(request, "stats/import_csv.html")
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse('import_csv'))

		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("import_csv"))

		file_data = csv_file.read().decode("utf-8")	
		lines = file_data.split("\n")
		movie_list = []	
		if "Title" not in lines[0] and "Name" not in lines[0]:
			messages.error(request, "Your list did not include a 'Title' (movie title) Column")
			return HttpResponseRedirect(reverse('import_csv'))
		for line in lines:
			fields = line.split(",")
			movie_list.append(fields)
		util.process(movie_list)
		print("DONE")

		

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
	
	return HttpResponseRedirect(reverse('import_csv'))