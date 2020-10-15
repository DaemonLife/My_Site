from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Data')

    # * foreignkey
    rubric = models.ForeignKey('Rubric', null=True, 
    on_delete=models.PROTECT, verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Ads'
        verbose_name = 'Ad'
        ordering = ['-published']

class Rubric(models.Model):

    # ? there is invisible pk (primary key == id)? Becouse there is 
    # ? foreignkey in Bb

    name = models.CharField(max_length=20, db_index=True,
    verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']

    