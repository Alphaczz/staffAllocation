# Generated by Django 4.0.3 on 2022-05-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timescale', '0010_alter_taskalloc_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskalloc',
            name='priority',
            field=models.FloatField(),
        ),
    ]
