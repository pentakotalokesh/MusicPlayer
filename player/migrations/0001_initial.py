# Generated by Django 4.2.2 on 2023-06-16 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Thumbnail', models.ImageField(default='', upload_to='images')),
                ('songFile', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('access', models.CharField(choices=[('PB', 'PB'), ('PR', 'PR'), ('PT', 'PT')], default='PB', max_length=2)),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
