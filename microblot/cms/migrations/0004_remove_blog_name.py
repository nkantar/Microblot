# Generated by Django 3.1.5 on 2021-01-14 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0003_remove_blog_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="name",
        ),
    ]
