# Generated by Django 5.0.6 on 2024-07-12 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsappSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='WhatsappApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whatsapp_api.whatsappsession')),
            ],
        ),
        migrations.RenameField(
            model_name='whatsappsession',
            old_name='number',
            new_name='wp_id',
        )
    ]
