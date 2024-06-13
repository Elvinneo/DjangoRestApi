from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from movies.views import movies_view,add__movie__view,api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies-api/',include('movies.api.urls')),
    path('movies/',movies_view,name='movies'),
    path('addmovie/',add__movie__view,name='addmovie'),
    path('withapi/',api_view,name='withapi'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)