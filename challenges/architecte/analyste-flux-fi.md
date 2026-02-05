# L'Analyste de Flux (Direction Fi)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | FI |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 320 |
| Prérequis | Notions de finance, Python ou SQL |

---

## Vision & Impact

Utiliser l'IA pour traiter des flux de données financières brutes en temps réel. L'IA permet de réconcilier des écritures ou de générer des reporting prédictifs, transformant la finance en un véritable **partenaire stratégique** de décision.

## Le saviez-vous ?

L'IA peut agir comme un analyste McKinsey de poche pour extraire les 5 insights les plus précieux d'un bilan en quelques secondes.

## Sources

- [Dexter - Application Claude Code pour la finance - Bruno Lu](https://www.linkedin.com/posts/brlu_ce-nest-pas-un-chatbot-de-plus-cest-activity-7422684992360808448-W1QK)
- [Claude Code génère un dashboard financier - Victor Galli](https://www.linkedin.com/posts/victor-galli_claude-code-g%C3%A9n%C3%A8re-moi-un-dashboard-financier-ugcPost-7422557370591092736-h2f1)

---

## Description

> *Créez un assistant d'analyse financière capable de traiter vos données et générer des insights.*

Excel et ses 47 onglets. Réconciliations manuelles. Reporting mensuel qui prend 3 jours. Ce challenge vous fait créer un assistant qui automatise l'analyse financière et génère des insights actionnables.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant capable de charger et analyser des données financières
- [ ] Automatisation d'une réconciliation
- [ ] Dashboard ou rapport généré automatiquement

**Critères de réussite :**

- Données traitées correctement (pas d'erreurs de calcul)
- Insights pertinents générés
- Temps d'analyse réduit de 80%

---

## Pistes de Solution

### Cas d'usage Finance

```
1. RÉCONCILIATION
   - Comparer deux sources de données
   - Identifier les écarts
   - Proposer des corrections

2. ANALYSE DE VARIANCE
   - Budget vs Réalisé
   - M vs M-1, Y vs Y-1
   - Explication des écarts

3. REPORTING
   - P&L automatique
   - KPIs financiers
   - Visualisations

4. PRÉDICTIF
   - Forecast de trésorerie
   - Tendances de revenus
   - Alertes précoces
```

### Prompt d'analyse financière

```
Tu es un analyste financier senior. Voici des données financières :

"""
[DONNÉES CSV/JSON]
"""

Analyse et génère :

## Synthèse exécutive
- 3 chiffres clés à retenir
- Tendance générale

## Analyse détaillée
- Performance par segment
- Variances significatives (>5%)
- Anomalies détectées

## Insights stratégiques
- Opportunités identifiées
- Risques à surveiller
- Recommandations

## Visualisation suggérée
- Quel graphique pour illustrer le point principal
```

### Architecture technique

```python
# Workflow type avec Claude + Python

import pandas as pd
from anthropic import Anthropic

# 1. Charger les données
df = pd.read_csv("financial_data.csv")

# 2. Pré-traitement
summary = df.describe().to_string()
trends = calculate_trends(df)

# 3. Analyse IA
prompt = f"""
Données financières :
{summary}

Tendances :
{trends}

Analyse et génère un rapport exécutif.
"""

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": prompt}]
)

# 4. Générer le rapport
generate_pdf_report(response.content)
```

### Template de réconciliation

```
## Réconciliation [Source A] vs [Source B]

### Résumé
- Total Source A : X€
- Total Source B : Y€
- Écart : Z€ (%)

### Écarts identifiés
| ID | Source A | Source B | Écart | Cause probable |
|----|----------|----------|-------|----------------|

### Actions recommandées
1. [Action 1]
2. [Action 2]

### Écritures de régularisation suggérées
[Si applicable]
```

---

## Animation Dojo (2h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | L'IA en finance : opportunités |
| 15-35 | Démo | Analyse d'un P&L en live |
| 35-65 | Cas 1 | Réconciliation automatique |
| 65-95 | Cas 2 | Reporting automatique |
| 95-115 | Discussion | Limites et contrôles |
| 115-120 | Clôture | Intégration dans les processus |

### Points d'attention

- TOUJOURS vérifier les calculs
- Sensibilité des données financières
- L'IA assiste, l'humain valide
