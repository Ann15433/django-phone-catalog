from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phones/')
    release_date = models.DateField(null=True, blank=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.name)
            self.slug = original_slug
            counter = 1
            while Phone.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        try:
            super().save(*args, **kwargs)
        except Exception as e:
            raise ValidationError(f"Ошибка сохранения телефона: {e}")

    def clean(self):
        if self.price < 0:
            raise ValidationError("Цена не может быть отрицательной")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
