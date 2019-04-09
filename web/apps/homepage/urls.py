from django.conf.urls import url

from web.apps.homepage.viewclasses import homepageviews

urlpatterns = [
    url(r'', homepageviews.HomePageView.as_view()),
]