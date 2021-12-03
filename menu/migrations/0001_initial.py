# Generated by Django 3.2.9 on 2021-12-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, choices=[('food', 'food'), ('beverage', 'beverage'), ('fruit', 'fruit')], max_length=50, null=True)),
                ('subcategory', models.CharField(blank=True, choices=[('potato', 'food'), ('rice', 'rice'), ('yogurt', 'yogurt'), ('limca', 'limca'), ('coke', 'coke'), ('dew', 'dew'), ('mango', 'mango'), ('apple', 'apple'), ('banana', 'banana')], max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
