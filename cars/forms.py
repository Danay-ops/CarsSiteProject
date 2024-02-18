from django import forms
from .models import Categories, Cars, AddContact
from django.core.validators import MinLengthValidator,MaxLengthValidator
class AddPostForm(forms.ModelForm):
   """ title = forms.CharField(max_length=255, label='Заголовок',min_length=2,
                            error_messages={
                                'min_length':'Короткий заголовок'
                            })
    slug = forms.SlugField(max_length=255, label='url',
                           validators=[
                                MinLengthValidator(2, message="Слишком коротко"),
                                MaxLengthValidator(100, message='Слишком много символов')
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5} ),required=False, label='Контент')
    is_published = forms.BooleanField( label='Статус')
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категории',empty_label='Не выбрано')"""

   cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категории', empty_label='Не выбрано')

   class Meta:
       model = Cars
       fields =['title', 'slug', 'content','photo','is_published', 'cat']
       widgets={
           'title': forms.TextInput(attrs={'class': 'form-input','placeholder':'Введите заголовок'}),
           'content': forms.Textarea(attrs={'cols': 50, 'rows': 5,'placeholder':'Введите контент поста' }),
       }
       labels= {'title': 'Заголовок',
                'slug': 'URL',
                'content': 'Контент',
                'is_published': 'Статус',
                'cat': 'Категории',
                }

class UploadFileF(forms.Form):
    file = forms.ImageField(label='Файл')
class ContactForm(forms.ModelForm):
    class Meta:
        model = AddContact
        fields = ['name', 'email','message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input','placeholder':'Введите ваше имя'}),
            'email': forms.TextInput(attrs={'class': 'form-input','placeholder':'Введите ваше email'}),
            'message': forms.Textarea(attrs={'cols': 50, 'rows': 5,'placeholder':'Ждем ваше сообщение'}),
        }
        labels = {'name': 'Имя',
                  'email': 'Email',
                  'message': 'Отзыв',
                  }

