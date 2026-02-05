# Le Networker Intelligent

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 16h |
| Durée Dojo | 2 jours (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Python, API OpenAI, notions de base de données vectorielles |

---

## Description

> *Construisez un système de matching sémantique pour connecter les experts de votre communauté — plus de "je cherche quelqu'un qui..." sans réponse.*

LinkedIn match sur des mots-clés, vous matcherez sur le sens. Ce challenge vous fait créer un système qui comprend "je cherche un expert Kubernetes pour une migration cloud" et trouve la bonne personne même si elle n'a pas écrit "Kubernetes" dans son profil.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Système d'indexation des profils (embeddings vectoriels)
- [ ] API de recherche sémantique
- [ ] Démo fonctionnelle de matching

**Critères de réussite :**

- Les résultats de recherche sont pertinents (pas juste des mots-clés)
- Le système gère des requêtes en langage naturel
- Le temps de réponse est acceptable (<2s)

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                 SEMANTIC MATCHING SYSTEM                 │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Profiles  │───▶│  Embedding  │───▶│   Vector    │  │
│  │             │    │   (OpenAI)  │    │   DB        │  │
│  │ • Skills    │    │             │    │ (Pinecone)  │  │
│  │ • Interests │    │             │    │             │  │
│  │ • Projects  │    │             │    │             │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│                                               │          │
│  ┌─────────────┐    ┌─────────────┐          ▼          │
│  │   Query     │───▶│   Search    │───▶ Matches ranked  │
│  │   (besoin)  │    │   (cosine)  │                     │
│  └─────────────┘    └─────────────┘                     │
└─────────────────────────────────────────────────────────┘
```

### Technologies

| Composant | Options | Recommandation |
|-----------|---------|----------------|
| Embeddings | OpenAI, Cohere, Hugging Face | OpenAI text-embedding-3-small |
| Vector DB | Pinecone, Weaviate, Chroma | Pinecone (managed) ou Chroma (local) |
| Backend | Python, Node.js | Python + FastAPI |

### Structure de profil

```python
profile = {
    "id": "uuid",
    "name": "Jean Dupont",
    "role": "Data Engineer",
    "skills": ["Python", "Spark", "dbt", "Airflow"],
    "interests": ["MLOps", "Data mesh", "FinOps"],
    "projects": ["Migration BigQuery", "Data platform startup"],
    "location": "Paris",
    
    # Texte enrichi pour embedding
    "rich_text": """
    Data Engineer senior spécialisé en Python et Spark.
    Expérience en migration BigQuery et data platforms.
    Intérêts : MLOps, Data mesh, optimisation cloud.
    """
}
```

### Code Python (éléments clés)

```python
from openai import OpenAI

def embed_profile(profile: dict) -> list[float]:
    """Créer l'embedding d'un profil"""
    client = OpenAI()
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=profile["rich_text"]
    )
    return response.data[0].embedding

def find_experts(query: str, top_k: int = 5):
    """Recherche sémantique"""
    query_embedding = embed_text(query)
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    return results.matches
```

### Cas d'usage

| Query | Matching attendu |
|-------|------------------|
| "Expert Kubernetes pour migration cloud" | DevOps avec XP K8s |
| "PM qui connaît la fintech" | PM avec projets finance |
| "Pair programming Python" | Dev Python disponible |

### Tips & astuces

- Enrichir le `rich_text` avec contexte métier, pas juste des mots-clés
- Tester différents modèles d'embeddings (trade-off qualité/coût)
- Prévoir des filtres classiques en complément (localisation, dispo)

---

## Animation Dojo (2 jours, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Créer des embeddings de texte avec l'API OpenAI
- Utiliser une base de données vectorielle (Pinecone/Chroma)
- Construire une API de recherche sémantique
- Interpréter et améliorer les résultats de matching

### Prérequis participants

- Python niveau intermédiaire
- Clé API OpenAI
- Notions de similarité (cosine distance)

### Matériel nécessaire

- [ ] Jeu de données de profils (20-50 fictifs)
- [ ] Compte Pinecone (free tier suffit) ou Chroma local
- [ ] Template de code de démarrage
- [ ] Liste de requêtes de test

### Déroulé (2 jours)

| Jour | Demi-journée | Contenu | Livrable |
|------|--------------|---------|----------|
| J1 | Matin | Théorie embeddings + similarité | Compréhension |
| J1 | Après-midi | Setup vector DB + indexation | Profils indexés |
| J2 | Matin | API de recherche (FastAPI) | Endpoint fonctionnel |
| J2 | Après-midi | UI simple + démo | Système complet |

### Points d'attention animateur

**Pièges courants :**

- Profils trop courts → Enrichir avec contexte
- Pas de données de test → Préparer des requêtes variées
- Attentes irréalistes → La recherche sémantique n'est pas magique

**Questions fréquentes :**

- "Coût des embeddings ?" → ~$0.02 pour 1000 profils (text-embedding-3-small)
- "Pinecone vs Chroma ?" → Pinecone = managed, Chroma = local/gratuit
- "Comment améliorer les résultats ?" → Enrichir les profils, fine-tuner

### Variantes

**Version découverte (4h) :**
- Utiliser Chroma local (pas de setup cloud)
- Script Python simple (pas d'API)
- Focus sur la compréhension des embeddings

**Version production (3 jours) :**
- Intégration avec un annuaire réel
- UI complète (Next.js)
- Système de feedback pour améliorer le matching

---

## Ressources complémentaires

- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [Chroma](https://www.trychroma.com/)
