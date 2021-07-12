# Generated by Django 3.0.3 on 2020-04-24 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20190901_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='coverimg1',
            field=models.ImageField(blank=True, upload_to='images/cover/1'),
        ),
        migrations.AddField(
            model_name='product',
            name='coverimg2',
            field=models.ImageField(blank=True, upload_to='images/cover/2'),
        ),
        migrations.AddField(
            model_name='product',
            name='coverimg3',
            field=models.ImageField(blank=True, upload_to='images/cover/3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]