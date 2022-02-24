# Generated by Django 4.0.2 on 2022-02-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_alter_operation_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(choices=[('Withdraw', 'Débit'), ('Credit', 'Crédit')], default='Withdraw', max_length=8),
        ),
    ]