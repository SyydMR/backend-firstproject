
from django.urls import path
from website.views import *
urlpatterns = [
    # path('test/', http_test),
    # path('json-test/', json_test)
    path('home', home_view, name="home"),
    path('about us', aboutus_view, name="about"),
    path('factor', factor_view, name="factor"),
    path('panel', panel_view, name="panel"),
    path('questions', questions_view, name="questions"),
    path('signup', signup_view, name="signup"),
    path('buy ticket', ticket_view, name="ticket"),
    path('login', login_view, name="login"),
]
