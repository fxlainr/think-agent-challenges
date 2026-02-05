# Auditeur FinOps

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Notions Cloud (AWS/GCP/Azure), accès aux données de facturation |

---

## Description

> *Concevez un agent "Cost Killer" qui analyse vos factures Cloud, détecte les anomalies et génère des recommandations d'économies chiffrées.*

Votre facture Cloud augmente mais personne ne sait pourquoi. Des instances tournent pour rien, des volumes ne sont rattachés à rien, vos Reserved Instances expirent... Cet agent analyse vos coûts, détecte les anomalies et vous dit exactement où économiser — avec le ROI de chaque action.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline d'analyse des données de coûts (fictives ou réelles)
- [ ] Système de détection d'anomalies
- [ ] Rapport avec recommandations chiffrées et priorisées

**Critères de réussite :**

- Anomalies détectées automatiquement (spike, ressource inutilisée)
- Chaque recommandation a un ROI calculé
- Les quick wins sont identifiés et priorisés

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FINOPS AUDITOR                        │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Collect   │───▶│   Analyze   │───▶│  Recommend  │  │
│  │             │    │             │    │             │  │
│  │ • AWS CUR   │    │ • Trends    │    │ • Actions   │  │
│  │ • GCP Bill  │    │ • Anomalies │    │ • ROI       │  │
│  │ • Azure     │    │ • Unused    │    │ • Priority  │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Sources de données

| Cloud | Source | Données |
|-------|--------|---------|
| AWS | Cost and Usage Reports (CUR) | Coûts détaillés par service |
| GCP | BigQuery Export | Billing data |
| Azure | Cost Management API | Usage + costs |

### Types d'anomalies à détecter

| Type | Détection | Action |
|------|-----------|--------|
| Spike soudain | Coût J > Coût J-7 × 1.5 | Alerte immédiate |
| Ressource inutilisée | CPU < 5% pendant 7 jours | Recommandation arrêt |
| Surdimensionnement | Utilisation < 30% | Recommandation resize |
| Absence de commitment | On-demand > 70% | Recommandation RI/Savings Plans |
| Stockage orphelin | EBS/S3 non attaché | Recommandation suppression |

### Prompt d'analyse FinOps

```
Analyse ces données de coûts Cloud :

[JSON avec données de facturation]

Génère un rapport FinOps avec :

## 1. Vue d'ensemble
- Coût total du mois
- Évolution vs mois précédent
- Top 5 services par coût

## 2. Anomalies détectées
Pour chaque anomalie :
- Type
- Ressource concernée
- Coût mensuel estimé
- Cause probable

## 3. Recommandations
Pour chaque recommandation :
- Action à prendre
- Économie potentielle (€/mois)
- Effort (Facile/Moyen/Complexe)
- ROI (payback en mois)

## 4. Quick Wins
Les 3 actions à faire immédiatement (effort faible, gain élevé)
```

### Exemple de rapport

```markdown
# Rapport FinOps - Janvier 2025

## 📊 Vue d'ensemble
| Métrique | Valeur | vs Déc |
|----------|--------|--------|
| Coût total | 45,230€ | +18% |
| EC2 | 22,400€ | +25% |
| RDS | 12,100€ | +5% |
| S3 | 4,200€ | +8% |

## 🚨 Anomalies détectées

### Spike EC2 (+25%)
- **Cause** : 8 nouvelles instances m5.2xlarge lancées le 15/01
- **Responsable** : Équipe Data (tag: project=data-lake)
- **Action** : Vérifier si besoin permanent ou temporaire

### Ressources inutilisées
- 3 EBS volumes (500GB) non attachés : 45€/mois
- 2 Elastic IPs non utilisées : 15€/mois
- 1 RDS instance (dev) éteinte mais facturée : 180€/mois

## 💡 Recommandations

| Action | Économie | Effort | ROI |
|--------|----------|--------|-----|
| Supprimer EBS orphelins | 45€/mois | Facile | Immédiat |
| Convertir EC2 en Savings Plans | 4,500€/mois | Moyen | 1 mois |
| Rightsize RDS prod | 800€/mois | Complexe | 2 mois |

## ⚡ Quick Wins (cette semaine)
1. Supprimer les 3 EBS orphelins → 45€/mois
2. Libérer les 2 Elastic IPs → 15€/mois
3. Arrêter l'instance RDS dev → 180€/mois

**Total quick wins : 240€/mois (2,880€/an)**
```

### Tips & astuces

- Commencer par les quick wins (ROI immédiat, effort minimal)
- Taguer les ressources pour identifier les responsables
- Automatiser les alertes de spike (>20% vs semaine précédente)

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Lire et interpréter une facture Cloud
- Identifier les principaux leviers d'économie FinOps
- Construire un pipeline d'analyse des coûts
- Calculer le ROI d'une action d'optimisation

### Prérequis participants

- Notions de services Cloud (EC2, S3, RDS...)
- Accès à des données de facturation (ou jeu de données fourni)
- Python basique (ou utilisation de n8n)

### Matériel nécessaire

- [ ] Jeu de données de facturation (fictif ou anonymisé)
- [ ] Template de rapport FinOps
- [ ] Calculateur de ROI (spreadsheet)
- [ ] Documentation des APIs de billing

### Déroulé (4h workshop)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-60 | Théorie | Principes FinOps, métriques clés, leviers | Compréhension |
| 60-120 | Pipeline | Extraction et structuration des données | Données prêtes |
| 120-180 | Détection | Algorithmes d'anomalies, seuils | Alertes configurées |
| 180-240 | Rapport | Recommandations et calcul ROI | Rapport final |

### Points d'attention animateur

**Pièges courants :**

- Se perdre dans les détails → Focus sur les gros postes (80/20)
- Oublier le contexte métier → Une ressource "inutilisée" peut être un backup
- Recommandations irréalistes → Valider la faisabilité technique

**Questions fréquentes :**

- "On n'a pas accès aux données réelles" → Utiliser le jeu de données fourni
- "C'est la faute des devs" → FinOps = responsabilité partagée
- "Savings Plans vs Reserved Instances ?" → Expliquer les différences

**Tips d'animation :**

- Utiliser des données anonymisées d'un cas réel si possible
- Faire calculer le ROI à la main avant d'automatiser
- Montrer des exemples de factures Cloud réelles

### Variantes

**Version découverte (2h) :**
- Analyse d'une facture fournie
- Focus sur l'identification des anomalies
- Pas de pipeline automatisé

**Version avancée (journée) :**
- Connexion aux vraies APIs Cloud
- Dashboard temps réel (Grafana/Metabase)
- Alertes automatisées (Slack/PagerDuty)

---

## Ressources complémentaires

- [FinOps Foundation](https://www.finops.org/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Infracost](https://www.infracost.io/) — estimation des coûts Terraform
