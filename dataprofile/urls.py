from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('',views.profileview),
    path('registration',views.registration),
    path('editlist',views.edit),
    path('editlist/<int:edit_id>',views.update ,name='update'),
    path('familyregistration',views.regfamily ),
    path('arearegistration',views.regarea ),
]
