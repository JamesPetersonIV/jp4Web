# Generated by Django 4.1.3 on 2023-07-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0005_delete_collection_alter_literature_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('summary', models.TextField()),
                ('category', models.CharField(blank=True, choices=[('Characters', 'Characters'), ('Furniture', 'Furniture'), ('Structures', 'Structures'), ('Buildings', 'Buildings'), ('Objects', 'Objects')], default=False, max_length=200)),
                ('obj', models.FileField(blank=True, null=True, upload_to='obj')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Models',
            },
        ),
    ]