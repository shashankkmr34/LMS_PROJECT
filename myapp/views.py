from django.shortcuts import render, redirect
from .models import Sales
from .models import Leads
from .forms import SalesForm
from .forms import LeadsForm


def welcome(request):
    return render(request, "welcome.html")


def load_form_sales(request):
    form = SalesForm
    return render(request, "index.html", {'form': form})


def load_form_leads(request):
    form = LeadsForm
    return render(request, "index_leads.html", {'form': form})


def addsales(request):
    form = SalesForm(request.POST)
    form.save()
    return redirect('/show')


def addleads(request):
    form = LeadsForm(request.POST)
    form.save()
    return redirect('/show_leads')


def show(request):
    sales = Sales.objects.all
    return render(request, 'show.html', {'sales': sales})


def show_leads(request):
    leads = Leads.objects.all
    return render(request, 'show_leads.html', {'leads': leads})


def edit(request, id):
    sales = Sales.objects.get(id=id)
    return render(request, 'edit.html', {'sales': sales})


def edit_leads(request, id):
    leads = Leads.objects.get(id=id)
    return render(request, 'edit_leads.html', {'leads': leads})


def update(request, id):
    sales = Sales.objects.get(id=id)
    form = SalesForm(request.POST, instance=sales)
    form.save()
    return redirect('/show')


def update_leads(request, id):
    leads = Leads.objects.get(id=id)
    form = LeadsForm(request.POST, instance=leads)
    form.save()
    return redirect('/show_leads')

def delete(request, id):
    sales = Sales.objects.get(id=id)
    sales.delete()
    return redirect('/show')

def delete_leads(request, id):
    leads = Leads.objects.get(id=id)
    leads.delete()
    return redirect('/show_leads')
