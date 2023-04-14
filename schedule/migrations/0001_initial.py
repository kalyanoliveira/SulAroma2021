# Generated by Django 3.2.6 on 2021-09-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('whenStart', models.DateTimeField()),
                ('whenEnd', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]