# Generated by Django 4.2 on 2023-04-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_sprcompetency_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprspecialization',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
