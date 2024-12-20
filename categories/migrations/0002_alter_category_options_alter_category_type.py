# Generated by Django 4.2.7 on 2024-12-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.IntegerField(choices=[(1, 'Income'), (2, 'Expense')], default=1),
        ),
    ]
