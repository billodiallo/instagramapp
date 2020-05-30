from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^accounts/profile/', views.add_profile, name='add_profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.get_image_by_id,name ='image'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^upload/', views.update_image, name='upload'),
    url(r'^comment/(?P<pk>\d+)',views.add_comment,name='comment'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    url(r'^all/(?P<pk>\d+)', views.all, name='all'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    #
