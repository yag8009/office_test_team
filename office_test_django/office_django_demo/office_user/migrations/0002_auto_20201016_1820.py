# Generated by Django 3.1.2 on 2020-10-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='加入日期'),
        ),
    ]
