# Generated by Django 4.0.6 on 2022-08-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0009_letterreview_like_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="letter",
            name="color",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="letter",
            name="font_family",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="letter",
            name="font_size",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
