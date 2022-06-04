# Generated by Django 4.0.3 on 2022-04-19 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timescale', '0002_alter_taskallocadmin_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskallocadmin',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentUsr', to=settings.AUTH_USER_MODEL),
        ),
    ]
