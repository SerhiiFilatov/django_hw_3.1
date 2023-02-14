from django.conf.urls.static import static
from django.urls import path

from tasks.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('task_form_c/', task_create_form, name='task_create'),
    path('<uuid:pk>/', task_detail, name='task_det'),
    path('<uuid:pk>/update', task_update_form, name='task_upd'),
]

