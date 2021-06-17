from django.conf.urls import url
from basic_app import views

# TEMPLATE RELATIVE URLs
app_name = "basicapp"

urlpatterns = [
    url(r'^other', views.other, name='other'),
    url(r'^relative', views.relative, name='relative'),
]
