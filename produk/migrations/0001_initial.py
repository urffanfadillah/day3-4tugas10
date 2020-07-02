# Generated by Django 2.2.12 on 2020-07-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=25)),
                ('keterangan', models.TextField()),
                ('harga', models.IntegerField()),
                ('jumlah', models.PositiveIntegerField()),
            ],
        ),
    ]