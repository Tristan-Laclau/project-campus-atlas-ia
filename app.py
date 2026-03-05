import plotly.express as px
import pandas as pd


# 5.

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

listeProduits = ["Produit A", "Produit B", "Produit C"];

for produit in listeProduits:
    données_produit = données[données["produit"] == produit];
    données_produit["chiffre_d_affaire"] = données_produit["qte"] * données_produit["prix"];
    print("-----------------", produit, "-----------------");
    print("Chiffre d'affaire moyen: ", round(données_produit["chiffre_d_affaire"].mean(), 2));
    print("Chiffre d'affaire médian: ", round(données_produit["chiffre_d_affaire"].median(), 2));
    print("Volume des ventes moyen: ", round(données_produit["qte"].mean(), 2));
    print("Volume des ventes médian: ", round(données_produit["qte"].median(), 2));
    print("Ecart-type du volume des ventes: ", round(données_produit["qte"].std(), 2));
    print("Variance du volume des ventes: ", round(données_produit["qte"].var(), 2));
    print();


# 6.
ventesTotales = {};
lignes = données.to_dict(orient="records");
for ligne in lignes:
    produit = ligne["produit"];
    qte = ligne["qte"];
    
    if produit not in ventesTotales:
        ventesTotales[produit] = 0;
    
    ventesTotales[produit] = ventesTotales[produit] + qte;

ventesMax = None;
produitLePlusVendu = None;

for produit,ventes in ventesTotales.items():

    if ventesMax is None or ventes > ventesMax:
        ventesMax = ventes;
        produitLePlusVendu = produit;

print("Produit le plus vendu : ", produitLePlusVendu, " Nombre de ventes : ", ventesMax);

ventesMin = None;
produitLeMoinsVendu = None;

for produit,ventes in ventesTotales.items():

    if ventesMin is None or ventes < ventesMin:
        ventesMin = ventes;
        produitLeMoinsVendu = produit;

print("Produit le moins vendu ", produitLeMoinsVendu, " Nombre de ventes : ", ventesMin);


# 7.

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

figure = px.pie(données, values='qte', names='produit', title='Quantité vendue par produit');
figure.write_html('ventes-par-produit.html');

données["ca"] = données["qte"] * données["prix"];
figure = px.pie(données, values='ca', names='produit', title='Chiffre d affaire par produit');
figure.write_html('chiffre-d-affaire-par-produit.html');