from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    banned_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('views_counter',)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену'
        })

        # self.fields['created_at'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Дата создания'
        # })
        #
        # self.fields['updated_at'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Дата последнего изменения'
        # })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in self.banned_list:
            raise ValidationError(f'Запрещенные слова для названия продукта: {', '.join(self.banned_list)}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if set(description.lower().split()).intersection(self.banned_list):
            raise ValidationError(f'Эти слова не должны присутствовать в описании: {', '.join(self.banned_list)}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('цена не может быть отрицательной')
        return price