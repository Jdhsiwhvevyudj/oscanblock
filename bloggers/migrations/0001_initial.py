# Generated by Django 4.1.7 on 2023-03-18 10:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')),
                ('birth_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('register_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('posts_count', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
