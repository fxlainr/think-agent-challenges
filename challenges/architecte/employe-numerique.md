# L'Employé Numérique

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | Tous |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 190 |
| Prérequis | n8n, notions d'API REST |

---

## Vision & Impact

"Dupliquer son soi" en entraînant l'IA pour qu'elle trouve tout dans votre environnement et travaille exactement comme vous. L'IA devient un **prolongement de votre identité professionnelle**.

## Le saviez-vous ?

La plupart des utilisateurs veulent que l'IA sonne comme eux pour maintenir l'authenticité de leur marque personnelle. Un "clone" bien entraîné peut gérer 80% des tâches répétitives à votre place.

## Sources

- [Most people want AI to sound like them - Ruben Hassid](https://www.linkedin.com/posts/ruben-hassid_most-people-want-ai-to-sound-like-them-share-7422150189815279616-7Ood)
- [ChatGPT looks like a toy in 2026 - Ruben Hassid](https://www.linkedin.com/posts/ruben-hassid_chatgpt-looks-like-a-toy-in-2026-i-cant-share-7420324242715672576-U247)

---

## Description

> *Concevez un agent capable de créer, modifier et superviser des workflows n8n à distance — l'automatisation qui s'auto-automatise.*

"Crée-moi un workflow qui envoie un email chaque matin avec la météo." Et l'agent le fait. Ce challenge vous fait construire un employé numérique qui comprend vos besoins en langage naturel et les traduit en automatisations n8n.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Agent capable de créer un workflow par conversation
- [ ] Modification de workflows existants
- [ ] Diagnostic de problèmes d'exécution

**Critères de réussite :**

- L'agent génère du JSON n8n valide
- Les workflows créés fonctionnent
- L'agent peut expliquer ce qu'il a fait

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   DIGITAL EMPLOYEE                       │
│                                                          │
│  ┌─────────────┐                      ┌─────────────┐   │
│  │   Langage   │                      │   n8n       │   │
│  │   naturel   │───▶ Agent IA ───────▶│   API       │   │
│  └─────────────┘                      └─────────────┘   │
│                                                          │
│                   ┌─────────────┐                        │
│                   │  Knowledge  │                        │
│                   │  Base       │                        │
│                   │  (nodes)    │                        │
│                   └─────────────┘                        │
└─────────────────────────────────────────────────────────┘
```

### Capacités de l'agent

| Capacité | API n8n | Exemple |
|----------|---------|---------|
| Créer workflow | POST /workflows | "Crée un workflow email chaque matin" |
| Modifier | PATCH /workflows/{id} | "Ajoute une étape de validation" |
| Activer/Désactiver | POST /workflows/{id}/activate | "Mets en pause le workflow X" |
| Lister | GET /workflows | "Quels workflows sont actifs ?" |
| Voir exécutions | GET /executions | "Le workflow a-t-il fonctionné hier ?" |

### Prompt système de l'agent

```
Tu es un expert n8n capable de créer et modifier des workflows via l'API.

## Tes capacités
1. Créer des workflows à partir de descriptions en langage naturel
2. Modifier des workflows existants
3. Diagnostiquer des problèmes d'exécution
4. Suggérer des améliorations

## Quand tu crées un workflow
1. Identifie le trigger (déclencheur)
2. Liste les étapes de transformation
3. Définis l'action finale
4. Génère le JSON n8n correspondant

## Nodes courants
- Schedule Trigger : Déclenchement périodique
- Webhook : Déclenchement externe
- HTTP Request : Appel API
- OpenAI : Traitement IA
- Slack/Email : Notifications
- IF : Conditions
- Code : Logique custom

## Format workflow
{
  "name": "Nom du workflow",
  "nodes": [...],
  "connections": {...}
}
```

### Exemple de création

**Demande :** "Crée un workflow qui m'envoie un résumé des news tech chaque matin à 8h"

**Réponse de l'agent :**
```json
{
  "name": "Daily Tech News Summary",
  "nodes": [
    {
      "name": "Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "rule": { "interval": [{ "field": "hours", "hour": 8 }] }
      }
    },
    {
      "name": "Fetch News",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://newsapi.org/v2/top-headlines?category=technology"
      }
    },
    {
      "name": "Summarize",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "parameters": {
        "prompt": "Résume ces articles en 5 bullet points..."
      }
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "user@example.com",
        "subject": "Daily Tech News"
      }
    }
  ]
}
```

### Tips & astuces

- Donner des exemples de workflows dans le prompt
- Inclure la doc des nodes les plus utilisés
- Toujours valider le JSON avant d'appeler l'API

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Utiliser l'API n8n programmatiquement
- Construire un agent conversationnel spécialisé
- Générer du JSON valide dynamiquement
- Debugger des workflows à distance

### Prérequis participants

- Instance n8n accessible (cloud ou self-hosted)
- API credentials n8n
- Expérience n8n basique

### Matériel nécessaire

- [ ] Prompt système de l'agent
- [ ] Documentation API n8n
- [ ] Exemples de workflows JSON
- [ ] Liste des nodes courants

### Déroulé (4h)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-30 | Théorie | API n8n + architecture agent | Compréhension |
| 30-90 | Agent basique | Agent qui liste et décrit les workflows | v0.1 fonctionnel |
| 90-150 | Création | Agent qui crée des workflows simples | v0.2 création |
| 150-180 | Modification | Ajout capacité de modification | v0.3 CRUD complet |
| 180-210 | Diagnostic | Ajout analyse des exécutions | v0.4 debug |
| 210-240 | Demo + Q&A | Chacun présente son agent | Démo finale |

### Points d'attention animateur

**Pièges courants :**

- JSON invalide → Valider avant d'envoyer
- Nodes qui n'existent pas → Base de connaissance à jour
- Credentials manquants → Préparer un compte de test

**Questions fréquentes :**

- "Comment gérer les erreurs ?" → Try/catch + messages explicites
- "Comment passer les credentials ?" → Variables d'environnement
- "Peut-on aller plus loin ?" → Orchestration multi-workflows

### Variantes

**Version découverte (2h) :**
- Agent read-only (list + describe)
- Pas de création

**Version avancée (8h) :**
- Multi-workflows orchestrés
- Auto-correction des erreurs
- Interface conversationnelle complète

---

## Ressources complémentaires

- [n8n API Documentation](https://docs.n8n.io/api/)
- [n8n Workflow Examples](https://n8n.io/workflows/)
