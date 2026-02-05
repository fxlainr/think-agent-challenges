# Le Consultant Stratégique Interne (NotebookLM RSS)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐⭐ |
| XP | 290 |
| Prérequis | Compte Google (NotebookLM) |

---

## Vision & Impact

Transformer des flux RSS et des données internes en **infographies décisionnelles** via NotebookLM. L'IA devient un conseiller spécialisé qui filtre le bruit pour ne garder que ce qui affecte la trésorerie ou la croissance.

## Le saviez-vous ?

On peut désormais demander à l'IA d'agir comme un **analyste McKinsey** pour éclairer chaque décision par des insights précieux extraits de vos propres données.

## Sources

- [Flux RSS → NotebookLM → Infographie décisionnelle - Lionel Louis](https://www.linkedin.com/posts/lionel-louis-ll_flux-rss-notebooklm-infographie-d%C3%A9cisionnelle-ugcPost-7422588098087260160-U_UC)

---

## Description

> *Créez votre propre consultant stratégique alimenté par vos sources.*

Payer un consultant 2000€/jour pour qu'il compile des infos que vous avez déjà ? Ce challenge vous fait créer un "consultant interne" nourri par vos données qui génère des analyses stratégiques sur demande.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] NotebookLM configuré avec sources pertinentes
- [ ] 3 analyses stratégiques générées
- [ ] Template de brief stratégique réutilisable

**Critères de réussite :**

- Analyses basées sur données réelles
- Insights actionnables (pas de généralités)
- Temps de génération < 10 min

---

## Pistes de Solution

### Sources à charger dans NotebookLM

```
VEILLE EXTERNE
├── RSS concurrents
├── Articles sectoriels
├── Rapports analystes
└── Newsletters clés

DONNÉES INTERNES
├── Rapports mensuels
├── KPIs historiques
├── Comptes-rendus COMEX
└── Feedbacks clients

CONTEXTE STRATÉGIQUE
├── Plan stratégique
├── OKRs en cours
├── Budgets
└── Roadmap produit
```

### Configuration NotebookLM

```
1. Créer un Notebook "Stratégie [Entreprise]"
2. Uploader les sources (PDF, docs, liens)
3. Attendre l'indexation
4. Tester avec des questions simples
5. Affiner les sources si nécessaire
```

### Prompts d'analyse stratégique

**Analyse de marché :**
```
En te basant sur les sources chargées, génère une analyse de marché :

1. Tendances émergentes (3-5)
2. Mouvements des concurrents
3. Opportunités identifiées
4. Menaces à surveiller
5. Recommandations (priorisées)

Cite tes sources pour chaque point.
```

**Brief décisionnel :**
```
Je dois prendre une décision sur [sujet].

En te basant sur nos données :
1. Résume le contexte en 3 phrases
2. Liste les options possibles
3. Pour chaque option : avantages, risques, données supportant
4. Recommandation argumentée
5. Questions restantes à clarifier
```

**Préparation COMEX :**
```
Prépare une note de synthèse pour le COMEX sur [sujet] :

- Executive summary (5 lignes max)
- Chiffres clés (3-5)
- Situation actuelle vs objectifs
- Points d'attention
- Décisions requises
- Prochaines étapes

Ton : factuel, direct, orienté action.
```

### Template d'infographie décisionnelle

```markdown
# [TITRE DE L'ANALYSE]
Date : [DATE] | Sources : [LISTE]

## 🎯 En une phrase
[Le message clé]

## 📊 Chiffres clés
| Indicateur | Valeur | Tendance |
|------------|--------|----------|
| ...        | ...    | ↑↓→      |

## 💡 Insights principaux
1. [Insight 1 + source]
2. [Insight 2 + source]
3. [Insight 3 + source]

## ⚠️ Points d'attention
- [Risque/opportunité 1]
- [Risque/opportunité 2]

## ✅ Recommandations
1. [Action immédiate]
2. [Action court terme]
3. [Action moyen terme]

## ❓ Questions ouvertes
- [Ce qu'il faudrait creuser]
```

---

## Animation Dojo (1h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Le consultant à 2000€/jour vs NotebookLM |
| 10-25 | Setup | Charger les sources dans NotebookLM |
| 25-45 | Analyse | Générer 2 analyses stratégiques |
| 45-55 | Template | Créer son template réutilisable |
| 55-60 | Clôture | Intégrer dans les rituels |

### Points d'attention

- La qualité des sources = qualité de l'analyse
- Toujours vérifier les citations
- L'IA aide à synthétiser, l'humain décide
