# L'Artisan du Détail (Animated UI)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐ |
| XP | 170 |
| Prérequis | Notions de CSS/React, Figma |

---

## Vision & Impact

Créer des micro-interactions complexes, comme des boutons dynamiques entièrement animés, en utilisant le codage assisté par IA. Cela apporte la touche de qualité **"Lovable"** nécessaire pour se différencier.

## Le saviez-vous ?

Le "Vibe Design" permet aux designers de diriger des animations complexes sans maîtriser parfaitement le code source. L'intention visuelle suffit.

## Sources

- [I just created an entire animated button - Vannarot Roeung](https://www.linkedin.com/posts/vannarot-roeung-868679341_i-just-created-an-entire-animated-button-ugcPost-7400417481502248960-PtFi)

---

## Description

> *Créez des micro-interactions et animations UI de qualité professionnelle avec l'IA.*

Un bouton qui fait "click". Boring. Un bouton avec un feedback haptique visuel, une animation de ripple, un état de loading élégant ? Ça, c'est du craft. Ce challenge vous fait créer des composants animés dignes des meilleures apps.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 3 composants animés (bouton, card, loader)
- [ ] Animations fluides (60fps, easing approprié)
- [ ] Code réutilisable et documenté

**Critères de réussite :**

- Animations à 60fps sans saccade
- Easing naturel (pas de linear)
- Code propre et maintenable

---

## Pistes de Solution

### Les principes d'animation UI

```
1. DURÉE : 150-300ms pour les micro-interactions
2. EASING : ease-out pour les entrées, ease-in pour les sorties
3. PROPRIÉTÉS : transform et opacity uniquement (GPU accelerated)
4. FEEDBACK : L'utilisateur doit sentir que son action a été prise en compte
```

### Prompt pour générer des animations

```
Crée un composant React/Tailwind avec ces animations :

Composant : [Button / Card / Modal / Toast]
Framework : React + Tailwind CSS + Framer Motion

Comportement souhaité :
- État idle : [description]
- État hover : [description]
- État active/pressed : [description]
- État loading : [description]
- État disabled : [description]

Contraintes :
- Animation < 300ms
- GPU accelerated (transform, opacity only)
- Accessible (prefers-reduced-motion)
- Mobile-friendly (touch feedback)

Génère le code complet avec les variants Framer Motion.
```

### Exemple : Bouton Premium

```jsx
// Prompt envoyé à Claude :
"Crée un bouton React avec Framer Motion qui a :
- Un gradient animé au hover (shimmer effect)
- Un effet de press (scale 0.98)
- Un loader intégré avec spinner
- Un ripple effect au click
- Support de prefers-reduced-motion"
```

### Composants à créer

**1. Bouton avec états multiples**
- Idle → Hover → Active → Loading → Success/Error

**2. Card avec reveal**
- Apparition avec stagger sur les éléments internes
- Hover avec élévation et highlight

**3. Loader créatif**
- Pas un spinner basique
- Animation qui raconte une histoire

### Tips Framer Motion

```jsx
// Variants réutilisables
const buttonVariants = {
  idle: { scale: 1 },
  hover: { scale: 1.02, transition: { duration: 0.2 } },
  tap: { scale: 0.98 },
  loading: { opacity: 0.7 }
};

// Respecter reduced motion
const prefersReducedMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)'
).matches;
```

### Workflow recommandé

1. **Décrire** l'animation en mots
2. **Générer** le code avec l'IA
3. **Tester** dans le browser
4. **Itérer** sur le timing et l'easing
5. **Documenter** les variants

---

## Animation Dojo (1h30, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Décrire une animation en termes techniques
- Générer du code d'animation avec l'IA
- Appliquer les principes d'animation UI

### Prérequis

- Environnement React fonctionnel (ou CodeSandbox)
- Framer Motion installé

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Les 12 principes de Disney appliqués à l'UI |
| 10-20 | Démo | Création d'un bouton animé en live |
| 20-35 | Composant 1 | Chacun crée son bouton |
| 35-50 | Composant 2 | Card avec animations |
| 50-65 | Composant 3 | Loader créatif |
| 65-80 | Showcase | Présentation des créations |
| 80-90 | Clôture | Intégration dans un Design System |

### Points d'attention animateur

- Avoir un environnement prêt à l'emploi
- Montrer les DevTools pour mesurer les FPS
- Insister sur l'accessibilité (reduced motion)

---

## Ressources complémentaires

- [Framer Motion Documentation](https://www.framer.com/motion/)
- [UI Animation Principles](https://material.io/design/motion/understanding-motion.html)
- [Easings.net](https://easings.net/) - Visualiser les courbes d'easing
