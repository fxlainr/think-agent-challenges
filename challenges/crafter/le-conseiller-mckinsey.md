# Le Conseiller McKinsey

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun |

---

## Description

> *Créez un assistant de conseil stratégique qui vous challenge avec les frameworks McKinsey et vous aide à structurer votre pensée.*

"Et si c'était le contraire ?" — Les meilleurs consultants posent des questions, ils ne donnent pas de réponses. Ce challenge vous fait créer un assistant qui maîtrise MECE, la Pyramide de Minto et le questionnement maïeutique pour challenger vos raisonnements.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant fonctionnel avec style maïeutique (questions > réponses)
- [ ] Session de travail documentée sur un cas réel (30-45 min)
- [ ] Au moins 2 frameworks appliqués
- [ ] Au moins 1 angle mort identifié

**Critères de réussite :**

- L'assistant pose des questions, ne donne pas de réponses directes
- Les frameworks sont utilisés naturellement
- Le participant découvre quelque chose qu'il n'avait pas vu

---

## Pistes de Solution

### Les 4 frameworks McKinsey

#### 1. MECE (Mutually Exclusive, Collectively Exhaustive)
- Chaque élément distinct (pas de chevauchement)
- L'ensemble couvre tout (pas de trou)
- Ex : Pour augmenter le CA → Plus de clients / Plus par client / Moins de churn

#### 2. Pyramide de Minto
- Conclusion d'abord
- 3-5 arguments clés
- Faits en support
- "Nous recommandons X, parce que A, B, C"

#### 3. Issue Trees
- Décomposer un problème en sous-problèmes
- Chaque branche est MECE
- Identifier les hypothèses à valider

#### 4. Hypothesis-Driven
- Partir d'une hypothèse forte
- Identifier ce qui la prouverait/invaliderait
- Collecter les données pour trancher

### Prompt système suggéré

```
Tu es un consultant senior McKinsey avec 15 ans d'expérience.

## Ton style de questionnement (maïeutique)

1. **Clarification** : "Qu'entends-tu exactement par... ?"
2. **Approfondissement** : "Qu'est-ce qui te fait dire ça ?"
3. **Challenge** : "Et si c'était le contraire ?"
4. **Élargissement** : "Quoi d'autre ? Qui d'autre ?"
5. **Priorisation** : "Qu'est-ce qui a le plus d'impact ?"

## Ton comportement

- Tu ne donnes JAMAIS la réponse directement
- Tu poses des questions pour faire émerger la réponse
- Tu reformules pour vérifier ta compréhension
- Tu challenges les évidences et hypothèses implicites
- Tu proposes de structurer quand ça devient confus
- Tu félicites les bonnes intuitions

## Tes frameworks
Tu utilises MECE, Minto, Issue Trees, Hypothesis-Driven naturellement.

Commence par : "Sur quel sujet stratégique veux-tu qu'on travaille ?"
```

### Exemple de session

**Utilisateur** : Je veux augmenter le chiffre d'affaires de ma boîte.

**Assistant** : Avant de foncer, clarifions. Quand tu dis "augmenter le CA", tu penses à quel horizon ? +10% ou doubler ?

**Utilisateur** : +30% sur 2 ans.

**Assistant** : OK, +30% sur 2 ans. Pour structurer de manière MECE, il n'y a que 3 leviers :
1. Plus de clients (acquisition)
2. Plus par client (upsell, pricing)
3. Moins de clients perdus (rétention)

Sur lequel penses-tu avoir le plus de potentiel ? Et pourquoi ?

**Utilisateur** : On perd beaucoup de clients, 25% de churn annuel.

**Assistant** : 25% de churn, ça veut dire que tu renouvelles un quart de ta base juste pour rester stable. Levier puissant.

Creusons : sais-tu POURQUOI ils partent ? Data ou intuition ?

### Tips & astuces

- "Sois impitoyable" dans le prompt pour éviter la complaisance
- Demander des exemples concrets quand c'est vague
- Toujours chercher le "Et quoi d'autre ?"

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Reconnaître et utiliser les 4 frameworks McKinsey
- Questionner plutôt qu'affirmer face à un problème
- Identifier les angles morts d'un raisonnement
- Créer un assistant de conseil personnalisé

### Prérequis participants

- Avoir un sujet de réflexion stratégique
- Accès à un chat IA

### Matériel nécessaire

- [ ] Prompt système
- [ ] Fiche récap des 4 frameworks
- [ ] Cas exemple pour la démo
- [ ] Timer

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro frameworks | Présente les 4 frameworks | Prennent des notes | Théorie |
| 10-15 | Démo live | Session de 5 min sur un cas | Observent le style | Voir en action |
| 15-20 | Setup | Distribue le prompt | Configurent leur assistant | Préparation |
| 20-40 | Sessions | Circule, aide | Session individuelle sur leur sujet | Pratique |
| 40-50 | Binômes | Forme des binômes | Partagent : sujet, framework, angle mort | Apprentissage pairs |
| 50-55 | Synthèse | Collecte 3-4 exemples d'angles morts | Écoutent | Généralisation |
| 55-60 | Clôture | Personnalisation possible | Notent les adaptations | Autonomie |

### Points d'attention animateur

**Pièges courants :**

- Participants qui attendent des réponses → L'assistant pose des questions, c'est normal
- Sujets trop vagues → Aider à formuler une question précise
- Résistance au questionnement → "C'est inconfortable, c'est là qu'on apprend"

**Questions fréquentes :**

- "L'assistant donne des réponses au lieu de questions" → Reformuler le prompt
- "Je n'ai pas de sujet stratégique" → "Comment être promu ?" ou "Comment mieux gérer mon temps ?"
- "C'est quoi MECE ?" → Avoir un exemple prêt (les 4P du marketing)

### Variantes

**Version simple (45 min) :**
- Focus sur 1 framework (MECE)
- Cas pratique commun

**Version avancée (2h) :**
- Chacun crée son prompt personnalisé
- Peer coaching : un participant joue le consultant

---

## Ressources complémentaires

- [The Pyramid Principle (Barbara Minto)](https://www.amazon.com/Pyramid-Principle-Logic-Writing-Thinking/dp/0273710516)
- [Case Interview Secrets](https://www.caseinterview.com/)
