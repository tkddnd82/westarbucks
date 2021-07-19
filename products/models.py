from django.db import models

# Create your models here
 
 # 각 메뉴들에 맞는 설정값을 입력해주자
class Menu(models.Model):
     name = models.CharField(max_length=20)

#카테고리의 경우 menu_id가 있는데, 이게 위에서 만든 Menu를 Foreign Key로 참조하고 있으니 주의하자!
class Categories(models.Model):
     name = models.CharField(max_length=20)
     menu = models.ForeignKey('Menu',on_delete=models.CASCADE)

#음료 메뉴도 다른 테이블에서 참조~!!
class Drinks(models.Model):
     category = models.ForeignKey('Categories', on_delete=models.CASCADE)
     korean_name = models.CharField(max_length=30)
     english_name = models.CharField(max_length=30)
     description = models.TextField()

class Images(models.Model):
     image_url = models.CharField(max_length=500)
     drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)


class Allergy_drink(models.Model):
     allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
     drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)

class Allergy(models.Model):
     name = models.CharField(max_length=20)

class Nutritions(models.Model):
     one_serving_kcal = models.DecimalField(max_digits = 5, decimal_places = 2)
     sodiumn_mg = models.DecimalField(max_digits = 5, decimal_places = 2)
     saturated_fat_g = models.DecimalField(max_digits = 10, decimal_places = 2)
     sugars_g = models.DecimalField(max_digits = 5, decimal_places = 2)
     protein_g = models.DecimalField(max_digits = 5, decimal_places = 2)
     caffeine_mg = models.DecimalField(max_digits = 5, decimal_places = 2)
     drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)
     size_ml =  models.CharField(max_length=20)
     size_fluid_ounce = models.CharField(max_length=20)
               
