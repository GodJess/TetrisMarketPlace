# Generated by Django 4.2.3 on 2024-04-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_salesman_phone_salesman_user_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesman',
            name='indif',
            field=models.CharField(default='', max_length=100, verbose_name='Индификатор'),
        ),
    ]
