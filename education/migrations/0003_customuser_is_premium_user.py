# Generated by Django 5.2.4 on 2025-07-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_customuser_age_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_premium_user',
            field=models.BooleanField(default=False),
        ),
    ]
