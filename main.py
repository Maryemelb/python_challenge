import fonction as f
print("produits")
print(f.afficher_produit())
print("Afficher les produit avec les prix")
print(f.produit_sup_30())
print("str")
print(f.transformation_en_str())
print("ordre croissant")

print( f.ordre_croissant())
print(f.classement_en_tuple())
print("produit le plus chere",f.produit_plus_chere() )
print("produit le moins chere",f.produit_moins_chers() )
while True:
    choice= input("choose an operation \n 1.affichage des produit et leurs prix \n 2.les produit avec le prix >=30 \n 3.afichage des produit et leur text format string\n 4.ordre croissant des produit \n 6.convertie le classement final en tuple \n 7.produit plus chere \n 8.produit moin chers ")
    match choice :
          case "1":
              print(f.afficher_produit())
              continue
          case "2":
              print(f.produit_sup_30())
              continue
          case "3":
              print(f.transformation_en_str())
              continue
          case "4":
              print( f.ordre_croissant())
              continue
          case "6":
              print(f.classement_en_tuple())
              continue
          case "7":
            print(f.produit_plus_chere() )
            continue
          case "8":
            print(f.produit_moins_chers() )
            continue
          case _:
            break

