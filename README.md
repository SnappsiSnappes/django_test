## Установка и запуск
- Клонируйте репозиторий на свой компьютер.
- Создайте виртуальное окружение с помощью команды в **CMD/powershell** 
```python -m venv venv``` и активируйте его ```.\venv\Scripts\activate``` windows или ```source venv/bin/activate```
- Python 3.10.6 x64 - проверено
- Установите все зависимости с помощью команды 
```
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```
Опционально
```
python manage.py createsuperuser
```
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

# Здравствуйте, в этом проекте есть:
### 1) Подключенный рабочий , настроенный bootstrap
### 2)рабочие карточки товаров/статей c отображением 
![изображение_2023-05-02_192158363 (1)](https://user-images.githubusercontent.com/111605401/235726017-3096d668-706b-4521-a9f0-47fe8006b399.png)
![изображение_2023-05-02_192454818](https://user-images.githubusercontent.com/111605401/235726563-b6260243-d198-4b34-a169-3b198c1e19bb.png)


### 3) Рабочая страница добавления товара/статьи , в том числе в админ панели. Установлен модуль RichCharField
![screencapture-127-0-0-1-8000-addpage-2023-05-02-19_26_32 (1)](https://user-images.githubusercontent.com/111605401/235727045-b3f8e0b9-727b-4ab2-8c27-cf7d177051f2.png)
![image](https://user-images.githubusercontent.com/111605401/235727585-26c80813-58d3-451e-a911-10de0b26d8ac.png)
- за это отвечает javascript в шаблоне post.html:
```
<script>
    function toggleFields() {
        var category = document.getElementById("id_category");
        var price = document.getElementById("id_price");
        var old_price = document.getElementById("id_old_price");
    
        if (category.value === "2") {  // ID выбранной категории (в данном случае "Статья")
            price.parentElement.style.display = "none";
            old_price.parentElement.style.display = "none";
        } else {
            price.parentElement.style.display = "block";
            old_price.parentElement.style.display = "block";
        }
    }
    
    // Вызываем функцию при загрузке страницы и каждый раз при изменении выбранной категории
    window.onload = toggleFields;
    document.getElementById("id_category").addEventListener("change", toggleFields);
    
</script>
```
### блок комментариев подключен Disqus
![screencapture-127-0-0-1-8000-post-f-2023-05-02-19_49_36 (1)](https://user-images.githubusercontent.com/111605401/235732160-bd7a7d8f-10f1-4fef-afd6-fa32648e9884.png)

### 4) работает слаг постов с кирилицей
![image](https://user-images.githubusercontent.com/111605401/235728538-c164c381-0f7b-46b1-b469-4b9edee8ec86.png)
![image](https://user-images.githubusercontent.com/111605401/235728908-cdac6966-c7fb-4d00-91eb-9f4e8ce03100.png)
за это отвечает функция Save в models.py - она отредактирована и использует специальный модуль slugify, так же использует ОРМ Джанго , чтобы проверить , существует ли запись с таким именем в базе данных, если да то добавляет цифру на конце +1

```
def save(self, *args, **kwargs):
        #* Если запись еще не сохранена в базе данных,
        #* создаем slug, добавляя случайное число
        base_slug = slugify2(self.title)
        slug = base_slug
        n = 1
        while Women.objects.filter(slug=slug).exists():
            slug = base_slug + '_' + str(n)
            n += 1
        self.slug = slug
        super(Women, self).save(*args, **kwargs)
```
### 5) интегрирована Регистрация
![изображение_2023-05-02_194344661](https://user-images.githubusercontent.com/111605401/235730910-2c71d915-694a-43e7-92e3-5d0319b7831b.png)
- так же авторизация через другие сервисы
![изображение_2023-05-02_194444855](https://user-images.githubusercontent.com/111605401/235731109-5b030e9a-c16b-4610-b51f-1328f32afb87.png)

### 6) в шаблоне используется template_tag с проверкой на user.is_stuff
![image](https://user-images.githubusercontent.com/111605401/235731509-0b174304-04e5-48b0-a25c-5e9130a69a2d.png)
![image](https://user-images.githubusercontent.com/111605401/235732486-e671dc48-fa7c-4c1d-bed5-9d46fc1d52c4.png)

### 7) Интегрирован crispy-forms
![image](https://user-images.githubusercontent.com/111605401/235732800-af931661-19b1-462b-8a9c-faf3f23e1162.png)

### 8) админка
![image](https://user-images.githubusercontent.com/111605401/235732991-cd1bf071-6648-4380-9c18-3f2aa5da1b0b.png)

- Поддерживает фильтрацию, настроен интерфейс
![image](https://user-images.githubusercontent.com/111605401/235733236-aba21ef3-a558-49ea-9676-0915ad9ee2d0.png)

- Позволяет добавлять категории ForeignKey от отдельной базы Cats
![image](https://user-images.githubusercontent.com/111605401/235733360-5f39ea5d-dcc8-4a28-9ba0-bc2c0a6a9754.png)
![image](https://user-images.githubusercontent.com/111605401/235733628-efbb4b41-b8aa-4f10-902d-d40f4f63ce44.png)

### а так же
![image](https://user-images.githubusercontent.com/111605401/235734302-b8ea2d86-d629-4ef3-91a0-4423c21549c4.png)

![image](https://user-images.githubusercontent.com/111605401/235734568-01100e4d-3317-4fb7-a7b1-4c4857a63ec0.png)

### настроенная пагинация
![image](https://user-images.githubusercontent.com/111605401/235735095-1b1abeb9-164f-414f-8f4f-0ab39e70a093.png)
![image](https://user-images.githubusercontent.com/111605401/235735145-afafe333-fc34-41ff-a36a-b4750893c5ca.png)

### настроено отображение большого текста на карточке 
![image](https://user-images.githubusercontent.com/111605401/235735528-1dfc946b-fee0-4178-9945-4ecee985cbb9.png)

### Настроен Кэш
![image](https://user-images.githubusercontent.com/111605401/235741482-4a5915ff-3bee-4b5e-a4b1-d0de4b0ddccd.png)
