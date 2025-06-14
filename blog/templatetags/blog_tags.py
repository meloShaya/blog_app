from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

# Register a simple template tag that returns the total number of published posts
@register.simple_tag
def total_posts():
    # Count the number of published posts
    return Post.published.count()

# Register an inclusion tag that renders the latest posts in a template
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    # Retrieve the latest 'count' number of published posts, ordered by publish date in descending order
    latest_posts = Post.published.order_by("-publish")[:count]
    # Return the latest posts to be included in the specified template
    return {"latest_posts": latest_posts}

# Register a simple template tag that returns the total number of comments
@register.simple_tag
def get_most_commented_posts(count=5):
    # Retrieve the 'count' number of posts with the most comments
    return Post.published.annotate(total_comments=Count("comments")).order_by("-total_comments")[:count]

# Register a filter that converts Markdown text to HTML
@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))