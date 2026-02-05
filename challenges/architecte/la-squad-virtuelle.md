# La Squad Virtuelle

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | Tous |
| Durée solo | 3h |
| Durée Dojo | 1h (version accélérée) |
| Difficulté | ⭐⭐⭐⭐⭐ |
| XP | 500 |
| Prérequis | Connaissance des rôles CPO, CTO, Growth |

---

## Vision & Impact

Concevoir une architecture où une seule personne orchestre des agents pour viser un impact business massif. On ne se considère plus comme un effectif, mais comme un **orchestrateur de système**.

## Le saviez-vous ?

"Watching isn't doing" : la maîtrise vient de la fabrication de ses propres outils et flux. Les "one-person teams" les plus efficaces en 2026 sont celles qui ont automatisé leur propre processus de décision.

## Sources

- [How to make $1B in 2026 as a one-person team](https://www.mattprd.com/p/how-to-make-1b-in-2026-as-a-one-person-team)
- [Je ne me considère plus comme un effectif - Salim Laimeche](https://www.linkedin.com/posts/salimlaimeche_aujourdhui-je-ne-me-consid%C3%A8re-plus-comme-activity-7414296783721459714-HNkI)

---

## Description

> *Simulez une équipe complète (CPO, CTO, Growth) via différents agents IA pour réaliser un cadrage stratégique en quelques heures au lieu de plusieurs semaines.*

Pas de CPO sous la main ? CTO débordé ? Growth en vacances ? Ce challenge vous fait créer une "squad virtuelle" : 3 agents IA spécialisés qui challengent votre projet sous différents angles et produisent un cadrage complet.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 3 agents configurés (CPO, CTO, Growth)
- [ ] PRD complet validé par l'agent CPO
- [ ] Architecture technique par l'agent CTO
- [ ] Stratégie GTM par l'agent Growth

**Critères de réussite :**

- Chaque agent a une personnalité et un style distincts
- Les livrables sont cohérents entre eux
- Les tensions entre agents sont identifiées et arbitrées

---

## Pistes de Solution

### Architecture multi-agents

```
                    ┌─────────────────┐
                    │   Orchestrateur │
                    │   (vous)        │
                    └────────┬────────┘
       ┌─────────────────────┼─────────────────────┐
       ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│     CPO      │    │     CTO      │    │    Growth    │
│ (Produit)    │    │ (Technique)  │    │ (Business)   │
└──────────────┘    └──────────────┘    └──────────────┘
       │                     │                     │
       ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│     PRD      │    │ Architecture │    │     GTM      │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Prompt Agent CPO

```
Tu es Sarah, CPO expérimentée (ex-Spotify, ex-Doctolib). 12 ans d'expérience.

## Ta mission
Cadrer le produit : vision, utilisateurs, problèmes, features prioritaires.

## Ton style
- Tu poses beaucoup de questions sur les utilisateurs
- Tu refuses de parler solutions avant de comprendre le problème
- Tu insistes sur les métriques de succès
- Tu penses en jobs-to-be-done

## Tes livrables
- Product Vision (1 page)
- User Personas (2-3)
- PRD structuré

Commence par : "Pitch-moi le projet en 2 phrases. Qui est l'utilisateur et quel problème on résout ?"
```

### Prompt Agent CTO

```
Tu es Marc, CTO pragmatique (ex-Algolia, ex-OVH). 15 ans d'expérience.

## Ta mission
Définir l'architecture, les choix technologiques, les risques et le planning.

## Ton style
- Tu demandes toujours les contraintes (budget, délai, équipe)
- Tu proposes des solutions simples avant de complexifier
- Tu identifies les risques tôt
- Tu penses en MVP et itérations

## Tes livrables
- Architecture macro
- Stack recommandée avec justifications
- Estimation de charge
- Risques et mitigations

Commence par : "Montre-moi le PRD. Ensuite on parle contraintes."
```

### Prompt Agent Growth

```
Tu es Julie, Growth Lead (ex-Qonto, ex-Alan). 8 ans d'expérience.

## Ta mission
Définir la stratégie go-to-market : positionnement, canaux, pricing.

## Ton style
- Tu raisonnes en funnel et cohortes
- Tu veux des chiffres (TAM, CAC, LTV)
- Tu penses viralité et rétention dès le début
- Tu proposes des expérimentations rapides

## Tes livrables
- Positionnement et messaging
- Stratégie GTM par phase
- Canaux d'acquisition prioritaires
- KPIs et objectifs

Commence par : "C'est quoi le marché ? Qui sont les concurrents ? Quel est notre angle unique ?"
```

### Processus d'orchestration

| Phase | Durée | Agent | Output |
|-------|-------|-------|--------|
| 1. Cadrage produit | 45 min | CPO | PRD validé |
| 2. Architecture | 45 min | CTO | Archi + estimations |
| 3. Go-to-Market | 45 min | Growth | GTM + métriques |
| 4. Synthèse | 30 min | Vous | Document intégré |

### Tips & astuces

- Copier-coller le PRD au CTO (pas de contexte perdu)
- Les agents qui se contredisent, c'est normal — vous arbitrez
- Time-boxing strict pour ne pas s'éterniser

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Créer et orchestrer plusieurs agents IA spécialisés
- Faire dialoguer les perspectives (produit, tech, business)
- Produire un cadrage stratégique accéléré
- Arbitrer les tensions entre disciplines

### Prérequis participants

- Avoir un projet/idée à cadrer
- Accès à un chat IA permettant de créer des assistants
- Connaissance basique des rôles

### Matériel nécessaire

- [ ] 3 prompts système
- [ ] Template de livrable final
- [ ] Cas exemple pour la démo
- [ ] Timer strict

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente le concept de squad virtuelle | Découvrent l'approche | Cadrage |
| 5-10 | Démo | Interaction avec 1 agent (CPO) | Observent le style | Voir le process |
| 10-15 | Setup | Distribue les prompts | Créent leurs 3 agents | Préparation |
| 15-25 | Phase CPO | Guide | Dialoguent avec CPO | Cadrage produit |
| 25-35 | Phase CTO | Guide | Dialoguent avec CTO | Cadrage technique |
| 35-45 | Phase Growth | Guide | Dialoguent avec Growth | Cadrage business |
| 45-55 | Synthèse | Fait identifier les tensions | Compilent les livrables | Intégration |
| 55-60 | Clôture | Meilleures pratiques | Partagent leurs learnings | Méta-apprentissage |

### Points d'attention animateur

**Pièges courants :**

- Trop de temps sur un agent → Timer strict
- Agents qui se contredisent → C'est le job d'arbitrer
- Pas de projet clair → Avoir des projets fictifs prêts

**Questions fréquentes :**

- "Mes agents ne sont pas d'accord" → Parfait ! Arbitrez
- "Le CTO dit que c'est trop ambitieux" → Négociez un MVP
- "Le Growth veut aller plus vite" → Faites dialoguer avec le CTO

### Variantes

**Version simple (45 min) :**
- 2 agents seulement (CPO + CTO)
- Projet fictif commun

**Version complète (4h) :**
- 4 agents (+ Design)
- Vrai projet
- Itérations multiples entre agents

---

## Ressources complémentaires

- [Shape Up (Basecamp)](https://basecamp.com/shapeup)
- [Inspired (Marty Cagan)](https://www.svpg.com/inspired-how-to-create-products-customers-love/)
