# Generated by Django 3.0.7 on 2020-10-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201001_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='target',
            field=models.DateTimeField(),
        ),
    ]