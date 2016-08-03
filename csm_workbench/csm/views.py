# _*_ coding: utf-8 _*_
from django.views.generic.base import TemplateView
from api.menu import set_menu

class CSMView(TemplateView):
    def __init__(self):
        # self.roles = roles
        # self.menu = menu
        self.role, self.menu = self._roles_menu()

    def dispatch(self, request, *args, **kwargs):
        return super(CSMView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CSMView, self).get_context_data(**kwargs)
        context['menu_list'] = set_menu(self.role, self.menu)
        context["role"] = self.role
        context["menu"] = self.menu
        return context