# Generated by Django 5.2 on 2025-06-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_passwordresetcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='adstatus',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adstatus',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adstatus',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='adstatus',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
