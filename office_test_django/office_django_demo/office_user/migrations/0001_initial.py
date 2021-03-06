# Generated by Django 3.1.2 on 2020-10-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户昵称')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('user', models.CharField(max_length=14, verbose_name='用户名称')),
                ('telephone', models.CharField(db_index=True, max_length=11, unique=True, verbose_name='手机号')),
                ('id_card', models.CharField(blank=True, db_index=True, max_length=18, unique=True, verbose_name='身份证')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('email', models.EmailField(blank=True, max_length=50, unique=True, verbose_name='电子邮件')),
                ('is_active', models.BooleanField(max_length=1, verbose_name='活跃用户')),
                ('is_staff', models.BooleanField(max_length=1, verbose_name='关闭用户')),
                ('date_joined', models.DateTimeField(default='2018/09/04 14:55:55', verbose_name='加入日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': '用户配置',
                'verbose_name_plural': '用户配置',
            },
        ),
    ]
