from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview_image = models.ImageField(
        upload_to="Blog/image",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title
