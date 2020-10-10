from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

CLS_CHOICES = (
    (0, '通知-重要通知'),
    (1, '通知-人事安排'),
    (2, '通知-工作动态'),
    (3, '文化-自然景观'),
    (4, '文化-好物推荐'),
    (5, '文化-体育文化'),
    (6, '文化-健康知识'),
    (7, '学术-专家观点'),
    (8, '学术-知识科普'),
    (9, '学术-学者论述'),
    (10, '学术-学术研究'),
    (11, '教育-培训资讯')
)

STATUS_CHOICES = (
    (False, '立项'),
    (True, '结项')
)

CEA_CHOICES = (
    (0, '专业人才'),
    (1, '荣誉证书'),
    (2, '学术顾问'),
    (3, '行业专家'),
    (4, '特聘研究员')
)


# 文章信息
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('标题'), help_text=_('标题'))
    date = models.DateField(auto_now_add=True, verbose_name=_('发布时间'), help_text=_('发布时间'))
    content = models.TextField(verbose_name=_('内容'), help_text=_('详情'))
    cls = models.IntegerField(verbose_name=_('所属分类'), help_text=_('所属分类'), choices=CLS_CHOICES)

    class Meta:
        verbose_name = _('文章')
        verbose_name_plural = verbose_name


# 课题
class Problem(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('课题名称'), help_text=_('课题名称'))
    number = models.CharField(max_length=300, verbose_name=_('编号'), help_text=_('编号'))
    status = models.BooleanField(verbose_name=_('状态'), help_text=_('状态'), default=False, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = _('课题')
        verbose_name_plural = verbose_name


# 基地
class Base(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('基地名称'), help_text=_('基地名称'))
    number = models.CharField(max_length=300, verbose_name=_('基地编号'), help_text=_('基地编号'))

    class Meta:
        verbose_name = _('基地')
        verbose_name_plural = verbose_name


# 证书
class Certificate(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('证书所有人'), help_text=_('证书所有人'))
    cardNumber = models.CharField(max_length=200, verbose_name=_('身份证号,为专业人才时不可以为空'), help_text=_('身份证号,为专业人才时不可以为空'),
                                  blank=True, null=True)
    cls = models.IntegerField(verbose_name=_('证书属性'), help_text=_('证书属性'), choices=CEA_CHOICES)

    class Meta:
        verbose_name = _('证书')
        verbose_name_plural = verbose_name
