# La Triade de Livraison (Agentic Delivery Cycle)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | FLOW |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 330 |
| Prérequis | Linear/Jira, GitHub, Claude Code ou Cursor |

---

## Vision & Impact

Implémenter le cycle de livraison en 3 étapes : 1. Le PM crée la tâche, 2. Un **agent de codage** la complète, 3. L'ingénieur de garde effectue la revue critique. Ce workflow réduit drastiquement le "lead time" tout en maintenant la qualité.

## Le saviez-vous ?

Linear utilise déjà ce type d'aperçu pour automatiser les tâches répétitives des développeurs. Le PM devient le "donneur d'ordre" et l'agent le "premier développeur".

## Sources

- [Linear's Head of Product - Aakash Newsletter](https://www.linkedin.com/posts/aakashnewsletter_linears-head-of-product-just-gave-us-a-glimpse-activity-7423364696998674432-HdGR)

---

## Description

> *Mettez en place un cycle de livraison où l'IA code et l'humain revoit.*

Le PM écrit un ticket. L'agent code. Le dev review. Livré. Ce challenge vous fait construire ce pipeline qui transforme la vélocité de livraison tout en gardant un humain dans la boucle.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline complet : Ticket → Agent → Code → Review
- [ ] 3 tickets traités par ce workflow
- [ ] Métriques : temps gagné, qualité du code généré

**Critères de réussite :**

- Le workflow est reproductible
- La qualité du code est acceptable (< 3 itérations de review)
- Lead time réduit d'au moins 50%

---

## Pistes de Solution

### Architecture de la Triade

```
┌─────────────────────────────────────────────────────────────────┐
│                     AGENTIC DELIVERY CYCLE                      │
├─────────────────┬─────────────────┬─────────────────────────────┤
│    ÉTAPE 1      │    ÉTAPE 2      │         ÉTAPE 3             │
│                 │                 │                             │
│  📝 PM          │  🤖 Agent       │  👨‍💻 Engineer               │
│  Crée le ticket │  Code la        │  Review + Merge             │
│  avec specs     │  solution       │  ou feedback                │
│                 │                 │                             │
│  Linear/Jira    │  Claude Code    │  GitHub PR                  │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

### Format de ticket optimal

```markdown
## [Feature] Ajouter filtres sur la liste des challenges

### Contexte
Les utilisateurs ont du mal à trouver les challenges pertinents.
La liste affiche tous les challenges sans possibilité de filtrer.

### Comportement attendu
- [ ] Dropdown pour filtrer par niveau (Explorer/Crafter/Architecte)
- [ ] Dropdown pour filtrer par marque
- [ ] Les filtres sont combinables (AND)
- [ ] Paramètres persistés dans l'URL

### Critères techniques
- Composant `FilterDropdown` réutilisable
- Hooks `useFilters` pour la logique
- Tests unitaires

### Out of scope
- Recherche full-text
- Filtres sauvegardés

### Maquette
[Lien Figma ou screenshot]

### Definition of Done
- [ ] PR mergée
- [ ] Tests passent
- [ ] Review par 1 dev
```

### Prompt pour l'agent

```
Tu dois implémenter ce ticket :

"""
[COLLER LE TICKET]
"""

Contexte du projet :
- Stack : [React/Next.js/TypeScript/Tailwind]
- Structure des dossiers : [décrire]
- Conventions : [liens ou description]

Processus :
1. Analyse le ticket et pose des questions si ambiguïté
2. Propose un plan d'implémentation
3. Implémente étape par étape
4. Écris les tests
5. Prépare le message de commit

Attends ma validation entre chaque étape majeure.
```

### Workflow automatisé (n8n/Zapier)

```
Trigger : Nouveau ticket avec label "agent-ready"
    ↓
Action 1 : Extraire le contenu du ticket
    ↓
Action 2 : Envoyer à Claude API avec le prompt
    ↓
Action 3 : Créer une branche Git
    ↓
Action 4 : Commiter le code généré
    ↓
Action 5 : Créer une PR
    ↓
Action 6 : Notifier le reviewer de garde
```

### Métriques à tracker

```
## Métriques de vélocité
- Lead time : Ticket créé → PR mergée
- Cycle time : Agent start → PR créée
- Review time : PR créée → PR mergée

## Métriques de qualité
- Nombre d'itérations de review
- Bugs trouvés post-merge
- Code coverage des tests générés

## Comparaison
- Baseline : Temps moyen sans agent
- Avec agent : Temps avec le workflow
- Delta : % de réduction
```

### Les 3 tickets à traiter

**Ticket 1 : UI simple (1h)**
```
Ajouter un composant Badge avec variants
```

**Ticket 2 : Feature avec logique (2h)**
```
Système de filtres avec persistence URL
```

**Ticket 3 : Intégration API (2h)**
```
Fetch et affichage des données depuis Supabase
```

---

## Animation Dojo (2h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Écrire des tickets "agent-ready"
- Piloter un agent de coding
- Reviewer efficacement du code généré

### Prérequis

- Accès à un projet avec repo Git
- Claude Code / Cursor configuré
- Linear/Jira pour les tickets

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | La Triade et ses bénéfices |
| 10-25 | Démo | Cycle complet sur un ticket simple |
| 25-40 | Rédaction | Chacun écrit un ticket agent-ready |
| 40-70 | Coding | L'agent traite les tickets |
| 70-100 | Review | Cross-review en binômes |
| 100-115 | Métriques | Calculer les gains |
| 115-120 | Clôture | Industrialiser le workflow |

### Points d'attention animateur

- La qualité du ticket détermine la qualité du code
- Le reviewer doit être exigeant mais constructif
- Mesurer le temps à chaque étape

---

## Ressources complémentaires

- [Linear](https://linear.app/)
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh/)
