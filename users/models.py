from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES=(
        (1,'남'),
        (2,'여'),
    )

    UNI_CHOICES=(
        ('KAIST','KAIST'),
        ('KC대학교','KC대학교'),
        ('가톨릭대학교(성신교정)','가톨릭대학교(성신교정)'),
        ('가톨릭대학교(성의교정)','가톨릭대학교(성의교정)'),
        ('감리교신학대학교','감리교신학대학교'),
        ('건국대학교','건국대학교'),
        ('경기대학교(서울캠퍼스)','경기대학교(서울캠퍼스)'),
        ('경희대학교','경희대학교'),
        ('고려대학교','고려대학교'),
        ('광운대학교','광운대학교'),
        ('국민대학교','국민대학교'),
        ('덕성여자대학교','덕성여자대학교'),
        ('덕성여자대학교(종로캠퍼스)','덕성여자대학교(종로캠퍼스)'),
        ('동국대학교','동국대학교'),
        ('동덕여자대학교','동덕여자대학교'),
        ('명지대학교','명지대학교'),
        ('삼육대학교','삼육대학교'),
        ('상명대학교','상명대학교'),
        ('서강대학교','서강대학교'),
        ('서경대학교','서경대학교'),
        ('서울과학기술대학교','서울과학기술대학교'),
        ('서울교육대학교','서울교육대학교'),
        ('서울기독대학교','서울기독대학교'),
        ('서울대학교','서울대학교'),
        ('서울대학교(연건캠퍼스)','서울대학교(연건캠퍼스)'),
        ('서울시립대학교','서울시립대학교'),
        ('서울여자대학교','서울여자대학교'),
        ('서울여자대학교(대학로캠퍼스)','서울여자대학교(대학로캠퍼스)'),
        ('서울한영대학교','서울한영대학교'),
        ('성공회대학교','성공회대학교'),
        ('성균관대학교','성균관대학교'),
        ('성신여자대학교','성신여자대학교'),
        ('성신여자대학교(운정그린캠퍼스)','성신여자대학교(운정그린캠퍼스)'),
        ('세종대학교','세종대학교'),
        ('숙명여자대학교','숙명여자대학교'),
        ('숭실대학교','숭실대학교'),
        ('연세대학교','연세대학교'),
        ('육군사관학교','육군사관학교'),
        ('이화여자대학교','이화여자대학교'),
        ('장로회신학대학교','장로회신학대학교'),
        ('중앙대학교','중앙대학교'),
        ('총신대학교','총신대학교'),
        ('추계예술대학교','추계예술대학교'),
        ('한국방송통신대학교','한국방송통신대학교'),
        ('한국방송통신대학교(서울지역대학)','한국방송통신대학교(서울지역대학)'),
        ('한국성서대학교','한국성서대학교'),
        ('한국예술종합학교','한국예술종합학교'),
        ('한국예술종합학교(서초동캠퍼스)','한국예술종합학교(서초동캠퍼스)'),
        ('한국외국어대학교','한국외국어대학교'),
        ('한국체육대학교','한국체육대학교'),
        ('한성대학교','한성대학교'),
        ('한양대학교','한양대학교'),
        ('홍익대학교','홍익대학교'),
    )
    pass
    gender=models.IntegerField(default="1", choices=GENDER_CHOICES)
    university=models.CharField(max_length=20, default="KAIST", choices=UNI_CHOICES)