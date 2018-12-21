# Generated by Django 2.1.3 on 2018-11-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=50)),
                ('credits', models.FloatField()),
                ('course_description', models.TextField()),
                ('course_outcomes', models.TextField()),
                ('course_URL', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('college', models.ForeignKey(on_delete='CASCADE', related_name='courses', to='loginregister.College')),
                ('created_by', models.ForeignKey(on_delete='CASCADE', related_name='addedcourses', to='loginregister.User')),
                ('department', models.ForeignKey(on_delete='CASCADE', related_name='courses', to='loginregister.Dept')),
                ('prereqs', models.ManyToManyField(related_name='_course_prereqs_+', to='Courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credits', models.FloatField()),
                ('college', models.ForeignKey(on_delete='cascade', related_name='degrees', to='loginregister.College')),
                ('reqcourses', models.ManyToManyField(related_name='requiredfordegree', to='Courses.Course')),
            ],
        ),
    ]
