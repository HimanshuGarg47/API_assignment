# Generated by Django 4.1.7 on 2023-02-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='Self', max_length=255),
        ),
    ]
