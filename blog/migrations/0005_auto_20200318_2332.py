# Generated by Django 3.0.4 on 2020-03-18 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200318_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makecomment',
            old_name='Comments',
            new_name='Comments_id',
        ),
    ]