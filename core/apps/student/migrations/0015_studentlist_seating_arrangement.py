# Generated by Django 4.0 on 2022-01-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_alter_student_middleschool_alter_student_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='seating_arrangement',
            field=models.CharField(default=' / / / / / / / / / / / / / / / / / / / / / / / ', max_length=10000),
        ),
    ]
