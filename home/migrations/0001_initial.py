# Generated by Django 4.2.2 on 2023-10-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('mrp', models.IntegerField()),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], default='Red', max_length=20)),
            ],
        ),
    ]