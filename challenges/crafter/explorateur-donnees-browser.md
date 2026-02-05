# L'Explorateur de Données (Browser as API)

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Marque | VALUE |
| Durée solo | 2h |
| Durée Dojo | 1h30 |
| Difficulté | ⭐⭐⭐⭐ |
| XP | 360 |
| Prérequis | Python, notions de scraping |

---

## Vision & Impact

Utiliser l'IA pour naviguer et extraire des données stratégiques directement depuis le web sans passer par des APIs traditionnelles. Le navigateur devient un **substitut puissant** pour collecter des insights concurrentiels en temps réel.

## Le saviez-vous ?

Nous quittons l'ère de l'interface comme goulot d'étranglement : si l'IA peut lire un écran, toute information devient une **donnée programmable**.

## Sources

- [GenAI Browser as API - Fred Cavazza](https://www.linkedin.com/posts/fredcavazza_genai-activity-7422541070640697344-dsSD)

---

## Description

> *Transformez n'importe quel site web en source de données exploitable.*

Pas d'API ? Pas de problème. Ce challenge vous fait utiliser l'IA comme "lecteur de pages web" pour extraire des données structurées de n'importe quelle source.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Script d'extraction de données depuis 3 sources sans API
- [ ] Pipeline de veille concurrentielle automatisé
- [ ] Dataset structuré exportable

**Critères de réussite :**

- Données extraites fiables
- Pipeline reproductible
- Respect des conditions d'utilisation

---

## Pistes de Solution

### Architecture Browser as API

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Source    │───▶│  Browser    │───▶│  IA Parse   │───▶│  Données    │
│   (Site)    │    │ (Playwright)│    │  (Claude)   │    │  (JSON/CSV) │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Setup avec Playwright

```python
from playwright.sync_api import sync_playwright
from anthropic import Anthropic

client = Anthropic()

def extract_data(url, extraction_prompt):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Récupérer le contenu visible
        content = page.content()
        # Ou screenshot pour analyse visuelle
        # screenshot = page.screenshot()
        
        browser.close()
    
    # Analyser avec Claude
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[{
            "role": "user",
            "content": f"""
            Voici le HTML d'une page web :
            
            {content[:50000]}  # Limiter la taille
            
            {extraction_prompt}
            
            Retourne les données en JSON structuré.
            """
        }]
    )
    
    return response.content
```

### Cas d'usage d'extraction

**1. Veille concurrentielle**
```
URL : Page pricing d'un concurrent
Extraction : Prix, features par plan, limites
Output : JSON comparatif
```

**2. Analyse de marché**
```
URL : LinkedIn d'une entreprise cible
Extraction : Nombre d'employés, postes ouverts, croissance
Output : Fiche entreprise
```

**3. Monitoring produit**
```
URL : Page de releases d'un concurrent
Extraction : Features récentes, dates, messaging
Output : Timeline de releases
```

### Prompt d'extraction

```
Analyse cette page web et extrait les informations suivantes en JSON :

Page : [TYPE DE PAGE]

Données à extraire :
- [Champ 1] : [Description]
- [Champ 2] : [Description]
- [Champ 3] : [Description]

Format de sortie :
{
  "source_url": "...",
  "extracted_at": "...",
  "data": {
    "champ1": "...",
    "champ2": "..."
  },
  "confidence": 0-1,
  "notes": "observations éventuelles"
}

Si une donnée n'est pas trouvable, mettre null.
```

### Pipeline de veille

```python
COMPETITORS = [
    {"name": "Competitor A", "pricing_url": "...", "releases_url": "..."},
    {"name": "Competitor B", "pricing_url": "...", "releases_url": "..."},
]

def daily_competitive_intel():
    results = []
    
    for competitor in COMPETITORS:
        # Extraire pricing
        pricing = extract_data(
            competitor["pricing_url"],
            "Extrait les plans, prix et features principales"
        )
        
        # Extraire releases
        releases = extract_data(
            competitor["releases_url"],
            "Extrait les 5 dernières releases avec dates et features"
        )
        
        results.append({
            "competitor": competitor["name"],
            "pricing": pricing,
            "releases": releases,
            "date": datetime.now().isoformat()
        })
    
    # Sauvegarder
    save_to_database(results)
    
    # Alerter si changement significatif
    detect_and_alert_changes(results)
```

---

## Animation Dojo (1h30)

| Temps | Phase | Activité |
|-------|-------|----------|
| 0-15 | Intro | Browser as API : le concept |
| 15-30 | Setup | Installer Playwright + config |
| 30-55 | Extraction 1 | Extraire des données pricing |
| 55-80 | Extraction 2 | Construire un pipeline de veille |
| 80-90 | Clôture | Éthique et limites |

### Points d'attention

- Respecter les robots.txt et ToS
- Rate limiting pour ne pas surcharger
- Données personnelles = interdit
