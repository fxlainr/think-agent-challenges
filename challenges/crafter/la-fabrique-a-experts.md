# La Fabrique à Experts

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Compte Google (pour NotebookLM) |

---

## Description

> *Créez une formation pédagogique complète sur un sujet complexe — modules structurés, quiz, synthèses et même un podcast audio généré automatiquement.*

Vulgariser un sujet complexe prend des heures de recherche et de structuration. Avec NotebookLM, vous importez vos sources, structurez une formation en modules progressifs et générez même un podcast audio de synthèse. En 2h, vous avez une formation complète prête à être partagée.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Structure de formation en 5 modules progressifs
- [ ] Contenu pédagogique pour chaque module
- [ ] Quiz d'évaluation (5 questions par module)
- [ ] Podcast audio de synthèse (généré par NotebookLM)

**Critères de réussite :**

- Les modules sont progressifs (du simple au complexe)
- Les concepts sont illustrés par des analogies accessibles
- Le podcast est engageant et synthétique

---

## Pistes de Solution

### Étape 1 : Rassembler les sources

1. **Choisir un sujet** : Complexe mais accessible (ordinateur quantique, IA générative, blockchain...)
2. **Collecter 3-5 sources de qualité** : Wikipedia, conférences, livres blancs
3. **Charger dans NotebookLM** : Créer un notebook, importer les sources

### Étape 2 : Structurer la formation

**Prompt dans NotebookLM :**
```
Analyse toutes les sources et propose une structure de formation en 5 modules pour un débutant complet. Pour chaque module :
- Titre accrocheur
- Objectif pédagogique (ce que l'apprenant saura faire)
- Concepts clés à retenir (3-5 max)
- Durée estimée
- Prérequis (module précédent si applicable)
```

### Étape 3 : Générer le contenu

Pour chaque module :
```
Pour le module [X] sur [titre], génère :
1. Une introduction engageante (2 paragraphes)
2. L'explication des concepts clés avec des analogies simples
3. Un exemple concret du monde réel
4. 3 points à retenir (format bullet)
5. Une transition vers le module suivant
```

### Étape 4 : Créer les quiz

```
Crée un quiz de 5 questions pour le module [X] :
- 3 questions à choix multiple (4 options, 1 bonne)
- 1 question vrai/faux avec explication
- 1 question ouverte de réflexion
Inclus les réponses et explications.
```

### Étape 5 : Générer le podcast

1. Dans NotebookLM → "Audio Overview"
2. Sélectionner le style conversationnel
3. Personnaliser : "Focus sur les concepts clés, ton accessible et engageant"
4. Générer (2-3 min) et télécharger

### Livrable final

```
📁 Formation : [Sujet]
├── 00-introduction.md
├── 01-module-fondamentaux.md
├── 02-module-concepts.md
├── 03-module-applications.md
├── 04-module-enjeux.md
├── 05-module-perspectives.md
├── quiz/
│   ├── quiz-module-01.md
│   └── ...
├── synthese-globale.md
└── podcast-formation.mp3
```

### Exemple : "Ordinateur Quantique pour les Nuls"

**Module 1 : Les bases de la physique quantique**
- Objectif : Comprendre ce qu'est un qubit vs un bit
- Concepts : Superposition, intrication, mesure
- Analogie : "Imaginez une pièce qui est pile ET face en même temps..."

**Module 2 : Comment fonctionne un ordinateur quantique**
- Objectif : Visualiser l'architecture d'un QC
- Concepts : Portes quantiques, cohérence, refroidissement

### Tips & astuces

- Sources de qualité = podcast de qualité
- 3-5 sources max (NotebookLM peut se perdre sinon)
- Cadrer le sujet (pas "l'IA" mais "l'IA générative pour le marketing")

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Utiliser NotebookLM pour synthétiser des sources complexes
- Structurer une formation pédagogique en modules
- Générer un podcast audio automatiquement
- Créer des quiz d'évaluation pertinents

### Prérequis participants

- Compte Google (pour NotebookLM)
- Avoir identifié un sujet (ou en choisir un sur place)
- 2-3 sources sur leur sujet (articles, PDF, liens)

### Matériel nécessaire

- [ ] Accès NotebookLM (notebook.google.com)
- [ ] Écouteurs (pour écouter les podcasts)
- [ ] Template de structure de formation
- [ ] 2-3 sujets avec sources pour les non-préparés

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro & démo | Montre un exemple + extrait de podcast | Découvrent le livrable cible | Vision |
| 5-10 | Setup | Vérifie accès NotebookLM | Créent leur notebook, chargent sources | Préparation |
| 10-15 | Structuration | Guide le premier prompt | Génèrent leur structure | Prompter NotebookLM |
| 15-30 | Génération | Circule, aide | Génèrent 2-3 modules | Production |
| 30-40 | Quiz | Montre le format attendu | Créent le quiz d'un module | Évaluation |
| 40-50 | Podcast | Explique Audio Overview | Génèrent leur podcast | Fonctionnalité clé |
| 50-55 | Écoute | Fait écouter 2-3 extraits | Écoutent, commentent | Valorisation |
| 55-60 | Clôture | Récapitule le workflow | Notent ce qu'ils vont compléter | Ancrage |

### Points d'attention animateur

**Pièges courants :**

- Sources de mauvaise qualité → Podcast médiocre. Insister sur la qualité des inputs
- Trop de sources → NotebookLM peut se perdre (3-5 max)
- Sujet trop large → Cadrer dès le début

**Questions fréquentes :**

- "Le podcast est en anglais" → Vérifier que les sources sont en français
- "La génération prend trop de temps" → Normal (2-5 min)
- "Je n'ai pas de sources" → Proposer un sujet par défaut

**Tips d'animation :**

- Préparer 2-3 sujets avec sources pour les non-préparés
- "Listening party" des meilleurs podcasts à la fin

### Variantes

**Version simple (45 min) :**
- Sources fournies (sujet commun)
- 2 modules + 1 quiz
- Pas de génération podcast (démo seulement)

**Version avancée (2h) :**
- Formation complète 5 modules
- Personnalisation du podcast
- Cross-review des formations

---

## Ressources complémentaires

- [NotebookLM](https://notebooklm.google.com/)
- Guide officiel NotebookLM
