# Generated by Django 4.2.4 on 2023-08-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_table_options_remove_table_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='num_of_reservations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest_count',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=2),
        ),
        migrations.AlterField(
            model_name='table',
            name='seats',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=2),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(unique=True),
        ),
    ]
