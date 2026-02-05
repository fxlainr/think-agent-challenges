# Entretien → Parcours

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Notions UX (user journey, user story) |

---

## Description

> *Transformez automatiquement vos entretiens utilisateurs en parcours utilisateur et user stories actionnables.*

Vous avez fait 10 entretiens utilisateurs. Maintenant il faut les analyser, extraire les insights, créer les parcours, rédiger les stories... Cet assistant fait le travail en quelques minutes : il lit le verbatim et génère un parcours émotionnel + les user stories associées.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Parcours utilisateur complet à partir d'un verbatim
- [ ] 5+ user stories extraites avec critères d'acceptation
- [ ] Identification des pain points et opportunités

**Critères de réussite :**

- Le parcours reflète fidèlement le verbatim
- Les émotions sont correctement identifiées
- Les stories sont actionnables (format INVEST)

---

## Pistes de Solution

### Prompt système suggéré

```
Tu es un UX Researcher senior. Tu transformes des verbatims bruts en livrables actionnables.

## Ton processus

### 1. Identifier le persona
- Qui parle ? Rôle/contexte ?
- Quels objectifs ?

### 2. Extraire les étapes
Découper chronologiquement :
- Trigger (déclencheur)
- Actions successives
- Résultat

### 3. Mapper les émotions
Pour chaque étape : 😊 Positive / 😐 Neutre / 😞 Négative

### 4. Identifier les opportunités
- Pain points → Problèmes à résoudre
- Moments positifs → À amplifier

### 5. Générer les User Stories
Format : "En tant que [persona], je veux [action] afin de [bénéfice]"

## Format de sortie

# Analyse - [Persona]

## Parcours utilisateur

| Phase | Action | Émotion | Verbatim | Opportunité |
|-------|--------|---------|----------|-------------|

## Pain points
1. **[Pain point]** : [Description]

## User Stories

### Story 1 : [Titre]
**En tant que** [persona]
**Je veux** [action]
**Afin de** [bénéfice]

**Critères d'acceptation :**
- [ ] Critère 1
- [ ] Critère 2

Commence par : "Colle-moi le verbatim de l'entretien."
```

### Exemple de transformation

**Verbatim :**
```
"Quand j'ai voulu commander, j'ai cherché sur Google. J'ai trouvé 
le site mais la navigation c'était pas clair, j'ai mis 10 minutes 
à trouver le produit. Le prix était bien mais les frais de livraison,
là j'ai hésité. J'ai commandé parce que j'en avais besoin, mais 
créer un compte c'est trop long. Le mail de confirmation était clair,
ça m'a rassuré."
```

**Parcours généré :**

| Phase | Action | Émotion | Verbatim | Opportunité |
|-------|--------|---------|----------|-------------|
| Recherche | Google | 😐 | "cherché sur Google" | - |
| Navigation | Explore le site | 😞 | "pas clair, 10 min" | 🔴 Pain point |
| Prix | Évalue | 😊 | "prix était bien" | ✅ Point fort |
| Livraison | Découvre frais | 😞 | "j'ai hésité" | 🔴 Pain point |
| Compte | Inscription | 😞 | "trop long" | 🔴 Pain point |
| Confirmation | Reçoit email | 😊 | "clair, rassuré" | ✅ Point fort |

**User Stories :**

```markdown
### Story 1 : Navigation simplifiée
**En tant que** nouveau visiteur
**Je veux** trouver mon produit en moins de 2 clics
**Afin de** ne pas perdre de temps

**Critères :**
- [ ] Barre de recherche visible
- [ ] Résultats pertinents

### Story 2 : Achat sans compte
**En tant que** acheteur pressé
**Je veux** commander en mode invité
**Afin de** ne pas créer de compte
```

### Tips & astuces

- Garder les verbatims exacts (entre guillemets)
- Un pain point = une story potentielle
- Valider les stories avec les critères INVEST

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Analyser un verbatim d'entretien utilisateur
- Créer un parcours utilisateur avec courbe émotionnelle
- Extraire des user stories actionnables
- Identifier pain points et opportunités

### Prérequis participants

- Notions de UX (parcours, personas)
- Un verbatim d'entretien (ou utiliser l'exemple)
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Verbatim exemple
- [ ] Template de parcours utilisateur
- [ ] Checklist INVEST pour les stories

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Montre un parcours utilisateur bien fait | Comprennent le livrable cible | Cadrage |
| 10-15 | Distribution | Distribue le verbatim exemple ou personnel | Préparent leur input | Setup |
| 15-35 | Transformation | Circule, aide à affiner | Génèrent parcours + stories | Production |
| 35-50 | Review | Fait vérifier les stories (INVEST) | Évaluent la qualité | Qualité |
| 50-60 | Partage | 2-3 présentations | Découvrent d'autres approches | Apprentissage |

### Points d'attention animateur

**Pièges courants :**

- Inventer des émotions non exprimées → S'en tenir au verbatim
- Stories trop vagues → Critères d'acceptation testables
- Oublier les moments positifs → Pas que les pain points

**Questions fréquentes :**

- "Mon entretien est trop long" → Découper en parcours distincts
- "Pas d'émotion exprimée" → Inférer prudemment, marquer comme hypothèse
- "Une story par pain point ?" → Pas forcément, regrouper si lié

### Variantes

**Version simple (45 min) :**
- Verbatim court fourni
- Focus sur le parcours (pas les stories)

**Version avancée (2h) :**
- Multi-entretiens → synthèse
- Création de personas
- Priorisation des stories

---

## Ressources complémentaires

- [User Story Mapping (Jeff Patton)](https://www.jpattonassociates.com/user-story-mapping/)
- [Jobs to Be Done framework](https://jtbd.info/)
