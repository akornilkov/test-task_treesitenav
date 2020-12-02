from django.db import models

import mptt
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class DomainModel(MPTTModel):
    """Элемент уровня сайта"""
    class Meta:
        db_table = 'domain'
        verbose_name_plural = 'Домены'
        verbose_name = 'Домен'
        ordering = ('tree_id', 'level')
    name = models.CharField('Название домена', max_length=255)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subdomains',
        verbose_name='Родительский домен',
    )

    @property
    def full_name(self):
        if self.parent:
            return f'{self.name}.{self.parent.full_name}'
        else:
            return f'{self.name}'

    def __unicode__(self):
        return self.full_name

    def __str__(self):
        return self.full_name

    class MPTTMeta:
        order_insertion_by = ['name']


class NavigationItem(MPTTModel):
    """Элемент уровня сайта"""
    class Meta:
        db_table = 'navigation_item'
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ('tree_id', 'level')
    name = models.CharField('Название категории', max_length=255)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская категория',
    )
    domain = TreeForeignKey(
        DomainModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='domain',
        verbose_name='Домен',
    )

    @property
    def f_path(self):
        if self.parent:
            return f'{self.parent.f_path}/{self.name}'
        else:
            if self.domain:
                return f'{self.domain.full_name}/{self.name}'
            else:
                return f'/{self.name}'

    def __unicode__(self):
        return self.f_path

    def __str__(self):
        return self.f_path

    class MPTTMeta:
        order_insertion_by = ['name']


mptt.register(DomainModel, order_insertion_by=['f_name'])
mptt.register(NavigationItem, order_insertion_by=['full_name'])
