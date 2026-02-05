# Le Concierge Connecté

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Crafter |
| Durée solo | 1h30 |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐ |
| Prérequis | Notions de base sur les APIs |

---

## Description

> *Créez un assistant qui interagit avec des APIs réelles via function calling : météo, calendrier, recherche web... Un vrai concierge connecté au monde.*

"Quel temps fait-il à Lyon pour ma réunion de demain ?" L'assistant vérifie votre calendrier, trouve le lieu, appelle l'API météo et vous répond. Ce challenge vous fait connecter un LLM au monde réel.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Assistant avec 2+ fonctions connectées
- [ ] Démo montrant l'appel de fonction en action
- [ ] Gestion des erreurs propre

**Critères de réussite :**

- Les fonctions sont appelées correctement par le LLM
- Les réponses intègrent les données récupérées
- Les erreurs sont gérées gracieusement

---

## Pistes de Solution

### Concept : Function Calling

```
Utilisateur → Question
     ↓
LLM → Décide quelle fonction appeler
     ↓
Fonction → Exécution (API externe)
     ↓
LLM → Formule une réponse naturelle
```

### Définir les fonctions

**Météo (OpenWeatherMap) :**
```json
{
  "name": "get_weather",
  "description": "Obtient la météo actuelle pour une ville",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "Nom de la ville (ex: Paris)"
      }
    },
    "required": ["city"]
  }
}
```

**Recherche web (Brave/Tavily) :**
```json
{
  "name": "search_web",
  "description": "Recherche sur le web",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Termes de recherche"
      }
    },
    "required": ["query"]
  }
}
```

### Implémenter les handlers

**Python - Météo :**
```python
import requests
import os

def get_weather(city: str) -> dict:
    api_key = os.environ["OPENWEATHER_API_KEY"]
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    response = requests.get(url, params={
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "fr"
    })
    
    if response.status_code != 200:
        return {"error": f"Ville non trouvée: {city}"}
    
    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
```

### Prompt système du concierge

```
Tu es Max, un assistant connecté avec accès à plusieurs outils :

## Outils disponibles
1. get_weather(city) : Météo d'une ville
2. search_web(query) : Recherche web

## Comportement
- Utilise tes outils AVANT de répondre si nécessaire
- Ne devine jamais ce que tu peux vérifier
- Combine plusieurs outils si utile
- Gère les erreurs gracieusement

## Exemples
"Il fait beau à Paris ?" → get_weather("Paris")
"C'est quoi les dernières news sur l'IA ?" → search_web("actualités IA")
```

### APIs gratuites recommandées

| API | Description | Clé requise |
|-----|-------------|-------------|
| OpenWeatherMap | Météo | Oui (gratuite) |
| JokeAPI | Blagues | Non |
| QuotableAPI | Citations | Non |
| RestCountries | Info pays | Non |

### Tips & astuces

- La description de la fonction guide le LLM
- Toujours gérer les erreurs d'API
- Tester avec des cas limites

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Comprendre le function calling
- Définir une fonction appelable par un LLM
- Connecter un LLM à une API externe
- Gérer les erreurs d'appel

### Prérequis participants

- Compte n8n ou environnement Python
- Clé API OpenWeatherMap (gratuite, 5 min)
- Notions de base sur les APIs

### Matériel nécessaire

- [ ] Template n8n ou code Python
- [ ] Liste d'APIs gratuites
- [ ] Guide "créer une clé API"
- [ ] Prompt système

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Explique le function calling | Comprennent le flux | Théorie |
| 5-12 | Démo | Construit un agent météo en live | Observent | Voir ça marche |
| 12-18 | Setup API | Aide sur les clés API | Créent leur compte | Préparation |
| 18-25 | Fonction 1 | Guide la création météo | Implémentent get_weather | Base |
| 25-35 | Fonction 2 | Présente d'autres APIs | Ajoutent une 2e fonction | Extension |
| 35-45 | Tests | Fait tester différentes requêtes | Testent, débuggent | Validation |
| 45-55 | Erreurs | Montre la gestion d'erreurs | Ajoutent le fallback | Robustesse |
| 55-60 | Clôture | Idées d'APIs à connecter | Notent les prochaines étapes | Inspiration |

### Points d'attention animateur

**Pièges courants :**

- Clé API manquante → Avoir des clés backup
- Erreurs JSON → Valider avec un linter
- LLM n'appelle pas la fonction → Vérifier la description

**Questions fréquentes :**

- "Pourquoi ça n'appelle pas ma fonction ?" → Description pas assez claire
- "Comment je sais qu'elle a été appelée ?" → Logs n8n ou mode debug
- "Je peux connecter n'importe quelle API ?" → Oui si accessible

### Variantes

**Version simple (45 min) :**
- 1 seule fonction (météo)
- Template pré-configuré

**Version avancée (2h) :**
- 3-4 fonctions interconnectées
- Chaînage (calendrier → météo du lieu)
- Mise en production

---

## Ressources complémentaires

- [OpenWeatherMap](https://openweathermap.org/api)
- [n8n Function Calling](https://docs.n8n.io/)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
