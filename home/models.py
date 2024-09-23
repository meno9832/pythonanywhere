from django.db import models
from django.utils import timezone

class Post(models.Model):
    category_sel = (
        ('p', 'pair'), ('t', 'TRPG log'), ('c','commission')
    )


    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=category_sel)
    tag = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumnail = models.URLField()

    def __str__(self):
        return self.title
    
class main_notice(models.Model):
    notice_text = models.TextField()
    cover_img_url = models.URLField()
    main_img1 = models.URLField()
    main_img2 = models.URLField()
    main_img3 = models.URLField()
    main_img4 = models.URLField()
    main_color = models.TextField()
    time_img = models.URLField()
    dday_img = models.URLField()
    header_img = models.URLField()

    
    def __str__(self):
        return self.notice_text

class banner(models.Model):
    name = models.TextField()
    site_src = models.URLField()
    banner_img = models.URLField()
    
    def __str__(self):
        return self.name
    
class dday(models.Model):
    name = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name

class gallery(models.Model):
    cate_sel = (
        ('1', '율숍'), ('2', '우르'), ('3','유피텔'), ('4', '니토필'), ('5', '카타튜링'), ('6', '기타')
    )
    text = models.CharField(max_length=100)
    cate = models.CharField(max_length=1, choices=cate_sel)
    img = models.URLField()
