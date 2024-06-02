# Generated by Django 5.0.6 on 2024-05-31 17:56

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_alter_zakazchik_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, default='news_images/photo_2023-05-23_14-28-57.jpg', null=True, upload_to='news_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proffesion', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, default='product_images/FCxARCPWYAEi9ux.jpg', null=True, upload_to='product_images/')),
                ('status', models.CharField(max_length=100)),
                ('amount', models.IntegerField(null=True)),
                ('product_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toys.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Rewiews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rewiew', models.CharField(max_length=1500)),
                ('date', models.DateField(null=True)),
                ('stars', models.PositiveSmallIntegerField(default=5, help_text='Rating from 1 to 5 stars', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toys.product')),
                ('zakazchik_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.zakazchik')),
            ],
        ),
    ]
