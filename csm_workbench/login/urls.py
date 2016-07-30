from django.conf.urls import include, url
from login.views import IndexView
urlpatterns = [
    url(r'^$', IndexView.as_view(),name="index"),
]