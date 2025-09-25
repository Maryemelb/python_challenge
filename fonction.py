import produit as p

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