# Generated by Django 4.0.6 on 2022-07-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('ticket_status', models.CharField(choices=[('p', 'pending'), ('c', 'complete'), ('ip', 'inprogress')], default='p', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=225)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('c', 'customer'), ('a', 'admin')], default='c', max_length=20)),
            ],
        ),
    ]
