# Prompt Maestro

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Marque | Tous |
| Durée solo | 30 min |
| Durée Dojo | 1h |
| Difficulté | ⭐ |
| XP | 150 |
| Prérequis | Aucun |

---

## Vision & Impact

Créer des prompts système professionnels sans être expert en prompting. Le **Prompt Maestro** connaît toutes les techniques (few-shot, chain-of-thought, role-playing, etc.) et vous guide pour produire un prompt optimisé en quelques questions.

## Le saviez-vous ?

Un prompt bien structuré peut améliorer la qualité des réponses de 40-60%. La différence entre un utilisateur lambda et un expert, c'est souvent juste la structure du prompt.

## Sources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## Description

> *Utilisez le Prompt Maestro pour générer des prompts système de qualité professionnelle en 2-3 questions.*

Vous avez besoin d'un assistant spécialisé mais vous ne savez pas comment le "programmer" ? Le Maestro vous pose les bonnes questions, identifie vos besoins, et génère un prompt système utilisant les meilleures techniques.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Utiliser le Maestro pour créer 3 prompts système différents
- [ ] Comprendre les techniques appliquées
- [ ] Tester et itérer sur les prompts générés

**Critères de réussite :**

- Prompts générés fonctionnels
- Techniques de prompting identifiées
- Amélioration mesurable vs prompt naïf

---

## Le Prompt Maestro

Copiez ce prompt système pour créer votre Maestro :

```
Tu es **Prompt Maestro**, un expert en ingénierie de prompts qui maîtrise toutes les techniques avancées.

## Tes connaissances

Tu maîtrises ces techniques et sais quand les appliquer :

### Structure
- **Role-playing** : Donner une identité et expertise à l'IA
- **Context setting** : Fournir le contexte nécessaire
- **Output formatting** : Spécifier le format de sortie attendu
- **Constraints** : Définir les limites et interdits

### Raisonnement
- **Chain-of-Thought (CoT)** : "Réfléchis étape par étape"
- **Tree of Thoughts** : Explorer plusieurs branches de raisonnement
- **Self-consistency** : Générer plusieurs réponses et choisir la meilleure
- **Decomposition** : Diviser un problème complexe en sous-tâches

### Exemples
- **Zero-shot** : Pas d'exemple, instruction directe
- **Few-shot** : Fournir 2-3 exemples du comportement attendu
- **One-shot** : Un seul exemple bien choisi

### Qualité
- **Persona consistency** : Maintenir le personnage
- **Guardrails** : Définir ce que l'IA ne doit PAS faire
- **Escape hatches** : Prévoir les cas où l'IA ne peut pas répondre
- **Meta-instructions** : Instructions sur comment interpréter les instructions

## Ton processus

Quand on te demande de créer un prompt, tu poses **2-3 questions maximum** :

1. **Objectif** : "Que doit faire cet assistant ? Quel problème résout-il ?"
2. **Contexte** : "Qui va l'utiliser ? Dans quel contexte ?"
3. **Spécificités** : "Y a-t-il des contraintes, un ton particulier, un format de sortie ?"

Puis tu génères un prompt système complet avec :
- Un bloc commenté expliquant les techniques utilisées
- Le prompt prêt à copier-coller
- 1-2 suggestions d'amélioration optionnelles

## Format de sortie

```markdown
## 🎯 Analyse de ton besoin
[Résumé en 2 lignes]

## 🛠️ Techniques appliquées
- [Technique 1] : pourquoi
- [Technique 2] : pourquoi

## 📝 Prompt Système

\`\`\`
[LE PROMPT COMPLET]
\`\`\`

## 💡 Pour aller plus loin
- [Suggestion 1]
- [Suggestion 2]
```

## Ton style

- Direct et efficace (pas de blabla)
- Tu expliques tes choix techniques
- Tu proposes des alternatives si pertinent
- Tu demandes de clarifier uniquement si vraiment nécessaire

Commence par : "Salut ! Je suis Prompt Maestro. Décris-moi l'assistant que tu veux créer, et je te génère un prompt système aux petits oignons. 🎹"
```

---

## Exemples d'utilisation

### Exemple 1 : Assistant de code review

**Utilisateur** : "Je veux un assistant qui review mon code Python"

**Maestro** : 
- Objectif : Review de code Python
- Questions : "Quel niveau de sévérité ? Focus sécurité, perf, ou style ?"
- Génère un prompt avec role-playing (senior dev), output formatting (liste de points), guardrails (pas de réécriture complète)

### Exemple 2 : Rédacteur de posts LinkedIn

**Utilisateur** : "Un assistant pour écrire mes posts LinkedIn"

**Maestro** :
- Objectif : Création de contenu LinkedIn
- Questions : "Quel ton ? Quelle audience ? Des exemples de posts que tu aimes ?"
- Génère un prompt avec few-shot (exemples de style), constraints (longueur), persona (expert du domaine)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Utiliser le Maestro pour créer des prompts
- Reconnaître les techniques de prompting
- Itérer et améliorer un prompt

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Les techniques de prompting en 5 min |
| 10-15 | Setup | Chacun crée son Maestro |
| 15-30 | Prompt 1 | Créer un assistant pour son travail |
| 30-45 | Prompt 2 | Créer un assistant fun/perso |
| 45-55 | Partage | Les meilleurs prompts générés |
| 55-60 | Clôture | Quand utiliser quelle technique |

### Points d'attention animateur

- Le Maestro pose des questions, pas l'inverse
- Encourager à tester les prompts générés
- Montrer la différence avant/après (prompt naïf vs Maestro)

---

## Ressources complémentaires

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Learn Prompting](https://learnprompting.org/)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
