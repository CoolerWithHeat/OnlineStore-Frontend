# Generated by Django 4.1.7 on 2023-05-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsBase', '0012_user_channellayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='SupportStaff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='ChannelLayer',
            field=models.CharField(blank=True, default='Need Attention here!', max_length=20, null=True),
        ),
    ]
