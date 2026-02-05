# Les Basiques du Prompting

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 30 min |
| Durée Dojo | 1h |
| Difficulté | ⭐ |
| Prérequis | Aucun |

---

## Description

> *Maîtrisez les 6 patterns fondamentaux du prompting pour décupler l'efficacité de vos interactions avec l'IA.*

Avant de construire des solutions IA complexes, il faut maîtriser les bases. Ce challenge vous fait découvrir les patterns de prompting essentiels : zero-shot, few-shot, chain-of-thought, persona, output formatting et délimiteurs. À la fin, vous saurez instinctivement quel pattern utiliser selon la situation.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Compléter un quiz de 20 questions sur les patterns de prompting
- [ ] Score minimum de 80% au quiz
- [ ] Réécrire 3 prompts en appliquant les patterns appropriés

**Critères de réussite :**

- Identifier correctement les 6 patterns fondamentaux
- Choisir le bon pattern selon le contexte
- Améliorer un prompt existant avec le pattern adapté

---

## Pistes de Solution

### Les 6 patterns fondamentaux

#### 1. Zero-Shot Prompting
Demander directement sans exemple.
```
Traduis ce texte en anglais : "Bonjour, comment allez-vous ?"
```

#### 2. Few-Shot Prompting
Donner des exemples avant la tâche.
```
Classifie le sentiment de ces phrases :
"J'adore ce produit" → Positif
"C'est une catastrophe" → Négatif
"Le colis est arrivé" → Neutre

Maintenant, classifie : "Ce service est exceptionnel" → ?
```

#### 3. Chain-of-Thought (CoT)
Demander de raisonner étape par étape.
```
Résous ce problème étape par étape :
Marie a 3 pommes. Elle en donne 1 à Paul, puis en achète 4 de plus. Combien en a-t-elle ?
```

#### 4. Persona/Role Prompting
Assigner un rôle à l'IA.
```
Tu es un expert en marketing digital avec 15 ans d'expérience. Analyse cette stratégie...
```

#### 5. Output Formatting
Spécifier le format de sortie.
```
Génère une liste de 5 idées au format JSON avec les champs : titre, description, difficulté.
```

#### 6. Délimiteurs
Utiliser des séparateurs clairs.
```
Résume le texte suivant :
---
[Texte à résumer]
---
Format : 3 bullet points maximum.
```

### Quiz de validation (extraits)

**Section 1 : Identification des patterns**
1. Quel pattern utilise des exemples avant la tâche ? → Few-shot
2. "Raisonne étape par étape" fait référence à ? → Chain-of-Thought
3. "Tu es un avocat spécialisé..." est un exemple de ? → Persona

**Section 2 : Application**
4. Pour une tâche simple et bien définie, quel pattern suffit ? → Zero-shot
5. Pour améliorer la précision sur une tâche complexe ? → Few-shot + CoT
6. Pour obtenir une sortie structurée ? → Output formatting

### Tips & astuces

- Il n'y a pas de pattern "meilleur" — c'est toujours contextuel
- On peut combiner les patterns (ex: Persona + Few-shot + Output formatting)
- En cas de doute, commencer simple (zero-shot) puis itérer

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Reconnaître les 6 patterns fondamentaux de prompting
- Choisir le bon pattern selon la tâche à accomplir
- Améliorer leurs prompts existants avec les patterns appropriés

### Prérequis participants

- Aucun prérequis technique
- Accès à un chat IA (ChatGPT, Claude, Mistral...)

### Matériel nécessaire

- [ ] Slides de présentation des 6 patterns
- [ ] Quiz interactif (Kahoot, Mentimeter ou similaire)
- [ ] Exemples de prompts "avant/après" à projeter
- [ ] Fiche récap des patterns (1 page) à distribuer

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro patterns | Présente les 6 patterns avec exemples concrets | Écoutent, posent questions | Découverte |
| 10-20 | Quiz interactif | Anime le quiz en temps réel | Répondent aux questions | Validation des acquis |
| 20-40 | Exercices pratiques | Distribue 3 prompts à améliorer, circule pour aider | Réécrivent les prompts avec les bons patterns | Mise en pratique |
| 40-55 | Partage | Fait présenter les avant/après, commente | Présentent leurs améliorations | Apprentissage par les pairs |
| 55-60 | Clôture | Récapitule les 6 patterns, distribue la fiche | Notent les points clés | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- Vouloir utiliser le pattern "le plus avancé" → Rappeler que simple = souvent mieux
- Confondre few-shot et exemples dans la réponse → Clarifier la différence
- Oublier les délimiteurs sur les textes longs → Montrer l'impact sur la qualité

**Questions fréquentes :**

- "Quel est le meilleur pattern ?" → Ça dépend du contexte, il n'y a pas de réponse universelle
- "On peut les combiner ?" → Oui, et c'est souvent la clé des prompts efficaces
- "Chain-of-thought marche toujours ?" → Non, parfois ça ralentit pour rien sur des tâches simples

**Tips d'animation :**

- Utiliser des exemples issus du quotidien des participants
- Faire deviner le pattern utilisé dans des prompts célèbres
- Montrer des échecs de prompts et faire diagnostiquer le problème

### Variantes

**Version courte (30 min) :**
- Quiz uniquement (pas d'exercices pratiques)
- Focus sur les 3 patterns les plus utiles (few-shot, persona, CoT)

**Version longue (2h) :**
- Ajouter des exercices sur des cas réels des participants
- Inclure une partie "prompt debugging" 
- Créer un mini-catalogue de prompts optimisés par métier

---

## Ressources complémentaires

- [Guide Anthropic sur le prompting](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
