# Generated by Django 4.1.7 on 2023-02-28 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Girlsband', 'verbose_name_plural': 'Girlsband'},
        ),
        migrations.AddField(
            model_name='people',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='people.category'),
        ),
    ]
