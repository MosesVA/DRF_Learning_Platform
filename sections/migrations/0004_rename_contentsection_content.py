# Generated by Django 5.0.9 on 2024-12-26 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_alter_contentsection_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContentSection',
            new_name='Content',
        ),
    ]
