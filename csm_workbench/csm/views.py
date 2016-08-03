# _*_ coding: utf-8 _*_
from django.views.generic.base import TemplateView
from api.menu import get_dataset, set_menu, set_breadcrumb

class CSMView(TemplateView):
    def __init__(self):
        self.role, self.menu, self.page_title = self._page_variables()

    def dispatch(self, request, *args, **kwargs):
        return super(CSMView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CSMView, self).get_context_data(**kwargs)
        dataset = get_dataset(self.role)
        context['menu_list'] = set_menu(dataset, self.menu)
        context["page_title"] =  self.page_title
        # context["breadcrumb_list"] = set_breadcrumb(dataset, self.menu)
        return context