from django.contrib.sitemaps import Sitemap
from blog.models import Entrada
from django.core.urlresolvers import reverse

from datetime import datetime

class BlogSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5
	
	def items(self):
		return Entrada.objects.order_by('-fecha_de_la_entrada')[:1]
		
	def lastmod(self, obj):
		return datetime.now()
		
	def location(self, obj):
		return '/'
		
