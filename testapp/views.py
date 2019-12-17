from django.shortcuts import render
from testapp.models import Client
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from testapp.forms import CreateForm
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from functools import reduce

class IndexView(ListView):
    model = Client
    template_name = 'testapp/home.html'

class UpdateView(UpdateView):
    model = Client
    form_class = CreateForm
    template_name = 'testapp/update.html'
    
    def get_success_url(self):
        return reverse('home')
    

class AddView(CreateView):
    model = Client
    form_class = CreateForm
    template_name = 'testapp/create.html'
    
    def get_success_url(self):
        return reverse('home')

def search(request):
    query = request.GET.get('q', '')
    select_option = request.GET['inputClient']   
    
    name_results = Client.objects.filter(client_name__contains=query)
    phone_results = Client.objects.filter(phone_number__contains=query)
    email_results = Client.objects.filter(email__contains=query)
    suburb_results = Client.objects.filter(address_suburb__contains=query)
    
    results = []
    

    if select_option == 'Name':
        for client in name_results:
            results.append(client)

    if select_option == 'Phone Number':
        for phone in phone_results:
            results.append(phone)
    
    if select_option == 'Email':
        for email in email_results:
            results.append(email)
    
    if select_option == 'Suburb':
         for suburb in suburb_results:
            results.append(suburb)       

        

    return render(request, 'testapp/search.html', {
        'results': results
        })
