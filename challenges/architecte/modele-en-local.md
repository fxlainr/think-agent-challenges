# Modèle en Local

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 2h |
| Durée Dojo | 1h |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Docker, notions de ligne de commande |

---

## Description

> *Déployez et opérez un LLM local avec Ollama : installation, conteneurisation, API REST et intégration dans vos workflows.*

Données sensibles ? Pas de budget API ? Besoin de travailler hors ligne ? Ce challenge vous fait déployer votre propre LLM en local — même performance qu'un GPT-3.5 sur votre machine, zéro donnée qui sort.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] LLM déployé en Docker avec Ollama
- [ ] API REST accessible et testée
- [ ] Intégration fonctionnelle (n8n ou script Python)
- [ ] Documentation complète

**Critères de réussite :**

- Le modèle répond en moins de 10 secondes
- L'API est accessible depuis d'autres services
- La documentation permet à un collègue de reproduire

---

## Pistes de Solution

### Architecture cible

```
┌─────────────────────────────────────────────────────┐
│                    Docker Host                       │
│  ┌─────────────────┐    ┌─────────────────┐         │
│  │     Ollama      │◀───│      n8n        │         │
│  │   Port 11434    │    │   Port 5678     │         │
│  └─────────────────┘    └─────────────────┘         │
│           ▲                                          │
│           │ API REST                                 │
│           ▼                                          │
│  ┌─────────────────┐                                │
│  │   Votre app     │                                │
│  └─────────────────┘                                │
└─────────────────────────────────────────────────────┘
```

### Installation Ollama

**Option A : Installation directe**
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2  # ~4 GB
ollama run llama3.2 "Bonjour !"
```

**Option B : Docker (recommandé)**
```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama

docker exec ollama ollama pull llama3.2
```

### Test de l'API REST

```bash
# Génération simple
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Explique le RGPD en une phrase",
  "stream": false
}'

# Chat avec historique
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {"role": "user", "content": "Capitale de la France ?"}
  ]
}'
```

### Docker Compose complet

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped

  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - OLLAMA_HOST=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:
```

### Modèles recommandés

| Modèle | Taille | RAM | Usage |
|--------|--------|-----|-------|
| phi3 | 2.3 GB | 4 GB | Ultra léger, rapide |
| mistral | 4 GB | 8 GB | Polyvalent |
| llama3.2 | 4.7 GB | 8 GB | Performant |
| llama3.2:70b | 40 GB | 48 GB | Maximum qualité |

### Client Python

```python
import requests

class OllamaClient:
    def __init__(self, host="http://localhost:11434"):
        self.host = host
    
    def chat(self, message: str, model: str = "llama3.2") -> str:
        response = requests.post(
            f"{self.host}/api/chat",
            json={
                "model": model,
                "messages": [{"role": "user", "content": message}],
                "stream": False
            }
        )
        return response.json()["message"]["content"]

# Usage
client = OllamaClient()
print(client.chat("Résume le RGPD en 3 points"))
```

### Tips & astuces

- GPU NVIDIA = 10x plus rapide (ajouter `--gpus all` dans Docker)
- Commencer par phi3 pour tester (plus léger)
- Le premier appel est lent (chargement en mémoire)

---

## Animation Dojo (1h, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Installer et configurer Ollama
- Déployer un LLM local avec Docker
- Appeler l'API REST du modèle
- Comprendre les trade-offs local vs cloud

### Prérequis participants

- Docker installé
- 8 GB RAM minimum
- Connexion internet (téléchargement modèle)

### Matériel nécessaire

- [ ] docker-compose.yml prêt
- [ ] Scripts de test (curl, Python)
- [ ] Modèle pré-téléchargé (backup)
- [ ] Tableau comparatif local vs cloud

### Déroulé minute par minute

| Temps | Phase | Animateur | Participants | Objectif |
|-------|-------|-----------|--------------|----------|
| 0-5 | Intro | Avantages du local (privacy, coût, latence) | Comprennent le contexte | Motivation |
| 5-10 | Démo | Ollama en action | Observent la rapidité | Preuve |
| 10-20 | Installation | Guide Docker | Lancent docker-compose | Setup |
| 20-25 | Pull modèle | Explique les modèles | Téléchargent phi3 | Configuration |
| 25-35 | Test API | Montre curl | Testent l'API | Validation |
| 35-45 | Intégration | Montre n8n ou Python | Créent un workflow | Application |
| 45-55 | Benchmark | Compare modèles | Testent différents modèles | Évaluation |
| 55-60 | Clôture | Use cases (audit, POC) | Notent les applications | Projection |

### Points d'attention animateur

**Pièges courants :**

- RAM insuffisante → phi3 en backup
- Téléchargement lent → Modèle sur clé USB
- Port 11434 pris → Changer le port

**Questions fréquentes :**

- "Aussi bien que ChatGPT ?" → Comparable à GPT-3.5 pour les bons modèles
- "C'est légal ?" → Oui, modèles open source
- "Hors ligne ?" → Oui, une fois téléchargé

### Variantes

**Version simple (45 min) :**
- Installation directe (pas Docker)
- Test en ligne de commande
- Un seul modèle

**Version avancée (2h) :**
- Multi-modèles, load balancing
- RAG local avec ChromaDB
- Fine-tuning

---

## Ressources complémentaires

- [Ollama](https://ollama.com/)
- [LM Studio](https://lmstudio.ai/) — alternative avec GUI
- [Open WebUI](https://github.com/open-webui/open-webui) — interface web pour Ollama
