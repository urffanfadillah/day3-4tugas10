from django.db import models

# Create your models here.
class Produk(models.Model):
    nama_produk     = models.CharField(max_length=25)
    keterangan      = models.TextField()
    harga           = models.IntegerField()
    jumlah          = models.PositiveIntegerField()

    def __str__(self):
        return self.nama_produk