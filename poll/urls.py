from django.conf.urls import url
from . import views


urlpatterns = [
    # the row below shows the default opened file if nothing else
    # was specified by the url -> in this case index (in views.py)
    url(r'^$', views.index, name='index'),
]