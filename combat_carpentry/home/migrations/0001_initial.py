# Generated by Django 3.1.3 on 2020-11-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('image', models.ImageField(upload_to='service')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=25)),
                ('headline', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='post')),
                ('description', models.TextField(null=True)),
                ('customer', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.service')),
            ],
        ),
    ]