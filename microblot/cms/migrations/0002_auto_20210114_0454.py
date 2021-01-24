# Generated by Django 3.1.5 on 2021-01-14 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="site",
            field=models.OneToOneField(
                default="", on_delete=django.db.models.deletion.CASCADE, to="sites.site"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="short_code",
            field=models.CharField(default="", max_length=16),
            preserve_default=False,
        ),
    ]