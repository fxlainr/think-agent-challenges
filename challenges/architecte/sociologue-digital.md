# Le Sociologue Digital

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 16h |
| Durée Dojo | 2 jours (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Python, notions de graphes, sensibilité RGPD |

---

## Description

> *Analysez les dynamiques sociales de votre organisation avec l'Organizational Network Analysis (ONA) : identifiez les silos, les connecteurs clés et les risques — le tout en respectant la vie privée.*

L'organigramme ne dit pas qui parle vraiment à qui. Ce challenge vous fait cartographier les relations réelles dans une organisation : qui fait circuler l'info, où sont les silos, qui est critique pour la collaboration. Privacy by Design obligatoire.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Pipeline d'analyse des interactions (anonymisées)
- [ ] Visualisation du graphe social
- [ ] Rapport avec insights et recommandations
- [ ] Guide de conformité RGPD intégré

**Critères de réussite :**

- Les données sont anonymisées AVANT analyse
- Les résultats sont agrégés (pas de surveillance individuelle)
- Les insights sont actionnables pour améliorer la collaboration

---

## Pistes de Solution

### Qu'est-ce que l'ONA ?

L'Organizational Network Analysis cartographie les **relations réelles** (pas l'organigramme) pour identifier :

| Élément | Définition | Insight |
|---------|------------|---------|
| **Connecteurs** | Personnes clés qui font circuler l'info | À préserver |
| **Silos** | Groupes isolés | À connecter |
| **Bottlenecks** | Points de congestion | À désengorger |
| **Risques** | Personnes critiques (bus factor) | À mitiger |

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   ONA ANALYSIS SYSTEM                    │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Data      │───▶│  Anonymize  │───▶│   Graph     │  │
│  │   (raw)     │    │   (RGPD)    │    │   (NetworkX)│  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│                                               │          │
│  ┌─────────────┐    ┌─────────────┐          ▼          │
│  │   Insights  │◀───│   Analyze   │◀──────────┘         │
│  │   (rapport) │    │   (metrics) │                     │
│  └─────────────┘    └─────────────┘                     │
│                                                          │
│  ⚠️ PRIVACY BY DESIGN                                    │
│  • Anonymisation AVANT analyse                          │
│  • Pas de surveillance individuelle                     │
│  • Résultats agrégés uniquement                         │
└─────────────────────────────────────────────────────────┘
```

### Sources de données (anonymisées)

| Source | Données | Usage |
|--------|---------|-------|
| Email metadata | Qui→Qui (PAS le contenu) | Flux communication |
| Calendrier | Participants réunions | Collaboration |
| Slack/Teams | Canaux, mentions | Interactions |
| Survey | Relations déclarées | Perception |

⚠️ **JAMAIS le contenu des messages — uniquement les métadonnées relationnelles.**

### Métriques de graphe

| Métrique | Définition | Insight |
|----------|------------|---------|
| Degree centrality | Nombre de connexions | Qui est bien connecté |
| Betweenness centrality | Nb chemins passant par le nœud | Qui fait le pont |
| Clustering coefficient | Connexion des voisins entre eux | Silos |
| PageRank | Importance pondérée | Influenceurs |

### Code Python (éléments clés)

```python
import networkx as nx

def build_graph(interactions):
    """Construire le graphe à partir des interactions anonymisées"""
    G = nx.Graph()
    for row in interactions:
        G.add_edge(
            row['from_id'],  # ID anonyme !
            row['to_id'],
            weight=row['count']
        )
    return G

def analyze_network(G):
    """Calculer les métriques"""
    return {
        'degree_centrality': nx.degree_centrality(G),
        'betweenness_centrality': nx.betweenness_centrality(G),
        'clustering': nx.clustering(G),
        'communities': list(nx.community.louvain_communities(G))
    }

def identify_risks(G, metrics):
    """Identifier les personnes critiques (bus factor)"""
    risks = []
    for node, score in metrics['betweenness_centrality'].items():
        if score > 0.3:  # Seuil à ajuster
            risks.append({
                'node': node,  # ID anonyme
                'risk': 'Connecteur critique - bus factor élevé'
            })
    return risks
```

### Considérations éthiques (OBLIGATOIRES)

| Principe | Application |
|----------|-------------|
| **Consentement** | Informer les participants avant |
| **Anonymisation** | IDs randomisés, pas de noms |
| **Agrégation** | Résultats par groupe, pas individuel |
| **Finalité** | Amélioration collective, pas surveillance |
| **Droit d'accès** | Permettre de se retirer |

### Tips & astuces

- Toujours anonymiser AVANT de charger dans l'outil
- Présenter les résultats par équipe, pas par personne
- Impliquer les RH et le DPO dès le début

---

## Animation Dojo (2 jours, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Collecter et anonymiser des données d'interactions
- Construire et analyser un graphe social avec NetworkX
- Interpréter les métriques de réseau
- Produire un rapport respectueux de la vie privée

### Prérequis participants

- Python niveau intermédiaire
- Notions de graphes (nœuds, arêtes)
- Sensibilité RGPD

### Matériel nécessaire

- [ ] Jeu de données fictif (interactions simulées)
- [ ] Environnement Python (NetworkX, matplotlib)
- [ ] Template de rapport ONA
- [ ] Checklist conformité RGPD

### Déroulé (2 jours)

| Jour | Demi-journée | Contenu | Livrable |
|------|--------------|---------|----------|
| J1 | Matin | Théorie ONA + éthique/RGPD | Compréhension |
| J1 | Après-midi | Setup données + anonymisation | Pipeline data |
| J2 | Matin | Analyse et métriques | Graphe analysé |
| J2 | Après-midi | Visualisation + rapport | Livrable final |

### Points d'attention animateur

**Pièges courants :**

- Données pas anonymisées → Bloquer tant que c'est pas fait
- Interprétation individuelle → Insister sur l'agrégation
- Surveillance déguisée → Clarifier la finalité

**Questions fréquentes :**

- "On peut identifier les gens quand même ?" → Non, c'est le but de l'anonymisation
- "C'est légal ?" → Oui si consentement et finalité légitime
- "Quid si quelqu'un refuse ?" → Le retirer du dataset

**Tips d'animation :**

- Commencer par un exercice éthique (débat)
- Utiliser des données simulées pour éviter les biais
- Faire valider le rapport par un "comité éthique" fictif

### Variantes

**Version découverte (4h) :**
- Données pré-anonymisées fournies
- Focus sur l'analyse et l'interprétation
- Pas de pipeline data

**Version avancée (3 jours) :**
- Connexion aux vraies sources (avec accord)
- Dashboard interactif
- Suivi longitudinal (évolution dans le temps)

---

## Ressources complémentaires

- [NetworkX Documentation](https://networkx.org/)
- [ONA Handbook](https://www.orgnet.com/)
- [CNIL - Guide RGPD](https://www.cnil.fr/)
