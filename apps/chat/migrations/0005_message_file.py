# Generated by Django 3.2.9 on 2023-07-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='chat_files/'),
        ),
    ]
