from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sub_categories'

class LowerCategory(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'lower_categories'

class Brand(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brands'

class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    coupon = models.ForeignKey('account.Coupon', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    delivery_fee = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'

class Additional(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'additionals'

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    url = models.URLField()

    class Meta:
        db_table = 'images'

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    content = models.TextField()
    agreement = models.BooleanField(default=0)
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
        db_table = 'reviews'
