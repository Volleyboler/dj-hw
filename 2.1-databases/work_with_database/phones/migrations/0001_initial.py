# Generated by Django 5.0.1 on 2024-03-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('release_date', models.DateTimeField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
