# Generated by Django 2.2.5 on 2019-10-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands_app', '0003_auto_20191022_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='assumed_office',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='politician',
            name='donors',
            field=models.ManyToManyField(blank=True, to='brands_app.Company'),
        ),
    ]
