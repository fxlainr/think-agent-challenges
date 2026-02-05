# L'Agilité Augmentée

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Expérience Scrum, accès JIRA/Confluence |

---

## Description

> *Créez un système d'amélioration continue autonome qui analyse vos rétros, détecte les patterns récurrents et suit l'implémentation des actions.*

"On en a déjà parlé en rétro" — cette phrase, tout le monde la connaît. Ce challenge vous fait construire un agent qui analyse l'historique de vos rétrospectives, identifie les problèmes qui reviennent, et s'assure que les actions décidées sont vraiment implémentées.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline de collecte des données (rétros, métriques sprints)
- [ ] Système de détection des patterns récurrents
- [ ] Dashboard de suivi des actions d'amélioration

**Critères de réussite :**

- Les patterns récurrents sont identifiés automatiquement
- Les corrélations métriques/problèmes sont mises en évidence
- Le suivi des actions est automatisé

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                 CONTINUOUS IMPROVEMENT SYSTEM            │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Collect   │───▶│   Analyze   │───▶│   Recommend │  │
│  │             │    │             │    │             │  │
│  │ • Rétros    │    │ • Patterns  │    │ • Actions   │  │
│  │ • Sprints   │    │ • Trends    │    │ • Priority  │  │
│  │ • Incidents │    │ • Root cause│    │ • Owner     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                                      │         │
│         ▼                                      ▼         │
│  ┌─────────────┐                      ┌─────────────┐   │
│  │   Monitor   │◀─────────────────────│   Execute   │   │
│  │   Métriques │                      │   Actions   │   │
│  └─────────────┘                      └─────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Sources de données

| Source | Données | API |
|--------|---------|-----|
| JIRA | Sprints, vélocité, bugs | REST API |
| Confluence | Rétros, ADRs | REST API |
| Slack | Discussions, incidents | API Slack |
| Git | Commits, PRs, cycle time | GitHub/GitLab API |

### Patterns à détecter

**Patterns récurrents :**
- "On manque de temps pour les tests" → 3 rétros consécutives
- "Les specs arrivent trop tard" → Mentionné par 4 personnes
- "Trop de context switching" → Corrélé avec baisse vélocité

**Corrélations :**
- Vélocité ↓ quand scope change > 20%
- Bugs ↑ quand pas de code review
- Satisfaction ↓ quand actions rétro non suivies

### Prompt d'analyse longitudinale

```
Analyse ces données de rétros et métriques des 6 derniers sprints.

Identifie :
1. Les 3 patterns récurrents les plus fréquents
2. Les corrélations entre métriques et problèmes
3. Les actions proposées mais jamais implémentées
4. Les "victoires" (actions qui ont marché)

Pour chaque pattern, propose :
- Une action concrète
- Un owner suggéré
- Une métrique de succès
- Un délai réaliste
```

### Exemple de rapport

```markdown
# Analyse Amélioration Continue - Q1 2025

## 🔄 Patterns récurrents

### 1. "Specs tardives" (5 mentions sur 6 sprints)
- **Impact** : Vélocité -15% quand specs < J-2
- **Action** : Refinement obligatoire J-3
- **Owner** : PO
- **Métrique** : % stories refined avant sprint

### 2. "Dette technique ignorée" (4 mentions)
- **Impact** : Bugs +40% au S2
- **Action** : 20% du sprint dédié à la dette
- **Owner** : Tech Lead

## 📊 Corrélations identifiées

| Si... | Alors... | Confiance |
|-------|----------|-----------|
| Scope change > 20% | Vélocité -25% | 85% |
| Pas de review | Bugs +60% | 90% |

## ⚠️ Actions non implémentées
- "Automatiser les tests E2E" (proposé S1, toujours pending)
- "Daily à 9h30 au lieu de 9h" (voté mais jamais appliqué)
```

### Tips & astuces

- Commencer par les 3 derniers sprints pour valider le système
- Anonymiser les données si sensibilité politique
- Présenter les findings en rétro, pas en comité

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Collecter et structurer les données de rétros
- Détecter des patterns dans des données textuelles
- Corréler des métriques avec des problèmes qualitatifs
- Mettre en place un suivi d'actions automatisé

### Prérequis participants

- Expérience Scrum (avoir vécu des rétros)
- Accès à JIRA/Confluence (ou données exportées)
- Python ou n8n basique

### Matériel nécessaire

- [ ] Export des 6 dernières rétros (anonymisé si besoin)
- [ ] Métriques de sprints (vélocité, bugs, scope change)
- [ ] Template de rapport d'analyse
- [ ] Checklist des patterns courants

### Déroulé (4h workshop)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-60 | Théorie | Amélioration continue, patterns courants | Compréhension |
| 60-120 | Extraction | Collecter et structurer les données | Dataset prêt |
| 120-180 | Analyse | Détection de patterns et corrélations | Insights |
| 180-240 | Suivi | Mise en place du monitoring | Dashboard |

### Points d'attention animateur

**Pièges courants :**

- Données trop sensibles → Anonymiser avant l'atelier
- Blâme individuel → Focus sur les systèmes, pas les personnes
- Trop de patterns → Prioriser les 3 plus impactants

**Questions fréquentes :**

- "On n'a pas de rétros documentées" → Commencer à documenter maintenant
- "Les métriques sont fausses" → Utiliser des proxies (ex: nb commits)
- "L'équipe va mal le prendre" → Présenter comme outil d'aide, pas de contrôle

### Variantes

**Version découverte (2h) :**
- Analyse manuelle des 3 dernières rétros
- Pas d'automatisation
- Focus sur l'identification des patterns

**Version production (2 jours) :**
- Connexion temps réel aux outils
- Dashboard automatisé
- Alertes proactives

---

## Ressources complémentaires

- [Agile Retrospectives (Derby & Larsen)](https://pragprog.com/titles/dlret/agile-retrospectives/)
- [Team Topologies](https://teamtopologies.com/)
