from django.urls import path

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'teachersapp'
urlpatterns = [
    #Sample
    path('Sample/', views.sampleMethod, name='sample_path1'),
    path('Sample2/', views.sampleMethod, name='sample_path2'),
] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
