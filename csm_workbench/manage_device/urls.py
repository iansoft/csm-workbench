from django.conf.urls import include, url
from manage_device.views import IndexView
urlpatterns = [
    url(r'^$', IndexView.as_view(),name="device"),
]