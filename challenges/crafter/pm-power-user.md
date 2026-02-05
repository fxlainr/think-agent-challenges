# Le PM Power User (Claude Code Commands)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐ |
| XP | 250 |
| Prérequis | Claude Code ou Cursor |

---

## Vision & Impact

Maîtriser les commandes spécifiques de Claude Code pour décupler sa productivité par 10. Le PM devient un **"navigateur d'incertitude"** capable de diriger la technique par l'intention.

## Le saviez-vous ?

L'IA permet d'écraser les étapes d'infrastructure pour prototyper et tester plus vite. Un PM qui maîtrise Claude Code peut valider une hypothèse en heures au lieu de semaines.

## Sources

- [I built 3 Claude Code commands to 10x productivity - Nuri Janian](https://open.substack.com/pub/nurijanian/p/i-built-3-claude-code-commands-to)
- [What really defines Product Managers - Aleksander Uznanski](https://www.linkedin.com/posts/aleksanderuznanski_ever-wonder-what-really-defines-product-managers-activity-7421879195867381760-CD1W)

---

## Description

> *Devenez un PM qui code (enfin, qui fait coder) à la vitesse de la pensée.*

"Je ne suis pas technique." Cette excuse ne tient plus. Ce challenge vous fait maîtriser les commandes et patterns Claude Code pour qu'un PM puisse prototyper, tester et itérer sans attendre les devs.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 5 commandes personnalisées dans Claude Code
- [ ] 1 prototype fonctionnel créé de A à Z
- [ ] Documentation de son workflow PM

**Critères de réussite :**

- Prototype créé en < 2h
- Commandes réutilisables
- Autonomie sur les itérations simples

---

## Pistes de Solution

### Commandes essentielles

```bash
# Commande 1 : Scaffold un projet
/project-init [type] [name]
"Crée la structure de base pour un projet [Next.js/React/etc]"

# Commande 2 : Implémenter une feature
/feature [description]
"Implémente cette feature en suivant les conventions du projet"

# Commande 3 : Debug
/debug [error]
"Analyse cette erreur et propose une solution"

# Commande 4 : Refactor
/refactor [file] [instruction]
"Améliore ce code selon l'instruction"

# Commande 5 : Test
/test [component]
"Génère les tests pour ce composant"
```

### Workflow PM type

```
1. IDÉE → /project-init pour scaffolder
2. MAQUETTE → Décrire l'UI voulue en mots
3. FEATURE → /feature pour chaque fonctionnalité
4. BUG → /debug quand ça casse
5. ITÉRATION → Décrire les changements voulus
6. LIVRAISON → git commit et deploy
```

### Prompt système PM

```
Tu m'aides en tant que PM à construire des prototypes.

Mon niveau technique : [débutant/intermédiaire]
Stack préférée : [Next.js + Tailwind + Supabase]

Quand je te demande quelque chose :
1. Explique brièvement ce que tu vas faire
2. Fais-le étape par étape
3. Dis-moi si tu as besoin de décisions produit
4. Préviens-moi des risques techniques

Je veux comprendre, pas juste copier-coller.
```

### Les 5 commandes à créer

**1. /prd-to-code**
```
Transforme ce PRD en structure de code :
- Composants nécessaires
- Modèle de données
- Routes API
```

**2. /user-story**
```
Implémente cette user story :
"En tant que [X], je veux [Y] pour [Z]"
```

**3. /quick-ui**
```
Génère rapidement cette interface :
[description]
```

**4. /connect-api**
```
Connecte ce composant à cette API :
[endpoint] [données attendues]
```

**5. /ship-it**
```
Prépare pour déploiement :
- Vérifie les erreurs
- Optimise
- Génère le commit message
```

---

## Animation Dojo (1h30)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | PM + Code = Superpouvoir |
| 15-30 | Setup | Configuration Claude Code |
| 30-50 | Commandes | Créer ses 5 commandes |
| 50-80 | Prototype | Construire un mini-produit |
| 80-90 | Clôture | Workflow et bonnes pratiques |

### Points d'attention

- Rassurer les non-techniques
- Commencer très simple
- L'objectif n'est pas de devenir dev, mais autonome
