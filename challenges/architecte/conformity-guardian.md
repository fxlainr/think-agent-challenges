# Le Conformity Guardian

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Notions de conformité financière (EMIR, MiFID), Python |

---

## Description

> *Concevez un agent de surveillance réglementaire continue qui monitore les positions, détecte les dépassements de limites et génère les reportings automatiquement.*

En finance, dépasser une limite réglementaire peut coûter des millions en amendes. Ce challenge vous fait construire un agent qui surveille en continu les positions, alerte immédiatement en cas de breach et génère les reportings EMIR/MiFID.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Engine de monitoring des limites (positions, concentration, VaR)
- [ ] Système d'alertes automatiques avec escalade
- [ ] Templates de reporting réglementaire

**Critères de réussite :**

- Les breaches sont détectés en quasi temps réel
- Les alertes contiennent toutes les infos pour agir
- Les reportings sont conformes aux formats réglementaires

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  CONFORMITY GUARDIAN                     │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Market    │    │   Positions │    │   Limits    │  │
│  │   Data      │    │   (real-t)  │    │   Config    │  │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘  │
│         └──────────────────┼──────────────────┘          │
│                            ▼                             │
│                   ┌─────────────┐                        │
│                   │   Monitor   │                        │
│                   │   Engine    │                        │
│                   └──────┬──────┘                        │
│         ┌────────────────┼────────────────┐              │
│         ▼                ▼                ▼              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Alerts    │  │   Reports   │  │   Audit     │      │
│  │   (breach)  │  │   (EMIR...) │  │   Trail     │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
```

### Types de limites à monitorer

| Type | Exemple | Réglementation |
|------|---------|----------------|
| Position limits | Max 10M€ par sous-jacent | MiFID II |
| Concentration | Max 25% d'un émetteur | UCITS |
| VaR limits | VaR < 5% du NAV | Bâle III |
| Leverage | Levier < 3x | AIFMD |
| Margin | Marge initiale couverte | EMIR |

### Logique de monitoring

```python
def check_limits(positions: list, limits: dict) -> list:
    breaches = []
    
    for pos in positions:
        # Check position limit
        if pos['notional'] > limits['max_position']:
            breaches.append({
                'type': 'POSITION_LIMIT',
                'severity': 'HIGH',
                'position': pos['id'],
                'value': pos['notional'],
                'limit': limits['max_position'],
                'excess': pos['notional'] - limits['max_position']
            })
        
        # Check concentration
        concentration = pos['notional'] / total_portfolio
        if concentration > limits['max_concentration']:
            breaches.append({
                'type': 'CONCENTRATION',
                'severity': 'MEDIUM',
                'issuer': pos['issuer'],
                'concentration': concentration,
                'limit': limits['max_concentration']
            })
    
    return breaches
```

### Format d'alerte

```markdown
🚨 BREACH ALERT - [TIMESTAMP]

**Type** : Position Limit Exceeded
**Severity** : HIGH
**Portfolio** : Equity Long/Short
**Position** : AAPL Equity
**Current** : 12.5M€
**Limit** : 10M€
**Excess** : 2.5M€ (25%)

**Required Action** : Réduire la position dans les 24h
**Escalation** : Risk Manager, Compliance Officer

**Regulatory Reference** : MiFID II Art. 57
```

### Templates de reporting

| Report | Fréquence | Contenu |
|--------|-----------|---------|
| EMIR Trade Reporting | T+1 | Transactions OTC |
| MiFID Transaction | T+1 | Transactions listées |
| Position Reporting | Daily | Positions > seuil |
| Best Execution | Quarterly | Qualité d'exécution |

### Tips & astuces

- Intégrer des buffers d'alerte (warning à 80% de la limite)
- Logger toutes les décisions pour l'audit trail
- Tester avec des données historiques de breaches réels

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Identifier les principales limites réglementaires
- Construire un engine de monitoring
- Configurer des alertes avec escalade
- Générer des reportings conformes

### Prérequis participants

- Notions de conformité financière
- Python niveau intermédiaire
- Compréhension des produits financiers de base

### Matériel nécessaire

- [ ] Jeu de données de positions (fictif)
- [ ] Configuration des limites exemple
- [ ] Templates de reporting
- [ ] Documentation réglementaire simplifiée

### Déroulé (4h workshop)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-60 | Théorie | Réglementations (EMIR, MiFID, Bâle) | Compréhension |
| 60-150 | Monitoring | Construction du monitoring engine | Code fonctionnel |
| 150-210 | Alerting | Système d'alertes et escalade | Alertes configurées |
| 210-240 | Reporting | Templates et documentation | Reports générés |

### Points d'attention animateur

**Pièges courants :**

- Limites mal comprises → Clarifier avant de coder
- Alertes trop verboses → Prioriser par sévérité
- Oubli de l'audit trail → Logger tout

**Questions fréquentes :**

- "C'est applicable hors finance ?" → Oui, adapter les limites (compliance, risk)
- "Temps réel obligatoire ?" → Dépend de la réglementation, souvent T+1 suffit
- "Quid des faux positifs ?" → Affiner les seuils, ajouter des confirmations

### Variantes

**Version découverte (2h) :**
- Données et limites fournies
- Focus sur la logique de détection
- Pas de reporting

**Version production (2 jours) :**
- Connexion à des flux de marché réels
- Dashboard temps réel
- Intégration avec systèmes de trading

---

## Ressources complémentaires

- [ESMA - MiFID II](https://www.esma.europa.eu/policy-rules/mifid-ii-and-mifir)
- [EMIR Regulation](https://www.esma.europa.eu/policy-rules/post-trading/emir)
