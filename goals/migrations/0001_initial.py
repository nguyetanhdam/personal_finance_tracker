# Generated by Django 4.2.7 on 2024-12-12 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('target_amount', models.IntegerField(blank=True, db_index=True, default=0, null=True)),
                ('saved_amount', models.IntegerField(blank=True, db_index=True, default=0, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'In Progress'), (2, 'Achieved')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
