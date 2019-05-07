from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'),
  	url(r'^history/$',views.SearchListView.as_view(),name='history'),
    
  	url(r'^accounts/',include('django.contrib.auth.urls')),
  	url(r'^search/create/$', views.NotificationCreateView.as_view(), name='create'),
    url(r'^/signup$', views.signup, name='signup'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)