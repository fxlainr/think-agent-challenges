# AgCraft - Boss Final

## Métadonnées

| Propriété | Valeur |
|-----------|--------|
| Type | Architecte |
| Durée solo | 16h+ |
| Durée Dojo | 2 jours (hackathon) |
| Difficulté | ⭐⭐⭐⭐⭐ |
| Prérequis | Développement full-stack, agents IA |

---

## Description

> *Créez une interface de jeu de stratégie pour piloter une équipe d'agents IA : visualisation temps réel, allocation des tâches, gestion des ressources.*

Imaginez StarCraft, mais au lieu de contrôler des unités militaires, vous pilotez une flotte d'agents IA. Voyez-les travailler en temps réel, assignez les tâches aux bons agents, gérez vos tokens API comme des ressources précieuses.

**C'est le projet Capstone du parcours Architecte.**

---

## Objectif du Challenge

**Ce que le participant doit produire :**

- [ ] Prototype jouable avec agents réels intégrés
- [ ] Visualisation temps réel des tâches
- [ ] Système d'allocation et de priorisation
- [ ] Gestion des ressources (tokens, temps)

**Critères de réussite :**

- L'interface est réactive et agréable à utiliser
- Les agents exécutent réellement des tâches
- Le système de scoring encourage l'optimisation

---

## Pistes de Solution

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                       AGCRAFT                            │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐│
│  │                    GAME UI                          ││
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   ││
│  │  │ Agent 1 │ │ Agent 2 │ │ Agent 3 │ │ Agent 4 │   ││
│  │  │ 🔵 Idle │ │ 🟢 Work │ │ 🟡 Queue│ │ 🔴 Error│   ││
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   ││
│  │                                                      ││
│  │  ┌──────────────────────────────────────────────┐   ││
│  │  │              TASK QUEUE                       │   ││
│  │  │  📋 Task A (High) → Agent 2                   │   ││
│  │  │  📋 Task B (Med)  → Waiting                   │   ││
│  │  └──────────────────────────────────────────────┘   ││
│  │                                                      ││
│  │  ┌──────────────────────────────────────────────┐   ││
│  │  │  💰 API Credits: 8,432 / 10,000               │   ││
│  │  │  📊 Throughput: 12 tasks/hour                 │   ││
│  │  └──────────────────────────────────────────────┘   ││
│  └─────────────────────────────────────────────────────┘│
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │                ORCHESTRATION ENGINE                  ││
│  │  • Task routing • Load balancing • Error handling   ││
│  └─────────────────────────────────────────────────────┘│
│                                                          │
│  ┌─────────────────────────────────────────────────────┐│
│  │                   AGENT FLEET                        ││
│  │  🤖 Research (Claude) • Coding (GPT-4) • Writing    ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
```

### Composants techniques

| Composant | Technologies | Responsabilité |
|-----------|--------------|----------------|
| Frontend | React/Vue + WebSocket | UI temps réel |
| Backend | FastAPI/Node.js | Orchestration |
| Agents | OpenClaw, n8n, custom | Exécution |
| Queue | Redis, RabbitMQ | File de tâches |
| Storage | PostgreSQL | Historique |

### Data models

**Agent Card :**
```typescript
interface AgentCard {
  id: string;
  name: string;
  type: 'researcher' | 'coder' | 'writer' | 'analyst';
  status: 'idle' | 'working' | 'queued' | 'error';
  currentTask?: Task;
  capabilities: string[];
  stats: { tasksCompleted: number; avgTime: number; successRate: number };
}
```

**Task :**
```typescript
interface Task {
  id: string;
  title: string;
  priority: 'critical' | 'high' | 'medium' | 'low';
  requiredCapabilities: string[];
  status: 'pending' | 'assigned' | 'running' | 'completed' | 'failed';
  progress: number;  // 0-100
}
```

### Fonctionnalités de jeu

- **Drag & Drop** — Glisser une tâche sur un agent pour l'assigner
- **Resource Management** — Budget tokens, time tracking
- **Scoring** — +10/task, +5 speed bonus, -15/error

### Tips & astuces

- Commencer par une version statique (pas de vrais agents)
- Ajouter le temps réel avec WebSocket
- Intégrer les agents un par un

---

## Animation Dojo (2 jours, équipe 3-5)

### Objectifs pédagogiques

À la fin du hackathon, les participants sauront :

- Concevoir une architecture multi-agents
- Développer une interface temps réel
- Orchestrer des agents IA
- Travailler en équipe sur un projet complexe

### Rôles suggérés

| Rôle | Responsabilité |
|------|----------------|
| Frontend Lead | UI React/Vue, animations |
| Backend Lead | API, orchestration |
| Agent Engineer | Intégration agents IA |
| Designer | UX, game feel |
| PM/QA | Coordination, tests |

### Déroulé (2 jours)

| Temps | Phase | Objectif |
|-------|-------|----------|
| J1 Matin | Architecture + setup | Fondations |
| J1 Après-midi | Core features (agents, queue) | MVP |
| J2 Matin | UI + intégration | Assemblage |
| J2 Après-midi | Polish + démo | Livrable |

### Critères de jugement

- **Innovation** — Originalité de l'approche
- **Fonctionnalité** — Ça marche vraiment
- **Fun** — Envie de l'utiliser
- **Polish** — Qualité de finition

### Variantes

**Version solo (8h) :**
- Interface simplifiée
- 2 agents seulement
- Pas de scoring

**Version production (1 mois) :**
- Multi-utilisateurs
- Marketplace d'agents
- Analytics avancés

---

## Ressources complémentaires

- [React DnD](https://react-dnd.github.io/react-dnd/) — drag and drop
- [Socket.io](https://socket.io/) — temps réel
- [Bull Queue](https://github.com/OptimalBits/bull) — file de tâches
