# Schèmes — définition de travail et observation de l'apprentissage

**Statut : notes de recherche non normatives — 15 novembre 2026.**

## 1. Définition de travail

Un **schème** est un élément de **contenu représentationnel interne acquis ou modifié par un modèle IA pendant son apprentissage**, susceptible de contribuer à son fonctionnement. Il peut concerner une caractéristique, une régularité, un motif, une corrélation, une relation, une organisation ou une abstraction ; il peut être fiable, incomplet ou trompeur. Un schème peut être distribué ou non isolable.

Cette terminologie permet de parler de **ce qui est appris**, sans réduire ce contenu à son support informatique. Elle n'est pas encore une définition normative de `tllib-specs`.

Le schème n'est **pas**, par définition, le pixel d'une image, une observation brute, un poids unique, une activation, un neurone, un embedding, un état temporaire, une sortie ou un artefact. Il n'est **pas un neuvième objet fondamental de TL**.

## 2. Exemple de la photographie inchangée

Une photographie contient un chien, une tasse et une fenêtre. Les pixels restent identiques. Apprendre à reconnaître le chien, la tasse ou la fenêtre peut conduire à mobiliser ou à acquérir des régularités internes distinctes. Les représentations peuvent toutefois se recouvrir, être partagées ou combinées ; une classification multilabel peut concerner simultanément plusieurs de ces catégories.

Le schème désigne le **contenu représentationnel appris et exploitable**, et non un élément matériel que la donnée apporterait déjà comme tel. La finalité, les signaux d'apprentissage, les ressources et le mécanisme du modèle participent à ce qui sera acquis.

## 3. Trois phénomènes distincts

**Acquérir ou modifier des schèmes** : des relations peuvent apparaître, se consolider, se différencier, être réorganisées, perdre de leur influence ou être corrigées. Les mécanismes concrets sont ceux des algorithmes concernés ; aucun opérateur universel « créer un schème » n'a été identifié.

**Exploiter des schèmes** : les contenus existants peuvent être sélectionnés, combinés et utilisés. L'exploitation ne garantit pas une modification durable de l'apprentissage. Une nouvelle combinaison peut toutefois devenir elle-même un contenu acquis selon le mécanisme.

**Transformer scientifiquement un Disciple selon TL** : phénomène distinct, régi par la Mission, les entités, les huit objets et les conditions scientifiques applicables. Une mise à jour des paramètres ou une amélioration de score ne suffit pas à l'établir ; inversement, une évolution TL n'exige pas nécessairement l'identification d'un schème isolable.

## 4. Observer le contenu à chaque instant et à chaque niveau

Dans les expériences de référence, on suit un modèle petit pendant des centaines ou milliers d'observations. À plusieurs instants, on examine **tout le répertoire de relations accessible**, pas seulement les différences entre deux points. Les relations relativement stables ont également de l'intérêt.

Dans un modèle linéaire, on peut analyser les relations réalisées par des coefficients ; dans un arbre, les chemins de décision ; dans un modèle probabiliste, les distributions et dépendances ; dans un réseau, les activations de couches et les effets de perturbations contrôlées. **Ces éléments sont des sondes ou supports, pas un inventaire direct des schèmes.**

Une différence d'activations entre deux entrées établit une sensibilité de la représentation calculée, mais ne prouve pas l'existence d'un schème unique. De même, une réduction de l'effet d'une caractéristique sur la sortie ne prouve pas la disparition de toute information interne sur cette caractéristique.

## 5. Variété des mécanismes

Les schèmes ne doivent pas être assimilés à une méthode neuronale particulière. Les six familles retenues mobilisent, selon les algorithmes, estimations de coefficients, constructions d'arbres, voisinages mémorisés, centres, distributions, modèles génératifs, espaces latents, valeurs et politiques. Certains algorithmes (par exemple k-NN ou certaines formes de clustering) conservent principalement des exemples ou déterminent des groupements, sans construire nécessairement une abstraction générale comparable à celle d'un réseau profond.

L'apprentissage peut aussi acquérir une **association trompeuse** : un appareil photographique au lieu d'une pathologie, un marqueur parasite au lieu d'une orientation, une corrélation de contexte au lieu de la relation recherchée. Un résultat correct ne prouve donc pas que le contenu interne est correct ou causalement fondé.

## 6. Distinction avec la famille « Représentation »

La **Représentation** est l'une des six familles opérationnelles de développement de modèles IA : la finalité est d'apprendre une transformation ou un espace de représentation. Le terme **schème** est, lui, transversal : la régression, la classification, la génération, le clustering ou la décision peuvent également donner lieu à des contenus représentationnels acquis. Les deux notions ne se substituent pas l'une à l'autre.

## 7. Limites et statut

Ce texte conserve le vocabulaire adopté pour la recherche. Il ne crée ni types scientifiques TL supplémentaires, ni équations, ni seuils, ni critères de maturité. Les expériences disponibles montrent l'évolution des **supports et manifestations** de contenus appris ; elles ne fournissent pas un détecteur universel et complet de schèmes.
