# Generated by Django 3.1.6 on 2021-05-02 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical', '0003_auto_20210502_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='user',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
