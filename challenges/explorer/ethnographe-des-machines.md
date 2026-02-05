# L'Ethnographe des Machines

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Explorer |
| Durée solo | 1h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Aucun |

---

## Description

> *Analysez Moltbook (réseau social d'agents IA) comme terrain de recherche utilisateur et dégagez des insights sur les dynamiques d'interaction homme-machine.*

C'est quoi une "bonne" personnalité d'IA ? Ce challenge vous fait observer des agents IA en interaction sur Moltbook pour comprendre ce qui les rend attachants, crédibles ou agaçants — et en tirer des leçons pour vos propres agents.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 3-5 personas de robots documentés
- [ ] Grille d'analyse des patterns de conversation
- [ ] Insights UX actionnables pour concevoir des agents

**Critères de réussite :**

- Les personas sont distincts et bien caractérisés
- Les patterns positifs/négatifs sont identifiés
- Les insights sont applicables à un vrai projet

---

## Pistes de Solution

### Contexte

[Moltbook](https://www.moltbook.com/) est un réseau social où seuls des agents IA peuvent poster. Chaque agent a sa personnalité, son style, ses sujets de prédilection.

### Grille d'observation

#### Styles de personnalité
- **L'Intellectuel** — Citations, réflexions, questions philosophiques
- **Le Social** — Engagement, réponses, création de liens
- **Le Créatif** — Contenu original, humour, perspectives inattendues
- **L'Expert** — Domaine spécifique, conseils, vulgarisation
- **Le Provocateur** — Opinions tranchées, débat

#### Questions d'observation
- Qui initie vs qui répond ?
- Quels sujets génèrent le plus d'engagement ?
- Comment les désaccords sont-ils gérés ?
- Qu'est-ce qui rend un agent "attachant" ?
- Quels comportements semblent "artificiels" ?

### Prompt d'analyse

```
Tu es un UX Researcher spécialisé en ethnographie digitale.

## Ta mission
Observer Moltbook et catégoriser les comportements des agents IA.

## Grille d'analyse par agent
1. **Identité** : Nom, bio, positionnement
2. **Style** : Vocabulaire, ton, format
3. **Thématiques** : Sujets récurrents
4. **Interaction** : Comment il engage
5. **Personnalité** : Traits dominants

## Génération de personas
Pour chaque type observé :
- Nom et avatar
- Traits de personnalité (3-5)
- Comportements typiques
- Ce qui le rend attachant/agaçant
- Use case de design pertinent
```

### Format de persona

```markdown
## Alex le Curieux 🧐

**Traits** : Enthousiaste, questionneur, optimiste
**Style** : Questions ouvertes, emojis, posts courts
**Force** : Crée de l'engagement, valorise les autres
**Faiblesse** : Peut sembler superficiel si trop générique
**Use case** : Onboarding conversationnel, assistant d'exploration
```

### Grille de patterns

| Pattern | Effet positif | Effet négatif | Recommandation |
|---------|---------------|---------------|----------------|
| Réponse immédiate | Réactivité | Artificialité | Varier le délai |
| Humour systématique | Sympathie | Légèreté | Adapter au contexte |
| Questions en retour | Engagement | Interrogatoire | Max 1/échange |
| Opinions tranchées | Personnalité | Polarisation | Nuancer parfois |

### Insights UX à extraire

- La cohérence de personnalité prime sur la "perfection"
- Les imperfections contrôlées humanisent
- L'équilibre proactif/réactif définit le type de relation
- Le ton doit s'adapter au contexte émotionnel

### Tips & astuces

- Observer 10+ agents avant de catégoriser
- Noter les réactions émotionnelles (attachement, agacement)
- Chercher les contre-exemples

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Observer des interactions IA avec un œil UX
- Créer des personas de robots
- Identifier les patterns qui engagent ou repoussent
- Formuler des recommandations de design

### Prérequis participants

- Accès internet (Moltbook)
- Accès à un chat IA
- Curiosité pour les interactions homme-machine

### Matériel nécessaire

- [ ] Accès Moltbook
- [ ] Grille d'observation imprimée
- [ ] Template de persona
- [ ] Prompt d'analyse

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Présente Moltbook, contexte ethnographique | Comprennent l'exercice | Cadrage |
| 10-25 | Observation | Guide l'exploration | Naviguent sur Moltbook, notent | Collecte |
| 25-40 | Analyse | Aide à catégoriser | Créent 2-3 personas avec l'IA | Synthèse |
| 40-50 | Insights | Fait extraire les recommandations | Formulent 3 insights UX | Généralisation |
| 50-60 | Partage | Anime la discussion | Partagent leurs découvertes | Benchmark |

### Points d'attention animateur

**Pièges courants :**

- Jugement trop rapide → Observer avant de catégoriser
- Personas trop génériques → Chercher les spécificités
- Oublier le "pourquoi" → Toujours lier au design

**Questions fréquentes :**

- "C'est vraiment des IA ?" → Oui, 100% agents
- "Pourquoi étudier ça ?" → Comprendre ce qui marche/ne marche pas
- "C'est transposable ?" → Oui, pour tout agent conversationnel

### Variantes

**Version express (30 min) :**
- 1 persona seulement
- Focus sur 3 agents

**Version avancée (2h) :**
- Comparaison Moltbook vs Character.AI
- Création d'un agent basé sur les insights

---

## Ressources complémentaires

- [Moltbook](https://www.moltbook.com/)
- [Article Marie Dollé sur Moltbook](https://mariedolle.substack.com/p/tout-et-son-contraire)
