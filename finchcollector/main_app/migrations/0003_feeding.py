# Generated by Django 4.2.4 on 2023-08-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_finch_habitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(max_length=1)),
            ],
        ),
    ]
