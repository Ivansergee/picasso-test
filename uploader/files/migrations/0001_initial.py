# Generated by Django 4.2.5 on 2023-09-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/%d%m%y/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
    ]
