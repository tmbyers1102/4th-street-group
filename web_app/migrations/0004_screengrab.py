# Generated by Django 3.1.1 on 2021-01-31 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_auto_20210129_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screengrab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_grab', models.ImageField(default='default_project_screen_grab.jpg', upload_to='screen_grabs')),
                ('assigned_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.project')),
            ],
        ),
    ]
