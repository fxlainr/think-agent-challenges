# Automated Platform Manager

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐⭐ |
| Prérequis | n8n, notions marketing digital |

---

## Description

> *Créez un système autonome de pilotage de plateforme : acquisition, onboarding, engagement, rétention — le tout orchestré par des workflows intelligents.*

Votre plateforme tourne 24/7 mais vous dormez. Ce challenge vous fait construire un gestionnaire automatique qui acquiert des utilisateurs, les onboarde, les engage et les retient — sans intervention humaine.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Système de workflows n8n interconnectés (4 phases)
- [ ] Dashboard de suivi des métriques AARRR
- [ ] Documentation des règles d'automatisation

**Critères de réussite :**

- Chaque phase du funnel est automatisée
- Les triggers sont bien définis
- Les métriques sont trackées

---

## Pistes de Solution

### Architecture AARRR

```
┌─────────────────────────────────────────────────────────┐
│                  PLATFORM MANAGER                        │
├─────────────┬─────────────┬─────────────┬───────────────┤
│ Acquisition │  Onboarding │ Engagement  │  Rétention    │
│             │             │             │               │
│ • Landing   │ • Welcome   │ • Usage     │ • Churn       │
│ • Signup    │ • Tutorial  │ • Features  │ • Win-back    │
│ • Activation│ • First     │ • Community │ • Feedback    │
│             │   value     │             │               │
└─────────────┴─────────────┴─────────────┴───────────────┘
         │             │             │             │
         ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                    AUTOMATION ENGINE (n8n)               │
│  • Triggers • Actions • Rules • Monitoring              │
└─────────────────────────────────────────────────────────┘
```

### Workflows à créer

| Phase | Trigger | Action | Objectif |
|-------|---------|--------|----------|
| Acquisition | Visite > 3 pages | Popup inscription | Conversion |
| Onboarding | Signup | Email bienvenue + séquence | Activation |
| Activation | 0 action après 24h | Email rappel + push | First value |
| Engagement | Feature non utilisée | Tutorial ciblé | Adoption |
| Rétention | Inactivité 7 jours | Email win-back | Anti-churn |

### Métriques à monitorer

| Métrique | Formule | Objectif |
|----------|---------|----------|
| Conversion | Signups / Visiteurs | > 5% |
| Activation | First value / Signups | > 60% |
| DAU/MAU | Daily / Monthly active | > 20% |
| Churn | Partis / Total | < 5%/mois |

### Structure du livrable

```
📁 Platform Manager
├── workflows/
│   ├── acquisition.json
│   ├── onboarding.json
│   ├── engagement.json
│   └── retention.json
├── dashboards/
│   └── metrics.md
└── documentation/
    └── rules.md
```

### Exemple de workflow : Onboarding

```json
{
  "name": "Onboarding Sequence",
  "nodes": [
    {
      "name": "Webhook - New Signup",
      "type": "webhook",
      "parameters": { "path": "signup" }
    },
    {
      "name": "Send Welcome Email",
      "type": "emailSend",
      "parameters": {
        "subject": "Bienvenue sur [Plateforme] !",
        "template": "welcome"
      }
    },
    {
      "name": "Wait 24h",
      "type": "wait",
      "parameters": { "amount": 24, "unit": "hours" }
    },
    {
      "name": "Check First Action",
      "type": "httpRequest",
      "parameters": { "url": "/api/user/{{userId}}/actions" }
    },
    {
      "name": "If No Action",
      "type": "if",
      "parameters": { "condition": "actions.length === 0" }
    },
    {
      "name": "Send Reminder",
      "type": "emailSend",
      "parameters": {
        "subject": "Tu n'as pas encore essayé [Feature] !",
        "template": "reminder"
      }
    }
  ]
}
```

### Tips & astuces

- Commencer par un workflow simple (onboarding)
- Tester chaque trigger manuellement
- Logger tout pour debug

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Concevoir un funnel AARRR automatisé
- Créer des workflows n8n interconnectés
- Définir des triggers et des règles métier
- Monitorer les métriques clés

### Prérequis participants

- Compte n8n (cloud ou self-hosted)
- Notions de marketing digital (funnel, conversion)

### Matériel nécessaire

- [ ] Templates de workflows n8n
- [ ] Liste des triggers/actions possibles
- [ ] Template de dashboard
- [ ] Schéma AARRR

### Déroulé (4h)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-45 | Théorie | AARRR + automatisation plateforme | Compréhension |
| 45-120 | Workflows | Construction des 4 workflows | n8n fonctionnel |
| 120-150 | Dashboard | Mise en place du suivi métriques | Monitoring |
| 150-180 | Tests | Simulation du parcours utilisateur | Validation |
| 180-210 | Documentation | Règles métier | Docs |
| 210-240 | Demo | Chacun présente son système | Partage |

### Points d'attention animateur

**Pièges courants :**

- Workflows trop complexes → Commencer simple
- Pas de tests → Simuler les triggers
- Oublier les cas d'erreur → Ajouter des fallbacks

**Questions fréquentes :**

- "Comment connecter à ma plateforme ?" → Webhooks + API
- "Quelle fréquence pour les relances ?" → Tester et itérer
- "Comment éviter le spam ?" → Limiter le nombre de touchpoints

### Variantes

**Version simple (2h) :**
- 2 workflows seulement (onboarding + rétention)
- Pas de dashboard

**Version avancée (8h) :**
- Multi-canaux (email, push, SMS)
- A/B testing des messages
- Scoring utilisateur

---

## Ressources complémentaires

- [n8n Documentation](https://docs.n8n.io/)
- [AARRR Framework](https://www.productplan.com/glossary/aarrr-framework/)
