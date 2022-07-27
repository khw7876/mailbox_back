# Generated by Django 4.0.6 on 2022-07-27 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0007_alter_letterreviewlike_letter_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="letterreviewlike",
            name="letter_review",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_page.letterreview"
            ),
        ),
        migrations.AlterField(
            model_name="worrycategory",
            name="cate_name",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
