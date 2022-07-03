from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Image(models.Model):
    image_url = models.CharField(max_length=400)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
    
class Allergy (models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergys'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'atod'

class Nutrition(models.Model):
    one_serving_Kcal = models.CharField(max_length=100)
    sodium_mg = models.CharField(max_length=100)
    saturated_fat_g = models.CharField(max_length=100)
    sugars_g = models.CharField(max_length=100)
    protein_g = models.CharField(max_length=100)
    caffeine_mg = models.CharField(max_length=100)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Size(models.Model):
    name = models.CharField(max_length=100)
    size_ml = models.CharField(max_length=100)
    size_fluid_ounce = models.CharField(max_length=100)
    size_g = models.CharField(max_length=100)
    class Meta:
        db_table = 'sizes'