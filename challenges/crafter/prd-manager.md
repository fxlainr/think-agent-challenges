# PRD Manager

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| XP | 180 |
| Prérequis | Notions de gestion de produit |

---

## Vision & Impact

Rédiger ses spécifications (PRD) en utilisant l'IA pour creuser les **objets métiers** et les scénarios d'utilisation complexes. Une spec bien décomposée est le socle indispensable pour que les agents de coding produisent un résultat fonctionnel.

## Le saviez-vous ?

Savoir **décomposer son intention** est LA compétence fondamentale du PM en 2026. L'IA peut tout produire, mais c'est votre capacité à clarifier ce que vous voulez qui fait la différence entre un prototype bancal et un produit solide.

## Sources

- [PRD avec l'IA - Marion Jachimski](https://www.linkedin.com/posts/marion-jachimski-7010996b_productmanagement-aiforpm-delivery-activity-7407670823781552128-jF--)

---

## Description

> *Créez un assistant qui vous interviewe et rédige un PRD (Product Requirements Document) complet et professionnel.*

Rédiger un bon PRD prend des heures. Entre les allers-retours avec les stakeholders, la structuration et les oublis, c'est un exercice fastidieux. Cet assistant mène l'interview à votre place, challenge vos hypothèses et génère un document utilisable par votre équipe.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un assistant qui mène une interview structurée
- [ ] Un PRD complet couvrant les 10 sections standard
- [ ] Document utilisable en l'état par une équipe produit

**Critères de réussite :**

- Les questions posées font émerger les vrais besoins
- Le PRD distingue clairement Must Have / Should Have / Nice to Have
- Les métriques de succès sont SMART (quantifiées)

---

## Pistes de Solution

### Structure du PRD

1. **Overview** — Titre, date, auteur, statut
2. **Problem Statement** — Problème, persona, contexte
3. **Goals & Metrics** — Objectifs business et KPIs
4. **User Stories** — Au format "En tant que... je veux... afin de..."
5. **Requirements** — P0 (Must) / P1 (Should) / P2 (Nice) / Out of scope
6. **Design & UX** — Wireframes, parcours utilisateur
7. **Technical Considerations** — Contraintes, dépendances
8. **Timeline** — Planning, jalons
9. **Risks** — Risques identifiés et mitigations
10. **Open Questions** — Points à clarifier

### Prompt système suggéré

```
Tu es un Product Manager senior avec 10 ans d'expérience. Tu excelles dans l'art de transformer des besoins flous en spécifications actionables.

## Ta mission
Mener un entretien structuré pour rédiger un PRD complet.

## Ton processus d'interview

### Phase 1 : Contexte (5 min)
- C'est quoi le projet en une phrase ?
- Qui demande ça et pourquoi maintenant ?

### Phase 2 : Problème (10 min)
- Quel problème résout-on ?
- Pour qui exactement ?
- Comment il fait aujourd'hui sans cette feature ?

### Phase 3 : Solution (10 min)
- Quelle est la vision ?
- Quelles features pour le MVP ?
- Qu'est-ce qui est hors scope ?

### Phase 4 : Succès (5 min)
- Comment on saura qu'on a réussi ?
- Quels objectifs chiffrés ?

### Phase 5 : Contraintes (5 min)
- Délai, budget, dépendances ?
- Questions ouvertes ?

## Ton style
- Une question à la fois
- Tu reformules pour confirmer
- Tu challenges les évidences
- Tu n'acceptes pas les métriques vagues

Commence par : "Salut ! C'est quoi le projet en une phrase, et qui le demande ?"
```

### Exemple de PRD généré (extrait)

```markdown
# PRD : Chatbot Support Client - v1.0

## 1. Overview
| Attribut | Valeur |
|----------|--------|
| Titre | Chatbot IA Support Client |
| Date | 2025-01-15 |
| Auteur | Marie Dupont (PM) |
| Statut | Draft |

## 2. Problem Statement

**Problème :**
2000 tickets/mois dont 60% sont répétitifs. Temps de réponse : 4h. NPS : 42.

**Pour qui :**
Clients avec questions simples voulant une réponse immédiate.

**Pourquoi maintenant :**
Pic de charge +80% sur les fêtes, budget recrutement gelé.

## 3. Goals & Metrics

| Type | Objectif | Target |
|------|----------|--------|
| Business | Réduire charge support | 40% tickets auto |
| Utilisateur | Réponse instantanée | < 30 sec |
| Qualité | Satisfaction | CSAT > 4/5 |

## 5. Requirements

**Must Have (P0) :**
- Réponse aux questions suivi de commande
- Escalade vers humain si incompris
- Disponible 24/7

**Should Have (P1) :**
- FAQ dynamique
- Historique des échanges

**Out of Scope :**
- Réclamations complexes
- Remboursements automatiques
```

### Tips & astuces

- Insister sur les métriques quantifiées (pas "améliorer", mais "+20%")
- Toujours demander ce qui est OUT of scope
- Challenge : un dev peut-il commencer avec ce PRD ?

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Structurer un PRD professionnel (10 sections)
- Mener un entretien de discovery efficace
- Distinguer Must Have / Should Have / Nice to Have
- Définir des métriques de succès SMART

### Prérequis participants

- Avoir un projet/feature en tête à spécifier
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Template PRD vide
- [ ] Exemple de PRD complété
- [ ] Checklist qualité PRD

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Présente la structure d'un bon PRD | Découvrent le template | Cadrage |
| 5-10 | Démo | Fait une interview de 5 min | Observent les questions | Voir le process |
| 10-15 | Setup | Distribue le prompt | Configurent leur assistant | Préparation |
| 15-35 | Génération | Circule, aide sur les questions difficiles | Font leur interview, génèrent le PRD | Production |
| 35-45 | Review | Distribue la checklist qualité | Auto-évaluent leur PRD | Qualité |
| 45-55 | Partage | Fait présenter 2 PRDs | Écoutent, commentent | Benchmarking |
| 55-60 | Clôture | Tips pour adapter au contexte | Notent les adaptations | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- PRD trop vague → Insister sur les métriques concrètes
- Confusion Must/Nice to Have → Faire prioriser vraiment
- Projet confidentiel → Masquer les infos sensibles

**Questions fréquentes :**

- "Je n'ai pas toutes les réponses" → C'est normal, le PRD fait ressortir les questions
- "C'est trop long" → Adapter selon contexte (MVP = PRD léger)
- "Mon équipe utilise un autre template" → Mapper les sections

**Tips d'animation :**

- Montrer un "mauvais" PRD vs un bon PRD
- Challenge : un dev peut-il commencer avec ce PRD ?

### Variantes

**Version courte (45 min) :**
- PRD simplifié (5 sections)
- Projet fictif commun

**Version longue (2h) :**
- PRD complet + wireframes
- Cross-review par un autre PM
- Présentation comme à un COMEX

---

## Ressources complémentaires

- [Writing Great PRDs (Marty Cagan)](https://www.svpg.com/)
- Template PRD Notion/Coda
