from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.name}'
     
class Meal(models.Model):
    meal_type = models.CharField(max_length=200) #eg breko
    def __str__(self):
        return f'{self.meal_type}'
    
    
class FoodType(models.Model):
    name = models.CharField(max_length=200) #eg carbohydrete
    def __str__(self):
        return f'{self.name}'
    
    
class FoodList(models.Model):
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    name_of_food = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.foodtype} {self.name_of_food}'
    
class RecomendedDiet(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.foodtype} {self.meal} {self.disease}'
    
class FoodDiet(models.Model): #patient
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_list = models.ForeignKey(FoodList, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.meal} {self.food_list}'