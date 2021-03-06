# Generated by Django 3.2.7 on 2021-10-03 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateTimeField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storeapp.books')),
            ],
        ),
    ]
