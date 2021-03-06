# Generated by Django 3.0.6 on 2020-05-16 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=200)),
                ('images', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
                ('minamount', models.IntegerField()),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Publish'), ('False', 'Draft')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]
