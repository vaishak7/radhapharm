# Generated by Django 4.0.5 on 2022-08-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=200)),
                ('Number', models.IntegerField(max_length=100)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
