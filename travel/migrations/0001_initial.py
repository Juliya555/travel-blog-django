# Generated by Django 2.0.2 on 2018-02-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_number', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('why_go_description', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('fun_fact_description', models.CharField(blank=True, default=None, max_length=128, null=True)),
            ],
            options={
                'verbose_name_plural': 'Places',
                'verbose_name': 'Place',
            },
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/gallery')),
                ('place', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='travel.Place')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
            },
        ),
    ]
