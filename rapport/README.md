# Rapport professionnel — Exploradôme

Rapport préparé après visite et entretien, destiné à une présentation à l'équipe de
l'Exploradôme. Construit **tâche par tâche**. Chaque volet distingue clairement :

- ✔ **Fait vérifié** (source officielle citée)
- 🌐 **Info Exploradôme** (site / sources publiques, à confirmer)
- 👁 **Observation** personnelle (visite / entretien)
- 💡 **Proposition**

## Plan du rapport

| # | Volet | Statut | Fichier |
|---|-------|--------|---------|
| 1 | Présentation de l'Exploradôme (mission, publics, médiation) | à faire | — |
| 2 | Ma visite (espaces, expositions, ateliers) | à faire | — |
| 3 | Les ateliers et programmes (dont numérique / IA) | à faire | — |
| 4 | Mon rôle potentiel de médiatrice IA | à faire | — |
| 5 | Analyse de la communication | intégré au volet 6 (§1) | `outils-open-source.html` |
| 6 | **Outils open source & automatisation** | ✅ **fait** | [`outils-open-source.html`](outils-open-source.html) |

## Volet 6 — Outils (partie majeure)

Quatre outils **réellement open source ET gratuits**, vérifiés à la source (sept. 2026) :

| Outil | Rôle | Licence (vérifiée) | Auto-hébergement |
|-------|------|--------------------|------------------|
| **Postiz** | Réseaux sociaux | AGPL-3.0 | Docker + PostgreSQL + Redis |
| **Listmonk** | Newsletters | AGPL-3.0 | Binaire Go + PostgreSQL |
| **Activepieces** | Automatisation + IA | MIT (Community) | Docker + PostgreSQL + Redis |
| **WordPress** | Site / CMS | GPLv2+ | PHP + MySQL |

> **n8n est écarté volontairement** : sa *Sustainable Use License* est du *fair-code /
> source-available*, **pas** de l'open source au sens OSI — exactement le piège que le
> rapport demande d'éviter. Il est documenté comme alternative, non recommandé au titre
> de « l'open source ».

Le volet contient aussi : analyse des tâches de communication automatisables, fiches
détaillées par outil (fonctionnalités, IA, intégrations/API, coûts, avantages/limites),
**tableau comparatif** (sans classement), **scénarios d'automatisation** avec validation
humaine, et un chapitre **« L'IA dans la communication »**.

### Ouvrir / présenter

Ouvrir `outils-open-source.html` dans un navigateur. Pour une version PDF à diffuser :
*Fichier → Imprimer → Enregistrer au format PDF* (mise en page optimisée pour l'impression).

### À confirmer sur place

Le site `exploradome.fr` n'était pas accessible depuis l'environnement de rédaction :
les éléments de contexte proviennent de sources publiques secondaires et doivent être
validés avec l'équipe et sur le site officiel.
