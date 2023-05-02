# Здравствуйте, в этом проекте есть:
### 1) Подключенный рабочий , настроенный бутстрап
### 2)рабочие карточки товаров/статей c отображением 
![изображение_2023-05-02_192158363 (1)](https://user-images.githubusercontent.com/111605401/235726017-3096d668-706b-4521-a9f0-47fe8006b399.png)
![изображение_2023-05-02_192454818](https://user-images.githubusercontent.com/111605401/235726563-b6260243-d198-4b34-a169-3b198c1e19bb.png)


### 3) Рабочая страница добавления товара/статьи , в том числе в админ панеле. Установлен модуль RichCharField
![screencapture-127-0-0-1-8000-addpage-2023-05-02-19_26_32 (1)](https://user-images.githubusercontent.com/111605401/235727045-b3f8e0b9-727b-4ab2-8c27-cf7d177051f2.png)
![image](https://user-images.githubusercontent.com/111605401/235727585-26c80813-58d3-451e-a911-10de0b26d8ac.png)
- за это отвечает javascript в шаблоне post.html:
```
<script>
    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */

    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = {{ post.slug }}; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };

    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://6656565.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
```
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
