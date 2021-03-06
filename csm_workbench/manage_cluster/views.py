# _*_ coding: utf-8 _*_
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
#from django.views.generic import TemplateView
from csm.views import CSMView

class IndexView(CSMView):
    template_name = 'manage_cluster/index.html'
    
    def _page_variables(self):
        return "admin", "Cluster", "Manage Cluster"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context