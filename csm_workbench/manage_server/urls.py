from django.conf.urls import include, url
from manage_server.views import IndexView
urlpatterns = [
    url(r'^$', IndexView.as_view(),name="index"),
]