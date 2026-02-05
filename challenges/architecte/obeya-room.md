# L'Architecte de l'Obeya (Transversal Sync)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | Tous |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 380 |
| Prérequis | Accès aux données de plusieurs équipes |

---

## Vision & Impact

Créer une **Obeya Room** augmentée par l'IA pour arrêter de gérer en silos. L'IA corrèle les données de toutes les directions pour offrir une visibilité 360° et identifier les risques de friction entre les départements.

## Le saviez-vous ?

Une Obeya Room virtuelle permet de passer du simple reporting à une **gouvernance prospective** du flux de valeur. On anticipe au lieu de réagir.

## Sources

- [Stop managing in silos - Sergio D'Amico](https://www.linkedin.com/posts/sergio-d-amico-cssbb-5856712_stop-managing-in-silos-and-scattered-dashboards-activity-7410673463411044352-hOA6)

---

## Description

> *Créez un centre de commandement qui unifie la vision de toutes les équipes.*

Flow avance. Value est bloqué. Shield n'est pas au courant. Fi découvre le problème trop tard. Ce challenge vous fait construire une Obeya Room digitale où tout le monde voit tout, en temps réel.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Dashboard unifié multi-équipes
- [ ] Système de détection de frictions
- [ ] Alertes croisées automatiques

**Critères de réussite :**

- Vision 360° en un coup d'œil
- Corrélations inter-équipes identifiées
- Décisions accélérées

---

## Pistes de Solution

### Concept Obeya

```
OBEYA (大部屋) = "Grande salle" en japonais

PRINCIPES :
1. Tout est visible (pas de données cachées)
2. Temps réel (pas de reporting mensuel)
3. Corrélé (les liens entre équipes)
4. Actionnable (pas juste de l'info)
```

### Architecture de l'Obeya digitale

```
┌─────────────────────────────────────────────────────────────┐
│                       OBEYA ROOM                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │  FLOW   │  │  VALUE  │  │ SHIELD  │  │   FI    │       │
│  │ Produit │  │  Tech   │  │ Qualité │  │ Finance │       │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘       │
│       │            │            │            │             │
│       └────────────┴────────────┴────────────┘             │
│                         │                                   │
│              ┌──────────▼──────────┐                       │
│              │   CORRÉLATIONS IA   │                       │
│              │   Frictions & Deps  │                       │
│              └─────────────────────┘                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ 🔴 ALERTES   🟡 RISQUES   🟢 ON TRACK   📊 TENDANCES      │
└─────────────────────────────────────────────────────────────┘
```

### Données à agréger

```
FLOW (Produit)
- Features en cours
- Backlog priorisé
- User feedback
- Dates de release

VALUE (Tech)
- Vélocité équipes
- Dette technique
- Incidents
- Déploiements

SHIELD (Qualité)
- Bugs ouverts/fermés
- Couverture tests
- Temps de résolution
- Vulnérabilités

FI (Finance)
- Budget consommé
- Prévisions
- ROI par projet
- Cash flow
```

### Prompt de corrélation

```
Voici les données de nos 4 directions :

FLOW : [données]
VALUE : [données]
SHIELD : [données]
FI : [données]

Analyse et identifie :

## Corrélations
- Quels éléments sont liés entre les équipes ?
- Quelles dépendances ne sont pas visibles ?

## Frictions potentielles
- Où y a-t-il des objectifs contradictoires ?
- Quelles équipes vont se bloquer mutuellement ?

## Risques croisés
- Si X échoue chez Flow, quel impact sur Value ?
- Si le budget Fi est dépassé, quelles conséquences ?

## Recommandations
- Actions de synchronisation à prendre
- Décisions à escalader
```

### Alertes croisées

```python
CROSS_ALERTS = [
    {
        "condition": "flow.release_delayed AND value.velocity_low",
        "alert": "Release à risque - Vélocité insuffisante",
        "notify": ["CPO", "CTO"]
    },
    {
        "condition": "shield.bugs_critical > 5 AND flow.release_imminent",
        "alert": "Bloquant : Bugs critiques avant release",
        "notify": ["QA Lead", "PM"]
    },
    {
        "condition": "fi.budget_remaining < 20% AND value.scope_increased",
        "alert": "Alerte budget vs scope",
        "notify": ["CFO", "CPO"]
    }
]
```

---

## Animation Dojo (2h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Le problème des silos |
| 15-35 | Concept | Obeya traditionnelle vs digitale |
| 35-65 | Données | Identifier les données de chaque équipe |
| 65-95 | Corrélations | Mapper les dépendances |
| 95-115 | Dashboard | Construire la vue unifiée |
| 115-120 | Clôture | Gouvernance et rituels |

### Points d'attention

- Accès aux données = politique
- Commencer simple, enrichir ensuite
- Le but est la décision, pas le dashboard parfait
