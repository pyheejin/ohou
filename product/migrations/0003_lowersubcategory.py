# Generated by Django 3.0.8 on 2020-07-13 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200713_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowerSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lower_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.LowerCategory')),
            ],
            options={
                'db_table': 'lower_sub_categories',
            },
        ),
    ]
