# Le Product System

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | FLOW |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 400 |
| Prérequis | Product Management, notions d'agents IA |

---

## Vision & Impact

Bâtir un Design System qui se maintient de lui-même en synchronisant le front et les outils de design. C'est la clé pour garantir une **qualité artisanale à l'échelle** sans effort manuel.

## Le saviez-vous ?

Le rôle de **Design Engineer** est la nouvelle étiquette pour ceux qui fusionnent code et design via l'IA. C'est le profil le plus recherché dans les startups produit en 2026.

## Sources

- [I built a Design System that updates itself](https://www.linkedin.com/posts/edwche_i-built-a-design-system-that-updates-itself-activity-7423990160117100544-tucg)
- [Le rôle de Design Engineer - Noé Chagué](https://www.linkedin.com/posts/noechague_le-r%C3%B4le-de-design-engineer-a-longtemps-%C3%A9t%C3%A9-activity-7419283828231380992--UVX)

---

## Description

> *Concevez un système autonome de Product Discovery : orchestration d'agents pour mener des interviews, synthétiser les insights et alimenter un backlog priorisé.*

Le Product Discovery prend des semaines ? Ce challenge vous fait construire un système multi-agents qui analyse les interviews, extrait les insights et génère un backlog priorisé automatiquement.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Système multi-agents fonctionnel
- [ ] Backlog généré automatiquement
- [ ] Dashboard de priorisation

**Critères de réussite :**

- Les agents ont des rôles distincts et complémentaires
- Les insights sont tracés jusqu'aux verbatims
- La priorisation est automatique (RICE ou WSJF)

---

## Pistes de Solution

### Architecture multi-agents

```
┌─────────────────────────────────────────────────────────┐
│                   PRODUCT SYSTEM                         │
├─────────────┬─────────────┬─────────────┬───────────────┤
│  Agent      │   Agent     │   Agent     │   Agent       │
│  Researcher │   Analyst   │   PM        │   Prioritizer │
│             │             │             │               │
│  • Mène les │  • Synthèse │  • Backlog  │  • Score      │
│    interviews│    insights │    stories  │    RICE/WSJF  │
│  • Capture  │  • Patterns │  • Specs    │  • Ranking    │
│    verbatims │  • Personas │             │               │
└─────────────┴─────────────┴─────────────┴───────────────┘
         │             │             │             │
         ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                   KNOWLEDGE BASE                         │
│  • Interviews • Insights • Backlog • Decisions          │
└─────────────────────────────────────────────────────────┘
```

### Agents et leurs rôles

| Agent | Inputs | Outputs |
|-------|--------|---------|
| Researcher | Transcripts | Synthèses structurées |
| Analyst | Synthèses | Themes, Insights, Opportunities |
| PM | Insights | User Stories, Specs |
| Prioritizer | Stories | Backlog priorisé RICE |

### Workflow orchestré

```
1. INPUT: Transcript d'interview
   ↓
2. RESEARCHER: Synthèse + verbatims clés
   ↓
3. ANALYST: Patterns (si N synthèses)
   ↓
4. PM: Génération user stories
   ↓
5. PRIORITIZER: Scoring RICE
   ↓
6. OUTPUT: Backlog dans Notion/JIRA
```

### Scoring RICE

```
RICE = (Reach × Impact × Confidence) / Effort
```

| Facteur | Valeur | Description |
|---------|--------|-------------|
| Reach | 1-10000 | Nb utilisateurs impactés |
| Impact | 0.25-3 | Niveau d'impact (massive=3) |
| Confidence | 0-100% | Certitude sur les estimations |
| Effort | 0.5-10 | Personnes-mois |

### Dashboard de priorisation

```markdown
| Story | Reach | Impact | Confidence | Effort | RICE |
|-------|-------|--------|------------|--------|------|
| [Story 1] | 1000 | 3 | 80% | 2 | 1200 |
| [Story 2] | 500 | 2 | 90% | 1 | 900 |
| [Story 3] | 2000 | 1 | 70% | 3 | 467 |
```

### Prompts des agents

**Researcher :**
```
Analyse ce transcript d'interview.
Extrais : problèmes mentionnés, besoins exprimés, 
verbatims clés (citations exactes), contexte utilisateur.
```

**Analyst :**
```
Compare ces synthèses d'interviews.
Identifie : patterns récurrents, insights clés, 
opportunités produit, segments utilisateurs.
```

**PM :**
```
Transforme ces insights en user stories.
Format : En tant que [persona], je veux [action] 
afin de [bénéfice]. Critères d'acceptation.
```

**Prioritizer :**
```
Score ces stories en RICE.
Estime : Reach, Impact, Confidence, Effort.
Justifie chaque estimation.
```

### Tips & astuces

- Tracer les insights jusqu'aux verbatims
- Revalider les scores RICE périodiquement
- Automatiser l'export vers l'outil de gestion

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Concevoir une architecture multi-agents
- Orchestrer un workflow de Product Discovery
- Automatiser la priorisation de backlog
- Connecter des agents à des outils de gestion

### Prérequis participants

- Expérience Product Management
- Notions d'agents IA
- Transcripts d'interviews (ou fournis)

### Matériel nécessaire

- [ ] Prompts des 4 agents
- [ ] Transcripts d'interviews (3-5)
- [ ] Template RICE
- [ ] Accès Notion ou Airtable

### Déroulé (4h)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-45 | Théorie | Product Discovery + architecture | Compréhension |
| 45-90 | Setup agents | Configuration des 4 agents | Agents prêts |
| 90-150 | Workflow | Connexion et orchestration | Pipeline fonctionnel |
| 150-180 | Test | Run sur données réelles | Backlog généré |
| 180-210 | Dashboard | Mise en place priorisation | Vue RICE |
| 210-240 | Présentation | Démo du système | Partage |

### Points d'attention animateur

**Pièges courants :**

- Agents trop génériques → Spécialiser les rôles
- Pas de traçabilité → Lier insights aux sources
- Scores RICE fantaisistes → Calibrer sur des exemples

**Questions fréquentes :**

- "Comment valider les insights ?" → Croiser plusieurs interviews
- "RICE ou WSJF ?" → RICE plus simple, WSJF pour l'agile
- "Ça remplace un PM ?" → Non, ça l'assiste

### Variantes

**Version simple (2h) :**
- 2 agents seulement (Researcher + PM)
- Pas de priorisation automatique

**Version avancée (1 jour) :**
- Intégration JIRA/Linear
- Alertes sur nouveaux insights
- Dashboard en temps réel

---

## Ressources complémentaires

- [RICE Scoring](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)
- [Continuous Discovery](https://www.producttalk.org/)
