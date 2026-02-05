# L'Architecte de Structure (PRD & Objets Métiers)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐ |
| XP | 310 |
| Prérequis | Product Management |

---

## Vision & Impact

Utiliser l'IA pour **décomposer son intention** et définir l'architecture des objets métiers avant tout développement. Ce cadrage profond garantit que la donnée manipulée est saine et que le système est robuste.

## Le saviez-vous ?

Savoir décomposer son intention est la **compétence fondamentale** pour transformer l'IA en partenaire d'ingénierie. Un PRD bien structuré = code bien structuré.

## Sources

- [Niche types for design studios - Thijs Kraan](https://www.linkedin.com/posts/thijskraan_7-niche-types-for-design-studios-to-build-share-7422277698011611136-XuWF)
- [GenAI Agents Vibe Coding - Renaud Chevalier](https://www.linkedin.com/posts/renaud-chevalier_genai-agents-vibecoding-activity-7407801308331536386-9Uqp)

---

## Description

> *Structurez vos spécifications avec une rigueur d'architecte pour un code sans surprise.*

"Ah, on n'avait pas pensé à ce cas." Combien de fois ? Ce challenge vous fait développer une méthode rigoureuse de décomposition : objets métiers, relations, contraintes, edge cases.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Modèle d'objets métiers complet pour une feature
- [ ] Diagramme de relations avec cardinalités
- [ ] Catalogue d'edge cases anticipés

**Critères de réussite :**

- Modèle traduit directement en schema DB
- Zéro cas non prévu à la review
- Code généré fidèle au modèle

---

## Pistes de Solution

### La méthode de décomposition

```
1. IDENTIFIER LES OBJETS
   "De quoi parle-t-on ?"
   → Noms = objets (User, Order, Product)

2. DÉFINIR LES ATTRIBUTS
   "Qu'est-ce qui caractérise cet objet ?"
   → Propriétés avec types et contraintes

3. ÉTABLIR LES RELATIONS
   "Comment les objets interagissent ?"
   → Cardinalités (1:1, 1:N, N:M)

4. LISTER LES RÈGLES MÉTIER
   "Qu'est-ce qui doit être vrai ?"
   → Invariants et contraintes

5. ANTICIPER LES EDGE CASES
   "Qu'est-ce qui peut mal tourner ?"
   → Scénarios limites
```

### Prompt de décomposition

```
Je veux implémenter : [FEATURE]

Aide-moi à décomposer en objets métiers :

## Objets identifiés
Pour chaque objet :
- Nom
- Description
- Attributs (nom, type, contraintes, nullable)
- Relations avec autres objets

## Diagramme
Représente les relations avec cardinalités :
User ---[1:N]--- Order ---[N:1]--- Product

## Règles métier
- [Invariant 1]
- [Invariant 2]
- [Contrainte 1]

## Edge cases
- Que se passe-t-il si... ?
- Et si l'utilisateur... ?
- Cas limite : ...

## Schema SQL suggéré
[DDL correspondant]
```

### Template d'objet métier

```markdown
## [NOM DE L'OBJET]

### Description
[1-2 phrases sur ce que représente cet objet]

### Attributs
| Nom | Type | Contraintes | Description |
|-----|------|-------------|-------------|
| id | UUID | PK | Identifiant unique |
| name | VARCHAR(100) | NOT NULL | Nom affiché |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Email de contact |
| status | ENUM | IN ('active', 'inactive') | État actuel |
| created_at | TIMESTAMP | DEFAULT NOW() | Date de création |

### Relations
- **User** : Belongs to (N:1) - Un [Objet] appartient à un User
- **Items** : Has many (1:N) - Un [Objet] contient plusieurs Items

### Règles métier
1. [Règle 1 : quand/condition]
2. [Règle 2 : validation]

### Edge cases
- [ ] Que faire si créé sans items ?
- [ ] Comportement si user supprimé ?
- [ ] Limite de taille/quantité ?
```

### Checklist de complétude

```markdown
## Validation du modèle

### Complétude
- [ ] Tous les objets identifiés
- [ ] Tous les attributs définis
- [ ] Types et contraintes précisés
- [ ] Relations avec cardinalités

### Cohérence
- [ ] Pas de redondance de données
- [ ] Normalisation appropriée
- [ ] Noms cohérents et clairs

### Edge cases
- [ ] Valeurs nulles gérées
- [ ] Limites définies (max, min)
- [ ] Cascade de suppression prévue
- [ ] États invalides impossibles

### Traçabilité
- [ ] Chaque objet lié à un besoin
- [ ] Règles métier sourcées
- [ ] Décisions documentées
```

---

## Animation Dojo (1h30)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Pourquoi structurer avant de coder |
| 15-35 | Démo | Décomposition d'une feature en live |
| 35-65 | Pratique | Chacun décompose sa feature |
| 65-80 | Review | Cross-review des modèles |
| 80-90 | Clôture | De la structure au code |

### Points d'attention

- Pas de code avant structure validée
- Les edge cases sont les vrais pièges
- Un bon modèle se traduit directement en DDL
