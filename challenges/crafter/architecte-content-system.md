# L'Architecte de Content System

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐ |
| XP | 220 |
| Prérequis | Notions de Content Design |

---

## Vision & Impact

Élaborer un système de contenu IA complet pour automatiser la production textuelle tout en gardant une **cohérence absolue**. Les Content Designers peuvent désormais construire leurs propres outils pour démultiplier leur impact.

## Le saviez-vous ?

En 2026, produire du contenu seul ne vaudra plus rien ; c'est la **gouvernance du système** qui comptera. Le Content Designer devient architecte, pas rédacteur.

## Sources

- [Content System IA - CD Henin](https://www.linkedin.com/posts/cdhenin_pour-%C3%A9laborer-votre-content-system-ia-on-activity-7423991067743617024-TbIl)
- [Content Designers can finally build their own tools - Yuval Kesh](https://www.linkedin.com/posts/yuvalkesh_content-designers-can-finally-build-their-share-7416523426137370624-9cE4)

---

## Description

> *Créez un système qui produit du contenu cohérent à l'échelle.*

"Ce texte ne sonne pas comme nous." Combien de fois l'avez-vous entendu ? Ce challenge vous fait construire un Content System : guidelines + prompts + validation = contenu cohérent à l'infini.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Guidelines de contenu documentées
- [ ] Bibliothèque de prompts par type de contenu
- [ ] Workflow de validation automatique

**Critères de réussite :**

- 10 contenus générés passent le test de cohérence
- Temps de production réduit de 70%
- Qualité constante sans intervention humaine

---

## Pistes de Solution

### Architecture du Content System

```
┌─────────────────────────────────────────────────────────┐
│                    CONTENT SYSTEM                        │
├─────────────────┬─────────────────┬─────────────────────┤
│   GUIDELINES    │    PROMPTS      │    VALIDATION       │
│                 │                 │                     │
│ - Tone of Voice │ - Par type      │ - Checklist auto    │
│ - Vocabulaire   │ - Par canal     │ - Score cohérence   │
│ - Do's/Don'ts   │ - Par audience  │ - A/B testing       │
└─────────────────┴─────────────────┴─────────────────────┘
```

### Template de guidelines

```markdown
## Voix de marque

### Personnalité
- [3-5 traits de personnalité]

### Ton selon contexte
- Erreur : [exemple]
- Succès : [exemple]
- Onboarding : [exemple]

### Vocabulaire
| On dit | On ne dit pas |
|--------|---------------|
| ...    | ...           |

### Exemples annotés
[Avant/Après avec explications]
```

### Prompt générique Content System

```
Tu es le Content System de [Marque].

Guidelines :
"""
[INSÉRER GUIDELINES]
"""

Génère : [type de contenu]
Contexte : [situation]
Audience : [cible]

Contraintes :
- Longueur : [X mots/caractères]
- Ton : [spécifier]
- CTA : [objectif]

Après génération, vérifie :
- [ ] Conforme au tone of voice
- [ ] Vocabulaire autorisé uniquement
- [ ] Longueur respectée
```

---

## Animation Dojo (1h30)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Qu'est-ce qu'un Content System |
| 15-35 | Guidelines | Chacun documente ses guidelines |
| 35-55 | Prompts | Créer 3 prompts par type |
| 55-75 | Test | Générer 5 contenus et valider |
| 75-90 | Clôture | Industrialisation |
