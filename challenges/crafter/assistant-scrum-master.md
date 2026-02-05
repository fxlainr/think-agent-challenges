# Assistant Scrum Master

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Accès JIRA (ou données mockées), notions Scrum |

---

## Description

> *Créez un assistant connecté à JIRA qui analyse la performance de votre équipe et génère des insights actionnables pour vos rétros.*

Vélocité en baisse ? Scope qui change en cours de sprint ? Tickets qui stagnent ? Cet assistant extrait les données de JIRA, calcule les métriques clés et génère un rapport d'analyse avec des recommandations concrètes pour le prochain sprint.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Extraction des données sprint (JIRA API ou mockup)
- [ ] Calcul des métriques clés (vélocité, engagement, blocages)
- [ ] Rapport d'analyse avec insights actionnables

**Critères de réussite :**

- Les métriques sont calculées correctement
- Le rapport identifie les tendances (pas juste les chiffres)
- Les recommandations sont concrètes et actionnables

---

## Pistes de Solution

### Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   JIRA      │───▶│   n8n/code   │───▶│   Analyse   │
│   (API)     │    │   (extract)  │    │   (LLM)     │
└─────────────┘    └──────────────┘    └─────────────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │   Rapport   │
                                       │   Sprint    │
                                       └─────────────┘
```

### Données à extraire de JIRA

| Donnée | Endpoint API | Usage |
|--------|--------------|-------|
| Sprints | `/rest/agile/1.0/board/{id}/sprint` | Liste des sprints |
| Issues du sprint | `/rest/agile/1.0/sprint/{id}/issue` | Tickets du sprint |
| Changelog | `/rest/api/3/issue/{id}/changelog` | Historique des changements |

### Métriques à calculer

```javascript
// Vélocité
const velocity = issues
  .filter(i => i.fields.status.name === 'Done')
  .reduce((sum, i) => sum + (i.fields.storyPoints || 0), 0);

// Engagement tenu
const committed = issues.length;
const completed = issues.filter(i => i.fields.status.name === 'Done').length;
const commitmentRate = (completed / committed) * 100;

// Scope change
const addedDuringSprint = issues.filter(i => {
  const created = new Date(i.fields.created);
  return created > sprintStart;
}).length;
```

### Prompt système suggéré

```
Tu es un Scrum Master analytique qui aide les équipes à s'améliorer.

## Tes analyses

### 1. Vélocité
- Vélocité du sprint (story points terminés)
- Tendance sur les 5 derniers sprints
- Écart vs engagement initial

### 2. Flux de travail
- Temps moyen par statut
- Tickets bloqués > 2 jours
- Pattern de changement de scope

### 3. Qualité
- Bugs introduits pendant le sprint
- Ratio bugs/features
- Tickets réouverts

### 4. Prédictibilité
- % d'engagement tenu
- Corrélation estimation/réel

## Format de rapport

# Rapport Sprint [Nom]

## 📊 Vue d'ensemble
| Métrique | Valeur | Tendance |
|----------|--------|----------|
| Vélocité | X pts | ↗️ +10% |
| Engagement tenu | X% | → Stable |
| Bugs | X | ↘️ -2 |

## ✅ Ce qui a bien fonctionné
- [Point positif 1]
- [Point positif 2]

## ⚠️ Points d'attention
- [Alerte 1]
- [Alerte 2]

## 🎯 Recommandations pour le prochain sprint
1. [Recommandation actionnable]
2. [Recommandation actionnable]

Commence par : "Donne-moi les données de ton sprint (ou connecte-moi à JIRA)."
```

### Exemple de rapport généré

```markdown
# Rapport Sprint 2024-S03

## 📊 Vue d'ensemble
| Métrique | Valeur | Tendance |
|----------|--------|----------|
| Vélocité | 34 pts | ↗️ +8% vs S02 |
| Engagement tenu | 85% | → Stable |
| Bugs | 2 | ↘️ -3 vs S02 |
| Scope change | 3 tickets ajoutés | ↗️ Attention |

## ✅ Ce qui a bien fonctionné
- Vélocité en hausse pour le 3ème sprint consécutif
- Zéro ticket bloqué plus de 48h
- Qualité en amélioration (moins de bugs)

## ⚠️ Points d'attention
- 3 tickets ajoutés en cours de sprint (scope creep)
- Le ticket PROJ-234 a changé 4 fois de statut (ping-pong)

## 🎯 Recommandations
1. **Protéger le sprint** : Refuser les ajouts non critiques après J3
2. **Clarifier PROJ-234** : Revoir les critères d'acceptation avec le PO
```

### Tips & astuces

- Commencer avec des données mockées si pas d'accès JIRA
- Comparer toujours sur plusieurs sprints (tendances > valeur absolue)
- Les recommandations doivent être actionnables (qui fait quoi)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les métriques Scrum pertinentes
- Extraire des données de JIRA (ou les simuler)
- Générer un rapport d'analyse avec l'IA
- Formuler des recommandations actionnables

### Prérequis participants

- Accès à un chat IA
- Données de sprint (JIRA export ou mockup fourni)
- Notions de Scrum (vélocité, sprint, story points)

### Matériel nécessaire

- [ ] Prompt système
- [ ] Jeu de données fictif (si pas d'accès JIRA)
- [ ] Template de rapport
- [ ] Liste des métriques Scrum avec définitions

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro métriques | Présente les KPIs Scrum clés | Découvrent les métriques | Théorie |
| 10-20 | Démo | Montre comment extraire/analyser les données | Observent | Voir le process |
| 20-40 | Construction | Circule, aide à configurer | Génèrent leur rapport | Production |
| 40-55 | Analyse | Fait discuter les insights | Interprètent leurs résultats | Sens critique |
| 55-60 | Discussion | Comment utiliser en rétro ? | Partagent leurs idées | Application |

### Points d'attention animateur

**Pièges courants :**

- Se noyer dans les métriques → Focus sur 3-4 max
- Chiffres sans contexte → Toujours comparer (vs sprint précédent, vs objectif)
- Recommandations vagues → "Qui fait quoi pour quand ?"

**Questions fréquentes :**

- "On n'a pas de story points" → Utiliser le nombre de tickets ou le temps
- "Nos sprints sont irréguliers" → Normaliser (vélocité/jour)
- "C'est pas la faute de l'équipe" → L'outil diagnostique, pas blâme

**Tips d'animation :**

- Avoir des données anonymisées d'un vrai sprint
- Faire le lien avec les pratiques de rétro
- Montrer comment challenger les chiffres

### Variantes

**Sans JIRA (45 min) :**
- Utiliser le jeu de données fourni
- Focus sur l'analyse et l'interprétation
- Pas de partie technique extraction

**Avec équipe réelle (2h) :**
- Connecter au vrai JIRA de l'équipe
- Analyser les 5 derniers sprints
- Préparer la prochaine rétro ensemble

---

## Ressources complémentaires

- [Scrum Guide](https://scrumguides.org/)
- [JIRA REST API Documentation](https://developer.atlassian.com/cloud/jira/software/rest/)
