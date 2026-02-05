# Le Cloneur de Patterns (Mobbin Reference)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐ |
| XP | 210 |
| Prérequis | Compte Mobbin, React/Tailwind |

---

## Vision & Impact

Extraire des références UI haut de gamme depuis Mobbin et utiliser Claude Code pour les convertir instantanément en composants fonctionnels. On ne réinvente plus la roue, on **assemble des briques d'excellence**.

## Le saviez-vous ?

Mobbin est devenu le standard pour alimenter l'IA en références visuelles de haute qualité. Les meilleures startups y puisent leur inspiration quotidiennement.

## Sources

- [Everyone loves Mobbin for UI references - VPZNC](https://www.linkedin.com/posts/vpznc_everyone-loves-mobbin-for-ui-references-ugcPost-7421901270732431360-XyWo)

---

## Description

> *Transformez les meilleures références Mobbin en composants prêts à l'emploi.*

Pourquoi réinventer un onboarding quand Duolingo l'a perfectionné ? Ce challenge vous fait extraire des patterns UI depuis Mobbin et les convertir en code réutilisable pour vos projets.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 5 patterns extraits de Mobbin
- [ ] 5 composants React correspondants
- [ ] Documentation des adaptations faites

**Critères de réussite :**

- Fidélité au pattern original
- Code propre et réutilisable
- Adaptations documentées

---

## Pistes de Solution

### Workflow Mobbin → Code

```
1. RECHERCHER sur Mobbin (ex: "pricing table")
2. CAPTURER le screenshot
3. ANALYSER les détails (espacements, couleurs)
4. PROMPTER Claude avec le screenshot
5. ITÉRER jusqu'à pixel-perfect
```

### Prompt de conversion Mobbin

```
Voici un screenshot d'un pattern UI de [App] trouvé sur Mobbin.

Reproduis ce composant en React + Tailwind CSS.

Analyse :
1. La structure (hiérarchie des éléments)
2. Les espacements (padding, margin, gap)
3. La typographie (tailles, poids)
4. Les couleurs (extrais les hex codes)
5. Les interactions probables (hover, click)

Génère un composant complet avec :
- Props pour la personnalisation
- États hover/active
- Responsive si pertinent
- Commentaires sur les choix

Adapte légèrement si nécessaire pour notre contexte.
```

### Patterns à collecter

**1. Onboarding (App: Duolingo, Headspace)**
- Carousel de slides
- Progress indicator
- Skip/Continue buttons

**2. Pricing (App: Notion, Linear)**
- Comparison table
- Feature highlights
- CTA hierarchy

**3. Empty States (App: Dropbox, Slack)**
- Illustration + message
- Primary action
- Secondary help

**4. Settings (App: iOS, Spotify)**
- Grouped lists
- Toggle switches
- Navigation patterns

**5. Dashboard Cards (App: Stripe, Vercel)**
- Metric display
- Sparklines/trends
- Action buttons

### Adapter vs Copier

```markdown
## Ce qu'on garde
- La structure générale
- L'espacement et le rythme
- Les patterns d'interaction

## Ce qu'on adapte
- Les couleurs (notre palette)
- La typographie (notre système)
- Les textes (notre contexte)
- Les icônes (notre library)

## Ce qu'on documente
- Source originale
- Adaptations faites
- Raisons des changements
```

### Organiser sa bibliothèque

```
/components
  /patterns
    /onboarding
      OnboardingCarousel.tsx
      README.md (source Mobbin, adaptations)
    /pricing
      PricingTable.tsx
      README.md
    /empty-states
      EmptyState.tsx
      README.md
```

---

## Animation Dojo (1h30, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Rechercher efficacement sur Mobbin
- Convertir un pattern en code
- Adapter sans dénaturer

### Prérequis

- Compte Mobbin (gratuit)
- Environnement React/Tailwind

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Mobbin comme source de vérité UI |
| 10-20 | Démo | Conversion d'un pricing en live |
| 20-35 | Pattern 1 | Chacun convertit un pattern choisi |
| 35-50 | Pattern 2 | Deuxième pattern |
| 50-70 | Revue | Comparaison original vs créé |
| 70-85 | Discussion | Quand adapter, quand innover |
| 85-90 | Clôture | Organiser sa pattern library |

### Points d'attention animateur

- Encourager la fidélité avant la créativité
- Montrer les DevTools pour mesurer
- Discuter des licences et éthique du "clonage"

---

## Ressources complémentaires

- [Mobbin](https://mobbin.com/)
- [UI Patterns](https://ui-patterns.com/)
- [Page Collective](https://pagecollective.com/)
