from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)
    rate = models.DecimalField(decimal_places=4, max_digits=7)

    def __str__(self):
        return f"{self.name} - {self.rate}"

    class Meta:
        ordering = ['-id']
