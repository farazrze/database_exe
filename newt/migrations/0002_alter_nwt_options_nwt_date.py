# Generated by Django 5.0.3 on 2024-03-12 17:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nwt',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='nwt',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
