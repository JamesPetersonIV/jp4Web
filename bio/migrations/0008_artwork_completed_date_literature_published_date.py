# Generated by Django 5.1.2 on 2025-03-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_delete_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='literature',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
