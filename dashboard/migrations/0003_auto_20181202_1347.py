# Generated by Django 2.1.3 on 2018-12-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_course_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_dashboard',
            name='course_average',
            field=models.CharField(default='-', max_length=15),
        ),
        migrations.AlterField(
            model_name='course_dashboard',
            name='exam_average',
            field=models.CharField(default='-', max_length=15),
        ),
    ]