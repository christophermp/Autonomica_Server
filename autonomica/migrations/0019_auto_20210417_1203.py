# Generated by Django 3.2 on 2021-04-17 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autonomica', '0018_auto_20210417_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macro',
            name='colors',
            field=models.CharField(choices=[('danger', 'Red'), ('success', 'Green'), ('info', 'Blue'), ('warning', 'Yellow')], default='danger', help_text='If you want a other button color you can select it here.', max_length=20),
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]