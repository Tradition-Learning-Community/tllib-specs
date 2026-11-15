# Pré-implémentation — Conception et études expérimentales

**Statut : documentation de travail non normative, en attente de revue et de décision de fusion.**  
**Périmètre :** les études préparatoires liées à Tradition Learning (TL) et aux modèles d'intelligence artificielle, rassemblées le 15 novembre 2026.

Ce répertoire conserve les idées, distinctions, hypothèses, questions ouvertes et **résultats expérimentaux sans TL** issus de nos travaux, afin de pouvoir les retrouver avant de décider ce qui mérite une formalisation scientifique ou une implémentation. Les textes de ce dossier ne changent ni la théorie, ni les contrats existants, ni les exigences de conformité.

## Organisation

- [`fondements/SCHEMES_NOTES_DE_TRAVAIL.md`](fondements/SCHEMES_NOTES_DE_TRAVAIL.md) — définition de travail des schèmes, acquisition et exploitation, limites de l'observation interne.
- [`fondements/SIX_FAMILLES_OPERATIONNELLES.md`](fondements/SIX_FAMILLES_OPERATIONNELLES.md) — classification opérationnelle des finalités des modèles IA, sans confondre architectures et paradigmes.
- [`fondements/MISSION_ENTITES_HUIT_OBJETS_ET_TRADITION.md`](fondements/MISSION_ENTITES_HUIT_OBJETS_ET_TRADITION.md) — compréhension de travail des rôles, de la Mission, des huit objets et des contributions.
- [`conception/CONSTITUTION_ET_FRONTIERES.md`](conception/CONSTITUTION_ET_FRONTIERES.md) — responsabilités de constitution et séparation entre ressources et fonctionnement scientifique.
- [`conception/QUESTIONS_OUVERTES.md`](conception/QUESTIONS_OUVERTES.md) — points à approfondir avant toute proposition de contrat.
- [`benchmarks/sans_tl/README.md`](benchmarks/sans_tl/README.md) — protocole et inventaire des six familles ; études intégrales et chronologies enregistrées.

## Autorité et garde-fous

1. Le **manuscrit scientifique Tradition Learning** demeure l'autorité théorique ; `maths/` conserve la source scientifique publiée dans ce dépôt.
2. Les contrats structurés de `registry/` et `handoff/` conservent leur autorité propre. **Rien dans ce dossier ne les modifie, ne les remplace ou n'ajoute une obligation.**
3. `tllib` est la bibliothèque d'implémentation séparée. Aucune API ni opération TL nouvelle n'est décidée ici.
4. Les six familles décrivent des **finalités opérationnelles de modèles IA** : régression, classification, clustering, génération, représentation et politique de décision. **TL n'est pas une septième famille.**
5. Le mot « schème » est un **terme de travail** sur les contenus représentationnels internes acquis ou modifiés, et **n'est pas un neuvième objet scientifique TL**.
6. Les benchmarks existants étudient les mécanismes d'apprentissage **sans TL**. Leurs sondes et chiffres ne mesurent ni une maturation scientifique de Disciple ni une Tradition.

Les questions et décisions futures devront suivre les circuits de revue et d'adjudication déjà en place. La simple présence de ces notes dans Git ne vaut pas validation scientifique.

## Conservation des expérimentations

Les études détaillées, leurs chronologies complètes et les inventaires SHA-256 sont conservés sous `benchmarks/sans_tl/`. Les archives et fichiers binaires bruts des expériences (NPZ, JSON, checkpoints, ZIP, scripts) restent **hors de ce dépôt**, dans l'archive autonome `ETUDE_SIX_FAMILLES_SANS_TL.zip`. Leur absence de ce répertoire est intentionnelle : cette proposition n'ajoute que des documents `.md`, conformément au périmètre retenu. Voir les limites de reproductibilité dans le README des benchmarks.
