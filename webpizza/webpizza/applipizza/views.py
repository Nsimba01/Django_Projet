from django.shortcuts import render

from applipizza.models import Pizza


from applipizza.models import Ingredient

from applipizza.models import Composition

from applipizza.forms import IngredientForm

from applipizza.forms import PizzaForm

from applipizza.forms import CompositionForm

# Create your views here.

def pizzas(request):
    
    lesPizzas=Pizza.objects.all()
    
    return render(
        request,
        "applipizza/pizzas.html",
        {"pizzas":lesPizzas}
        
        )

def ingredients(request):
    
    lesIngredients=Ingredient.objects.all()
    
    return render(
        request,
        "applipizza/ingredients.html",
        {"ingredients":lesIngredients}
        
        )

def pizza(request,pizza_id):
    
    formulaire=CompositionForm()
    
    laPizza=Pizza.objects.get(idPizza=pizza_id)
    
   
    
    #ingredient_id_compo=Composition.objects.filter(pizza = pizza_id).only('quantite','ingredient_id').values('ingredient_id')
    
    
    compo_quantite_idIng=list(Composition.objects.filter(pizza = pizza_id).only('quantite','ingredient_id').values())
    
    lesNomIngredients_QT_ingredients=[]
    
    lesNomIngredients=[]
    
    #Qt_ingredients=[]
    

    

    for item in compo_quantite_idIng:
        
        
        lesNomIngredient=Ingredient.objects.only('idIngredient','nomIngredient').filter(idIngredient=item['ingredient_id']).values('nomIngredient')
    
        lesNomIngredients_QT_ingredients.append(lesNomIngredient)
        
        lesNomIngredients.append(lesNomIngredient)
        
        Qt_ingredient=Composition.objects.filter(ingredient_id=item['ingredient_id']).values('quantite')
        
        lesNomIngredients_QT_ingredients.append(Qt_ingredient)
   
   #compo_part_ingredient=compo.objects.filter(ingredient_id=appli_pizza("idIngredient"))
    

    

        
    if lesNomIngredients_QT_ingredients.__len__() != 0:
        
        return render(
        request,
        "applipizza/pizza.html",
        {'pizza':laPizza,
         'ingredient_QT':lesNomIngredients_QT_ingredients,
         'nbre_ingredient':lesNomIngredients,
         'form':formulaire
   
         }
        )
    
def formulaireCreationIngredient(request):
    
    formulaire=IngredientForm()
    
    return render(
        request,
        "applipizza/formulaireCreationIngredient.html",
        {"form":formulaire}
        
        )

def creerIngredient(request):
    
    form = IngredientForm(request.POST)
    
    if form.is_valid():
        
        nomIng=form.cleaned_data['nomIngredient']
        
        ing=Ingredient()
        
        ing.nomIngredient=nomIng
        
        ing.save()
        
        return render(
            request,
            "applipizza/traitementFormulaireCreationIngredient.html",
            {"nom":nomIng}
            
            )
    

        
def formulaireCreationPizza(request):
    
    formulaire = PizzaForm(request.POST)
    
    
    return render(
        request,
        "applipizza/formulaireCreationPizza.html",
        {'form':formulaire}
        )
        
def creerPizza(request):
    
    form = PizzaForm(request.POST)
    
    if form.is_valid():
        
        nomPizza=form.cleaned_data['nomPizza']
        
        prixPizza=form.cleaned_data['prix']
        
        piz=Pizza()
        
         
        piz.nomPizza=nomPizza
        
        piz.prix=prixPizza
        
        piz.save()
        
        return render(
            request,
            "applipizza/traitementFormulaireCreationPizza.html",
            {"nom":nomPizza,"prix":prixPizza}
            
            )
        
def ajouterIngredientDansPizza(request,pizza_id):
    
    formulaire=CompositionForm(request.POST)
    
    if formulaire.is_valid():
        
        idIng=formulaire.cleaned_data['ingredient'].idIngredient# On obtient l'idIngredient d' Ingredient de select 
        
        qte=formulaire.cleaned_data['quantite']
        
        compo=Composition()
        
        compo.ingredient=Ingredient.objects.get(idIngredient=idIng)
        
    
                
        #compo.ingredient=Ingredient.objects.filter(nomIngredient=idIng).values("idIngredient")
        
        
        
        compo.pizza=Pizza.objects.get(idPizza=pizza_id)
        
        compo.quantite=qte
        
        compo.save()
        
    formulaire=CompositionForm()
   
    laPizza=Pizza.objects.get(idPizza=pizza_id)
    
   
    
    #ingredient_id_compo=Composition.objects.filter(pizza = pizza_id).only('quantite','ingredient_id').values('ingredient_id')
    
    
    compo_quantite_idIng=list(Composition.objects.filter(pizza = pizza_id).only('quantite','ingredient_id').values())
    
    lesNomIngredients_QT_ingredients=[]
    
    lesNomIngredients=[]
    
    #Qt_ingredients=[]
    

    

    for item in compo_quantite_idIng:
        
        
        lesNomIngredient=Ingredient.objects.only('idIngredient','nomIngredient').filter(idIngredient=item['ingredient_id']).values('nomIngredient')
    
        lesNomIngredients_QT_ingredients.append(lesNomIngredient)
        
        lesNomIngredients.append(lesNomIngredient)
        
        Qt_ingredient=Composition.objects.filter(ingredient_id=item['ingredient_id']).values('quantite')
        
        lesNomIngredients_QT_ingredients.append(Qt_ingredient)
   
   #compo_part_ingredient=compo.objects.filter(ingredient_id=appli_pizza("idIngredient"))
    

    

        
    if lesNomIngredients_QT_ingredients.__len__() != 0:
        
        return render(
        request,
        "applipizza/pizza.html",
        {'pizza':laPizza,
         'ingredient_QT':lesNomIngredients_QT_ingredients,
         'nbre_ingredient':lesNomIngredients,
         'form':formulaire
   
         }
        )
    
    

def supprimerPizza(request,pizza_id):
    
    laPizza=Pizza.objects.get(idPizza=pizza_id)

    laPizza.delete()
    
    lesPizzas=Pizza.objects.all()
    
    return render(
        request,
        "applipizza/pizzas.html",
        {"pizzas":lesPizzas}
        
        )

    
 
        
def afficherFormulaireModificationPizza(request,pizza_id):
    
    laPizza=Pizza.objects.get(idPizza=pizza_id)
    
    formulaire=PizzaForm(instance=laPizza)
    
    return render(
        request,
        "applipizza/formulaireModificationPizza.html",
        {"form":formulaire,"pizza":laPizza}
        )

    
    

def modifierPizza(request, pizza_id):
    
    laPizza=Pizza.objects.get(idPizza=pizza_id)
    
    formulaire=PizzaForm(request.POST,instance=laPizza)
    
    if formulaire.is_valid():
        
        laPizza.save()
        
    return render(
        request,
        "applipizza/traitementFormulaireModificationPizza.html",
        {"form":formulaire,"pizza":laPizza}
        )
    
    

def supprimerIngredient(request,idIngredient ):
    
    inGredient=Ingredient.objects.get(idIngredient=idIngredient)
    
    inGredient.delete()
    
    lesIngredients=Ingredient.objects.all()
    
    return render(
        request,
        "applipizza/ingredients.html",
        {"ingredients":lesIngredients}
        
        )

    
    
    
    
def afficherFormulaireModificationIngredient(request,idIngredient):
    
    ingredient=Ingredient.objects.get(idIngredient=idIngredient)
    
    formulaire=IngredientForm(instance=Ingredient)
    
    
    return render(
        request,
        "applipizza/formulaireModificationIngredient.html",
        {"form":formulaire,"ingredient":ingredient}
        )
    
    
    
    
    
def   modifierIngredient(request, idIngredient):
    
    ingredient=Ingredient.objects.get(idIngredient=idIngredient)
    
    formulaire=IngredientForm(request.POST,instance=ingredient)
    
    if formulaire.is_valid():
        
        ingredient.save()
        
        return render(
            request,
            "applipizza/traitementFormulaireModificationIngredient.html",
            {"form":formulaire,"ingredient":ingredient}
            )
      
    
    
    

    
    

    
    