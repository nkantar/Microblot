# Generated by Django 3.0.7 on 2020-06-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200627_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slack_id',
            field=models.CharField(default='foo', max_length=128),
            preserve_default=False,
        ),
    ]