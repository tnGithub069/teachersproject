from django.urls import path

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'teachersapp'
urlpatterns = [
    #Sample
    path('', views.v999_sampleMethod, name='index'),
    path('Sample/', views.v999_sampleMethod, name='sample_path1'),
    path('Sample2/', views.v999_sampleMethod2, name='sample_path2'),
    path('SystemError/', views.v999_systemError, name='systemError'),
] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
