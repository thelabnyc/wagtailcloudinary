from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtailcloudinary.fields import CloudinaryField
from wagtailcloudinary.widgets import AdminCloudinaryChooser
from wagtailcloudinary.blocks import CloudinaryImageBlock, CloudinarySnippetChooserBlock
from wagtail.api import APIField

from .snippets import ImageSnippet


class FooPage(Page):
    image = CloudinaryField(blank=True)
    body = StreamField(
        [
            ("image", CloudinaryImageBlock(required=False)),
            ("snippet_image", CloudinarySnippetChooserBlock(ImageSnippet)),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image", widget=AdminCloudinaryChooser),
        FieldPanel("body"),
    ]

    api_fields = [
        APIField("image"),
        APIField("body"),
    ]
