# Generated by Django 3.2.4 on 2021-06-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DriverMore',
            new_name='ConsumerMore',
        ),
        migrations.RenameModel(
            old_name='SpyMore',
            new_name='CreatorMore',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Spy',
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('CREATOR', 'Creator'), ('CONSUMER', 'Consumer')], default='CREATOR', max_length=50, verbose_name='Type'),
        ),
    ]
