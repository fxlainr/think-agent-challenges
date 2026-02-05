# Le Simulateur Lean

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun (les concepts Lean seront expliqués) |

---

## Description

> *Créez un assistant d'excellence opérationnelle qui diagnostique vos processus, identifie les gaspillages (Muda) et propose des améliorations chiffrées.*

"On perd du temps mais on ne sait pas où." Ce challenge vous donne les outils du Lean Six Sigma pour analyser n'importe quel processus, identifier les 8 types de gaspillages et chiffrer les gains potentiels.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Diagnostic Lean d'un processus réel
- [ ] Identification des Muda avec quantification
- [ ] Recommandations priorisées avec ROI

**Critères de réussite :**

- Les 8 types de Muda sont compris et appliqués
- Le ratio d'efficience (VA/NVA) est calculé
- Les gains sont chiffrés de manière crédible

---

## Pistes de Solution

### Les 8 Muda (TIMWOODS)

| Muda | Description | Exemple |
|------|-------------|---------|
| **T**ransport | Déplacements inutiles | Envoi de docs entre services |
| **I**nventory | Stocks excessifs | Backlog gonflé, emails non traités |
| **M**otion | Mouvements inutiles | Chercher une info, aller-retours |
| **W**aiting | Temps d'attente | Attente de validation |
| **O**verproduction | Produire trop | Rapports non lus, features non utilisées |
| **O**verprocessing | Sur-traitement | Contrôles redondants |
| **D**efects | Erreurs et reprises | Bugs, retours, corrections |
| **S**kills | Sous-utilisation talents | Tâches répétitives pour experts |

### Prompt système suggéré

```
Tu es un consultant Lean Six Sigma Black Belt avec 15 ans d'expérience.

## Ton processus de diagnostic

### Phase 1 : Comprendre
- Quelle activité ? Quelles étapes ? Quels acteurs ?
- Quels indicateurs actuels (délai, qualité, coût) ?

### Phase 2 : Cartographier (VSM simplifié)
- Chaque étape avec temps estimé
- VA (Valeur Ajoutée) vs NVA (Non Valeur Ajoutée)
- Files d'attente et stocks

### Phase 3 : Identifier les Muda
Pour chaque étape : Type ? Ampleur ? Cause racine ?

### Phase 4 : Recommander
- Quick wins (facile, impact immédiat)
- Kaizen (amélioration continue)
- Kaikaku (transformation radicale)

### Phase 5 : Chiffrer
Temps économisé, coût évité, ROI estimé

Commence par : "Décris-moi le processus à optimiser : étapes, acteurs, problèmes observés."
```

### Exemple de diagnostic

**Processus :** Traitement demandes de remboursement (50/semaine, délai 10 jours)

**Cartographie :**

| Étape | Durée | VA/NVA | Acteur |
|-------|-------|--------|--------|
| Réception | 5 min | VA | N1 |
| Attente inbox | 24h | NVA ⚠️ | - |
| Qualification | 10 min | VA | N1 |
| Attente N2 | 48h | NVA ⚠️ | - |
| Analyse | 20 min | VA | N2 |
| Attente validation | 72h | NVA ⚠️ | - |
| Validation | 5 min | VA | Manager |

**Ratio d'efficience :** 1h VA / 80h total = **1.25%** 🔴

**Recommandations :**

| Action | Muda | Gain | Effort |
|--------|------|------|--------|
| Délégation < 50€ | Waiting | -48h | ⭐ Faible |
| Fusion N1/N2 | Transport | -48h | ⭐⭐ Moyen |
| Self-service client | Tous | -70% volume | ⭐⭐⭐ Élevé |

### Tips & astuces

- Toujours quantifier (même approximativement)
- L'objectif est d'améliorer le quotidien, pas de blâmer
- Quick wins d'abord pour créer la dynamique

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les 8 types de gaspillages (Muda)
- Cartographier un processus avec VA/NVA
- Calculer un ratio d'efficience
- Proposer des améliorations chiffrées

### Prérequis participants

- Avoir un processus en tête à optimiser
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Poster TIMWOODS (8 Muda)
- [ ] Template de Value Stream Map
- [ ] Processus exemples

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-7 | Intro Lean | Présente les 8 Muda avec exemples | Reconnaissent des situations | Théorie |
| 7-12 | VSM | Montre comment cartographier | Comprennent VA vs NVA | Méthode |
| 12-18 | Démo | Analyse un processus en live | Observent | Voir en action |
| 18-23 | Choix | Aide à choisir un processus | Sélectionnent leur cas | Préparation |
| 23-43 | Diagnostic | Circule, aide à quantifier | Analysent leur processus | Production |
| 43-53 | Chiffrage | Montre comment calculer ROI | Chiffrent leurs gains | Business case |
| 53-60 | Pitch | 2-3 présentations | Découvrent d'autres cas | Inspiration |

### Points d'attention animateur

**Pièges courants :**

- Processus trop vague → "Décris étape par étape"
- Pas de données → Estimer avec des ordres de grandeur
- Solutions avant diagnostic → "D'abord les Muda"

**Questions fréquentes :**

- "Valable pour les services ?" → Oui, Lean Office s'applique partout
- "Comment mesurer ?" → Observation, estimation avec les acteurs
- "Ça va braquer les équipes ?" → L'objectif est d'améliorer leur quotidien

### Variantes

**Version simple (45 min) :**
- Focus sur identification des Muda
- Pas de chiffrage

**Version avancée (2h) :**
- VSM détaillé
- Outils 5S, 5 Pourquoi, Ishikawa

---

## Ressources complémentaires

- [Lean Thinking (Womack & Jones)](https://www.lean.org/)
- [The Toyota Way](https://www.amazon.com/Toyota-Way-Management-Principles-Manufacturer/dp/0071392319)
