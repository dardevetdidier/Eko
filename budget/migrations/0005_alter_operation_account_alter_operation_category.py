# Generated by Django 4.0.2 on 2022-02-24 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_rename_budget_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations_account', to='budget.account'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations_category', to='budget.category'),
        ),
    ]