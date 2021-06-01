from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,
                            help_text='Укажите заголовок категории')
    slug = models.SlugField(max_length=160, unique=True,
                            verbose_name='Slug (идентификатор)',
                            help_text='Slug это уникальная строка,'
                                      'понятная человеку')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,
                            help_text='Укажите жанр')
    slug = models.SlugField(max_length=160, unique=True,
                            verbose_name='Slug (идентификатор)',
                            help_text='Slug это уникальная строка,'
                                      'понятная человеку')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Жанр'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    year = models.IntegerField(verbose_name="Год выпуска")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='title',
                                 verbose_name='Категория')

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'Название'

    def __str__(self):
        return self.name[:15]
