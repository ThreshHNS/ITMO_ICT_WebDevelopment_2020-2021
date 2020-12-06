# Generated by Django 3.1.4 on 2020-12-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20, verbose_name='Возраси')),
                ('gender', models.CharField(choices=[('MALE', 'Мальчик'), ('FEMALE', 'Девочка')], default='MALE', max_length=14, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]