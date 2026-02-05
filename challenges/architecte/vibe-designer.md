# Le Vibe Designer (Building live in Claude)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | FLOW |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 320 |
| Prérequis | Design UI/UX, notions de code |

---

## Vision & Impact

Entrer dans l'ère du **"Vibe Design"** en construisant des interfaces en direct dans Claude. Le designer ne dessine plus, il **dirige la création de l'UI par l'intention visuelle**.

## Le saviez-vous ?

Le workflow classique (Double Diamond) est en train de craquer sous la pression de cette vélocité. On passe de semaines à heures pour un prototype haute fidélité.

## Sources

- [MCP Apps are live on Claude - Anton Pidkuiko](https://www.linkedin.com/posts/anton-pidkuiko-7535409b_mcp-apps-are-live-on-claudeai-my-favorite-ugcPost-7421612984097038337-0X6i)
- [Bienvenue dans l'ère du Vibe Design - Maxime Frère](https://www.linkedin.com/posts/maximefrere_bienvenue-dans-l%C3%A8re-du-vibe-design-on-ugcPost-7420370135481294848-7FvE)

---

## Description

> *Construisez des interfaces complètes en conversant avec l'IA, sans ouvrir Figma.*

"Fais-moi un dashboard analytics avec un vibe Apple minimaliste." Et boom, c'est fait. Ce challenge vous fait maîtriser le Vibe Design : la capacité à diriger la création d'interfaces par la description d'intentions plutôt que par le dessin pixel par pixel.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 3 interfaces complètes créées uniquement par conversation
- [ ] Documentation du "langage de vibe" utilisé
- [ ] Comparaison temps Figma vs temps Vibe Design

**Critères de réussite :**

- Interfaces utilisables et esthétiques
- Cohérence visuelle maintenue
- Temps de création < 30 min par interface

---

## Pistes de Solution

### Le vocabulaire du Vibe Design

```
## Mood / Atmosphère
- "Corporate moderne" vs "Startup friendly"
- "Apple minimaliste" vs "Notion fonctionnel"
- "Dark mode premium" vs "Light mode aéré"

## Densité d'information
- "Dashboard data-heavy" vs "Landing épurée"
- "Compact comme Linear" vs "Spacieux comme Notion"

## Énergie
- "Calme et professionnel"
- "Dynamique et playful"
- "Premium et luxueux"

## Références
- "Comme Stripe mais pour [X]"
- "Le love child de Linear et Notion"
- "Si Apple faisait un CRM"
```

### Prompt de Vibe Design

```
Crée une interface [type] avec ce brief :

## Vibe recherché
[Description de l'atmosphère, 2-3 lignes]

## Références visuelles
- [App/site 1] pour [aspect spécifique]
- [App/site 2] pour [aspect spécifique]

## Contenu
- [Liste des éléments à afficher]

## Contraintes
- [Responsive / Dark mode / Accessibilité...]

Génère le code React + Tailwind complet.
Commence par me montrer un aperçu de la structure.
```

### Exemple de session Vibe Design

**Prompt 1 :**
"Dashboard analytics pour une app SaaS. Vibe : Linear meets Vercel. Dark mode. Sidebar navigation, main area avec 4 KPI cards, graphique principal, table d'activité récente."

**Itération 2 :**
"Les cards sont trop espacées, resserre. Ajoute un subtle gradient sur les icônes. Le graphique doit avoir un vibe plus 'glowy'."

**Itération 3 :**
"Parfait. Maintenant rends le responsive. Mobile : cards en 2x2, sidebar devient bottom nav."

### Les 3 interfaces à créer

**1. Dashboard SaaS (1h)**
- Navigation, KPIs, graphiques, tables
- Interactions hover et feedback

**2. Landing Page (45min)**
- Hero, features, pricing, CTA
- Responsive et optimisé conversion

**3. Interface complexe (1h15)**
- Au choix : Settings multi-tabs, Checkout flow, ou Chat interface
- États multiples (loading, error, success)

### Documenter son langage de vibe

```markdown
## Mon Vocabulaire Vibe Design

### Termes que j'utilise souvent
- "Aéré" → padding généreux, whitespace
- "Punchy" → contrastes forts, CTAs visibles
- "Subtle" → hover states discrets, ombres légères

### Références par type de projet
- Dashboard : Linear, Vercel, Raycast
- Landing : Stripe, Notion, Arc
- App mobile : Apple, Things, Bear

### Phrases qui marchent bien
- "Plus de breathing room autour de X"
- "Un accent color plus saturé"
- "Hierarchy visuelle plus marquée sur Y"
```

---

## Animation Dojo (2h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Décrire une interface par son "vibe"
- Itérer rapidement par conversation
- Créer un prototype haute fidélité en < 1h

### Prérequis

- Accès Claude (Artifacts activés)
- Environnement pour tester le code (optionnel)

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | Qu'est-ce que le Vibe Design ? |
| 10-25 | Démo | Dashboard créé en live |
| 25-50 | Interface 1 | Chacun crée un dashboard |
| 50-80 | Interface 2 | Landing page |
| 80-100 | Partage | Showcase des créations |
| 100-120 | Clôture | Vocabulaire et bonnes pratiques |

### Points d'attention animateur

- Encourager l'itération rapide
- Montrer comment "parler design" à l'IA
- Comparer avec le temps qu'aurait pris Figma

---

## Ressources complémentaires

- [Claude Artifacts](https://www.anthropic.com/news/claude-artifacts)
- [Tailwind CSS Components](https://tailwindui.com/)
- [Refactoring UI](https://www.refactoringui.com/)
