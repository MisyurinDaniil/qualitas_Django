# Generated by Django 4.0.5 on 2023-10-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductItem', '0003_alter_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ip',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Дата отзыва'),
        ),
    ]
