# Generated by Django 3.1.5 on 2021-01-22 05:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('room_name', models.TextField(blank=True, null=True)),
                ('members', models.BigIntegerField(blank=True, null=True)),
                ('entry_fee', models.IntegerField(default=0)),
                ('total_fee', models.BigIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'room',
                'ordering': ['id'],
            },
        ),
    ]
