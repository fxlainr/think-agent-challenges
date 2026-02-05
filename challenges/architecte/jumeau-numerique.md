# Le Jumeau Numérique

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 16h |
| Durée Dojo | 2 jours (workshop) |
| Difficulté | ⭐⭐⭐ |
| Prérequis | Python, notions de simulation |

---

## Description

> *Construisez un système de simulation industrielle avec optimisation par agents IA — modélisez une ligne de production, testez des configurations, identifiez les goulots.*

Votre usine tourne, mais est-elle optimisée ? Acheter une machine de plus ? Embaucher un opérateur ? Ce challenge vous fait créer un jumeau numérique : une réplique virtuelle de votre ligne de production où vous pouvez tester des configurations sans risque et laisser l'IA trouver l'optimum.

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Modèle de simulation fonctionnel (SimPy)
- [ ] Agent d'optimisation testant plusieurs configurations
- [ ] Visualisation des résultats (throughput, goulots)
- [ ] Gains quantifiés entre config actuelle et optimisée

**Critères de réussite :**

- La simulation reflète fidèlement la réalité (paramétrage calibré)
- L'agent identifie correctement les goulots
- Les recommandations sont chiffrées (ROI)

---

## Pistes de Solution

### Concept de Digital Twin

Un jumeau numérique est une réplique virtuelle d'un système physique qui permet de :
- **Simuler** : Tester des configurations sans risque
- **Prédire** : Anticiper les problèmes
- **Optimiser** : Trouver la meilleure configuration
- **Monitorer** : Suivre en temps réel

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    DIGITAL TWIN SYSTEM                   │
├─────────────────────────────────────────────────────────┤
│  PHYSICAL WORLD              │    DIGITAL WORLD          │
│  ┌─────────────┐             │    ┌─────────────┐       │
│  │   Sensors   │────────────►│───▶│   Model     │       │
│  │   (IoT)     │             │    │   (SimPy)   │       │
│  └─────────────┘             │    └──────┬──────┘       │
│                              │           │              │
│  ┌─────────────┐             │    ┌──────▼──────┐       │
│  │   Actuators │◄────────────│◄───│  Optimizer  │       │
│  │             │             │    │   (Agent)   │       │
│  └─────────────┘             │    └──────┬──────┘       │
│                              │           │              │
│                              │    ┌──────▼──────┐       │
│                              │    │  Dashboard  │       │
│                              │    │  (Visu)     │       │
│                              │    └─────────────┘       │
└─────────────────────────────────────────────────────────┘
```

### Modélisation avec SimPy (Python)

```python
import simpy
import random

class ProductionLine:
    def __init__(self, env, config):
        self.env = env
        self.config = config
        
        # Ressources
        self.machine_a = simpy.Resource(env, capacity=config['machine_a_capacity'])
        self.machine_b = simpy.Resource(env, capacity=config['machine_b_capacity'])
        self.operators = simpy.Resource(env, capacity=config['operators'])
        
        # Métriques
        self.completed = 0
        self.cycle_times = []
    
    def process_item(self, item_id):
        arrival = self.env.now
        
        # Machine A
        with self.machine_a.request() as req:
            yield req
            yield self.env.timeout(random.normalvariate(
                self.config['machine_a_time'], 
                self.config['machine_a_variance']
            ))
        
        # Machine B
        with self.machine_b.request() as req:
            yield req
            yield self.env.timeout(random.normalvariate(
                self.config['machine_b_time'], 
                self.config['machine_b_variance']
            ))
        
        # Contrôle qualité (opérateur)
        with self.operators.request() as req:
            yield req
            yield self.env.timeout(self.config['qc_time'])
        
        self.completed += 1
        self.cycle_times.append(self.env.now - arrival)

def run_simulation(config, duration=480):  # 8h = 480 min
    env = simpy.Environment()
    line = ProductionLine(env, config)
    
    def item_generator():
        item_id = 0
        while True:
            yield env.timeout(random.expovariate(1/config['arrival_rate']))
            env.process(line.process_item(item_id))
            item_id += 1
    
    env.process(item_generator())
    env.run(until=duration)
    
    return {
        'throughput': line.completed,
        'avg_cycle_time': sum(line.cycle_times) / len(line.cycle_times),
    }
```

### Agent d'optimisation

```python
def optimize_config(base_config, budget):
    """
    Agent qui teste différentes configurations
    et recommande la meilleure dans le budget.
    """
    
    scenarios = [
        {'name': 'Base', 'config': base_config, 'cost': 0},
        {'name': '+1 Machine A', 'config': {**base_config, 'machine_a_capacity': 2}, 'cost': 50000},
        {'name': '+1 Operator', 'config': {**base_config, 'operators': 3}, 'cost': 30000},
        {'name': 'Upgrade Machine B', 'config': {**base_config, 'machine_b_time': 4}, 'cost': 80000},
    ]
    
    results = []
    for scenario in scenarios:
        if scenario['cost'] <= budget:
            sim_result = run_simulation(scenario['config'])
            roi = calculate_roi(sim_result, scenario['cost'])
            results.append({**scenario, **sim_result, 'roi': roi})
    
    results.sort(key=lambda x: x['roi'], reverse=True)
    return results[0]  # Meilleure option
```

### Identification des goulots

| Indicateur | Calcul | Goulot si... |
|------------|--------|--------------|
| Utilisation | Temps occupé / Temps total | > 85% |
| File d'attente | Nb items en attente | Croissante |
| Temps de cycle | Temps à cette étape | > autres étapes |

### Tips & astuces

- Commencer par un modèle simple (3-4 étapes max)
- Calibrer avec des données réelles si disponibles
- Visualiser l'utilisation des ressources pour identifier les goulots

---

## Animation Dojo (2 jours, ~10 personnes)

### Objectifs pédagogiques

À la fin de l'atelier, les participants sauront :

- Modéliser un processus avec SimPy
- Créer des agents d'optimisation
- Analyser les résultats de simulation
- Identifier et résoudre les goulots d'étranglement

### Prérequis participants

- Python niveau intermédiaire
- Notions de processus industriels ou logistiques
- Environnement de dev configuré (Python, pip)

### Matériel nécessaire

- [ ] Code de démarrage SimPy
- [ ] Jeu de données exemple (ligne de production fictive)
- [ ] Templates de visualisation (matplotlib/plotly)
- [ ] Documentation SimPy

### Déroulé (2 jours)

| Jour | Demi-journée | Contenu | Livrable |
|------|--------------|---------|----------|
| J1 | Matin | Théorie simulation + intro SimPy | Compréhension des concepts |
| J1 | Après-midi | Modélisation ligne de production | Modèle qui tourne |
| J2 | Matin | Agent d'optimisation + tests | Agent fonctionnel |
| J2 | Après-midi | Visualisation + analyse | Dashboard + recommandations |

### Points d'attention animateur

**Pièges courants :**

- Modèle trop complexe au départ → Commencer simple, itérer
- Paramètres irréalistes → Calibrer avec des données terrain
- Oublier la variabilité → Utiliser des distributions, pas des constantes

**Questions fréquentes :**

- "C'est applicable à mon secteur ?" → Oui, adapter les entités (machines → étapes de process)
- "Comment calibrer le modèle ?" → Mesurer les temps réels, ajuster les paramètres
- "Et si le système change ?" → Le jumeau évolue avec le système réel

**Tips d'animation :**

- Avoir un cas fil rouge réaliste
- Faire des points réguliers pour recaler
- Prévoir du support technique (debug Python)

### Variantes

**Version découverte (4h) :**
- Modèle pré-construit à paramétrer
- Focus sur l'analyse des résultats
- Pas de code, interface graphique

**Version avancée (3 jours) :**
- Intégration de données IoT réelles
- Machine learning pour la prédiction
- Dashboard temps réel

---

## Ressources complémentaires

- [Documentation SimPy](https://simpy.readthedocs.io/)
- [Digital Twin Consortium](https://www.digitaltwinconsortium.org/)
- Livre : "Simulation Modeling and Analysis" (Law & Kelton)
