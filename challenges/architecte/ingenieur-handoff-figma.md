# L'Ingénieur du Handoff (Figma Sync)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | FLOW |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐ |
| XP | 280 |
| Prérequis | Figma, React/Tailwind, Claude Code ou Cursor |

---

## Vision & Impact

Connecter Figma et Claude via des connecteurs spécialisés pour traduire les maquettes en code **Pixel Perfect**. Le design devient la source de vérité directe pour le développement.

## Le saviez-vous ?

Savoir **décomposer son intention** est la compétence clé pour réussir ce passage fluide de la forme au code. Le meilleur prompt, c'est une maquette bien structurée.

## Sources

- [Figma to Code workflow - Nashmil Mobasseri](https://www.linkedin.com/posts/nashmil-mobasseri_ugcPost-7421961687370596352-Z7aR)
- [My Pixel Perfect Workflow - Miha Ezhov](https://www.linkedin.com/posts/miha-ezhov_my-pixel-perfect-workflow-figma-cursor-activity-7420194040740118528-fdLO)

---

## Description

> *Transformez vos maquettes Figma en code pixel-perfect automatiquement.*

Le handoff designer → dev, c'est souvent 50% de l'effort de développement. "C'est pas aligné", "Il manque 2px", "Le hover c'était quoi déjà ?"... Ce challenge vous fait créer un workflow où Figma génère directement du code utilisable.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Workflow Figma → Code fonctionnel
- [ ] 3 composants convertis en pixel-perfect
- [ ] Documentation du process

**Critères de réussite :**

- Différence visuelle < 2px avec la maquette
- Code propre et maintenable
- Workflow réutilisable

---

## Pistes de Solution

### Architecture du workflow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Figma     │───▶│  Export     │───▶│   Claude    │───▶│   Code      │
│   Design    │    │  (Plugin)   │    │   Code      │    │   Review    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Méthode 1 : Screenshot + Description

```
Voici une capture de mon design Figma.

Génère le code React + Tailwind pour ce composant.

Spécifications :
- Dimensions exactes : [lire dans Figma]
- Couleurs : [copier les hex codes]
- Espacements : [relever les paddings/margins]
- Typo : [font-family, sizes, weights]

Contraintes :
- Responsive (breakpoints : sm, md, lg)
- Dark mode support
- États hover/active
```

### Méthode 2 : Figma Plugin Export

Plugins recommandés :
- **Figma to Code** : Export direct en Tailwind
- **Locofy** : Conversion automatique
- **Anima** : Export React/Vue

### Méthode 3 : Figma Dev Mode + Claude

```
1. Activer Dev Mode dans Figma
2. Copier le CSS généré
3. Envoyer à Claude pour conversion Tailwind
4. Itérer sur les ajustements
```

### Prompt de conversion

```
Convertis ce CSS Figma en composant React + Tailwind :

CSS Figma :
"""
[COLLER LE CSS]
"""

Structure du composant :
- [Décrire la hiérarchie des éléments]

Assets :
- Icônes : [lucide-react / heroicons]
- Images : [placeholder ou URL]

Génère :
1. Le composant React complet
2. Les variants si applicable (size, color, state)
3. Les props TypeScript
```

### Checklist Pixel Perfect

```markdown
## Vérification Pixel Perfect

### Dimensions
- [ ] Width/Height corrects
- [ ] Padding interne exact
- [ ] Margin externe exact

### Typographie
- [ ] Font family correcte
- [ ] Font size exact
- [ ] Line height correct
- [ ] Letter spacing si spécifié

### Couleurs
- [ ] Background color
- [ ] Text color
- [ ] Border color
- [ ] Shadow color et blur

### Layout
- [ ] Alignement (flex, grid)
- [ ] Gap entre éléments
- [ ] Ordre des éléments

### États
- [ ] Hover
- [ ] Active/Pressed
- [ ] Focus
- [ ] Disabled
```

### Les 3 composants à convertir

**1. Card complexe**
- Image, titre, description, tags, CTA
- Multiple états (default, hover, selected)

**2. Form avec validation**
- Inputs, labels, error states
- Responsive layout

**3. Navigation**
- Desktop (horizontal) + Mobile (hamburger)
- Active states, dropdowns

---

## Animation Dojo (2h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Exporter efficacement depuis Figma
- Convertir en code pixel-perfect
- Vérifier et ajuster le résultat

### Prérequis

- Figma avec un design prêt
- Environnement React/Tailwind

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Le coût du handoff traditionnel |
| 10-25 | Démo | Conversion d'une card en live |
| 25-50 | Composant 1 | Chacun convertit une card |
| 50-75 | Composant 2 | Form avec validation |
| 75-100 | Composant 3 | Navigation responsive |
| 100-115 | Revue | Pixel-perfect check |
| 115-120 | Clôture | Industrialiser le workflow |

### Points d'attention animateur

- Avoir des designs Figma prêts à convertir
- Montrer les DevTools pour comparer
- Insister sur la structure Figma (bien nommer les layers)

---

## Ressources complémentaires

- [Figma Dev Mode](https://www.figma.com/dev-mode/)
- [Figma to Code Plugin](https://www.figma.com/community/plugin/738792275227324584)
