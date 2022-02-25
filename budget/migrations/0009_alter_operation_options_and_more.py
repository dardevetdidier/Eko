# Generated by Django 4.0.2 on 2022-02-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_alter_operation_operation_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(choices=[('Débit', 'Débit'), ('Crédit', 'Crédit')], default='Débit', max_length=8),
        ),
    ]
