# Generated by Django 3.0.4 on 2020-04-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('image', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default='This is good games'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]