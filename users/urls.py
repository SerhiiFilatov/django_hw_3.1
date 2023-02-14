from django.conf.urls.static import static
from django.urls import path
from users.views import *



urlpatterns = [
    path('signin/', sign_in_f, name='sign_in'),
    path('signup/', sign_up_f, name='sign_up'),
    path("log_out/", logout_f, name="log_out")
]


