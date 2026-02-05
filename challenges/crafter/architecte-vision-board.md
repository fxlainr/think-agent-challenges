# L'Architecte de Vision (Vision Board)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐ |
| XP | 200 |
| Prérequis | Aucun |

---

## Vision & Impact

Matérialiser la vision produit via un **Visionary Board** généré par IA. Cela permet d'aligner l'équipe sur un futur tangible malgré l'accélération technologique.

## Le saviez-vous ?

NotebookLM peut simuler des "doubles de penseurs" pour challenger votre vision stratégique. Vous pouvez débattre avec des versions IA de Steve Jobs ou Marty Cagan.

## Sources

- [Je crée des doubles de penseurs - Élodie Hughes](https://www.linkedin.com/posts/elodiehughes_je-cr%C3%A9e-des-doubles-de-penseurs-pas-pour-share-7420875320133783553-pjK3)

---

## Description

> *Créez un Vision Board stratégique qui aligne votre équipe sur le futur du produit.*

"Notre vision ? Euh... être le leader de notre marché." Ce n'est pas une vision, c'est un vœu pieux. Ce challenge vous fait créer un Vision Board concret : l'état du produit dans 3 ans, les utilisateurs servis, les problèmes résolus, visualisé et partageable.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Vision Board visuel complet (Miro/Figma/Notion)
- [ ] 3 scénarios futurs explorés (optimiste, réaliste, pessimiste)
- [ ] Validation par "débat" avec des doubles de penseurs IA

**Critères de réussite :**

- La vision est concrète (pas de buzzwords vides)
- Les 3 scénarios sont plausibles
- L'équipe peut s'y projeter

---

## Pistes de Solution

### Structure du Vision Board

```
┌─────────────────────────────────────────────────────────────┐
│                    VISION BOARD - [PRODUIT]                 │
│                     Horizon : 3 ans (2029)                  │
├─────────────────┬─────────────────┬─────────────────────────┤
│   UTILISATEURS  │    PROBLÈMES    │      SOLUTION           │
│                 │     RÉSOLUS     │                         │
│ Qui servons-nous│ Quelles douleurs│ Comment nous les        │
│ dans 3 ans ?    │ avons-nous      │ résolvons ?             │
│                 │ éliminées ?     │                         │
├─────────────────┼─────────────────┼─────────────────────────┤
│   MÉTRIQUES     │   DIFFÉRENCIANT │      RISQUES            │
│                 │                 │                         │
│ Comment on sait │ Pourquoi nous   │ Ce qui pourrait nous    │
│ qu'on a réussi ?│ et pas un autre?│ faire échouer           │
└─────────────────┴─────────────────┴─────────────────────────┘
```

### Prompt de génération de vision

```
Je travaille sur [produit/projet].
Contexte actuel : [situation]

Génère une vision produit à 3 ans avec :

## L'état futur
- Décris une journée type d'un utilisateur en 2029
- Quels problèmes ont disparu de sa vie ?
- Comment notre produit s'intègre dans son quotidien ?

## Les métriques de succès
- 3-5 indicateurs quantifiés (ARR, users, NPS...)
- Ce qui aura changé dans le marché

## Le différenciant durable
- Pourquoi un concurrent ne peut pas nous copier ?
- Quel "moat" avons-nous construit ?

## Les paris stratégiques
- Quelles hypothèses doivent être vraies ?
- Quels risques acceptons-nous ?

Sois concret et ambitieux mais réaliste.
```

### Les doubles de penseurs

```
Tu vas jouer 3 personnalités qui challengent ma vision :

1. **Steve Jobs** - Focus obsessionnel sur l'expérience
   "Est-ce que c'est insanely great ? Qu'est-ce qu'on enlève ?"

2. **Marty Cagan** - Product Discovery rigoureux
   "Quelle preuve avez-vous que les clients veulent ça ?"

3. **L'avocat du diable** - Sceptique constructif
   "Si ça échoue, ce sera pour quelle raison ?"

Ma vision : [décrire la vision]

Chaque personnalité pose 3 questions qui challengent.
```

### Scénarios futurs (Futurospective)

```
Produit : [nom]
Vision : [résumé]

Génère 3 scénarios à 3 ans :

## Scénario Optimiste (10% chances)
- Ce qui s'est passé de magique
- Métriques atteintes
- Ce qui a permis ce succès

## Scénario Réaliste (60% chances)
- Progression attendue
- Obstacles rencontrés et surmontés
- État du produit et du marché

## Scénario Pessimiste (30% chances)
- Ce qui a mal tourné
- Signaux d'alerte qu'on aurait dû voir
- Comment on aurait pu l'éviter

Pour chaque scénario : 1 décision clé qui l'a causé.
```

---

## Animation Dojo (1h30, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Formuler une vision concrète et inspirante
- Explorer plusieurs futurs possibles
- Challenger une vision avec des perspectives multiples

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Vision vs Roadmap vs Stratégie |
| 10-25 | Génération | Chacun génère sa vision (prompt) |
| 25-40 | Scénarios | Explorer optimiste/réaliste/pessimiste |
| 40-55 | Challenge | Doubles de penseurs en binômes |
| 55-75 | Visualisation | Créer le Vision Board (Miro) |
| 75-90 | Partage | Présentation des visions |

### Points d'attention animateur

- Éviter les visions trop vagues ("être le leader")
- Pousser à quantifier les métriques
- Les scénarios pessimistes sont les plus instructifs

---

## Ressources complémentaires

- [Inspired - Marty Cagan](https://www.svpg.com/inspired-how-to-create-products-customers-love/)
- [Good Strategy Bad Strategy - Richard Rumelt](https://goodbadstrategy.com/)
