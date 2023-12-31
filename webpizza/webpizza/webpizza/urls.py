"""
URL configuration for webpizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from applipizza import views

urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('pizzas/', views.pizzas),
    path('ingredients/', views.ingredients),
    path('pizzas/<int:pizza_id>/', views.pizza),
    path('ingredients/add/', views.formulaireCreationIngredient),
    path('pizzas/add/', views.formulaireCreationPizza),
    path('ingredients/create/', views.creerIngredient),
    path('pizzas/create/', views.creerPizza),
    path('pizzas/<int:pizza_id>/addIngredient/', views.ajouterIngredientDansPizza),
    path('pizzas/<int:pizza_id>/delete/', views.supprimerPizza),
    path('pizzas/<int:pizza_id>/update/', views.afficherFormulaireModificationPizza),
    path('pizzas/<int:pizza_id>/updated/', views.modifierPizza),
    path('ingredients/<int:idIngredient>/delete/', views.supprimerIngredient),
    path('ingredients/<int:idIngredient>/update/', views.afficherFormulaireModificationIngredient),
    path('ingredients/<int:idIngredient>/updated/', views.modifierIngredient),
   
]
