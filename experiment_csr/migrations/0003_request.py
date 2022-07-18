# Generated by Django 4.0.5 on 2022-07-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment_csr', '0002_alter_csr_set_issuer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(help_text='enter url', max_length=264)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('state', models.CharField(blank=True, max_length=64)),
                ('org_name', models.CharField(blank=True, max_length=64)),
                ('org_unit', models.CharField(blank=True, max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('certificate', models.TextField(unique=True)),
            ],
        ),
    ]