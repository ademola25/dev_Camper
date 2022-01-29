# Generated by Django 4.0.1 on 2022-01-28 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bootcamp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('weeks', models.CharField(max_length=255)),
                ('tuition', models.CharField(max_length=255)),
                ('minimumSkill', models.CharField(max_length=255)),
                ('scholarhipsAvailable', models.BooleanField(default=False)),
                ('bootcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bootcamp.bootcamp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
