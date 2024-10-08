# Generated by Django 5.0.6 on 2024-05-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0007_remove_employee_name_admin_image_admin_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_rewiews',
            field=models.BooleanField(default=False, verbose_name='has_rewiews'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
    ]
