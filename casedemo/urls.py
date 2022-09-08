
# http://127.0.0.1:8000/

from django.contrib import admin
from . import views
from rest_framework_swagger.views import get_swagger_view
from django.urls import path


schema_view = get_swagger_view(title="API")


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('foursquare-api/', views.home),
    #path('', schema_view)
    path('', views.home)
]

#urlpatterns = [
    #path('home/', schema_view, name='some_name'),
    #path('admin/', admin.site.urls),
    # regex for swagger creation
    #path('', schema_view), #url in swagger
    #path('question_list/', views.home, name='question_list')
    #]