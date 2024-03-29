# Generated by Django 3.2 on 2021-04-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autonomica', '0020_auto_20210417_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='colors',
            field=models.CharField(choices=[('danger', 'Red'), ('success', 'Green'), ('info', 'Blue'), ('warning', 'Yellow')], default='danger', help_text='If you want a other button color you can select it here.', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(help_text='If PulseRelay message will be an INT representing Rout JNIOR', max_length=100),
        ),
    ]
