# Generated by Django 2.2.1 on 2019-08-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merckchallengeapp', '0003_auto_20190829_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='id',
        ),
        migrations.RemoveField(
            model_name='protein',
            name='id',
        ),
        migrations.AlterField(
            model_name='compound',
            name='compound_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='protein',
            name='protein_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
