# Generated by Django 3.1.8 on 2021-05-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('alter_ego', models.CharField(max_length=30)),
                ('primary_ability', models.CharField(max_length=20)),
                ('secondary_ability', models.CharField(max_length=20)),
                ('catchphrase', models.CharField(max_length=100)),
            ],
        ),
    ]
