# Le Documentaliste de Vélocité (Storybook-Cursor)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | FLOW |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐ |
| XP | 320 |
| Prérequis | Storybook, React, Cursor ou Claude Code |

---

## Vision & Impact

Automatiser la documentation du design via le workflow **Storybook-Cursor**. L'IA génère instantanément la documentation technique des composants codés, assurant une vélocité totale.

## Le saviez-vous ?

Ce workflow permet aux équipes de rester concentrées sur la création de valeur plutôt que sur la rédaction de documentation technique pénible.

## Sources

- [Storybook Design Ops - Valeriya Tkacheva](https://www.linkedin.com/posts/valeriya-tkacheva_designops-productdesign-figma-activity-7417659708574068736-S784)

---

## Description

> *Générez automatiquement une documentation de composants toujours à jour.*

Documentation obsolète. Props non documentées. Exemples qui ne marchent plus. Ce challenge vous fait créer un workflow où la documentation se génère automatiquement à chaque commit.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] 5 composants documentés automatiquement
- [ ] Workflow de génération en place
- [ ] Documentation toujours synchronisée avec le code

**Critères de réussite :**

- Stories générées automatiquement
- Props documentées avec types
- Exemples fonctionnels

---

## Pistes de Solution

### Architecture du workflow

```
Code Component → Analyse IA → Stories générées → Storybook

Sur chaque commit :
1. Détecter les composants modifiés
2. Analyser le code (props, variants)
3. Générer/mettre à jour les stories
4. Commit automatique de la doc
```

### Prompt de génération de stories

```
Analyse ce composant React et génère la documentation Storybook :

"""
[CODE DU COMPOSANT]
"""

Génère :

1. Story par défaut (Default)
2. Story pour chaque variant significatif
3. Story pour les états (loading, error, disabled)
4. Documentation des props (JSDoc ou MDX)
5. Exemples d'utilisation

Format : CSF3 (Component Story Format)
Inclure les argTypes avec descriptions.
```

### Template de story généré

```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      description: 'Style variant of the button',
      options: ['primary', 'secondary', 'ghost'],
      control: { type: 'select' },
    },
    size: {
      description: 'Size of the button',
      options: ['sm', 'md', 'lg'],
      control: { type: 'select' },
    },
    disabled: {
      description: 'Disable the button',
      control: { type: 'boolean' },
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Default: Story = {
  args: {
    children: 'Click me',
    variant: 'primary',
  },
};

export const Secondary: Story = {
  args: {
    children: 'Secondary',
    variant: 'secondary',
  },
};

// ... autres stories
```

### Script d'automatisation

```bash
#!/bin/bash
# generate-stories.sh

# Trouver les composants modifiés
MODIFIED=$(git diff --name-only HEAD~1 | grep "\.tsx$" | grep -v "\.stories\.")

for file in $MODIFIED; do
  # Générer la story via Claude
  story_content=$(claude "Génère la story Storybook pour: $(cat $file)")
  
  # Écrire le fichier story
  story_file="${file%.tsx}.stories.tsx"
  echo "$story_content" > "$story_file"
done

# Commit si changements
git add "*.stories.tsx"
git commit -m "📚 Auto-generate stories for modified components"
```

### Les 5 composants à documenter

```
1. Button (variants, sizes, states)
2. Input (types, validation states)
3. Card (layouts, avec/sans image)
4. Modal (sizes, with/without footer)
5. Table (sorting, pagination)
```

---

## Animation Dojo (1h30)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Le coût de la documentation manuelle |
| 15-30 | Setup | Configurer Storybook + Claude |
| 30-60 | Génération | Documenter 3 composants |
| 60-80 | Automatisation | Mettre en place le workflow |
| 80-90 | Clôture | Intégration CI/CD |

### Points d'attention

- Toujours relire la doc générée
- Les edge cases peuvent être manqués
- La doc doit rester utile, pas juste exhaustive
