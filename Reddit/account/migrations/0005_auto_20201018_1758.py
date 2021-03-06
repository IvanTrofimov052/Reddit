# Generated by Django 3.1 on 2020-10-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_userthatconfirmemail_confirm_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session', models.CharField(max_length=100)),
                ('user_age', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=100)),
                ('number_attempts', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='userthatconfirmemail',
            name='confirm_code',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
