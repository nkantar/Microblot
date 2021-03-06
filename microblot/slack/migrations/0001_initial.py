# Generated by Django 3.1.5 on 2021-01-27 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SlackWorkspace",
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
                ("slack_id", models.CharField(max_length=16)),
                ("icon", models.CharField(max_length=512)),
                ("bot_user_id", models.CharField(max_length=128)),
                ("bot_access_token", models.CharField(max_length=128)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.blog"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SlackUser",
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
                ("slack_id", models.CharField(max_length=16)),
                ("icon", models.CharField(max_length=512)),
                ("slack_username", models.CharField(max_length=128)),
                ("real_name", models.CharField(max_length=128)),
                ("display_name", models.CharField(max_length=128)),
                ("avatar", models.CharField(max_length=512)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cms.author"
                    ),
                ),
                (
                    "workspace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="slack.slackworkspace",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
