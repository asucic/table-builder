# Generated by Django 4.2.3 on 2023-07-14 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='columns',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='TableRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=dict)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_tables.table')),
            ],
        ),
    ]
