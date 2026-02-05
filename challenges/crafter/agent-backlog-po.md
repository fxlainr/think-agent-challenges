# Agent Backlog PO

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Notions de méthodologie Agile |

---

## Description

> *Créez un assistant qui transforme vos specs, emails et comptes-rendus en tickets de backlog actionnables en quelques minutes.*

Entre les specs qui traînent, les emails de demandes et les CR de réunions, les besoins se perdent. Ce challenge vous fait créer un assistant Product Owner qui analyse n'importe quel document et génère des User Stories conformes aux critères INVEST, prêtes à être importées dans JIRA ou Linear.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un assistant fonctionnel qui analyse des documents variés
- [ ] 10 User Stories générées à partir d'un document réel
- [ ] Tickets conformes aux critères INVEST

**Critères de réussite :**

- L'assistant distingue User Story, tâche technique et bug
- Les critères d'acceptation sont testables
- Le format est exploitable (Markdown, JSON pour import)

---

## Pistes de Solution

### Approche recommandée

Un assistant qui :
1. Demande le document source (spec, email, CR)
2. Identifie chaque besoin distinct
3. Transforme en tickets avec le bon format
4. Vérifie la conformité INVEST

### Prompt système suggéré

```
Tu es un Product Owner expert avec 8 ans d'expérience en méthodologies agiles. Tu excelles dans la rédaction de User Stories claires, estimables et testables.

## Ta mission
Analyser des documents sources (specs, emails, comptes-rendus de réunion) et les transformer en tickets de backlog actionnables.

## Formats de tickets que tu génères :

### User Story (feature utilisateur)
**Titre** : [Action] [Objet] [Bénéfice court]

**En tant que** [persona/rôle]
**Je veux** [action/fonctionnalité]
**Afin de** [bénéfice/valeur]

**Critères d'acceptation :**
- [ ] Critère 1 (vérifiable)
- [ ] Critère 2 (vérifiable)
- [ ] Critère 3 (vérifiable)

**Notes techniques :**
[Contraintes, dépendances, questions pour l'équipe]

**Estimation** : [XS/S/M/L/XL] (à confirmer par l'équipe)
**Priorité** : [P0/P1/P2]
**Labels** : [epic, module, type]

### Tâche technique (non visible utilisateur)
**Titre** : [TECH] [Action] [Composant]

**Objectif :**
[Ce qu'on cherche à accomplir techniquement]

**Definition of Done :**
- [ ] Condition 1
- [ ] Condition 2
- [ ] Tests passent

### Bug
**Titre** : [BUG] [Comportement observé] - [Contexte]

**Comportement observé / attendu / étapes de reproduction**
**Sévérité** : [Bloquant/Majeur/Mineur]

---

## Qualité INVEST
Vérifie que chaque User Story est :
- **I**ndépendante : peut être développée seule
- **N**égociable : pas trop détaillée, permet la discussion
- **V**aluable : apporte de la valeur à l'utilisateur
- **E**stimable : l'équipe peut estimer l'effort
- **S**mall : réalisable en un sprint
- **T**estable : on peut vérifier qu'elle est terminée

## Ton style
- Tu demandes le document source avant de commencer
- Tu poses des questions si quelque chose est ambigu
- Tu proposes des regroupements (epics) si pertinent
- Tu signales les trous ou incohérences dans le document

Commence par : "Salut ! Envoie-moi le document à transformer (spec, email, CR...) et précise le contexte projet si besoin."
```

### Exemple de transformation

**Document source (email) :**
```
De: Marie (Marketing)
À: Jean (PM)
Objet: Demandes pour la page produit

Suite à notre réunion, voici les retours du marketing :
- On voudrait pouvoir mettre des vidéos sur les fiches produit
- Le bouton "Ajouter au panier" est trop petit sur mobile
- Il faudrait afficher les avis clients directement sur la fiche
- On aimerait programmer les mises en avant à l'avance
```

**Tickets générés :**

```markdown
## Story 1 : Support vidéo fiches produit

**En tant que** client e-commerce
**Je veux** voir des vidéos sur les fiches produit
**Afin de** mieux visualiser le produit avant achat

**Critères d'acceptation :**
- [ ] Upload vidéo possible depuis le back-office (MP4, max 100MB)
- [ ] Lecture intégrée sur la fiche (pas de redirection YouTube)
- [ ] Player avec contrôles (play/pause, volume, plein écran)
- [ ] Affichage correct sur mobile et desktop

**Estimation** : L | **Priorité** : P1

---

## Story 2 : Améliorer CTA mobile

**En tant que** client sur mobile
**Je veux** un bouton d'ajout au panier facilement cliquable
**Afin de** pouvoir ajouter des produits sans erreur de clic

**Critères d'acceptation :**
- [ ] Bouton de taille minimum 44x44px
- [ ] Bouton sticky en bas d'écran sur mobile
- [ ] Contraste suffisant (ratio 4.5:1 minimum)

**Estimation** : S | **Priorité** : P0 (plaintes clients)
```

### Tips & astuces

- Si l'info manque, l'assistant doit poser des questions (pas inventer)
- Un besoin = un ticket (atomicité)
- Les critères d'acceptation doivent être "cochables" oui/non

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Rédiger des User Stories conformes aux critères INVEST
- Transformer un document informel en tickets actionnables
- Distinguer User Story, tâche technique et bug
- Définir des critères d'acceptation testables

### Prérequis participants

- Avoir un document à transformer (email, spec, CR)
- Accès à un chat IA
- Notion de ce qu'est une User Story (intro en 5 min si besoin)

### Matériel nécessaire

- [ ] Prompt système
- [ ] Checklist INVEST imprimée
- [ ] Exemple de transformation (avant/après)
- [ ] 2-3 documents fictifs pour ceux qui n'ont rien

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro INVEST | Présente les critères INVEST avec exemples | Découvrent les bonnes pratiques | Théorie |
| 5-10 | Démo | Transforme un email en 2 stories en live | Observent le processus | Voir le résultat |
| 10-15 | Setup | Distribue le prompt, vérifie les documents | Préparent leur document source | Préparation |
| 15-35 | Génération | Circule, aide sur les cas ambigus | Génèrent leurs tickets | Production |
| 35-45 | Review INVEST | Fait vérifier les tickets avec la checklist | Évaluent leurs stories vs INVEST | Qualité |
| 45-55 | Partage | Fait présenter 2-3 transformations | Écoutent, commentent | Apprentissage pairs |
| 55-60 | Clôture | Tips pour intégrer dans leur workflow | Notent les next steps | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Stories trop grosses → Faire découper (split)
- Critères d'acceptation vagues → "Testable = quelqu'un peut cocher oui/non"
- Mélange story/tâche technique → Clarifier la distinction

**Questions fréquentes :**

- "Story ou tâche technique ?" → Si l'utilisateur voit la différence = story
- "Comment estimer ?" → L'assistant propose, l'équipe valide
- "Et les dépendances ?" → Les noter mais ne pas bloquer la rédaction

**Tips d'animation :**

- Avoir des exemples de "mauvaises" stories à améliorer
- Faire le jeu des "3 questions du dev" (c'est clair ? c'est testable ? c'est estimable ?)
- Montrer un import JIRA si pertinent

### Variantes

**Version courte (45 min) :**
- Document simple fourni (5 besoins max)
- Focus sur le format User Story uniquement

**Version longue (1h30) :**
- Document complexe (spec technique, CR de 3 pages)
- Génération d'un epic avec stories liées
- Export JSON pour import JIRA/Linear

**Duo Dev + QA :**
- PM génère les stories
- Dev challenge les notes techniques
- Discussion sur les estimations

---

## Ressources complémentaires

- [User Stories Applied (Mike Cohn)](https://www.mountaingoatsoftware.com/books/user-stories-applied)
- Critères INVEST détaillés
