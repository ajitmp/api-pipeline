# Generated by Django 2.2.28 on 2024-08-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=2048)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
