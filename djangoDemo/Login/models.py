from django.db import models

# Create your models here.

class WebUser(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名",db_column='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月",db_column="出生年月")
    gender = models.CharField(null=True, blank=True, max_length=6, choices=(("1", u"男"), ("0", "女")), default="1",
                              verbose_name="性别",db_column="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话", unique=True,db_column="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱",db_column="邮箱")
    unionId = models.CharField(null=True, blank=True, max_length=255, verbose_name="unionId")
    open_id = models.CharField(null=True, blank=True, max_length=255, verbose_name="openid")
    session_key = models.CharField(null=True, blank=True, max_length=255, verbose_name="session_key")
    info = models.TextField(null=True, blank=True, max_length=50, verbose_name="info",db_column="简介")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    loginIp = models.CharField(max_length=200,verbose_name="登录IP",db_column="登录ip")
    recent_login_time = models.DateField(null=True, blank=True, verbose_name="上次登录时间",db_column="上次登录时间")


    class Meta:
        db_table = 'WebUserTable'
        unique_together = ('name','mobile')

    def __str__(self):
        return self.name

# class WebUserGroup(models.Model):
#     pass