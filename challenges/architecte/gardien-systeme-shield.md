# Le Gardien du Système (Direction Shield)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | SHIELD |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 340 |
| Prérequis | Notions de sécurité, scripting |

---

## Vision & Impact

Automatiser la **recette globale** et la détection de vulnérabilités via des scripts de test autonomes. L'IA permet de gagner un temps massif tout en assurant une couverture de sécurité exhaustive.

## Le saviez-vous ?

L'IA est particulièrement efficace pour repérer les **signaux faibles** et les comportements anormaux dans les logs de sécurité. Elle voit des patterns que l'humain manque.

## Sources

- [L'IA m'a fait gagner 18 min par test QA - Marion Jachimski](https://www.linkedin.com/posts/marion-jachimski-7010996b_lia-ma-fait-gagner-18-min-par-test-qa-activity-7417822957655236608-Cpwn)
- [50 use cases IA - Nicolas Hircq](https://www.linkedin.com/posts/nicolas-hircq_jai-pass%C3%A9-30h-%C3%A0-compiler-50-use-cases-ia-ugcPost-7396806722742390784-Ctqm)

---

## Description

> *Construisez un système de surveillance et de test de sécurité automatisé.*

Tests manuels. Logs ignorés. Vulnérabilités découvertes trop tard. Ce challenge vous fait créer un gardien automatique qui surveille, teste et alerte en continu.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Suite de tests de sécurité automatisés
- [ ] Analyseur de logs avec détection d'anomalies
- [ ] Système d'alertes configuré

**Critères de réussite :**

- Tests exécutables automatiquement
- Anomalies détectées dans les logs de test
- Alertes pertinentes (pas de faux positifs excessifs)

---

## Pistes de Solution

### Architecture du Gardien

```
┌─────────────────────────────────────────────────────────┐
│                    GUARDIAN SYSTEM                       │
├─────────────────┬─────────────────┬─────────────────────┤
│   PRÉVENTION    │   DÉTECTION     │    RÉACTION         │
│                 │                 │                     │
│ - Tests auto    │ - Analyse logs  │ - Alertes           │
│ - Audit code    │ - Anomalies     │ - Isolation         │
│ - Scan deps     │ - Patterns      │ - Rapport           │
└─────────────────┴─────────────────┴─────────────────────┘
```

### Tests de sécurité automatisés

```python
# Tests à automatiser

SECURITY_TESTS = [
    {
        "name": "SQL Injection",
        "payloads": ["'; DROP TABLE--", "1' OR '1'='1"],
        "check": "error_or_unexpected_response"
    },
    {
        "name": "XSS",
        "payloads": ["<script>alert(1)</script>", "javascript:alert(1)"],
        "check": "payload_reflected"
    },
    {
        "name": "Auth Bypass",
        "tests": ["access_without_token", "expired_token", "wrong_role"],
        "check": "401_or_403"
    },
    {
        "name": "Rate Limiting",
        "action": "100_requests_in_10_seconds",
        "check": "429_returned"
    }
]
```

### Prompt d'analyse de logs

```
Analyse ces logs de sécurité :

"""
[LOGS]
"""

Recherche :

## Anomalies
- Patterns inhabituels (horaires, fréquence, source)
- Tentatives d'accès échouées répétées
- Requêtes malformées

## Signaux faibles
- Comportements qui précèdent souvent une attaque
- Reconnaissance (scanning)
- Énumération

## Classification
Pour chaque anomalie :
- Sévérité : Critique / Haute / Moyenne / Basse
- Confiance : Certaine / Probable / Possible
- Action recommandée

## Faux positifs probables
- Ce qui ressemble à une anomalie mais n'en est pas
```

### Workflow de surveillance

```
TOUTES LES 5 MIN :
├── Collecter les logs
├── Analyser avec l'IA
├── Si anomalie critique → Alerte immédiate
└── Sinon → Agrégation pour rapport quotidien

TOUTES LES NUITS :
├── Exécuter la suite de tests
├── Scanner les dépendances
├── Générer le rapport
└── Envoyer aux responsables

HEBDOMADAIRE :
├── Revue des alertes
├── Mise à jour des patterns
└── Amélioration des tests
```

### Template de rapport sécurité

```markdown
# Rapport Sécurité - [Date]

## Résumé exécutif
- Score global : X/100
- Alertes critiques : X
- Tests passés : X/Y

## Alertes

### Critiques 🔴
[Liste avec détails]

### Hautes 🟠
[Liste avec détails]

## Tests automatisés
| Test | Résultat | Détails |
|------|----------|---------|

## Recommandations
1. [Priorité 1]
2. [Priorité 2]

## Évolution
[Graphique semaine/semaine]
```

---

## Animation Dojo (2h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Pourquoi automatiser la sécurité |
| 15-35 | Démo | Suite de tests en action |
| 35-65 | Tests | Créer sa suite de tests |
| 65-95 | Logs | Configurer l'analyse de logs |
| 95-115 | Alertes | Système d'alertes |
| 115-120 | Clôture | Intégration CI/CD |

### Points d'attention

- Ne pas tester sur la production sans autorisation
- Environnement de test isolé
- Les alertes doivent être actionnables
