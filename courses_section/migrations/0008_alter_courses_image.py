# Generated by Django 4.2.2 on 2023-07-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_section', '0007_alter_courses_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to='course_images'),
        ),
    ]
