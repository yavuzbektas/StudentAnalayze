# Generated by Django 4.0 on 2022-02-01 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('student', '0001_initial'),
        ('attendance', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='LessonClassList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_classname', to='student.studentlist')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_lesson', to='lessons.lesson')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_profil', to='home.profil')),
            ],
        ),
        migrations.CreateModel(
            name='LessonPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessonplan_lessonclasslist', to='lessons.lessonclasslist')),
                ('lessonPeriods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessonplan_LessonPeriods', to='attendance.lessonperiods')),
            ],
        ),
    ]
