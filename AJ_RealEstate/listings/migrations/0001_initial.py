# Generated by Django 2.2.10 on 2020-10-16 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.BooleanField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_published', models.BooleanField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('list_date', models.DateTimeField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor')),
            ],
        ),
    ]