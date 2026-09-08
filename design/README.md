# Exploradôme — maquettes mobiles

Maquettes haute fidélité de l'application mobile du musée de sciences
**Exploradôme**, réalisées pour un entretien technique. Interface entièrement
en français.

## Contenu

| Fichier | Écran |
| --- | --- |
| `Main.dc.html` | 1 · Accueil — logo, « Commencer la visite », « Scanner un QR code », expositions du moment |
| `Scanner.dc.html` | 2 · Scanner QR — cadre caméra, « Placez le QR code dans le cadre » |
| `Exposition.dc.html` | 3 · Exposition — visuel, titre, description, « Découvrir avec l'IA », « Ajouter aux favoris » |
| `Assistant.dc.html` | 4 · Assistant IA — conversation, questions suggérées, champ « Posez votre question… » |
| `Visite.dc.html` | 5 · Ma visite — progression « 4/12 découvertes », salles visitées et à venir |
| `Favoris.dc.html` | 6 · Favoris — contenus enregistrés |
| `HorsConnexion.dc.html` | 7 · Hors connexion — contenus en cache, « Continuer ma visite » |
| `Profil.dc.html` | 8 · Profil — compte, découvertes, favoris, préférences |
| `Architecture.dc.html` | Schéma d'architecture technique |
| `Flow.dc.html` | Parcours utilisateur (Accueil → QR → Exposition → IA → Favoris → Visite) |
| `canvas.json` | Disposition des plans de travail sur le canevas |
| `exploradome-mockups.html` | Canevas assemblé (page autonome, ouvrable dans un navigateur) |

## Système de design

- **Typographie** — Instrument Serif (titres éditoriaux, nom du musée),
  Manrope (interface), avec polices de repli à métriques proches.
- **Couleurs** — encre `#101A2B`, papier `#FBFAF7`, cuivre `#B5653C`
  (action, accent), sarcelle `#2F6F7E` (IA, science, état validé).
- **Gabarit** — écrans 390 × 844, navigation basse commune à 5 entrées,
  zones tactiles ≥ 44 px, pas de fausse barre d'état système.
- **Visuels d'exposition** — compositions vectorielles intégrées
  (aucune ressource externe), à remplacer par les photographies du musée.

## Architecture représentée

React Native / Expo → Node.js / Express → PostgreSQL + Neo4j ·
Node.js / Express → OpenAI API · Clerk → authentification ·
Redis / Upstash → cache · QR code → données d'exposition.

## Modifier les maquettes

Les fichiers `.dc.html` sont la source. Après modification, réassembler
le canevas avec le script `seed-canvas.mjs` de la compétence *design*,
puis republier.
