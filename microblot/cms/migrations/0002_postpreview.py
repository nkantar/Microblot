# Generated by Django 3.1.5 on 2021-01-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostPreview",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("body_markdown", models.TextField()),
                ("body_html", models.TextField()),
                ("short_code", models.CharField(max_length=16)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.author"
                    ),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.blog"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.category"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
