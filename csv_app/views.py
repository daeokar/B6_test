import csv , io
from cgitb import text
from os import name
# from distutils.command.upload import upload
from re import template
from urllib import response

from django.http import HttpResponse
from django.shortcuts import render

from csv_app.models import Emplayees
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request , template_name="home.html")


def csv_export(request):
    all_active_data = Emplayees.objects.filter(active= True)
    # print(all_active_data)
    # return HttpResponse(all_active_data)
    response = HttpResponse(content_type="text/csv")
    csv_writer = csv.writer(response)
    csv_writer.writerow(["Id" , "Name" , "Salary" , "Company" , "Designation" , "DOJ" , "Active"])


    for emp in all_active_data.values_list("id", "name", "salary", "company", "designation", "DOJ", "active"):
        csv_writer.writerow(emp)

    response['Content-Disposition'] = "attachment; filename= 'Employee_data.csv"
    return response


def upload_csv(request):
    template = "upload.html"
    data = Emplayees.objects.all()
    prompt = {'order': 'Order of the CSV should be id, name, salary, company, designation, DOJ , activa','employees': data }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Emplayees.objects.update_or_create(
        id=column[0],
        name=column[1],
        salary=column[2],
        company=column[3],
        designation=column[4],
        DOJ=column[5],
        active=column[6])
    context = {}
    return render(request, template, context)











