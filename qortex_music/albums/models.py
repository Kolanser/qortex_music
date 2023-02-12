from datetime import datetime as dt
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


def year_validator(year):
    """Проверка что год не превышает текущий."""
    if year > dt.now().year:
        raise ValidationError(
            'Год выхода альбома не может превышать текущий.'
        )
    return year


class Singer(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='Название исполнителя',
        unique=True,
    )

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Sing(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='Название песни'
    )

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.name


class AlbumSing(models.Model):
    album = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
        verbose_name='Альбом'
    )
    sing = models.ForeignKey(
        'Sing',
        on_delete=models.CASCADE,
        verbose_name='Песня'
    )
    number_sing = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ],
        verbose_name='Порядковый номер песни в альбоме',
    )

    class Meta:
        ordering = ('album',)
        verbose_name = 'Связь альбома и песни'
        constraints = [
            models.UniqueConstraint(fields=['album', 'sing', 'number_sing'],
                                    name=('unique sing in album')),
        ]

    def __str__(self):
        return f'{self.sing} относится к альбому {self.album}'


class Album(models.Model):
    name = models.CharField(
        max_length=48,
        verbose_name='Название альбома'
    )
    year = models.PositiveIntegerField(
        validators=[year_validator],
        verbose_name='Год выхода')
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель альбома',
        related_name='albums'
    )
    sings = models.ManyToManyField(
        Sing,
        through=AlbumSing,
        related_name='albums'
    )

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.name
