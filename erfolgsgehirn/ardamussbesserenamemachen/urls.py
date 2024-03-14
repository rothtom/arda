from django.urls import path
from . import views


urlpatterns = [
    #path(path on the website, view,function that renders the template and does serverside stuff, app_name.function_name)
    path("", views.index, name="homepage.index")
]
