from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'post_tag'
        verbose_name = '포스트_태그'
        verbose_name_plural = '포스트_태그'

    def __str__(self):
        return self.name


class Post(models.Model):
    dsuser = models.ForeignKey('user.Dsuser', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='제목', null=True)
    content = models.TextField(verbose_name='내용', null=False)
    img_src = models.ImageField(verbose_name='이미지주소', upload_to="image")
    create_date = models.DateField(verbose_name='등록일', auto_now_add=True, null=False, blank=False)
    tags = models.ManyToManyField(Tag, verbose_name='태그', related_name='tagged')

    class Meta:
        db_table = 'post'
        verbose_name = '포스트'
        verbose_name_plural = '포스트'
        ordering = ('create_date',)

    def __str__(self):
        return str(self.title)
