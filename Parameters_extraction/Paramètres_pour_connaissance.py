annee_avant=1989
annee=1990
pays='Kuwait'



mort=ma.inf
col_mort=-1
n,l=xparametre.shape



prediction=clf.predict(xparametre_scaled)

for i in range(n):
    if(tab[i,0]==pays and tab[i,1]==annee):
        mortalite_sans_modif=prediction[i]
    if(tab[i,0]==pays and tab[i,1]==annee_avant):
        mortalite_objectif=prediction[i]

i=0
while(i<n and not(tab[i,0]==pays and tab[i,1]==annee)):
    i+=1
ligne_annee=xparametre_scaled[i,:]
i=0
while(i<n and not(tab[i,0]==pays and tab[i,1]==annee_avant)):
    i+=1
ligne_annee_avant=xparametre_scaled[i,:].copy()



for q in range(378):
    aux=ligne_annee[q]
    ligne_annee[q]=ligne_annee_avant[q]
    mort_aux=clf.predict(ligne_annee.reshape((1,378)))
    
    if(mort>mort_aux):
        mort=mort_aux
        col_mort=q
    ligne_annee[q]=aux
print(c2[col_mort+3],mort)

ligne_annee[col_mort]=ligne_annee_avant[col_mort]