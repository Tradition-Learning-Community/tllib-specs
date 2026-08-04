# Sources scientifiques de Tradition Learning

Le dossier `maths/` contient l’autorité scientifique amont de `tllib-specs`.

## Convention documentaire

Chaque domaine pertinent dispose de son propre dossier. Chaque dossier contient obligatoirement :

- un `README.md` bref, limité à la présentation du domaine, aux sources et à l’organisation des fichiers ;
- un ou plusieurs fichiers `.md` distincts portant le contenu scientifique du domaine.

Le `README.md` d’un domaine n’est jamais utilisé comme substitut au texte scientifique. Les domaines existants conservent leur contenu sans réécriture. Les nouveaux domaines ne contiennent pour l’instant qu’une ossature explicitement marquée comme non transcrite.

## Domaines

| Index | Domaine | État documentaire |
|---:|---|---|
| 00 | [Maître](00-master/) | Existant, contenu conservé |
| 01 | [Disciple](01-disciple/) | Existant, contenu conservé |
| 02 | [Communauté](02-community/) | Existant, contenu conservé |
| 03 | [Huit dimensions de TL](03-huit-dimensions-de-tl/) | Existant, contenu conservé |
| 04 | [Invariants](04-invariants/) | Existant, contenu conservé |
| 05 | [Dynamiques](05-dynamics/) | Existant, contenu conservé |
| 06 | [Théorèmes](06-theorems/) | Existant, contenu conservé |
| 07 | [Message](07-message/) | Existant, contenu conservé |
| 08 | [Principe](08-principle/) | Existant, contenu conservé |
| 09 | [Valeurs](09-values/) | Existant, contenu conservé |
| 10 | [Vertus](10-virtues/) | Existant, contenu conservé |
| 11 | [Capacités](11-capacities/) | Existant, contenu conservé |
| 12 | [Compétences](12-competencies/) | Existant, contenu conservé |
| 13 | [Pratique](13-practice/) | Existant, contenu conservé |
| 14 | [Expérience vécue](14-lived-experience/) | Existant, contenu conservé |
| 15 | [Relations](15-relations/) | Existant, contenu conservé |
| 16 | [Cohorte](16-cohort/) | Ossature créée, transcription à faire |
| 17 | [Transmission en cascade](17-cascade-transmission/) | Ossature créée, transcription à faire |
| 18 | [Évaluation](18-evaluation/) | Ossature créée, transcription à faire |
| 19 | [Régulation](19-regulation/) | Ossature créée, transcription à faire |
| 20 | [Robustesse](20-robustness/) | Ossature créée, transcription à faire |
| 21 | [Équité](21-fairness/) | Ossature créée, transcription à faire |
| 22 | [Temporalité](22-temporality/) | Ossature créée, transcription à faire |
| 23 | [Mémoire](23-memory/) | Ossature créée, transcription à faire |
| 24 | [Contexte](24-context/) | Ossature créée, transcription à faire |
| 25 | [Culture](25-culture/) | Ossature créée, transcription à faire |
| 26 | [Identité](26-identity/) | Ossature créée, transcription à faire |
| 27 | [Réflexivité](27-reflexivity/) | Ossature créée, transcription à faire |
| 28 | [Finalité et téléologie évolutive](28-finality-and-evolutionary-teleology/) | Ossature créée, transcription à faire |
| 29 | [Propagation générationnelle](29-generational-propagation/) | Ossature créée, transcription à faire |
| 30 | [Expansion](30-expansion/) | Ossature créée, transcription à faire |
| 31 | [Institutionnalisation](31-institutionalization/) | Ossature créée, transcription à faire |
| 32 | [Dérive et correction](32-drift-and-correction/) | Ossature créée, transcription à faire |
| 33 | [Architecture pour environnements à faibles données](33-low-data-architecture/) | Ossature créée, transcription à faire |
| 34 | [Cycle de transmission](34-transmission-lifecycle/) | Ossature créée, transcription à faire |
| 35 | [Fidélité au noyau invariant](35-fidelity-to-invariant-core/) | Ossature créée, transcription à faire |

## Textes intégrateurs

Les documents de synthèse générale se trouvent dans [`integration/`](integration/). Ils ne sont pas comptés comme domaines autonomes dans cette première organisation.

## Compatibilité des chemins historiques

Les seize anciens fichiers `maths/00-*.md` à `maths/15-*.md` sont maintenus comme liens symboliques vers les nouveaux emplacements. Cette compatibilité évite de rompre immédiatement les références de traçabilité existantes. Leur retrait éventuel devra faire l’objet d’une migration distincte de tous les chemins consommateurs.
