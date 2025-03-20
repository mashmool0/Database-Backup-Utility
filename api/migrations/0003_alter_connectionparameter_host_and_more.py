# Generated by Django 5.1.7 on 2025-03-20 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_backuphistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionparameter',
            name='host',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='connectionparameter',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='connectionparameter',
            name='port',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='connectionparameter',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
