# Generated by Django 3.0.3 on 2020-05-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20200424_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('query', models.CharField(max_length=20000)),
            ],
        ),
    ]
