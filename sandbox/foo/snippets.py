from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtailcloudinary.fields import CloudinaryField, CloudinaryWidget


@register_snippet
class ImageSnippet(models.Model):
    image = CloudinaryField()
    
    panels = [
        FieldPanel('image', widget=CloudinaryWidget),
    ]