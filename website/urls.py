
from django.urls import path
from website.views import *


app_name = 'website'
urlpatterns = [
    path('home', home_view, name="home"),
    path('about us', aboutus_view, name="about"),
    path('factor', factor_view, name="factor"),
    path('panel', panel_view, name="panel"),
    path('questions', questions_view, name="questions"),
    path('ticket/<int:pid>', ticket_view, name="ticket"),
]
