# Generated by Django 4.0.2 on 2022-02-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_alter_operation_account_alter_operation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(choices=[('Withdraw', 'Débit'), ('Credit', 'Crédit')], default='Crédit', max_length=8),
        ),
    ]