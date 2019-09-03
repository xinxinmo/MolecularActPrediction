# Generated by Django 2.2.1 on 2019-08-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merckchallengeapp', '0006_auto_20190829_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='compound_act',
        ),
        migrations.CreateModel(
            name='ProteinCompound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('compound_id', models.ForeignKey(on_delete='models.CASCADE', to='merckchallengeapp.Compound')),
                ('protein_id', models.ForeignKey(on_delete='models.CASCADE', to='merckchallengeapp.Protein')),
            ],
        ),
        migrations.AddField(
            model_name='protein',
            name='compounds',
            field=models.ManyToManyField(through='merckchallengeapp.ProteinCompound', to='merckchallengeapp.Compound'),
        ),
    ]