# Generated by Django 3.1 on 2020-11-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments_text',
            new_name='comment_text',
        ),
    ]
