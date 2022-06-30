# Generated by Django 3.2.13 on 2022-06-24 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workspaces',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('kind', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'workspace',
                'verbose_name_plural': 'workspaces',
            },
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataField', models.DateField(auto_now_add=True)),
                ('yearField', models.CharField(max_length=4)),
                ('monthField', models.CharField(max_length=2)),
                ('dayOfMonth', models.CharField(max_length=2)),
                ('dayOfWeek', models.CharField(max_length=1)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.workspaces')),
            ],
            options={
                'verbose_name': 'visits',
            },
        ),
    ]
