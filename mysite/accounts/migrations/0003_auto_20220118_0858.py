# Generated by Django 3.1.7 on 2022-01-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220118_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
