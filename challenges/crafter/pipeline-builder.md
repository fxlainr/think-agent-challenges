# Le Pipeline Builder

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 4h |
| Durée Dojo | 4h (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | SQL, notions de data engineering |

---

## Description

> *Créez un assistant qui vous aide à concevoir des pipelines de données robustes : sources, transformations, tests de qualité et documentation automatique.*

"D'où vient cette donnée ? Elle est fiable ? C'est quoi ce champ ?" — Des questions qu'on entend tous les jours. Ce challenge vous fait construire un assistant qui documente et structure vos pipelines de bout en bout, avec tests de qualité intégrés.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant de conception de pipeline fonctionnel
- [ ] Pipeline documenté de bout en bout
- [ ] Tests de qualité des données intégrés

**Critères de réussite :**

- Le pipeline est idempotent (relançable sans effet de bord)
- Les tests de qualité couvrent freshness, uniqueness, nulls
- La documentation est générée automatiquement

---

## Pistes de Solution

### Architecture d'un pipeline de données

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   Sources   │───▶│   Extract    │───▶│  Transform  │───▶│    Load      │
│             │    │   (E)        │    │   (T)       │    │    (L)       │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
      │                                      │                    │
      ▼                                      ▼                    ▼
┌─────────────┐                       ┌─────────────┐      ┌──────────────┐
│  Catalogage │                       │  Data Tests │      │   Docs       │
└─────────────┘                       └─────────────┘      └──────────────┘
```

### Prompt système suggéré

```
Tu es un Data Engineer senior. Tu aides à concevoir des pipelines de données robustes.

## Tes livrables
1. Schéma du pipeline (sources → transformations → destination)
2. Spécifications des transformations (SQL/Python)
3. Tests de qualité des données
4. Documentation automatique

## Bonnes pratiques que tu appliques
- **Idempotence** : relançable sans effet de bord
- **Tests de qualité** : freshness, uniqueness, nulls
- **Lineage** : traçabilité des données
- **Documentation as code**

## Questions à poser
1. Quelles sont les sources de données ?
2. Quelle est la destination ?
3. Quelles transformations sont nécessaires ?
4. Quelle fraîcheur est attendue ?
5. Quelles sont les règles métier à respecter ?

Génère le pipeline au format dbt si possible.
```

### Technologies clés

| Outil | Usage |
|-------|-------|
| **dbt** | Transformations SQL, tests, docs |
| **Airflow** | Orchestration |
| **Great Expectations** | Tests de qualité avancés |
| **dbt docs** | Documentation automatique |

### Exemple de modèle dbt

```sql
-- models/marts/customers.sql

{{
  config(
    materialized='table',
    unique_key='customer_id'
  )
}}

with source as (
    select * from {{ ref('stg_customers') }}
),

enriched as (
    select
        customer_id,
        first_name,
        last_name,
        email,
        created_at,
        -- Transformation métier
        case 
            when total_orders > 10 then 'VIP'
            when total_orders > 3 then 'Regular'
            else 'New'
        end as customer_segment
    from source
)

select * from enriched
```

### Tests de qualité (schema.yml)

```yaml
version: 2

models:
  - name: customers
    description: "Table des clients enrichie"
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null
      - name: email
        tests:
          - unique
          - not_null
          - accepted_values:
              values: ['%@%.%']  # Format email
      - name: customer_segment
        tests:
          - accepted_values:
              values: ['VIP', 'Regular', 'New']
```

### Tips & astuces

- Toujours commencer par le schéma de la destination
- Les tests sont aussi importants que le code
- La documentation se génère automatiquement si le code est bien structuré

---

## Animation Dojo (4h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Concevoir un pipeline de données robuste
- Implémenter des tests de qualité des données
- Documenter automatiquement avec dbt
- Appliquer les bonnes pratiques de data engineering

### Prérequis participants

- SQL niveau intermédiaire
- Notions de data warehouse
- Environnement Python ou dbt installé

### Matériel nécessaire

- [ ] Dataset exemple (CSV ou base de données)
- [ ] Template de projet dbt
- [ ] Checklist des tests de qualité
- [ ] Exemple de documentation générée

### Déroulé (4h workshop)

| Temps | Phase | Contenu | Livrable |
|-------|-------|---------|----------|
| 0-60 | Théorie | Architecture pipeline, bonnes pratiques | Compréhension |
| 60-150 | Conception | Design du pipeline avec l'assistant | Schéma validé |
| 150-210 | Tests | Implémentation des tests de qualité | Tests passants |
| 210-240 | Documentation | Génération et revue de la doc | Doc publiée |

### Points d'attention animateur

**Pièges courants :**

- Partir du code avant le schéma → Toujours designer d'abord
- Oublier les tests → Ils sont obligatoires
- Documentation après coup → Elle doit être dans le code

**Questions fréquentes :**

- "dbt vs Airflow ?" → dbt = transformations, Airflow = orchestration
- "Tests unitaires vs tests de données ?" → Les deux ! Tests de données = Great Expectations
- "Comment gérer les erreurs ?" → Alertes + retry + dead letter queue

### Variantes

**Version découverte (2h) :**
- Pipeline simple (1 source, 3 transformations)
- Tests basiques (unique, not_null)
- Pas d'orchestration

**Version production (2 jours) :**
- Multi-sources, multi-destinations
- Orchestration Airflow
- CI/CD pour les tests

---

## Ressources complémentaires

- [dbt Documentation](https://docs.getdbt.com/)
- [Great Expectations](https://greatexpectations.io/)
- [Fundamentals of Data Engineering (O'Reilly)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
