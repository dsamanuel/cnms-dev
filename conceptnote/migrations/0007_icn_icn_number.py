# Generated by Django 4.2.10 on 2024-03-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conceptnote', '0006_alter_icn_approval_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='icn',
            name='icn_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
