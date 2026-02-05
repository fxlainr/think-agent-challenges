# La Boucle Ralph Wiggum

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 30 min |
| Durée Dojo | 1h |
| Difficulté | ⭐ |
| Prérequis | Les Basiques du Prompting |

---

## Description

> *Maîtrisez l'auto-correction itérative : apprenez à faire critiquer et améliorer ses propres réponses par l'IA en plusieurs passes.*

Première réponse de l'IA = brouillon. Ce challenge vous apprend à forcer l'IA à évaluer son propre travail et l'améliorer, créant une boucle de qualité. Résultat : des outputs significativement meilleurs sans effort supplémentaire de votre part.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Un prompt avec boucle de feedback intégrée
- [ ] Comparaison V1 vs V2 montrant une amélioration mesurable
- [ ] Au moins 2 itérations critique/amélioration

**Critères de réussite :**

- La V2 est objectivement meilleure que la V1
- L'amélioration est quantifiable (score, critères)
- Le pattern est réutilisable sur d'autres cas

---

## Pistes de Solution

### Le concept

```
Génération → Critique → Amélioration → Critique → Amélioration
    ↑                                                    │
    └────────────────────────────────────────────────────┘
```

### Méthode 1 : Prompt en une seule passe

```
Tu vas répondre à cette demande en 3 étapes :

## ÉTAPE 1 : Première réponse
[Génère ta réponse initiale]

## ÉTAPE 2 : Auto-critique
Analyse ta réponse selon ces critères :
- Clarté (1-10) : Est-ce compréhensible ?
- Complétude (1-10) : Ai-je tout couvert ?
- Exactitude (1-10) : Y a-t-il des erreurs ?
- Style (1-10) : Le ton est-il approprié ?
Liste les points faibles identifiés.

## ÉTAPE 3 : Version améliorée
Réécris ta réponse en corrigeant les faiblesses identifiées.

---
DEMANDE : [La demande originale]
```

### Méthode 2 : Multi-tours

**Tour 1 - Génération :**
```
[Demande originale]
```

**Tour 2 - Critique :**
```
Évalue ta réponse précédente :
1. Points forts (liste)
2. Points faibles (liste)
3. Ce qui manque
4. Note globale /10

Sois impitoyable dans ta critique.
```

**Tour 3 - Amélioration :**
```
Réécris ta réponse en tenant compte de ta critique.
Focus sur les points faibles identifiés.
```

### Exemple concret

**Demande :** "Explique le machine learning en 3 phrases pour un enfant de 10 ans."

**V1 (brute) :**
"Le machine learning est une branche de l'intelligence artificielle qui permet aux ordinateurs d'apprendre à partir de données. Les algorithmes analysent des patterns pour faire des prédictions. C'est utilisé dans la reconnaissance d'images."

**Critique :**
- Clarté : 5/10 — Trop de jargon (algorithmes, patterns, IA)
- Adaptation : 4/10 — Pas adapté à un enfant de 10 ans
- Points faibles : vocabulaire technique, pas d'exemple concret

**V2 (améliorée) :**
"Le machine learning, c'est quand on apprend à un ordinateur à reconnaître des choses tout seul, comme toi tu as appris à reconnaître un chat d'un chien. On lui montre plein de photos, et petit à petit, il devient meilleur. C'est comme ça que ton téléphone peut reconnaître ton visage !"

**Score : 5/10 → 9/10** ✅

### Tips & astuces

- Demander d'être "impitoyable" dans la critique
- Plus de 3 itérations = rendements décroissants
- Vérifier que la V2 n'a pas régressé sur certains points

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Forcer l'IA à s'auto-évaluer
- Créer des boucles d'amélioration
- Mesurer la progression de qualité
- Appliquer le pattern à différents cas

### Prérequis participants

- Accès à un chat IA
- Avoir fait "Les Basiques du Prompting"

### Matériel nécessaire

- [ ] Exemples de prompts avec/sans boucle
- [ ] Grille d'évaluation (clarté, complétude, style)
- [ ] 3-4 cas d'usage variés à tester
- [ ] Timer visible

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro concept | Pourquoi l'auto-correction améliore la qualité | Comprennent le principe | Motivation |
| 5-15 | Démo live | Montre V1 vs V2 sur un exemple | Observent la différence | Preuve |
| 15-25 | Méthode 1 | Guide le prompt "une passe" | Testent sur leur cas | Pratique |
| 25-40 | Méthode 2 | Guide la méthode multi-tours | Comparent les deux méthodes | Approfondissement |
| 40-50 | Comparaison | Collecte les gains observés | Partagent leurs résultats | Validation |
| 50-60 | Extension | Montre comment automatiser (n8n) | Notent les possibilités | Projection |

### Points d'attention animateur

**Pièges courants :**

- L'IA "trop gentille" dans sa critique → Demander d'être impitoyable
- V2 régresse sur certains points → Faire une comparaison explicite
- Boucle infinie → Limiter à 2-3 itérations

**Questions fréquentes :**

- "Ça marche pour du code ?" → Oui, très efficace pour le debugging
- "C'est pas de la triche ?" → Non, c'est du prompt engineering avancé
- "Combien d'itérations max ?" → 2-3 généralement suffisent

**Tips d'animation :**

- Faire voter "V1 ou V2 ?" en aveugle
- Chronométrer : montrer que ça ne prend que 30s de plus
- Collecter les meilleurs exemples avant/après

### Variantes

**Version courte (30 min) :**
- Méthode 1 uniquement (une passe)
- Un seul cas d'usage commun

**Version avancée (1h30) :**
- Automatisation avec n8n
- Boucle conditionnelle (si score < 8, continuer)
- Application sur des cas complexes (code, rédaction longue)

---

## Ressources complémentaires

- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- Pattern "Chain of Verification" d'Anthropic
