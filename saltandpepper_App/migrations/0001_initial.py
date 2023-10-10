# Generated by Django 4.2.4 on 2023-08-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pImage', models.URLField()),
            ],
        ),
    ]
