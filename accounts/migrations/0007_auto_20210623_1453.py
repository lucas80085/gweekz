# Generated by Django 3.2.4 on 2021-06-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210623_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]