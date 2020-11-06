from django.urls import path
from . import views as bitly
from django.views.decorators.csrf import csrf_exempt

app_name = 'bitly'

urlpatterns = [
    path('', bitly.main),
    path('link/', csrf_exempt(bitly.link)),
    path('link/<link>', csrf_exempt(bitly.link)),
]
