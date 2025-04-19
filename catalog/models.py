from django.db import models

from users.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        #help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        #help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        #help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        #help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="Product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        #help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        #help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="Products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена продукта",
        #help_text="Введите цену продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        #help_text="Введите дату создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        #help_text="Введите дату последнего изменения",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="счетчик просмотров",
        #help_text="Укажите количество просмотров",
        default=0,
    )

    publication = models.BooleanField(
        default=False,
        verbose_name='Статус публикации'
    )

    owner = models.ForeignKey(
        User,
        verbose_name='имя владельца',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name
