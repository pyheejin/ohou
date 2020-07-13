from django.db import models
from urllib.parse import urlparse
from django.core.files import File
from utils.file import download, get_buffer_ext


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=150)
    nickname = models.CharField(max_length=50)
    agree_years = models.BooleanField(default=0)
    agree_terms = models.BooleanField(default=0)
    agree_policy = models.BooleanField(default=0)
    agree_promotion = models.BooleanField(default=0)
    homepage = models.CharField(max_length=200)
    gender = models.BooleanField(default=0)
    introduction = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/image', blank=True)

    def save(self, *args, **kwargs):
        # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
        if self.purchase_url and not self.image_file:
            # 우선 purchase_url의 대표 이미지를 크롤링하는 로직은 생략하고, 크롤링 결과 이미지 url을 임의대로 설정
            item_image_url = 'https://cdn.pixabay.com/photo/2016/08/27/11/17/bag-1623898_960_720.jpg'

            if item_image_url:
                temp_file = download(item_image_url)
                file_name = '{urlparse}.{ext}'.format(
                    # url의 마지막 '/' 내용 중 확장자 제거
                    # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720'
                    urlparse=urlparse(item_image_url).path.split('/')[-1].split('.')[0],
                    ext=get_buffer_ext(temp_file)
                )
                self.image_file.save(file_name, File(temp_file))
                super().save()
            else:
                super().save()

    class Meta:
        db_table = 'users'

class Point(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 'points'

class Coupon(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    period = models.DateField()
    condition = models.CharField(max_length=150)

    class Meta:
        db_table = 'coupons'
