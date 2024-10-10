# Generated by Django 5.1.2 on 2024-10-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('marca', models.CharField(max_length=50)),
                ('cantidad_min', models.IntegerField()),
                ('cantidad_max', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
