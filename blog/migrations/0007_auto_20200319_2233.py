# Generated by Django 3.0.4 on 2020-03-19 19:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200318_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]