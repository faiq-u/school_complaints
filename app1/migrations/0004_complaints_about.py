# Generated by Django 4.2.2 on 2023-08-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_complaints_acceptable'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='about',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
