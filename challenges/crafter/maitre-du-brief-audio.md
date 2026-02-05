# Le Maître du Brief (Audio to Text)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 140 |
| Prérequis | Outil de transcription (Whisper, Otter.ai, etc.) |

---

## Vision & Impact

Ne plus prendre de notes manuellement. Utiliser l'IA pour écouter les briefs et transformer la voix en **tickets Linear ou Jira** structurés.

## Le saviez-vous ?

L'IA peut détecter des signaux faibles dans la voix d'un client lors d'un entretien de découverte — hésitations, enthousiasme, doutes non-dits.

## Sources

- [Linear's Head of Product - Aakash Newsletter](https://www.linkedin.com/posts/aakashnewsletter_linears-head-of-product-just-gave-us-a-glimpse-activity-7423364696998674432-HdGR)

---

## Description

> *Transformez vos réunions et briefs audio en tickets structurés automatiquement.*

Sortir de réunion avec 3 pages de notes illisibles, puis passer 30 min à les transformer en tickets... C'est fini. Ce challenge vous fait créer un pipeline audio → texte → tickets structurés.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline fonctionnel : audio → transcription → tickets
- [ ] Template de ticket adapté (Linear/Jira/Notion)
- [ ] Démonstration sur un brief réel (ou simulé)

**Critères de réussite :**

- Les tickets générés sont exploitables en l'état
- Les priorités sont identifiées automatiquement
- Les questions ouvertes sont flaggées

---

## Pistes de Solution

### Architecture du pipeline

```
┌──────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────────────┐
│ Réunion/Brief│───▶│ Transcription│───▶│ Structuration│───▶│ Tickets      │
│ (Audio)      │    │ (Whisper)    │    │ (LLM)        │    │ (Linear/Jira)│
└──────────────┘    └─────────────┘    └─────────────┘    └──────────────┘
```

### Options de transcription

- **Whisper (OpenAI)** : Local ou API, excellent en français
- **Otter.ai** : Cloud, bonne UX mais anglais principalement
- **Grain** : Spécialisé meetings, intégration Zoom/Meet
- **Mac Dictation** : Gratuit, qualité correcte

### Prompt de structuration

```
Voici la transcription d'un brief client/interne :

"""
[TRANSCRIPTION]
"""

Analyse et génère :

## Contexte
Résumé en 2-3 phrases de l'objet de la réunion

## Tickets à créer
Pour chaque besoin identifié, génère un ticket :
- Titre : [Action verb] + [Object]
- Description : Contexte et détails
- Critères d'acceptance : Liste de bullets
- Priorité : P0/P1/P2/P3 (basée sur l'urgence perçue)
- Verbatim clé : Citation exacte du stakeholder

## Questions ouvertes
Points à clarifier avant de commencer

## Décisions prises
Ce qui a été acté pendant la réunion

## Prochaines étapes
Actions concrètes avec owners si mentionnés
```

### Template de ticket

```markdown
## [TITRE]

### Contexte
[Pourquoi ce ticket existe - lien avec le brief]

### Description
[Ce qui doit être fait]

### Critères d'acceptance
- [ ] Critère 1
- [ ] Critère 2
- [ ] Critère 3

### Verbatim client
> "[Citation exacte du brief]"

### Questions ouvertes
- Question 1 ?
- Question 2 ?

---
Priorité: P[X] | Source: Brief du [DATE]
```

### Workflow n8n (optionnel)

1. **Webhook** : Reçoit le fichier audio
2. **Whisper API** : Transcrit
3. **OpenAI** : Structure en tickets
4. **Linear/Jira API** : Crée les tickets
5. **Slack** : Notifie l'équipe

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Transcrire efficacement un brief audio
- Structurer une transcription en tickets actionnables
- Identifier les signaux faibles dans un brief

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-5 | Intro | Le coût caché de la prise de notes |
| 5-10 | Démo | Pipeline complet sur un brief de 5 min |
| 10-20 | Setup | Chacun configure son outil de transcription |
| 20-35 | Pratique | Traitement d'un brief audio fourni |
| 35-45 | Revue | Comparer les tickets générés |
| 45-55 | Optimisation | Affiner les prompts |
| 55-60 | Clôture | Intégration dans le workflow quotidien |

### Points d'attention animateur

- Avoir des fichiers audio de démo prêts
- Prévoir des alternatives si problèmes de connexion API
- Insister sur la vérification humaine des tickets

---

## Ressources complémentaires

- [Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [Grain - Meeting Recorder](https://grain.com/)
