# Le Superviseur de Code (Direction Value)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | VALUE |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 350 |
| Prérequis | Expérience développement, Claude Code ou Cursor |

---

## Vision & Impact

Passer d'une production manuelle à une **supervision d'agents** de codage. L'objectif est de piloter le développement logiciel comme un système orchestré plutôt que de simplement "écrire des lignes", garantissant une vélocité industrielle.

## Le saviez-vous ?

Chez Anthropic, on ne produit plus de code, on le supervise. C'est une urgence de réapprendre à **décider** plutôt que d'exécuter.

## Sources

- [AI Software Engineering - Souleymane Yattara](https://www.linkedin.com/posts/souleymane-yattara-6b565861_ai-softwareengineering-developers-activity-7420736553343307776--WHp)
- [Le développement logiciel sera automatisable - Renald Vie](https://www.linkedin.com/posts/renaldvie_le-d%C3%A9veloppement-logiciel-sera-automatisable-activity-7419656454921519105-QLfp)

---

## Description

> *Devenez un superviseur d'agents de codage plutôt qu'un développeur.*

Taper du code ligne par ligne, c'est fini. Ce challenge vous fait passer du rôle de développeur à celui de superviseur : vous définissez l'intention, l'agent code, vous validez et itérez.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Workflow de supervision documenté
- [ ] 3 features développées en mode supervision
- [ ] Métriques de productivité avant/après

**Critères de réussite :**

- Code généré de qualité (review passé)
- Temps de développement réduit de 60%
- Le développeur reste en contrôle

---

## Pistes de Solution

### Le nouveau rôle du développeur

```
AVANT (Développeur)
├── Écrire le code
├── Debugger
├── Tester
└── Documenter

APRÈS (Superviseur)
├── Définir l'intention clairement
├── Piloter l'agent
├── Valider la qualité
├── Intégrer dans le système
└── Gérer les cas limites
```

### Workflow de supervision

```
1. INTENTION
   "Je veux une API REST pour gérer les utilisateurs"

2. SPEC
   - Endpoints : GET/POST/PUT/DELETE /users
   - Validation : email, password min 8 chars
   - Auth : JWT

3. DÉLÉGATION
   "Implémente cette API en suivant nos conventions"

4. REVIEW
   - Le code respecte-t-il la spec ?
   - Tests présents et passants ?
   - Conventions respectées ?

5. ITÉRATION
   "Ajoute la pagination sur GET /users"

6. INTÉGRATION
   Merge + Deploy
```

### Prompt de supervision efficace

```
Tu es mon agent de développement. Je supervise, tu codes.

Contexte projet :
- Stack : [X]
- Conventions : [lien ou description]
- Structure : [arborescence]

Ta mission :
[DESCRIPTION FEATURE]

Processus :
1. Propose un plan d'implémentation
2. Attends ma validation
3. Implémente étape par étape
4. Montre-moi le code pour review
5. Corrige selon mes retours

Règles :
- Pas de raccourcis sur les tests
- Documente les choix techniques
- Signale les ambiguïtés
```

### Les 3 features à superviser

**Feature 1 : CRUD simple (1h)**
```
API de gestion de ressources
- Modèle de données
- Endpoints REST
- Validation
- Tests
```

**Feature 2 : Intégration externe (1.5h)**
```
Connexion à une API tierce
- Auth
- Fetch et transformation
- Gestion d'erreurs
- Cache
```

**Feature 3 : Feature complexe (2h)**
```
Système avec logique métier
- Plusieurs composants
- États et transitions
- Edge cases
- Tests d'intégration
```

### Checklist du superviseur

```markdown
## Avant de valider

### Qualité du code
- [ ] Lisible et maintenable
- [ ] Conventions respectées
- [ ] Pas de code mort

### Tests
- [ ] Tests unitaires présents
- [ ] Cas nominaux couverts
- [ ] Edge cases testés

### Sécurité
- [ ] Inputs validés
- [ ] Pas de données sensibles exposées
- [ ] Auth/authz correcte

### Performance
- [ ] Pas de N+1 queries
- [ ] Complexité raisonnable
- [ ] Pagination si liste
```

---

## Animation Dojo (2h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Du développeur au superviseur |
| 15-30 | Démo | Supervision d'une feature en live |
| 30-60 | Feature 1 | CRUD supervisé |
| 60-90 | Feature 2 | Intégration supervisée |
| 90-110 | Revue | Comparaison et apprentissages |
| 110-120 | Clôture | Le futur du développement |

### Points d'attention

- Le superviseur doit comprendre le code
- La qualité de l'intention = qualité du résultat
- Toujours review avant merge
