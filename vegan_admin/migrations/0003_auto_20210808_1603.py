# Generated by Django 3.2.6 on 2021-08-08 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegan_admin', '0002_add_report'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Add',
        ),
        migrations.RemoveField(
            model_name='market_comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Market_Post',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='Market_Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
