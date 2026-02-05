# Le Protecteur de l'Agence Utilisateur (Ethical AI UX)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | SHIELD |
| Durée solo | 3h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐ |
| XP | 280 |
| Prérequis | Notions UX, réflexion éthique |

---

## Vision & Impact

Concevoir des interfaces IA qui ne sont pas des outils mais des **partenaires de confiance**. Le challenge est d'assurer la transparence et l'agence utilisateur. Il n'y a pas de qualité artisanale sans responsabilité éthique.

## Le saviez-vous ?

La question "Qui est coupable quand l'IA se trompe ?" devient un **critère de design majeur** en 2026. L'utilisateur doit toujours comprendre et contrôler.

## Sources

- [AI UX Human Collaboration - Sinem Aslan](https://www.linkedin.com/posts/sinem-aslan_aiux-humanaicollaboration-responsibleai-activity-7406552914099576833-38xo)

---

## Description

> *Designez des interfaces IA qui respectent l'autonomie et la compréhension de l'utilisateur.*

"L'IA a décidé." Non. L'utilisateur a décidé, assisté par l'IA. Ce challenge vous fait concevoir des interfaces où l'humain reste aux commandes, comprend ce qui se passe, et peut toujours dire non.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Audit éthique d'une interface IA existante
- [ ] Redesign avec les principes d'agence utilisateur
- [ ] Checklist éthique réutilisable

**Critères de réussite :**

- Transparence : l'utilisateur comprend les recommandations
- Contrôle : l'utilisateur peut refuser/modifier
- Responsabilité : claire sur qui décide quoi

---

## Pistes de Solution

### Les 5 principes d'agence utilisateur

```
1. TRANSPARENCE
   "Pourquoi l'IA recommande ça ?"
   → Expliquer le raisonnement

2. CONTRÔLE
   "Je peux refuser ou modifier ?"
   → Toujours donner le choix

3. RÉVERSIBILITÉ
   "Je peux revenir en arrière ?"
   → Permettre l'annulation

4. COMPRÉHENSION
   "Je comprends ce qui se passe ?"
   → Pas de magie noire

5. RESPONSABILITÉ
   "Qui est responsable ?"
   → Clarifier humain vs IA
```

### Audit éthique : Questions à poser

```markdown
## Checklist Audit Éthique IA

### Transparence
- [ ] L'utilisateur sait qu'il interagit avec une IA ?
- [ ] Les recommandations sont expliquées ?
- [ ] Les limites de l'IA sont communiquées ?

### Contrôle
- [ ] L'utilisateur peut refuser la recommandation ?
- [ ] Il peut modifier les paramètres de l'IA ?
- [ ] Il peut désactiver l'assistance IA ?

### Réversibilité
- [ ] Les actions IA sont annulables ?
- [ ] Un historique est disponible ?
- [ ] On peut revenir à un état précédent ?

### Compréhension
- [ ] L'interface est compréhensible sans formation ?
- [ ] Les termes utilisés sont accessibles ?
- [ ] Les conséquences des actions sont claires ?

### Responsabilité
- [ ] C'est clair qui décide quoi ?
- [ ] Les erreurs IA sont identifiables ?
- [ ] L'humain peut toujours prendre le contrôle ?

### Biais
- [ ] Les biais potentiels sont documentés ?
- [ ] Des safeguards sont en place ?
- [ ] Un feedback est possible ?
```

### Patterns de design éthique

```
PATTERN 1 : EXPLICATION INLINE
"Recommandé car vous avez aimé X et Y"
→ Transparence sur le "pourquoi"

PATTERN 2 : CONFIDENCE SCORE
"85% de confiance" avec option "voir alternatives"
→ Honnêteté sur l'incertitude

PATTERN 3 : CONTRÔLE GRADUEL
Off → Suggestions → Assistance → Automatique
→ L'utilisateur choisit son niveau

PATTERN 4 : OVERRIDE FACILE
Bouton "Ignorer la suggestion" toujours visible
→ Le contrôle reste à l'humain

PATTERN 5 : FEEDBACK LOOP
"Cette suggestion était-elle utile ?"
→ L'utilisateur améliore le système
```

### Exercice de redesign

```
AVANT (Dark Pattern IA) :
"L'IA a optimisé votre planning"
[OK]

APRÈS (Agence utilisateur) :
"Suggestion d'optimisation de votre planning"
- Réunion A déplacée de 14h à 10h (créneau libre identifié)
- Réunion B raccourcie de 1h à 45min (historique des durées)

Pourquoi ? Basé sur vos préférences : "matinées productives"

[Accepter] [Modifier] [Refuser] [Ne plus suggérer ce type]
```

---

## Animation Dojo (2h)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Pourquoi l'éthique IA est un enjeu UX |
| 15-35 | Audit | Analyser une interface IA avec la checklist |
| 35-65 | Redesign | Corriger les problèmes identifiés |
| 65-95 | Patterns | Créer une bibliothèque de patterns éthiques |
| 95-115 | Débat | Cas limites et dilemmes |
| 115-120 | Clôture | Intégrer l'éthique dans le process |

### Points d'attention

- L'éthique n'est pas un frein, c'est un différenciateur
- Les dark patterns IA sont tentants mais dangereux
- La confiance se construit, se perd en un instant
