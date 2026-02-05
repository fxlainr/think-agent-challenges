# L'Architecte d'Intention (Computer Use)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Marque | VALUE |
| Durée solo | 4h |
| Durée Dojo | 2h |
| Difficulté | ⭐⭐⭐⭐⭐ |
| XP | 450 |
| Prérequis | Python, API Anthropic, notions d'automatisation |

---

## Vision & Impact

Utiliser Claude pour piloter tous les outils logiciels (Photoshop, Figma, Blender) **par le langage**. Le logiciel cesse d'être un outil que l'on manipule pour devenir un système que l'on dirige.

## Le saviez-vous ?

C'est la **fin de l'interface comme goulot d'étranglement primaire**. Si l'IA peut cliquer, l'expertise devient la capacité à formuler l'intention, pas à maîtriser 50 raccourcis clavier.

## Sources

- [Anthropic just killed traditional UIs - Linas Beliunas](https://www.linkedin.com/posts/linasbeliunas_anthropic-just-killed-traditional-uis-claude-ugcPost-7421998087759450112-LBoW)
- [Using Claude to build scenes in Blender - Marcus Byrne](https://www.linkedin.com/posts/marcus-byrne_using-claude-to-build-scenes-in-blender-feels-activity-7416418673847869440-BE4j)

---

## Description

> *Pilotez n'importe quel logiciel par la voix ou le texte grâce à Claude Computer Use.*

"Claude, ouvre Figma, duplique ce frame, change la couleur en bleu, exporte en PNG." Et il le fait. Ce challenge vous fait maîtriser Computer Use pour automatiser des workflows logiciels complexes par simple intention.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Script Computer Use fonctionnel
- [ ] Automatisation d'un workflow multi-étapes
- [ ] Documentation des patterns et limitations

**Critères de réussite :**

- Workflow automatisé de bout en bout
- Gestion des erreurs et retry
- Au moins 3 applications pilotées

---

## Pistes de Solution

### Qu'est-ce que Computer Use ?

```
Computer Use = Capacité de Claude à :
1. Voir l'écran (screenshot)
2. Cliquer (coordonnées x, y)
3. Taper (texte)
4. Naviguer (scroll, raccourcis clavier)

C'est comme un humain devant un écran, mais piloté par langage naturel.
```

### Setup de base

```python
import anthropic

client = anthropic.Anthropic()

# Message avec Computer Use
response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=[
        {
            "type": "computer_20241022",
            "name": "computer",
            "display_width_px": 1920,
            "display_height_px": 1080,
            "display_number": 0,
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "Ouvre Chrome et va sur google.com"
        }
    ]
)
```

### Workflow type

```python
"""
Workflow : Export automatique Figma → Optimisation → Upload

1. Ouvre Figma
2. Sélectionne le frame "Hero"
3. Export en PNG @2x
4. Ouvre ImageOptim
5. Optimise l'image
6. Upload sur S3
"""

instructions = """
Tu dois exporter et optimiser une image depuis Figma.

Étapes :
1. Clique sur l'icône Figma dans le dock
2. Attends que Figma charge (5 sec)
3. Utilise Cmd+/ pour la recherche
4. Tape "Hero" et sélectionne le frame
5. Clic droit → Export → PNG @2x
6. Sauvegarde sur le Bureau
7. Ouvre ImageOptim (Cmd+Space, tape ImageOptim)
8. Drag le fichier dans ImageOptim
9. Attends l'optimisation
10. Confirme quand terminé

Si une étape échoue, décris ce que tu vois et attends des instructions.
"""
```

### Gestion des erreurs

```python
def run_with_retry(task, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = execute_computer_use(task)
            if result.success:
                return result
            else:
                # Demander à Claude de diagnostiquer
                diagnosis = diagnose_failure(result.screenshot)
                task = f"{task}\n\nProblème précédent: {diagnosis}"
        except Exception as e:
            log_error(e)
    raise MaxRetriesExceeded()
```

### Cas d'usage à automatiser

**1. Design workflow (1h30)**
```
Figma → Export → Optimisation → Upload CDN
```

**2. Data workflow (1h)**
```
Excel → Nettoyage → Copier vers Google Sheets → Générer graphique
```

**3. Dev workflow (1h30)**
```
VS Code → Créer fichiers → Lancer serveur → Ouvrir browser → Tester
```

### Patterns efficaces

```
## Ce qui marche bien
- Instructions étape par étape
- Attendre entre les actions (loading)
- Vérifier visuellement après chaque étape
- Utiliser les raccourcis clavier quand possible

## Ce qui marche moins bien
- Actions trop rapides (pas le temps de charger)
- Zones trop petites à cliquer
- Applications avec beaucoup d'animations
- Authentification (captcha, 2FA)
```

### Limitations connues

```
⚠️ Limitations actuelles :
- Latence : ~2-3 sec par action
- Précision : ±10px sur les clics
- Pas de son/vidéo
- Captchas bloquants
- Certaines apps résistent (Electron parfois)
```

---

## Animation Dojo (2h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Configurer Computer Use
- Écrire des instructions efficaces
- Automatiser un workflow multi-app

### Prérequis

- API key Anthropic (Computer Use beta)
- Python 3.9+
- macOS ou Linux (Windows expérimental)

### Déroulé minute par minute

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-10 | Intro | La révolution Computer Use |
| 10-25 | Setup | Configuration de l'environnement |
| 25-40 | Démo | Workflow simple en live |
| 40-70 | Pratique | Chacun crée son automatisation |
| 70-100 | Debug | Résolution des problèmes |
| 100-115 | Showcase | Démo des workflows |
| 115-120 | Clôture | Vers des agents autonomes |

### Points d'attention animateur

- Setup peut être long → faire en amont
- Avoir des workflows de démo prêts
- Prévoir des alternatives si beta instable

---

## Ressources complémentaires

- [Anthropic Computer Use Docs](https://docs.anthropic.com/claude/docs/computer-use)
- [Computer Use Examples](https://github.com/anthropics/anthropic-cookbook)
