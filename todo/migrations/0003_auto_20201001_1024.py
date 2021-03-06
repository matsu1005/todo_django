# Generated by Django 3.0.7 on 2020-10-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('todo', '0002_auto_20201001_1004'),
    # ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('target', models.DateTimeField(null=True)),
            ],
        ),
    ]