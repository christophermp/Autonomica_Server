# Generated by Django 3.2 on 2021-04-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autonomica', '0004_auto_20210411_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macro',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autonomica.device'),
        ),
    ]
