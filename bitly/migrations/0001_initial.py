# Generated by Django 3.0.4 on 2020-11-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000, verbose_name='link')),
                ('status', models.BooleanField(default=True, verbose_name='state link')),
                ('short_link', models.CharField(max_length=1000, unique=True, verbose_name='short_link')),
            ],
        ),
    ]
