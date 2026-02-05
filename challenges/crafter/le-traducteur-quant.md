# Le Traducteur Quant

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Culture finance de marché (basique) |

---

## Description

> *Créez un assistant qui traduit les spécifications métier finance en spécifications techniques — le pont entre traders et développeurs.*

"On veut le P&L explain sur nos positions options." Qu'est-ce que ça veut dire techniquement ? Ce challenge vous fait créer un traducteur bilingue métier/IT pour la finance de marché.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant de traduction métier → technique
- [ ] Spec technique générée à partir d'un besoin réel ou fictif
- [ ] Format exploitable par une équipe IT/Quant

**Critères de réussite :**

- Le vocabulaire finance est correctement interprété
- Les formules sont explicitées
- Les cas de bord sont identifiés

---

## Pistes de Solution

### Vocabulaire bilingue

**Pricing / Valorisation :**
| Métier dit... | IT comprend... |
|---------------|-----------------|
| "Prix de marché" | Mark-to-Market (MtM) |
| "Grecques" | Delta, Gamma, Vega, Theta, Rho |
| "La vol" | Volatilité implicite |

**Risque :**
| Métier dit... | IT comprend... |
|---------------|-----------------|
| "VaR" | Value at Risk |
| "Stress test" | Scénarios de choc |
| "P&L explain" | Attribution de performance |

### Prompt système suggéré

```
Tu es un Business Analyst senior spécialisé marchés financiers.

## Ta mission
Traduire les besoins métier (traders, risk managers) en spécifications techniques (développeurs, quants).

## Ton processus

### 1. Écoute active
- Reformuler le besoin
- Identifier les termes ambigus
- Poser des questions de clarification

### 2. Structuration
- Décomposer en sous-problèmes
- Identifier les données nécessaires
- Formaliser les règles de calcul

### 3. Rédaction
- Spec technique au format standard
- Formules mathématiques si nécessaire
- Cas de bord et erreurs

Commence par : "Décris-moi le besoin métier. Qui le demande et quel problème ça résout ?"
```

### Format de spécification

```markdown
# Spécification Technique
## [Nom du projet]

### 1. Contexte métier
- Demandeur : [Desk, équipe]
- Besoin : [Description]
- Criticité : [Haute/Moyenne/Basse]

### 2. Périmètre
- Produits : [Types d'instruments]
- Devises : [EUR, USD...]
- Volume : [Estimation]

### 3. Règles de calcul
[Formules mathématiques]

### 4. Données entrantes

| Donnée | Source | Format | Fréquence |
|--------|--------|--------|-----------|

### 5. Données sortantes

| Résultat | Destination | Format | SLA |
|----------|-------------|--------|-----|

### 6. Cas de bord
- [Situation] → [Traitement]

### 7. Critères de recette
- [ ] [Critère 1]
- [ ] [Critère 2]
```

### Exemple de demande métier

```
"Salut, on a besoin d'avoir le P&L explain sur nos positions 
options sur actions européennes. Aujourd'hui on a juste le 
P&L total, on veut voir ce qui vient du delta, de la vol, 
du temps, etc. C'est pour le reporting quotidien."
```

**→ Traduit en :** Décomposition P&L Taylor 1er ordre (Delta, Gamma, Vega, Theta, Rho, Résiduel)

### Tips & astuces

- Toujours reformuler pour confirmer
- Les conventions comptent (jour calendaire vs ouvré)
- Identifier les zones grises tôt

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Comprendre le vocabulaire finance de base
- Poser les bonnes questions de clarification
- Structurer une spécification technique
- Identifier les cas de bord critiques

### Prérequis participants

- Culture finance basique (ou curiosité)
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Glossaire métier/technique
- [ ] 2-3 demandes métier à traduire
- [ ] Template de spec

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente le défi Front/IT | Comprennent l'enjeu | Contexte |
| 5-12 | Glossaire | Parcourt le vocabulaire clé | Découvrent les termes | Vocabulaire |
| 12-18 | Démo | Traduit une demande simple | Observent le processus | Voir en action |
| 18-23 | Setup | Distribue prompt et demandes | Forment des binômes | Préparation |
| 23-43 | Traduction | Circule, aide sur le vocabulaire | Traduisent leur demande | Production |
| 43-53 | Review | Fait reviewer par un autre binôme | Challengent les specs | Qualité |
| 53-60 | Clôture | Bonnes pratiques | Notent les apprentissages | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- Jargon non traduit → Toujours définir
- Cas de bord oubliés → "Et si la donnée manque ?"
- Spec trop vague → "Quelle formule exactement ?"

**Questions fréquentes :**

- "Je ne connais pas la finance" → Le glossaire suffit pour l'exercice
- "Comment valider avec le métier ?" → Reformuler et confirmer
- "C'est trop technique" → Adapter le niveau à l'audience

### Variantes

**Version simple (45 min) :**
- Demande simple (calcul de P&L basique)
- Template pré-rempli

**Version avancée (2h) :**
- Demande complexe (pricing exotique)
- Formules mathématiques complètes

---

## Ressources complémentaires

- [Investopedia](https://www.investopedia.com/)
- [Options Greeks](https://www.investopedia.com/terms/g/greeks.asp)
