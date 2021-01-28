from django.db import models

# Create your models here.
from django.views.generic import ListView


class Test(models.Model):
    subject=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',blank=True)
    summary = models.TextField(max_length=500, help_text='설명을 적으세요')
    upload_date = models.DateField(null=True, blank=True)
    acount = models.CharField(max_length=1)
    def __str__(self):
        """String for representing the Model object."""
        return self.subject


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True) #media폴더 안에 users부터 년 월 일 폴더가 만들어지고 그 안에 이미지 존재
    #image = models.ImageField(upload_to='images')  media 폴더 안에 images 폴더 안에 모두 이미지가 들어감

    def __str__(self):
        return self.title

class Product(models.Model):
    serial_number=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    content=models.TextField(max_length=300,null=True)
    price=models.IntegerField()
    make_date=models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='products')

    def __str__(self):
        return self.name

class ProductList(ListView):
    paginate_by = 5
    model = Product

class Pcomment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(max_length=300, null=True)
    make_date = models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #게시물 첫 생성시 날짜 생성
    last_modified = models.DateTimeField(auto_now=True) #변경 및 save 될 때마다 날짜가 바뀜

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


"""
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #게시물 첫 생성시 날짜 생성
    last_modified = models.DateTimeField(auto_now=True) #변경 및 save 될 때마다 날짜가 바뀜
    categories = models.ManyToManyField('Category', related_name='posts')  #다대다 관계 설정

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)  #일대 다 관계 설정 Post 테이블의 pk 즉 id 필드가 기본키가 된다.

"""