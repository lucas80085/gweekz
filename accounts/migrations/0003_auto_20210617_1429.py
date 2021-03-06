# Generated by Django 3.2.4 on 2021-06-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210609_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumermore',
            name='make',
        ),
        migrations.RemoveField(
            model_name='consumermore',
            name='model',
        ),
        migrations.RemoveField(
            model_name='consumermore',
            name='year',
        ),
        migrations.RemoveField(
            model_name='creatormore',
            name='gadgets',
        ),
        migrations.AddField(
            model_name='creatormore',
            name='console',
            field=models.CharField(choices=[('PC', 'Pc'), ('PLAYSTATION', 'Playstation'), ('XBOX', 'Xbox'), ('OTHERS', 'Others')], default='PC', max_length=50, verbose_name='Console'),
        ),
        migrations.AddField(
            model_name='creatormore',
            name='description',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AddField(
            model_name='creatormore',
            name='game',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='creatormore',
            name='hours_played',
            field=models.IntegerField(default=0, verbose_name='Hours Played'),
        ),
        migrations.AddField(
            model_name='creatormore',
            name='pictures',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='creatormore',
            name='rank',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('CREATOR', 'Creator'), ('CONSUMER', 'Consumer')], default='CONSUMER', max_length=50, verbose_name='Type'),
        ),
    ]
