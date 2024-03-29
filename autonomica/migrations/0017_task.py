# Generated by Django 3.2 on 2021-04-15 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autonomica', '0016_auto_20210412_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('modified', models.CharField(max_length=100)),
                ('macro_name', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomica.screen')),
            ],
        ),
    ]
