# Generated by Django 3.1.3 on 2024-05-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.TextField(blank=True)),
                ('status', models.TextField(blank=True)),
            ],
        ),
    ]