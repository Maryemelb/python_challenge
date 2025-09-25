import produit as p
from functools import reduce

produit_prix =[]
#Associer chaque produit a son prix
def afficher_produit():
      global produit_prix
      produit_prix= list(zip(p.produit,p.prix))
      return produit_prix
#filter les produit
def sup30(produit) :
    produit_to_list = list(produit)
    prix= produit_to_list[-1]
    if prix >= 30:
      return produit

def produit_sup_30():
     global produit_prix
     produit_chere= list(filter(sup30, produit_prix))
     return produit_chere

    
def ordre_croissant():
    global produit_prix
    print(produit_prix)
    produit_prix.sort(key=lambda x: x[1])
    return produit_prix
def classement_en_tuple():
    produit_prix_tuple = tuple(produit_prix)
    return produit_prix_tuple
def produit_plus_chere(produits = None):
    global produit_prix
    if produits:
        produit_prix = produits
    else:
      product_test= ( ' ', 0)
      for product in produit_prix:
       if(product[1] >= product_test[1]):
          product_test= product
      return product_test
  
def produit_moins_chers():
    
    for product in produit_prix:
       product_test= ( product[0] ,product[1] )
       break
    for product in produit_prix:
       if(product[1] <= product_test[1]):
          product_test= product
    return product_test
#Bonus
def check_if_luxe(produit):
    if produit[1] > 1000:
        return produit[0] + " coute " + str(produit[1]) + " DH(luxe)"
    else: 
       return produit[0] + " coute "+ str(produit[1]) + " DH"

def transformation_en_str():
   list_chaine= list(map(check_if_luxe, produit_prix))
   for chaine in list_chaine:
         print(chaine)
