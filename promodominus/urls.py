from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from blog.models import Entrada
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from blog.sitemaps import BlogSitemap

admin.autodiscover()

info_dict = {
    'queryset': Entrada.objects.all(),
    'date_field': 'fecha_de_la_entrada',
}

sitemaps = {
    'index': BlogSitemap,
	'blog': GenericSitemap(info_dict, priority=0.6),
    
	
}

urlpatterns = patterns('',
    # urls del administrador
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # en esta url se encontaran las imagenes subidas
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
	),
    # urls del blog
    url(r'^$','blog.views.index'),
    url(r'^entrada/(?P<id_entrada>\d+)$','blog.views.detalle_entrada'),
    url(r'^usuario/$','blog.views.nuevo_usuario'),
    url(r'^login/$','blog.views.login'),
    url(r'^logout/$','blog.views.logout_sesion'),
    url(r'', include('robots_txt.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^', include('favicon.urls')),
    url(r'', include('social_auth.urls')),
)


