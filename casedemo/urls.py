
# http://127.0.0.1:8000/

from django.contrib import admin
from . import views
from rest_framework_swagger.views import get_swagger_view
from django.urls import path


schema_view = get_swagger_view(title="API")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('foursquare-api/', views.home),
    #path('', schema_view)
    path('', views.home)
]
