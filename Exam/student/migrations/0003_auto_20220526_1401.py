# Generated by Django 3.1.3 on 2022-05-26 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_stu_question_stuexam_db_sturesults_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='picture',
        ),
    ]
