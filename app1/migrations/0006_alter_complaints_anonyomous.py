# Generated by Django 4.2.2 on 2023-08-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_complaints_complainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='anonyomous',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
