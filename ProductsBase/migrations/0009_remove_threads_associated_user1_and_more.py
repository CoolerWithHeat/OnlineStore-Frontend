# Generated by Django 4.1.7 on 2023-05-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsBase', '0008_alter_messages_options_alter_threads_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threads',
            name='associated_user1',
        ),
        migrations.RemoveField(
            model_name='threads',
            name='associated_user2',
        ),
        migrations.DeleteModel(
            name='messages',
        ),
        migrations.DeleteModel(
            name='Threads',
        ),
    ]
