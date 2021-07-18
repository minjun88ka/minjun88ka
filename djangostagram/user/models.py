from django.db import models

class Dsuser(models.Model):
    id = models.CharField(verbose_name='아이디', primary_key=True, max_length=128, unique=True)
    email = models.EmailField(verbose_name='이메일', max_length=255, null=False, blank=False)
    password = models.CharField(verbose_name='패스워드', max_length=128, null=False, blank=False)
    create_date = models.DateField(verbose_name='등록일', auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = 'dsuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.id

