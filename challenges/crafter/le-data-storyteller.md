# Le Data Storyteller

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Avoir des données à transformer |

---

## Description

> *Transformez vos analyses data et tableaux de chiffres en narratifs business qui font bouger les décideurs.*

Les décideurs n'ont pas le temps de lire vos dashboards. Ils veulent savoir : "C'est bien ou pas ? On fait quoi ?". Cet assistant prend vos données brutes et les transforme en synthèses percutantes adaptées à votre audience — COMEX, sponsor, client.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Une synthèse COMEX à partir de données brutes
- [ ] Adaptation à différentes audiences (email, slide, note)
- [ ] Message clair avec call to action

**Critères de réussite :**

- Le message clé est identifiable en 5 secondes
- Le "so what" est explicite (pas juste des chiffres)
- L'action demandée est claire

---

## Pistes de Solution

### Approche recommandée

Le data storytelling repose sur 3 principes :

1. **Pyramide inversée** — Le message clé en premier
2. **So What?** — Chaque donnée doit répondre à "Et alors ?"
3. **Les 3 C** — Clair, Concis, Convaincant

### Prompt système suggéré

```
Tu es un expert en data storytelling avec 12 ans d'expérience en conseil stratégique.

## Ta mission
Transformer des données brutes en communications impactantes pour les décideurs.

## Tes principes

### Pyramide inversée
- **Lead** : Le message clé en premier (1 phrase)
- **Contexte** : Pourquoi c'est important (2-3 phrases)
- **Détails** : Les chiffres qui supportent

### Le "So What?"
Pour chaque donnée :
- "Et alors ?" → Impact business
- "Pour qui ?" → Qui est concerné
- "On fait quoi ?" → Décision à prendre

## Formats de sortie

### Format COMEX (1 page)
# [Titre accrocheur avec le chiffre clé]

## 💡 En une phrase
[Le message principal]

## 📊 Les chiffres qui comptent
| Métrique | Avant | Après | Signal |
|----------|-------|-------|--------|

## 🎯 Ce que ça veut dire
[2-3 phrases d'interprétation]

## ⚡ Actions recommandées
1. [Action prioritaire]

### Format Email
Objet : [Chiffre clé] - [Action attendue]

En 30 secondes :
• [Constat principal]
• [Impact chiffré]
• [Recommandation]

Besoin de ta validation pour [action] d'ici [date].

### Format Slide
## [Titre = Message clé]
[Un seul visuel]
### Insight : [1 phrase]
### Recommandation : [1 action]

Commence par : "Envoie-moi les données à transformer et dis-moi à qui c'est destiné."
```

### Exemple de transformation

**Données brutes :**
```
Janvier 2025
- Visiteurs : 45,230 (-12% vs décembre)
- Conversion : 3.2% (+0.5 pts)
- Panier moyen : 87€ (+8€)
- CA : 126,450€ (-5%)
- NPS : 67 (+12 pts)
```

**Synthèse COMEX :**

```markdown
# Le CA recule mais les fondamentaux sont au vert

## 💡 En une phrase
Malgré une baisse de trafic post-fêtes (-12%), les indicateurs de qualité progressent tous : conversion record, panier en hausse, satisfaction au plus haut.

## 📊 Les chiffres qui comptent

| Métrique | Janvier | vs Déc | Signal |
|----------|---------|--------|--------|
| Visiteurs | 45,230 | -12% | 🟡 Saisonnier |
| Conversion | 3.2% | +0.5 pts | 🟢 Record |
| Panier | 87€ | +8€ | 🟢 Upsell OK |
| NPS | 67 | +12 pts | 🟢 Excellent |

## 🎯 Ce que ça veut dire
Le recul du CA est un effet volume, pas performance. Chaque visiteur convertit mieux et dépense plus. Le NPS confirme que l'expérience s'améliore.

## ⚡ Actions recommandées
1. **Investir en acquisition** — les fondamentaux sont solides
2. **Capitaliser sur le NPS** — lancer le programme parrainage
```

### Tips & astuces

- Un seul message principal (pas 5)
- Toujours finir par une action ou une question
- Adapter le niveau de détail à l'audience (COMEX = synthèse, équipe = détail)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier le message clé dans un jeu de données
- Adapter leur communication à l'audience
- Utiliser la pyramide inversée
- Créer des synthèses impactantes rapidement

### Prérequis participants

- Avoir des données à transformer (ou utiliser l'exemple)
- Accès à un chat IA
- Aucune compétence data requise

### Matériel nécessaire

- [ ] Prompt système
- [ ] Dataset exemple
- [ ] Templates de sortie (COMEX, email, slide)
- [ ] Exemples avant/après

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Montre un avant/après | Découvrent la valeur | Motivation |
| 5-10 | Principes | Présente pyramide inversée et "So What" | Comprennent les techniques | Théorie |
| 10-15 | Démo | Transforme le dataset exemple | Observent le processus | Voir en action |
| 15-20 | Setup | Distribue le prompt | Préparent leurs données | Préparation |
| 20-40 | Transformation | Circule, aide à trouver l'angle | Transforment leurs données | Production |
| 40-50 | Pitch | Fait pitcher 3-4 synthèses (1 min) | Présentent leur message | Communication |
| 50-55 | Feedback | Donne du feedback sur la clarté | Notent les améliorations | Amélioration |
| 55-60 | Clôture | Récapitule les bonnes pratiques | Notent leur prochain use case | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Trop de chiffres → "Quel est LE chiffre qui compte ?"
- Pas de "so what" → "Ok, et alors ?"
- Jargon technique → "Ta grand-mère comprendrait ?"

**Questions fréquentes :**

- "J'ai trop de données" → Prioriser, un message principal
- "Je ne sais pas quel angle choisir" → Quelle décision ça doit éclairer ?
- "C'est trop simplifié ?" → Non, les décideurs veulent la conclusion

**Tips d'animation :**

- Faire le jeu "Trouve le headline"
- Chrono 2 min pour forcer la synthèse
- Vote pour le pitch le plus convaincant

### Variantes

**Version courte (30 min) :**
- Dataset simple fourni
- Un seul format (email)

**Version longue (2h) :**
- Données complexes
- Multi-formats (COMEX + email + slide)
- Présentation orale avec Q&A

---

## Ressources complémentaires

- Livre : "Storytelling with Data" (Cole Nussbaumer Knaflic)
- [Datawrapper](https://www.datawrapper.de/) — pour les visualisations
