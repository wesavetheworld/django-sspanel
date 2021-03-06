# Generated by Django 2.0 on 2018-02-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0003_auto_20180220_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('ip', models.CharField(max_length=128, verbose_name='设备ip')),
                ('user', models.CharField(max_length=128, verbose_name='用户名')),
                ('log_time', models.DateTimeField(auto_now=True, verbose_name='日志时间')),
            ],
        ),
    ]
