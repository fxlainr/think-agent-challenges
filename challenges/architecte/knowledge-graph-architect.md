# Knowledge Graph Architect

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Maîtrise d'un outil de notes (Obsidian, Notion...) |

---

## Description

> *Construisez un système de gestion des connaissances augmenté par l'IA qui organise, lie et fait émerger automatiquement les connexions entre vos idées.*

Vos notes s'accumulent mais restent isolées. Les bonnes idées se perdent. Les connexions entre projets, personnes et concepts restent dans votre tête. Ce challenge vous fait construire un "second cerveau" intelligent : un vault Obsidian augmenté par l'IA qui auto-tag, suggère des liens et fait émerger les patterns cachés dans vos connaissances.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un vault Obsidian structuré avec conventions de nommage et organisation
- [ ] Un workflow IA (n8n ou script) pour auto-tagging et suggestion de liens
- [ ] Une démo de recherche sémantique fonctionnelle

**Critères de réussite :**

- Structure de vault claire et maintenable (PARA ou équivalent)
- Nouvelles notes automatiquement analysées et enrichies
- Capacité à retrouver une information par sens (pas juste mots-clés)

---

## Pistes de Solution

### Architecture du système

```
┌─────────────────────────────────────────────────────────┐
│                    OBSIDIAN VAULT                        │
├─────────────────────────────────────────────────────────┤
│  Notes                                                   │
│  • Dailies (journal)                                     │
│  • Projects (projets actifs)                             │
│  • Areas (domaines de responsabilité)                    │
│  • Resources (références, docs)                          │
│  • Archives                                              │
├─────────────────────────────────────────────────────────┤
│  Metadata                                                │
│  • Tags (#concept, #action, #person)                     │
│  • Properties (YAML frontmatter)                         │
│  • Links ([[note]])                                      │
└─────────────────────────────────────────────────────────┘
         │                     │
         ▼                     ▼
┌─────────────────┐   ┌─────────────────┐
│  Smart Search   │   │  AI Augmentation │
│  (local)        │   │  (n8n + LLM)     │
│                 │   │                  │
│  • Full-text    │   │  • Auto-tagging  │
│  • Backlinks    │   │  • Link suggest  │
│  • Graph view   │   │  • Summarize     │
└─────────────────┘   └─────────────────┘
```

### Structure de vault recommandée (PARA)

```
📁 Vault
├── 00 - Inbox/          # Capture rapide
├── 01 - Daily/          # Notes quotidiennes
├── 10 - Projects/       # Projets actifs
├── 20 - Areas/          # Domaines (santé, finance, travail...)
├── 30 - Resources/      # Références, docs, livres
├── 40 - Archives/       # Projets terminés
├── Templates/           # Templates de notes
└── Attachments/         # Images, fichiers
```

### Plugins Obsidian recommandés

| Plugin | Fonction |
|--------|----------|
| **Smart Connections** | Recherche sémantique IA |
| **Dataview** | Requêtes sur les notes |
| **Templater** | Templates automatisés |
| **Graph Analysis** | Analyse du graphe |
| **Excalidraw** | Diagrammes intégrés |

### Workflow d'augmentation IA (n8n)

```json
{
  "trigger": "Nouvelle note créée",
  "actions": [
    {
      "name": "Analyser contenu",
      "type": "OpenAI",
      "prompt": "Analyse cette note et suggère : 5 tags pertinents, 3 notes existantes à lier, 1 résumé en 2 phrases"
    },
    {
      "name": "Mettre à jour frontmatter",
      "type": "File Update",
      "action": "Ajouter tags et liens suggérés"
    }
  ]
}
```

### Prompt pour auto-linking

```
Voici une nouvelle note :
---
[Contenu de la note]
---

Et voici la liste des notes existantes dans le vault :
[Liste des titres]

Suggère :
1. Les 3-5 notes les plus pertinentes à lier (format [[Note]])
2. Les tags à ajouter (#tag)
3. Un résumé de la note (2 phrases)
4. Une question que cette note soulève (pour exploration future)
```

### Tips & astuces

- Commencer petit : importer 20-30 notes existantes avant d'automatiser
- Tester le workflow IA manuellement avant de l'automatiser
- Prévoir une revue hebdomadaire pour valider les suggestions IA

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Structurer un vault de notes selon la méthode PARA
- Configurer les plugins essentiels d'Obsidian
- Créer un workflow d'augmentation IA pour leurs notes
- Migrer leurs notes existantes dans le nouveau système

### Prérequis participants

- Obsidian installé
- Compte OpenAI ou accès à un LLM
- Optionnel : n8n ou Make pour l'automatisation
- Quelques notes existantes à migrer

### Matériel nécessaire

- [ ] Guide d'installation des plugins
- [ ] Templates de notes prêts à l'emploi
- [ ] Workflow n8n à importer
- [ ] Exemples de vaults bien structurés

### Déroulé (4h workshop)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-60 | Théorie | PKM, graphes de connaissances, méthode PARA | Compréhension du modèle |
| 60-120 | Setup vault | Installation plugins, création structure, templates | Vault configuré |
| 120-180 | Workflow IA | Configuration n8n/script, test auto-tagging | Workflow fonctionnel |
| 180-240 | Migration | Import notes existantes, test end-to-end | Système opérationnel |

### Points d'attention animateur

**Pièges courants :**

- Sur-structurer au départ → Commencer simple, affiner après
- Trop de plugins → Se limiter aux 5 essentiels au début
- Automatiser trop tôt → Valider le workflow manuellement d'abord

**Questions fréquentes :**

- "Obsidian ou Notion ?" → Obsidian pour le contrôle local, Notion pour la collaboration
- "Ça prend combien de temps à maintenir ?" → 5-10 min/jour une fois le système en place
- "Et si l'IA se trompe sur les tags ?" → C'est des suggestions, vous validez toujours

**Tips d'animation :**

- Montrer votre propre vault comme exemple
- Faire des pauses régulières (workshop long)
- Prévoir du support technique pour l'installation

### Variantes

**Version découverte (2h) :**
- Focus sur la structure et les plugins
- Pas d'automatisation IA
- Objectif : vault fonctionnel de base

**Version avancée (journée) :**
- Ajout de workflows avancés (résumé automatique de meetings, extraction de tâches)
- Intégration avec calendrier et emails
- Construction d'un dashboard personnel

---

## Ressources complémentaires

- [Documentation Obsidian](https://help.obsidian.md/)
- [Méthode PARA de Tiago Forte](https://fortelabs.com/blog/para/)
- [Smart Connections plugin](https://github.com/brianpetro/obsidian-smart-connections)
