# Generated by Django 4.2.1 on 2024-04-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='NameOfProduct')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('price', models.CharField(max_length=10, verbose_name='Price')),
                ('img1', models.ImageField(upload_to='images/')),
                ('img2', models.ImageField(upload_to='images/')),
                ('img3', models.ImageField(upload_to='images/')),
                ('dateOfPublic', models.DateField(verbose_name='DateOfPublic')),
                ('discount', models.CharField(max_length=10, verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
