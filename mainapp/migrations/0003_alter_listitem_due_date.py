# Generated by Django 4.1.7 on 2023-04-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_listitem_description_alter_todolist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]