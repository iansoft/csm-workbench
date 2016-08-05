from django.conf.urls import include, url
from manage_account.views import IndexView,service

urlpatterns = [
    url(r'^$', IndexView.as_view(),name="account"),
    url(r'^service/(?P<method>\w+)/$', service, name="service"),
]