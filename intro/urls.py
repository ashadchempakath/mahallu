from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('',views.index, name="introd"),
    path('instruction',views.instruction),
    path('contact',views.contact),
    path('about',views.about),
    
]
