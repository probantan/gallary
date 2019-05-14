
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[    
    url('^$', views.index, name='welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\w+)/', views.get_image_by_location, name='locations'),
    url(r'^category/(\w+)/', views.category_results, name='categories'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
