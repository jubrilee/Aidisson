# Generated by Django 2.0.6 on 2018-07-19 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20180719_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_datetime', models.DateTimeField(auto_now=True)),
                ('units', models.CharField(choices=[('lbs', 'pounds'), ('kg', 'kilograms')], default='lbs', max_length=3)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Trainee')),
            ],
        ),
    ]
