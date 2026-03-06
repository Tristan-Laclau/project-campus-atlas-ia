# Fiche synthèse - Analyse des ventes
## Données
- Fichier : `ventes.csv`
- Format : [date, produit, prix, qte, region]

---

## Résultats clés via SQL (3.)
### Chiffre d'affaire total : **44825**

| Produit | Ventes |
|---|---:|
| A | 1 750|
| B | 1 055 |
| C | 575 |

| Région | Ventes |
|---|---:|
| Nord | 1 605 |
| Sud | 1 775 |

## Statistiques avec Panda (5.)

### Produit A
| Indicateur | Valeur |
|---|---:|
| CA moyen | 1 250.00 |
| CA médian | 1 225.00 |
| Volume moyen (qte) | 125.00 |
| Volume médian (qte) | 122.50 |
| Écart-type du volume | 38.08 |
| Variance du volume | 1 450.00 |

### Produit B
| Indicateur | Valeur |
|---|---:|
| CA moyen | 1 217.31 |
| CA médian | 1 200.00 |
| Volume moyen (qte) | 81.15 |
| Volume médian (qte) | 80.00 |
| Écart-type du volume | 21.23 |
| Variance du volume | 450.64 |

### Produit C
| Indicateur | Valeur |
|---|---:|
| CA moyen | 958.33 |
| CA médian | 900.00 |
| Volume moyen (qte) | 47.92 |
| Volume médian (qte) | 45.00 |
| Écart-type du volume | 17.90 |
| Variance du volume | 320.27 |

## Produit le plus populaire et produit le moins populaire (6.)
**Produit le plus vendu** :  Produit A => **Nombre de ventes** :  1 750
**Produit le moins vendu** : Produit C => **Nombre de ventes** :  575

## Graphiques (7.)

### Ventes par produit
<img alt="Ventes par produit" src="/images/ventes_par_produit.png" width="400px"/><br/>

### Chiffre d'affaire par produit
<img alt="Chiffre d'affaire par produit" src="/images/ca_par_produit.png" width="400px"/>