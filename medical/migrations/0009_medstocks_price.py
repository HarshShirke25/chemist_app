# Generated by Django 3.1.6 on 2021-05-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_medstocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='medstocks',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]
