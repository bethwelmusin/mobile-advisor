from django.contrib import admin

from pages.models import Disease, Meal, RecomendedDiet, FoodDiet, FoodList, FoodType
# Register your models here.

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ["meal_type"]
    list_display_links = ["meal_type"]
    list_filter = ["meal_type"]  

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"] 
    
@admin.register(FoodList)
class FoodListAdmin(admin.ModelAdmin):
    list_display = ["foodtype", "name_of_food", "meal"]
    list_display_links = ["name_of_food"]
    list_filter = ["foodtype","meal","name_of_food"] 
    
     
@admin.register(RecomendedDiet)
class RecomendedDietAdmin(admin.ModelAdmin):
    list_display = ["disease","foodtype", "meal"]
    list_display_links = ["foodtype"]
    list_filter = ["foodtype", "meal", "disease"] 

@admin.register(FoodDiet)
class FoodDietAdmin(admin.ModelAdmin):
    list_display = ["food_list", "meal"]
    list_display_links = ["food_list"]
    list_filter = ["food_list", "meal"]  
        