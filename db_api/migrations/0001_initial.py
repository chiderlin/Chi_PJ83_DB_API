# Generated by Django 2.1 on 2020-11-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainListAll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('AgentID', models.CharField(max_length=30, unique=True)),
                ('CodeToMatch', models.CharField(max_length=50, unique=True)),
                ('DomainListAPP', models.CharField(max_length=300)),
                ('DomainListInner', models.CharField(max_length=300)),
                ('DomainListOuter', models.CharField(max_length=300)),
                ('CreatedTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('DomainType', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'DomainListAll',
            },
        ),
        migrations.CreateModel(
            name='DomainTestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestTime', models.DateTimeField(blank=True, null=True)),
                ('UrlIn', models.CharField(max_length=200)),
                ('UrlOut', models.CharField(max_length=200)),
                ('MyIP', models.CharField(max_length=200)),
                ('MyZone', models.CharField(max_length=200)),
                ('CDN', models.CharField(max_length=200)),
                ('CDNIP', models.CharField(max_length=200)),
                ('PageLoadTime', models.FloatField()),
                ('Status', models.CharField(max_length=50)),
                ('IPScreenshot', models.CharField(max_length=300)),
                ('ProductScreenshot1', models.CharField(max_length=300)),
                ('ProductScreenshot2', models.CharField(max_length=300)),
                ('ProductScreenshot3', models.CharField(max_length=300)),
                ('CreatedTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('ProductScreenshot4', models.CharField(max_length=300)),
                ('DomainType', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'DomainTestLog',
            },
        ),
    ]
