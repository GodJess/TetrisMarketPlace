# Generated by Django 4.2.3 on 2024-04-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_salesman_salername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesman',
            name='salerName',
            field=models.CharField(default='', max_length=30, verbose_name=' Name'),
        ),
    ]
