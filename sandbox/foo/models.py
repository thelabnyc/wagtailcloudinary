from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtailcloudinary.fields import CloudinaryField, CloudinaryWidget
from wagtailcloudinary.blocks import CloudinaryImageBlock, CloudinarySnippetChooserBlock
from wagtail.api import APIField

from .snippets import ImageSnippet


class FooPage(Page):
    image = CloudinaryField()
    body = StreamField([
        ('image', CloudinaryImageBlock()),
        ('snippet_image', CloudinarySnippetChooserBlock(ImageSnippet)),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('image', widget=CloudinaryWidget),
        StreamFieldPanel('body'),
    ]

    api_fields = [
        APIField('image'),
        APIField('body'),
    ]
