# Le ML Experimenter

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Python, notions de ML |

---

## Description

> *Créez un assistant de prototypage ML qui guide vos expérimentations : hypothèses, code, documentation et interprétation des résultats.*

"On a essayé XGBoost mais ça marche pas." Pourquoi ? Ce challenge vous fait construire un système d'expérimentation ML structuré — hypothèses claires, code reproductible, résultats documentés.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant guidant les expérimentations ML
- [ ] Notebook documenté avec hypothèses et résultats
- [ ] Interprétation des modèles

**Critères de réussite :**

- Chaque expérience a une hypothèse claire
- Les résultats sont reproductibles
- Les erreurs du modèle sont analysées

---

## Pistes de Solution

### Workflow d'expérimentation

```
Problème Business → Hypothèse → Expérience → Résultats
         ↓              ↓           ↓           ↓
    "Prédire X"    "Approche Y"   "Code"    "Métriques"
                                              ↓
                              Interprétation → Décision (next)
```

### Prompt système suggéré

```
Tu es un ML Engineer/Data Scientist senior.

## Ton processus

### 1. Cadrage
- Quel problème business ?
- Quel type de ML ? (classification, régression, clustering...)
- Quelles données disponibles ?
- Quelle métrique de succès ?

### 2. Hypothèses
- Quelles approches tester ?
- Pourquoi cette approche ?
- Baseline à battre ?

### 3. Expérimentation
- Code propre et reproductible
- Logging des hyperparamètres
- Versioning des expériences

### 4. Interprétation
- Feature importance
- Analyse des erreurs
- Limites du modèle

Commence par : "Quel problème ML veux-tu résoudre ? Quelles données as-tu ?"
```

### Format de documentation

```markdown
# Experiment Log

## Contexte
- **Problème** : [Description business]
- **Données** : [Sources, taille, période]
- **Métrique** : [Métrique principale + seuil de succès]
- **Baseline** : [Performance à battre]

---

## Expérience #1

### Hypothèse
[Ce qu'on teste et pourquoi]

### Approche
- **Modèle** : [Nom]
- **Features** : [Liste]
- **Hyperparams** : [Valeurs]

### Code
```python
# Code minimal reproductible
```

### Résultats
| Métrique | Train | Test |
|----------|-------|------|
| Accuracy | X% | X% |
| F1 | X | X |

### Analyse
- [Pourquoi ce résultat]
- [Erreurs typiques]

### Next
- [Prochaine expérience à tenter]

---

## Expérience #2
[Même structure]
```

### Outils recommandés

| Outil | Usage |
|-------|-------|
| MLflow | Tracking expériences |
| Weights & Biases | Visualisation |
| Jupyter | Prototypage |
| Scikit-learn | Modèles classiques |
| XGBoost/LightGBM | Gradient boosting |

### Tips & astuces

- Une hypothèse = une expérience
- Toujours commencer par un baseline simple
- Logger TOUT (même les échecs)

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Structurer une démarche d'expérimentation ML
- Documenter proprement les expériences
- Interpréter les résultats et erreurs
- Itérer de manière rigoureuse

### Prérequis participants

- Python niveau intermédiaire
- Notions de ML (train/test, métriques de base)
- Jupyter installé

### Matériel nécessaire

- [ ] Dataset préparé (classification binaire)
- [ ] Notebook de démarrage
- [ ] Template d'experiment log
- [ ] Prompt système

### Déroulé (4h)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-45 | Théorie | Workflow d'expérimentation | Compréhension |
| 45-90 | Setup | Environnement + baseline | Première expérience |
| 90-150 | Itérations | 2-3 expériences guidées | Experiment log |
| 150-180 | Interprétation | Feature importance, erreurs | Analyse |
| 180-210 | Documentation | Mise au propre | Notebook final |
| 210-240 | Présentation | Chacun présente ses learnings | Partage |

### Points d'attention animateur

**Pièges courants :**

- Pas d'hypothèse claire → "Qu'est-ce qu'on teste ?"
- Overfitting → "Compare train vs test"
- Pas de baseline → "Comment tu sais que c'est mieux ?"

**Questions fréquentes :**

- "Quel modèle choisir ?" → Commence simple (logistic regression)
- "C'est pas assez bon" → Analyse les erreurs avant de complexifier
- "Je log quoi ?" → Hyperparams, métriques, temps, version code

### Variantes

**Version découverte (2h) :**
- Dataset fourni et préparé
- 1 seule expérience complète
- Focus sur la documentation

**Version avancée (8h) :**
- Problème ouvert (NLP, time series)
- MLflow ou W&B intégré
- Présentation formelle

---

## Ressources complémentaires

- [MLflow](https://mlflow.org/)
- [Weights & Biases](https://wandb.ai/)
- [Made With ML](https://madewithml.com/)
