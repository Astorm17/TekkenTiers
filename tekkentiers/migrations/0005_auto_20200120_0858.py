# Generated by Django 3.0.2 on 2020-01-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekkentiers', '0004_remove_tierlist_tierdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='tierlist',
            name='rows',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tierlist',
            name='tiers',
            field=models.TextField(default=''),
        ),
    ]
