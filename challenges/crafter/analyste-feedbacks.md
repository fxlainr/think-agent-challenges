# Analyste Feedbacks

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Avoir des verbatims clients à analyser |

---

## Description

> *Transformez vos avis clients, tickets support et commentaires réseaux sociaux en insights actionnables pour votre équipe produit.*

Des centaines de feedbacks clients arrivent chaque mois. Mais qui les lit vraiment ? Cet assistant analyse vos verbatims en masse, détecte les sentiments, identifie les irritants majeurs et fait émerger les opportunités — le tout en un rapport actionnable.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Analyse de sentiment sur un corpus de verbatims
- [ ] Identification des irritants et opportunités
- [ ] Rapport Voice of Customer avec recommandations

**Critères de réussite :**

- Les thèmes récurrents sont identifiés et quantifiés
- Les irritants sont priorisés par impact (fréquence × intensité)
- Les recommandations sont concrètes et actionnables

---

## Pistes de Solution

### Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Sources       │───▶│   Analyse IA     │───▶│   Outputs       │
│                 │    │                  │    │                 │
│ - Avis clients  │    │ - Sentiment      │    │ - Dashboard     │
│ - Tickets       │    │ - Thèmes         │    │ - Alertes       │
│ - Réseaux       │    │ - Insights       │    │ - Rapports      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Prompt système suggéré

```
Tu es un expert en Voice of Customer (VoC). Tu aides les équipes à extraire des insights actionnables de leurs feedbacks clients.

## Ton processus d'analyse

### 1. Analyse de sentiment
Pour chaque feedback :
- 😊 Positif : Satisfaction, recommandation
- 😐 Neutre : Factuel, question
- 😞 Négatif : Plainte, frustration
- Score : -2 à +2

### 2. Extraction thématique
Thèmes courants :
- Produit (qualité, fonctionnalités, bugs)
- Prix (rapport qualité/prix)
- Service (délai, réactivité)
- Livraison (délai, état)
- UX (navigation, ergonomie)

### 3. Identification des insights
- **Irritants** : fréquence × intensité
- **Opportunités** : demandes récurrentes
- **Signaux faibles** : tendances émergentes

## Format de rapport

# Analyse VoC - [Source] - [Période]

## 📊 Vue d'ensemble
| Sentiment | % | Volume |
|-----------|---|--------|
| 😊 Positif | X% | XXX |
| 😐 Neutre | X% | XXX |
| 😞 Négatif | X% | XXX |

## 🔥 Top 5 Irritants
| # | Thème | Mentions | Sentiment | Exemple |
|---|-------|----------|-----------|---------|

## 💡 Top 3 Opportunités
| Insight | Source | Potentiel |

## 🎯 Recommandations
1. Quick Win
2. Priorité
3. À explorer

Commence par : "Partage-moi les feedbacks à analyser et précise le contexte (produit, période)."
```

### Exemple d'analyse

**Input (10 verbatims) :**
```
1. "Super app, très intuitive !" ⭐⭐⭐⭐⭐
2. "Impossible de me connecter depuis la MAJ" ⭐
3. "RAS, fait le job" ⭐⭐⭐
4. "Déçu par le délai de livraison" ⭐⭐
5. "Équipe réactive, merci !" ⭐⭐⭐⭐⭐
```

**Output :**
```markdown
## 📊 Vue d'ensemble
- Volume : 10 feedbacks
- Sentiment global : +0.6 (positif)

## 🔥 Top Irritant
| Bugs/Stabilité | 1 mention | -2.0 | "Impossible de me connecter" |

## 🎯 Recommandation
**URGENT** : Investiguer le bug de connexion post-MAJ
```

### Tips & astuces

- Minimum 20-30 verbatims pour des patterns fiables
- Ne pas confondre fréquence et importance (un irritant rare peut être critique)
- Toujours illustrer avec des verbatims réels

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Analyser le sentiment d'un corpus de verbatims
- Extraire les thèmes récurrents
- Prioriser les irritants par impact
- Produire un rapport VoC actionnable

### Prérequis participants

- Avoir des verbatims clients (ou utiliser le corpus exemple)
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Corpus exemple (50-100 verbatims)
- [ ] Template de rapport VoC
- [ ] Grille de scoring sentiment

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente l'importance de la VoC | Comprennent l'enjeu | Motivation |
| 5-10 | Méthodologie | Explique sentiment, thèmes, matrice | Apprennent les techniques | Théorie |
| 10-15 | Démo | Analyse 5 verbatims en live | Observent | Voir en action |
| 15-20 | Setup | Distribue le prompt et corpus | Préparent leurs données | Préparation |
| 20-40 | Analyse | Circule, aide sur l'interprétation | Analysent leur corpus | Production |
| 40-50 | Insights | Fait identifier le top 3 irritants | Priorisent leurs findings | Synthèse |
| 50-55 | Partage | 2-3 présentations des insights | Découvrent d'autres analyses | Apprentissage |
| 55-60 | Clôture | Comment automatiser (n8n, webhooks) | Notent les next steps | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Trop peu de verbatims → Minimum 20-30 pour des patterns
- Confondre fréquence et importance → Un irritant rare peut être critique
- Pas d'action → "OK et on fait quoi maintenant ?"

**Questions fréquentes :**

- "Combien de verbatims faut-il ?" → 50+ pour des tendances fiables
- "Comment automatiser ?" → Webhook depuis outil d'avis → n8n → analyse
- "Plusieurs langues ?" → Les LLM gèrent bien le multilingue

**Tips d'animation :**

- Avoir un corpus avec des patterns clairs
- Montrer l'impact d'un insight transformé en action

### Variantes

**Version simple (45 min) :**
- Corpus de 20 verbatims
- Focus sur sentiment + 1 insight

**Version avancée (2h) :**
- 100+ verbatims multi-sources
- Dashboard de suivi automatisé

---

## Ressources complémentaires

- [Voice of Customer (Wikipedia)](https://en.wikipedia.org/wiki/Voice_of_the_customer)
- Outils : Medallia, Qualtrics, MonkeyLearn
