# L'Ingénieur Durable

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐⭐ |
| Prérequis | Notions d'éco-conception |

---

## Description

> *Concevez un système d'aide à la décision pour l'ingénierie durable : scoring multi-critères, comparaison d'options, recommandations argumentées.*

"On prend le plastique recyclé ou le bioplastique ?" Ce challenge vous fait construire un système qui analyse les choix techniques, score leur impact environnemental et propose des alternatives — avec les trade-offs explicites.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Système de scoring multi-critères
- [ ] Comparateur d'options techniques
- [ ] Rapport d'aide à la décision automatisé

**Critères de réussite :**

- Les critères sont pertinents et pondérables
- Le comparatif est visuel et compréhensible
- Les trade-offs sont explicités

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│              SUSTAINABLE ENGINEERING SYSTEM              │
│                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Options   │    │   Impact    │    │ Alternative │  │
│  │   Input     │───▶│   Scoring   │───▶│  Generator  │  │
│  │             │    │             │    │             │  │
│  │ • Tech A    │    │ • CO2       │    │ • Suggest   │  │
│  │ • Tech B    │    │ • Eau       │    │ • Compare   │  │
│  │ • Tech C    │    │ • Ressources│    │ • Trade-off │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│                                               │          │
│                                               ▼          │
│  ┌─────────────────────────────────────────────────────┐│
│  │                  DECISION REPORT                     ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
```

### Critères d'évaluation

| Critère | Indicateur | Unité | Source |
|---------|------------|-------|--------|
| Carbone | Empreinte CO2 | kg CO2eq | Base Carbone ADEME |
| Eau | Consommation | L | Water Footprint |
| Ressources | Épuisement | ADP | Ecoinvent |
| Énergie | Consommation | kWh | Mesure directe |
| Recyclabilité | Taux | % | Analyse composition |
| Réparabilité | Indice | /10 | Évaluation qualitative |

### Prompt du système de scoring

```
Tu es un ingénieur en éco-conception.

## Input
Options techniques à comparer avec leurs caractéristiques.

## Critères (0-10 chacun)
1. Empreinte carbone (10 = très faible)
2. Consommation d'eau (10 = très faible)
3. Durabilité/longévité (10 = très durable)
4. Recyclabilité (10 = 100% recyclable)
5. Énergie d'usage (10 = très sobre)
6. Réparabilité (10 = facilement réparable)

## Output

### Tableau comparatif
| Critère | Option A | Option B | Option C |
|---------|----------|----------|----------|
| Carbone | X/10 | X/10 | X/10 |
| ... | ... | ... | ... |
| **TOTAL** | X/60 | X/60 | X/60 |

### Recommandation
[Option recommandée + justification]

### Trade-offs
[Ce qu'on sacrifie avec chaque choix]
```

### Format de rapport

```markdown
# Rapport de Décision Durable
## [Choix technique]

### 1. Contexte
[Description du projet et contraintes]

### 2. Options évaluées

#### Option A : [Nom]
| Critère | Score | Justification |
|---------|-------|---------------|
| Carbone | 7/10 | Fabrication locale |
| Eau | 5/10 | Process intensif |
| ... | ... | ... |
| **Total** | **X/60** | |

#### Option B : [Nom]
[Même structure]

### 3. Recommandation
**Choix recommandé** : Option A

**Justification** :
- Principal avantage : [...]
- Trade-off accepté : [...]

### 4. Pistes d'amélioration
[Comment réduire encore l'impact]
```

### Tips & astuces

- Utiliser des ordres de grandeur quand les données précises manquent
- Toujours expliciter les hypothèses
- Proposer des pistes pour les options non retenues

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Définir des critères d'évaluation environnementale
- Construire un système de scoring multi-critères
- Générer des rapports d'aide à la décision
- Expliciter les trade-offs techniques

### Prérequis participants

- Notions d'éco-conception ou envie d'apprendre
- Accès à un chat IA
- Un choix technique à évaluer (ou cas fourni)

### Matériel nécessaire

- [ ] Grille de critères
- [ ] Facteurs d'émission (Base Carbone)
- [ ] Template de rapport
- [ ] Cas d'étude (si participants sans projet)

### Déroulé (4h)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-45 | Théorie | ACV et critères d'évaluation | Compréhension |
| 45-120 | Construction | Système de scoring | Grille fonctionnelle |
| 120-180 | Application | Cas réel ou fourni | Rapport complet |
| 180-210 | Présentation | Chacun présente sa recommandation | Partage |
| 210-240 | Discussion | Trade-offs et améliorations | Apprentissage collectif |

### Points d'attention animateur

**Pièges courants :**

- Données trop précises → Accepter les ordres de grandeur
- Oublier les trade-offs → Toujours les expliciter
- Score sans contexte → Expliquer les hypothèses

**Questions fréquentes :**

- "Les scores sont arbitraires ?" → Basés sur des données, mais simplifiés
- "Comment pondérer les critères ?" → Selon les priorités du projet
- "Ça remplace une ACV ?" → Non, c'est une aide à la décision simplifiée

### Variantes

**Version simple (2h) :**
- Critères fixes (pas de personnalisation)
- Cas d'étude fourni
- Focus sur l'analyse

**Version avancée (1 jour) :**
- Données réelles collectées
- Multi-critères pondérés
- Présentation à des décideurs

---

## Ressources complémentaires

- [Base Carbone ADEME](https://base-empreinte.ademe.fr/)
- [Ecoinvent](https://ecoinvent.org/)
- [ISO 14040](https://www.iso.org/standard/37456.html)
