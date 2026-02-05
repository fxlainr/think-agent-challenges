# La BD dont vous êtes le PO

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Accès à un outil de génération d'images (Midjourney, DALL-E) |

---

## Description

> *Transformez vos entretiens utilisateurs ou workflows abstraits en storyboards visuels impactants pour vos présentations.*

"Une image vaut mille mots" — surtout pour un COMEX. Ce challenge vous apprend à transformer un verbatim utilisateur ou un workflow complexe en BD visuelle. Parfait pour les présentations, les specs ou les workshops.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Storyboard de 6-10 planches illustrées
- [ ] Fidèle au verbatim/workflow source
- [ ] Visuellement cohérent et présentable

**Critères de réussite :**

- Chaque scène a un contexte, une action, une émotion
- Les bulles de dialogue capturent l'essentiel
- Le storyboard est compréhensible sans explication

---

## Pistes de Solution

### Quand utiliser cette approche

| Contexte | Usage |
|----------|-------|
| User research | Illustrer des verbatims |
| Workshop cadrage | Visualiser un parcours client |
| Présentation COMEX | Rendre concret un concept abstrait |
| Spécifications | Clarifier un workflow complexe |

### Étape 1 : Découper en scènes

**Prompt :**
```
Analyse ce verbatim et découpe-le en 6-8 scènes pour un storyboard.

Pour chaque scène, décris :
- Le contexte visuel (où, quand)
- Les personnages présents
- L'action principale
- L'émotion dominante
- Le dialogue/pensée clé (bulle)

Verbatim :
[Coller l'entretien]
```

### Étape 2 : Générer les images

**Prompt Midjourney/DALL-E :**
```
[Style] clean line illustration, simple, business context

Scene: [Description]
Characters: [Description]
Action: [Ce qui se passe]
Mood: [Émotion]

--ar 16:9 --style raw
```

**Styles recommandés :**
- `clean line illustration` — Pro, épuré
- `comic book style` — Dynamique
- `storyboard sketch` — Brouillon volontaire
- `flat design illustration` — Corporate

### Étape 3 : Assembler

1. Créer un frame par planche (ex: 1920x1080)
2. Grille 2x3 ou 3x2 pour 6 cases
3. Ajouter les images générées
4. Ajouter les bulles de dialogue
5. Numéroter les cases

### Exemple : Parcours demande de congés

**Verbatim :**
"Quand je veux poser mes congés, je vérifie le planning, je remplis un formulaire papier, je cherche mon manager qui n'est jamais là, je scanne, j'envoie aux RH..."

**Découpage :**

| # | Scène | Émotion | Bulle |
|---|-------|---------|-------|
| 1 | Marie devant le planning mural | Concentration | "Voyons voir..." |
| 2 | Marie remplit un formulaire | Ennui | "Encore ce formulaire..." |
| 3 | Bureau vide du manager | Frustration | "Pas encore là !" |
| 4 | Marie laisse le doc sur le bureau | Résignation | "Je reviendrai..." |
| 5 | Marie au scanner | Lassitude | "Bientôt fini..." |
| 6 | Marie envoie un email | Soulagement | "Enfin !" |

### Tips & astuces

- Garder un style visuel cohérent (même prompt de style)
- Les émotions doivent être lisibles sur les visages
- Moins de texte dans les bulles = plus d'impact

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Découper un verbatim en scènes visuelles
- Générer des images cohérentes avec l'IA
- Assembler un storyboard présentable
- Utiliser le format pour communiquer efficacement

### Prérequis participants

- Accès à Midjourney, DALL-E ou Canva
- Un verbatim ou workflow à illustrer
- Figma ou outil de mise en page basique

### Matériel nécessaire

- [ ] Prompt de découpage en scènes
- [ ] Prompts de génération d'images par style
- [ ] Template Figma de storyboard
- [ ] Exemples de storyboards UX réussis

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-10 | Intro | Montre des exemples de storyboards UX | Découvrent le format | Inspiration |
| 10-20 | Découpage | Guide le prompt de découpage | Découpent leur verbatim en scènes | Structure |
| 20-40 | Génération | Montre les différents styles | Génèrent leurs images | Production |
| 40-55 | Assemblage | Aide sur Figma/Canva | Assemblent leur storyboard | Finalisation |
| 55-60 | Galerie | Fait défiler les créations | Admirent et commentent | Valorisation |

### Points d'attention animateur

**Pièges courants :**

- Trop de scènes → 6-8 max pour rester lisible
- Style incohérent → Garder le même prompt de style
- Bulles trop longues → Max 10 mots par bulle

**Questions fréquentes :**

- "Pas d'accès à Midjourney ?" → Canva, Excalidraw, stock photos
- "Ça prend combien de temps en vrai ?" → 30-45 min une fois rodé
- "C'est utilisable en prez client ?" → Oui, très impactant

### Alternatives sans génération d'images

- **Canva** : Templates de storyboard + illustrations stock
- **Excalidraw** : Dessins rapides style whiteboard
- **Stock photos** : Unsplash + montage

### Variantes

**Version rapide (30 min) :**
- 4 scènes seulement
- Un seul style imposé
- Pas d'assemblage Figma

**Version avancée (2h) :**
- Storyboard animé (Figma prototype)
- Plusieurs parcours comparés
- Présentation narrative

---

## Ressources complémentaires

- [Storyboarding in UX Design](https://www.nngroup.com/articles/storyboards-visualize-ideas/)
- [Midjourney Documentation](https://docs.midjourney.com/)
