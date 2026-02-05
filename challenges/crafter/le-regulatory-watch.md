# Le Regulatory Watch

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Compte n8n, culture réglementaire basique |

---

## Description

> *Créez un pipeline de veille réglementaire qui surveille les régulateurs, résume les publications et vous alerte sur les deadlines critiques.*

MiFID, EMIR, DORA, Bâle... Les textes tombent chaque semaine. Qui les lit vraiment ? Ce challenge automatise votre veille réglementaire : collecte des sources, résumé IA des impacts et alertes sur les deadlines.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Workflow n8n collectant plusieurs sources (ESMA, EBA, AMF...)
- [ ] Bulletin de veille généré automatiquement
- [ ] Alertes sur les deadlines critiques

**Critères de réussite :**

- Les publications sont classifiées par réglementation et urgence
- Les résumés sont orientés "impact opérationnel"
- Les alertes arrivent à temps (avant les deadlines)

---

## Pistes de Solution

### Sources à surveiller

| Régulateur | Périmètre | Flux RSS |
|------------|-----------|----------|
| **ESMA** | UE - Marchés | esma.europa.eu/press-news |
| **EBA** | UE - Banques | eba.europa.eu/news-press |
| **AMF** | France - Marchés | amf-france.org/actualites |
| **ACPR** | France - Banques | acpr.banque-france.fr |
| **Comité de Bâle** | International | bis.org/bcbs |

### Prompt de classification et résumé

```
Analyse cette publication réglementaire.

## Classification
- **Réglementation** : Bâle / MiFID / EMIR / DORA / Autre
- **Type** : Consultation / Final / Guidance / Q&A
- **Urgence** : Critique / Important / Information
- **Impact** : Élevé / Moyen / Faible

## Résumé (3 phrases max)
[Résumé orienté impact opérationnel]

## Impacts opérationnels
- [Impact 1]
- [Impact 2]

## Dates clés
- [Date et événement]

## Action requise
[Ce qui doit être fait concrètement]

Publication à analyser :
[Contenu]
```

### Format du bulletin

```markdown
# Bulletin de Veille Réglementaire
## Semaine du [date]

### 🚨 Alertes prioritaires

#### [Titre]
**Régulateur** : ESMA | **Réglementation** : DORA
**Type** : Texte final | **Deadline** : 17/01/2025

**Résumé** : [3 phrases]

**Impact** :
- [Impact 1]
- [Impact 2]

**Action** : [Ce qu'il faut faire]

---

### 📋 Autres publications

| Date | Régulateur | Titre | Type |
|------|------------|-------|------|

### 📅 Prochaines deadlines

| Date | Événement | Réglementation |
|------|-----------|----------------|
```

### Architecture workflow n8n

```
Schedule (hebdo) → Fetch RSS (multi-sources) → Merge → Filter récent
     ↓
Classify & Summarize (IA) → Generate Bulletin → Send Email
     ↓
If Urgent → Slack Alert
```

### Tips & astuces

- Hebdo pour le bulletin, temps réel pour les alertes critiques
- Affiner le filtrage par mots-clés selon votre activité
- Inclure les liens vers les sources officielles

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les sources réglementaires clés
- Automatiser la collecte avec n8n
- Résumer et classifier les publications
- Configurer des alertes pertinentes

### Prérequis participants

- Compte n8n
- Culture réglementaire basique
- Connaissance des flux RSS

### Matériel nécessaire

- [ ] Template workflow n8n
- [ ] Liste des flux RSS des régulateurs
- [ ] Prompt de classification
- [ ] Exemple de bulletin

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | L'enjeu de la veille réglementaire | Comprennent l'importance | Contexte |
| 5-10 | Sources | Montre les sites et flux RSS | Découvrent les sources | Connaissance |
| 10-18 | Démo | Construit le workflow en live | Observent | Technique |
| 18-25 | Setup | Aide à configurer | Importent le template | Préparation |
| 25-40 | Construction | Circule, aide sur les prompts | Personnalisent le workflow | Production |
| 40-50 | Test | Fait tourner les workflows | Génèrent leur premier bulletin | Validation |
| 50-55 | Alertes | Configure Slack/email | Configurent leurs alertes | Extension |
| 55-60 | Clôture | Planification de l'automatisation | Notent le planning | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- RSS mal formaté → Avoir des alternatives
- Trop de bruit → Filtrage par mots-clés
- Résumés trop génériques → Contexte métier dans le prompt

**Questions fréquentes :**

- "Gérer les PDF ?" → Extraction texte avant analyse
- "Quelle fréquence ?" → Hebdo bulletin, temps réel alertes
- "IA se trompe sur l'impact ?" → Toujours vérifier les alertes critiques

### Variantes

**Version simple (45 min) :**
- 1 seul régulateur
- Résumé via chat IA (pas de workflow)

**Version avancée (2h) :**
- Multi-régulateurs (5+)
- Dashboard de suivi
- Historique des publications

---

## Ressources complémentaires

- [ESMA](https://www.esma.europa.eu/)
- [EBA](https://www.eba.europa.eu/)
- [AMF](https://www.amf-france.org/)
