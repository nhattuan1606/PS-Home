# Generated by Django 3.2.8 on 2021-12-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
