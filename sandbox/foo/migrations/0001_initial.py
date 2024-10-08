# Generated by Django 2.1.5 on 2019-01-18 14:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtailcloudinary.blocks
import wagtailcloudinary.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
    ]

    operations = [
        migrations.CreateModel(
            name="FooPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("image", wagtailcloudinary.fields.CloudinaryField(max_length=255)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [("image", wagtailcloudinary.blocks.CloudinaryImageBlock())]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
