from django  import forms
from django.forms import ModelForm
from applipizza.models import Ingredient,Pizza,Composition


class IngredientForm(ModelForm):
    
    class Meta:
        
        model=Ingredient
        fields=['nomIngredient']
        
        
        

        
class PizzaForm(ModelForm):
    
    class Meta:
        
        model=Pizza
        fields=['nomPizza','prix'] # 2 champs de saisie
        
        
        
class CompositionForm(ModelForm):
    
    class Meta:
        
        model=Composition
        fields=['ingredient','quantite'] # 2 champs de saisie
    
    
        