# Generated by Django 3.2 on 2021-04-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autonomica', '0013_alter_screen_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macro',
            name='ip',
            field=models.CharField(help_text='This is the grey text', max_length=100),
        ),
    ]
