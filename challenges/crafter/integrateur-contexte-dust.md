# L'Intégrateur de Contexte (Collaboration Dust)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | Tous |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐⭐ |
| XP | 250 |
| Prérequis | Compte Dust ou équivalent |

---

## Vision & Impact

Utiliser les **mentions Dust** pour collaborer mieux et plus vite en intégrant le contexte de l'entreprise directement dans les conversations IA. L'IA dispose de toute la connaissance interne pour agir comme un véritable équipier.

## Le saviez-vous ?

L'IA active ne se contente pas de répondre, elle **collabore** au sein même de vos flux de travail existants. Elle connaît vos docs, vos projets, votre historique.

## Sources

- [Dust Mentions - Collaborate better together](https://www.linkedin.com/posts/dust-tt_mentions-collaborate-better-together-activity-7414331166507569153-YNUF)

---

## Description

> *Donnez à l'IA le contexte complet de votre entreprise pour des réponses pertinentes.*

"L'IA ne connaît pas notre contexte." Plus maintenant. Ce challenge vous fait connecter l'IA à votre base de connaissances pour qu'elle réponde avec le contexte de votre entreprise, pas des généralités.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Base de connaissances connectée à l'IA
- [ ] Workflow de mise à jour du contexte
- [ ] 5 use cases métier fonctionnels

**Critères de réussite :**

- Réponses contextualisées à l'entreprise
- Sources citées dans les réponses
- Mise à jour du contexte < 24h

---

## Pistes de Solution

### Sources de contexte à connecter

```
DOCUMENTATION
├── Wiki interne
├── Confluence/Notion
├── Google Drive
└── SharePoint

COMMUNICATION
├── Slack (canaux publics)
├── Emails (archivés)
└── Meeting notes

DONNÉES MÉTIER
├── CRM (Salesforce, HubSpot)
├── Tickets (Jira, Linear)
├── Analytics

CODE & TECHNIQUE
├── README
├── Documentation API
└── Architecture decisions
```

### Architecture avec Dust

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  SOURCES        │────▶│  DUST           │────▶│  CHAT           │
│  (Notion, Slack)│     │  (Indexation)   │     │  (Contextuel)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │
                              ▼
                        ┌─────────────────┐
                        │  @mentions      │
                        │  @docs @projet  │
                        └─────────────────┘
```

### Use cases métier

```
1. ONBOARDING
   "Explique-moi comment fonctionne notre système de facturation"
   → Réponse basée sur la doc interne

2. SUPPORT CLIENT
   "Ce client a-t-il déjà eu ce problème ?"
   → Recherche dans l'historique des tickets

3. PRODUCT
   "Quelles features ont été demandées pour le module X ?"
   → Agrégation des feedbacks et tickets

4. SALES
   "Résume l'historique avec ce prospect"
   → Synthèse CRM + emails

5. TECH
   "Pourquoi avons-nous choisi cette architecture ?"
   → Recherche dans les ADRs
```

### Prompt avec contexte

```
Tu es un assistant qui connaît le contexte de [Entreprise].

Tu as accès à :
- Notre documentation produit
- Notre wiki interne
- L'historique des tickets

Quand on te pose une question :
1. Recherche d'abord dans le contexte interne
2. Cite tes sources (document, date)
3. Si tu ne trouves pas, dis-le clairement
4. Propose de créer la doc si elle manque

Question : [QUESTION]
```

### Workflow de mise à jour

```
QUOTIDIEN (automatique)
├── Sync Notion/Confluence
├── Index nouveaux messages Slack
└── Mise à jour tickets

HEBDOMADAIRE (manuel)
├── Review des sources obsolètes
├── Ajout de nouvelles sources
└── Test de qualité des réponses

MENSUEL
├── Audit complet du contexte
├── Nettoyage des données périmées
└── Feedback utilisateurs
```

---

## Animation Dojo (1h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Le problème du contexte |
| 10-25 | Setup | Connecter 2-3 sources |
| 25-45 | Use cases | Tester les 5 use cases |
| 45-55 | Optimisation | Améliorer les réponses |
| 55-60 | Clôture | Maintenance et gouvernance |

### Points d'attention

- Données sensibles : attention aux accès
- Qualité du contexte = qualité des réponses
- Prévoir la gouvernance (qui met à jour quoi)
