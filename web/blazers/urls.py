import os
from django.conf.urls import include, url
from django.views.static import serve

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

urlpatterns = [
    url(r'^home/', include('apps.homepage.urls'))
]
