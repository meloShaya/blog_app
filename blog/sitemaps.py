from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    # Define the change frequency of the posts in the sitemap
    changefreq = 'weekly'
    # Define the priority of the posts in the sitemap
    priority = 0.9

    def items(self):
        # Return all published posts to be included in the sitemap
        return Post.published.all()

    def lastmod(self, obj):
        # Return the last modified date of the post
        return obj.updated