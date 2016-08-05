# _*_ coding: utf-8 _*_
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from csm.views import CSMView
from api.auth import get_role_list, get_domain_list, create_account

class IndexView(CSMView):
    template_name = 'manage_account/index.html'
    
    def _page_variables(self):
        return "admin", "Account", "Manage Account"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["role_list"] = get_role_list()
        context["domain_list"] = get_domain_list()
        return context

def service(request,method):
    '''
        the repsonse:
            status:0:success 1:failed
            message:
    '''
    reps = {
        "status": -1, 
        "message": ""
    }

    if method == "get_account_list":
        pass
    elif method == "create":
        data = json.loads(request.body)
        username = data["username"],
        account = {
            "username":data["username"],
            "password":data["password"],
            "domain":data["domain"],
            "role_id":data["role_id"]
        }
        # execuate create the account and return the status code 
        if create_account(account) == 0:
            reps["status"] = 0
            reps["message"] = "create the " + data["username"] + " successfully."
        else: 
            reps["status"] = 1
            reps["message"] = "create the " + data["username"] + " failed."
    
    return HttpResponse(json.dumps(reps))