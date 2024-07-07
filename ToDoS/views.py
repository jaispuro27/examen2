from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Pending
from .forms import PendingForm

class PendingDetailView(DetailView):
    model = Pending
    template_name = 'pending_detail.html'
    context_object_name = 'pending' 
    
class PendingListViewIDs(ListView):
    model = Pending
    template_name = 'pending_list.html'
    context_object_name = 'pendings'

class PendingListViewIDsTitles(ListView):
    model = Pending
    template_name = 'pending-id-titles.html'
    context_object_name = 'pendings'

class PendingListViewUnresolved(ListView):
    model = Pending
    template_name = 'pending-unresolved.html'
    context_object_name = 'pendings'
    queryset = Pending.objects.filter(is_resolved=False)

class PendingListViewResolved(ListView):
    model = Pending
    template_name = 'pending-resolved.html'
    context_object_name = 'pendings'
    queryset = Pending.objects.filter(is_resolved=True)

class PendingListViewIDsUsers(ListView):
    model = Pending
    template_name = 'pending-id-userid.html'
    context_object_name = 'pendings'

class PendingListViewResolvedIDsUsers(ListView):
    model = Pending
    template_name = 'pending-id-userid-resolved.html'
    context_object_name = 'pendings'
    queryset = Pending.objects.filter(is_resolved=True)

class PendingListViewUnresolvedIDsUsers(ListView):
    model = Pending
    template_name = 'pending-id-userid-unresolved.html'
    context_object_name = 'pendings'
    queryset = Pending.objects.filter(is_resolved=False)

class PendingCreateView(CreateView):
    model = Pending
    form_class = PendingForm
    template_name = 'pending_form.html'
    success_url = reverse_lazy('index')

def apis_index(request):
    return render(request, 'apisindex.html')