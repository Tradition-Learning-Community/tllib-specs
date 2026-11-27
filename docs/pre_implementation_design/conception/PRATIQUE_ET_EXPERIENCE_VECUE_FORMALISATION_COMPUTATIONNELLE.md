# Pratique et Expérience vécue — formalisation computationnelle de travail

> **Statut :** décisions de conception pré-implémentation, non normatives.
> **Date :** 23 novembre 2026.
> **Produit visé :** `tllib`.
> **Portée :** deux des huit objets fondamentaux de Tradition Learning (TL).
> **Implémentation et tests :** aucun changement de code ni test scientifique ou de conformité effectué pour cette note.
> **Autorité :** les manuscrits scientifiques gouvernent la théorie ; `tllib-specs` gouverne les contrats ; `tllib` constitue le produit. Cette note ne remplace aucune de ces sources.

## 1. Objet et décisions retenues

Cette note fixe l'interprétation computationnelle retenue pour **Pratique** et **Expérience vécue**, afin de préparer leur représentation et leur utilisation dans `tllib`. Elle ne crée ni neuvième objet fondamental, ni nouvelle loi de Tradition Learning.

### 1.1. Pratique

> **Pratique :** moyen d'apprentissage configurable et réutilisable, définissant les opérations et les conditions par lesquelles une unité d'apprentissage exerce une activité susceptible de la transformer.

### 1.2. Expérience vécue

> **Expérience vécue :** ensemble intégré, non nécessairement exhaustif, de schèmes acquis ou modifiés et conservés par une unité d'apprentissage au cours de son parcours effectif, pouvant être représenté par les structures internes propres à cette unité.

### 1.3. Schème — terminologie de travail

> **Un schème est un contenu représentationnel interne acquis ou modifié par un modèle IA pendant son apprentissage**, susceptible de contribuer à son fonctionnement.

Un schème peut notamment concerner une caractéristique, une régularité, une corrélation, une relation, un motif ou une abstraction ; il peut être fiable, incomplet, trompeur, distribué ou non isolable.

**Les schèmes constituent le contenu représentationnel de l'apprentissage.** L'analogie des molécules aide à raisonner sur leur rôle, sans supposer des unités physiques discrètes ou un inventaire exhaustif possible. Le schème n'est ni un neuvième objet TL, ni un synonyme de poids, de neurone, d'activation ou de dataset. Il reste une notion de travail, non normative.

## 2. Pratique : définition, instanciation et exécution

### 2.1. Nature

La Pratique définit un **moyen** d'apprendre ; elle ne présuppose ni résultat favorable ni transformation scientifique TL déjà constatée. Elle peut être proposée par un Maître, configurée par le développeur ou autrement constituée dans un système TL sous les conditions scientifiques applicables.

Le caractère réutilisable de la définition permet d'associer une même Pratique à plusieurs Disciples avec des paramètres ou conditions différents. Le terme « instance » désigne ici une **organisation informatique** de cette réutilisation, et non un nouvel objet scientifique.

### 2.2. Composantes informatiques candidates

| Composante | Responsabilité | Remarque |
| --- | --- | --- |
| Configuration | Paramétrer l'activité | Peut varier entre les instances |
| Algorithme d'apprentissage | Fournir la procédure mobilisée | Peut provenir d'un outil externe |
| Critère d'apprentissage | Fournir le signal ou la règle guidant l'apprentissage | Sa forme dépend du paradigme |
| Mécanisme de modification | Décrire comment l'apprentissage modifie les structures ou acquis | Ne se confond pas systématiquement avec l'algorithme |
| Ressources et conditions pertinentes | Rendre l'activité réalisable dans son contexte | Ne sont pas toutes des attributs obligatoires à saisir |

Cette liste n'est **ni une signature normative**, ni une composition mathématique arrêtée, ni une obligation de créer cinq classes. Certains éléments peuvent être réunis, fournis par une ressource externe ou définis lors de l'exécution. Les onze éléments de l'étude de l'apprentissage IA classique demeurent des responsabilités analytiques, **pas** onze champs obligatoires de la Pratique.

### 2.3. Définition et réalisation

Pour le développement, distinguer :

1. **Définition de Pratique** : contenu configurable, réutilisable et transmissible.
2. **Instance adaptée** : application de cette définition à un Disciple, avec des paramètres et conditions déterminés.
3. **Réalisation effective** : opérations réellement effectuées avec les ressources, données, interactions et signaux disponibles.

Ces distinctions ne constituent pas trois nouveaux objets TL. Une instance définie ne prouve pas qu'une activité s'est exécutée ; une exécution ne prouve pas à elle seule la transformation scientifique du Disciple.

### 2.4. Exemple concret

Une Pratique commune consiste à entraîner un classificateur d'images.

- **D0 :** entraînement avec une architecture à deux couches et une configuration A ;
- **D1 :** même famille de Pratique avec une architecture à sept couches et une configuration B.

Les instances peuvent partager un critère d'apprentissage et un type d'algorithme, tout en mobilisant des réglages, données et ressources différents. Le cas est illustratif : TL ne prescrit aucune architecture neuronale et n'exige pas que `tllib` réimplémente les algorithmes existants.

L'analogie humaine équivalente est une même Pratique de pompes adaptée à plusieurs Disciples (400 sur une main, 100 avec pauses, 10 ordinaires). Ce sont des variations de configuration et de réalisation d'un moyen d'apprentissage.

### 2.5. Analogies de transmission et de configuration

Les exemples humains ont servi à identifier l'invariant de la **Pratique** sans transposer littéralement à l'IA une intention humaine, une croyance, un corps ou un rapport moral. Ils montrent qu'un Maître peut communiquer une activité, qu'elle peut être reprise par plusieurs Disciples et que sa configuration effective varie.

**Exercice de pompes.** Une même consigne générale (« pratiquer les pompes ») peut devenir trois instances : 400 pompes avec une main pour un Disciple, 100 pompes avec deux pauses pour un autre, 10 pompes ordinaires pour un troisième. L'activité est apparentée ; l'intensité, la manière de procéder, les pauses et les contraintes sont adaptées. Il serait faux d'en conclure que la simple prescription a déjà produit une transformation.

**Enseignement par questionnement.** Dans l'analogie Socrate–Platon, le Maître peut provoquer une activité de réflexion par des questions successives. La Pratique n'est pas nécessairement une démonstration suivie d'une reproduction : elle peut organiser une exploration et laisser ouverte la réponse que le Disciple découvrira.

**Entraînement Shaolin.** Dans l'analogie du Maître et de son Disciple Jackie, le Maître peut prescrire des exercices, observer leur exécution, corriger les gestes et adapter la difficulté. La définition de l'exercice, sa configuration et sa réalisation sont distinguables.

**Récit religieux de Pierre marchant sur l'eau.** Employé exclusivement comme analogie de transmission, cet exemple illustre une consigne visant l'exercice et le développement d'une disposition du Disciple. Il ne signifie pas que l'IA doit reproduire la foi, une intention spirituelle ou un phénomène surnaturel.

**Correspondance IA.** Deux Disciples peuvent recevoir une même Pratique de classification tout en utilisant des architectures à deux et sept couches, des réglages différents, des ensembles de données différents, des algorithmes ou critères adaptés. Des différences de paramètres, de ressources, de mécanismes et de conditions peuvent influer sur les acquisitions. Inversement, des configurations proches n'impliquent pas une expérience identique.

Ces exemples justifient la possibilité de **définir une Pratique, en créer des instances et les associer à plusieurs Disciples**, sans imposer une configuration universelle ni inventer un objet scientifique « instance de Pratique » supplémentaire.

### 2.6. Définition, exécution et résultat : trois faits distincts

Une Pratique peut être **définie** sans être réalisée ; elle peut être **réalisée** sans apprentissage mesurable ; un apprentissage informatique peut être constaté sans que toutes les conditions d'une transformation scientifique TL soient satisfaites.

L'algorithme, le critère, le mécanisme, la configuration et les ressources ne se confondent pas nécessairement. Selon le paradigme, certains éléments sont incorporés à un autre, ou dépendent des outils mis à disposition. Le cas d'un entraînement par gradient n'est pas une structure générale obligatoire pour toute Pratique TL.

### 2.7. Conséquences envisagées pour `tllib`

La conception peut prévoir des moyens de définir, configurer, instancier, associer, mobiliser et poursuivre une Pratique. L'API, le cycle de vie exact, le partage des ressources, les providers et les preuves d'exécution seront déterminés **à partir du code existant et des contrats applicables**, sans promesse d'une interface déjà implémentée.

## 3. Expérience vécue : contenu, intégration et représentation

### 3.1. Nature

L'Expérience vécue répond à la question : **quels contenus représentationnels une unité d'apprentissage a-t-elle effectivement acquis ou modifiés, intégrés et conservés à travers son parcours ?**

Elle ne se définit ni comme la totalité du dataset, ni comme un journal exhaustif des opérations, ni comme le simple fait de disposer d'un modèle entraînable.

L'Expérience vécue est un **ensemble intégré de schèmes**, et pas nécessairement une liste d'éléments individualisés. Les schèmes peuvent se recouvrir, être distribués ou rester non isolables ; leur organisation et leurs relations contribuent à l'intégration de l'expérience.

### 3.2. Non-exhaustivité

Une expérience particulière, par exemple `e0` associée à D0, **n'a pas l'obligation de restituer tous les acquis ou tous les événements du parcours de D0**.

Comme une biographie représente une partie cohérente d'un parcours sans en épuiser chaque instant, une Expérience vécue peut rendre compte d'acquis issus d'une période, d'une activité ou d'un ensemble de situations. Plusieurs expériences d'un même Disciple peuvent coexister, se compléter ou se recouvrir.

« Non nécessairement exhaustive » ne signifie pas « arbitraire » : les contenus représentés doivent correspondre à des acquis effectivement conservés, et non à une histoire supposée de l'apprentissage.

### 3.3. Supports informatiques : schèmes, poids et mémoire

Les schèmes sont des **contenus représentationnels**. Les supports informatiques peuvent être différents selon le système :

| Système | Support ou manifestation possible |
| --- | --- |
| Réseau neuronal | Poids et autres paramètres appris ; structures persistantes utiles |
| Arbre de décision | Branches, conditions, seuils et valeurs appris |
| Modèle probabiliste | Distributions et dépendances estimées |
| Système à mémoire ou k-NN | Exemples et informations conservés |
| Agent apprenant | Valeurs, politiques, représentations et mémoire acquises |

Ces supports peuvent porter des schèmes. **Ils ne constituent pas des catégories d'acquis concurrentes des schèmes**, mais il n'existe pas nécessairement une correspondance un poids = un schème, ou un exemple = un schème. Un exemple mémorisé peut porter ou contribuer à des schèmes sans que chaque octet de l'exemple soit, à lui seul, un schème.

Par conséquent, **rien n'interdit d'utiliser des poids, exemples mémorisés, états persistants ou d'autres structures pour représenter concrètement une Expérience vécue**. La bibliothèque ne doit pas enfermer cette représentation dans la seule famille des réseaux neuronaux.

### 3.4. Conservation sans utilité obligatoire

Un schème conservé peut être pertinent, erroné, latent ou ne jamais servir à nouveau. Sa contribution à une Expérience vécue ne dépend donc pas d'une amélioration de score, d'une utilisation ultérieure ou d'une preuve de généralisation.

L'Expérience vécue peut évoluer avec l'apprentissage : des contenus apparaissent, changent, se réorganisent ou cessent d'être conservés. Toute modification informatique n'établit pas automatiquement une transformation scientifique du Disciple.

### 3.5. Conséquences envisagées pour `tllib`

La bibliothèque doit pouvoir **associer une Expérience vécue à une unité d'apprentissage et à une représentation informatique pertinente**, sans exiger :

- l'identification individuelle et exhaustive des schèmes ;
- la reconstitution exhaustive de toutes les interactions passées ;
- une copie obligatoire des paramètres ou du dataset ;
- la démonstration que chaque acquis sera réutilisé.

Le mode concret d'accès, de conservation, d'extraction ou de référence aux supports dépendra des ressources, des providers et des contrats réellement disponibles. Une référence à des poids ou à un checkpoint **ne prouve pas à elle seule** qu'une Expérience vécue scientifiquement conforme a été établie.

### 3.6. Analogie du foufou : des éléments et du processus à ce qui est retenu

L'analogie du **foufou** a servi à déplacer l'attention des micro-événements vers le **résultat intégré** d'une transformation.

- La farine et l'eau participent à la préparation ; le feu et la cuisson interviennent dans la transformation.
- Les grains de farine, considérés dans l'analogie comme les « molécules » du contenu, ne restent pas nécessairement individuellement reconnaissables dans le résultat.
- On ne décrit pas le foufou final en récitant chaque seconde de cuisson ni en faisant l'inventaire de tous les gestes et échanges thermiques.
- Ce qui nous intéresse est **ce qui résulte de la préparation et demeure**.

L'analogie n'identifie pas littéralement un schème à une molécule physique. Elle explique qu'une multitude de contenus et d'interactions peuvent contribuer à un acquis intégré sans qu'il soit possible ou nécessaire de séparer toutes leurs contributions.

Dans une unité d'apprentissage IA, les schèmes sont des **contenus représentationnels internes** ; ils peuvent être acquis ou modifiés, se combiner et se distribuer dans les structures du système. L'Expérience vécue est l'ensemble intégré et conservé de ces contenus à travers un parcours effectif. Elle n'est **ni la farine initiale**, ni le récit exhaustif de la cuisson, ni seulement le nom du récipient qui la contient.

Cette lecture n'interdit pas l'accès aux éléments informatiques qui portent les contenus : pour un réseau neuronal, cela peut inclure les poids, pour un autre système des observations mémorisées ou des structures persistantes.

### 3.7. Analogie de la biographie : une expérience particulière ne raconte pas toute une vie

Une biographie ou un film biographique d'une personnalité présente certains faits, transformations et aspects cohérents de son parcours. Il permet de comprendre cette personne sans prétendre reproduire chaque instant de sa vie.

De même, **`e0` peut être une Expérience vécue de D0 sans représenter tout ce que D0 a vécu ni tous ses schèmes**. Une expérience peut porter sur une pratique, une période ou une partie de ses acquis. D'autres expériences peuvent rendre compte d'autres acquisitions, y compris avec des recouvrements.

La non-exhaustivité ne dispense pas de fidélité : ce que l'expérience représente doit avoir été effectivement acquis ou modifié et conservé ; il ne suffit pas d'attribuer arbitrairement à D0 un contenu qu'il n'a pas appris.

### 3.8. Exemple : reconnaître chien, tasse et intérieur de maison

Considérons une photographie montrant simultanément **un chien, une tasse et l'intérieur d'une maison**. Ses pixels peuvent rester strictement identiques, tandis que les activités d'apprentissage et les schèmes sollicités ou développés changent :

- reconnaître la présence du chien ;
- reconnaître la tasse ;
- reconnaître des caractéristiques de l'intérieur de la maison ;
- apprendre plusieurs de ces reconnaissances ensemble.

Selon le problème, les exemples, le modèle et la Pratique, l'unité peut acquérir des régularités, des corrélations, des relations spatiales et des abstractions différentes. Certains schèmes peuvent être partagés ; d'autres peuvent être propres à certaines reconnaissances. La photographie n'apporte pas à elle seule des schèmes déjà constitués.

L'Expérience vécue de D0 peut intégrer une partie de ces acquisitions **sans être obligatoirement une liste de schèmes explicitement détectés**. Elle peut également comprendre des corrélations trompeuses, par exemple l'association erronée d'une classe avec un décor ou un appareil de prise de vue.

### 3.9. Exemples mémorisés, états persistants et poids : pas trois catégories concurrentes des schèmes

Lors de la discussion, une séparation initialement proposée entre schèmes, exemples mémorisés et états persistants a été rejetée comme trop rigide.

Un exemple mémorisé, des paramètres appris, une structure d'arbre, une distribution estimée ou une mémoire persistante **peuvent porter des schèmes**, sans qu'il existe une correspondance universelle « un exemple = un schème » ou « un poids = un schème ». Les schèmes désignent le contenu représentationnel interne de l'apprentissage, quel que soit le support numérique concerné.

Quelques cas :

1. **Réseau neuronal profond :** les poids et structures apprises peuvent servir de support à un contenu représentationnel distribué. Ils ne doivent pas être exclus d'une représentation de l'Expérience vécue au seul motif qu'ils sont des paramètres.
2. **Arbre de décision :** les règles, seuils et branchements peuvent porter des régularités acquises. L'Expérience vécue ne suppose pas un tenseur de poids.
3. **k-NN ou mémoire d'exemples :** les exemples conservés peuvent soutenir le fonctionnement appris et porter des contenus représentationnels. La conservation des observations ne doit pas être assimilée automatiquement à la copie intégrale de l'expérience.
4. **Agent apprenant :** une politique, une mémoire ou des valeurs apprises peuvent porter des schèmes relatifs à des situations et relations rencontrées.
5. **Paramètres initialisés avant l'apprentissage :** leur existence seule ne démontre aucune acquisition issue d'un parcours effectif.

Les supports changent selon les architectures ; **ce que désigne l'Expérience vécue reste l'acquis intégré et conservé**, éventuellement partiel. Aucun détecteur exhaustif de schèmes n'est présupposé.

### 3.10. Plusieurs pratiques, plusieurs expériences, influence ultérieure facultative

Deux Disciples peuvent exécuter une Pratique voisine avec des configurations différentes, puis conserver des expériences distinctes. Une même unité peut aussi intégrer des acquis provenant de plusieurs Pratiques, d'observations ou d'autres interactions. Inversement, un schème peut contribuer à plus d'une expérience représentée.

Il faut distinguer **ce qui a été conservé** de **ce qui est ensuite utilisé**. Un schème conservé peut ne jamais être réactivé, peut être erroné ou n'avoir aucun effet constaté sur les activités ultérieures. Son éventuelle inutilisation ne l'exclut pas de l'Expérience vécue.

Enfin, la modification de poids ou l'amélioration d'un score ne démontre pas automatiquement une transformation scientifique du Disciple selon les contrats TL. La représentation informatique de l'expérience et sa qualification scientifique restent deux opérations distinctes.

## 4. Articulation entre les objets

| Dimension | Pratique | Expérience vécue |
| --- | --- | --- |
| Question principale | Par quel moyen l'unité apprend-elle ? | Qu'a-t-elle acquis et conservé ? |
| Nature | Moyen configurable et réutilisable | Acquis représentationnel intégré |
| Particularisation | Instances adaptées aux Disciples | Contenus propres au parcours considéré |
| Réalisation | Opérations et conditions effectives | Résultat conservé, éventuellement partiel |
| Informatique | Algorithmes, configuration, critères, mécanismes et ressources | Schèmes portés par poids, mémoires, structures ou autres supports |
| Condition insuffisante | Exécuter un algorithme ne prouve pas une transformation TL | Sauvegarder un modèle ne prouve pas une expérience conforme |

Une Pratique peut contribuer à plusieurs expériences vécues ; une Expérience vécue peut intégrer des acquis issus de plusieurs Pratiques et d'autres interactions d'apprentissage. Aucune correspondance obligatoire un-à-un n'est postulée.

Cette articulation n'assimile pas l'Expérience vécue à la Tradition : celle-ci demeure un héritage vivant, intégré, évolutif et transmissible au sein du système TL, distinct d'un modèle, de poids ou d'un artefact.

## 5. Correspondance à rechercher avec les mathématiques existantes

Les textes scientifiques de `tllib-specs` formalisent notamment :

**Pratique :**

```math
\mathcal{P}:\mathcal{C}_p\times\mathcal{E}\times\mathcal{F}\rightarrow\mathcal{C}_a
```

**Expérience vécue :**

```math
\mathcal{LE}=(\mathcal{T},\mathcal{H})
```

La formalisation de l'Expérience vécue décrit des traces temporelles `T` et une interprétation intégrée `H` ; le texte scientifique comporte également une synthèse visant un noyau expérientiel. **Ces constructions restent l'autorité théorique.**

La représentation computationnelle proposée s'intéresse directement **au contenu intégré et conservé dans le système d'apprentissage**. Savoir lire, représenter ou conserver les poids et autres supports peut rendre inutile, pour certains usages informatiques, la reconstitution de toutes les traces historiques ; cela **ne supprime pas** les notions théoriques de traces et d'interprétation.

Une correspondance — voire une équivalence mathématique — entre les deux descriptions pourra être étudiée sur cette base. **Elle n'est ni démontrée ni introduite ici sous forme d'un nouvel opérateur ou d'une nouvelle équation.** Aucune condition scientifique normative n'est remplacée par la seule disponibilité d'une représentation informatique.

Références directes :
- [`maths/13-practice/practice.md`](../../../maths/13-practice/practice.md)
- [`maths/14-lived-experience/lived-experience.md`](../../../maths/14-lived-experience/lived-experience.md)
- [`fondements/SCHEMES_NOTES_DE_TRAVAIL.md`](../fondements/SCHEMES_NOTES_DE_TRAVAIL.md)
- [`conception/EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md`](EXERCICES_PARCELLES_SIX_FAMILLES_11_ELEMENTS.md)
- [`conception/SEPT_PHASES_PARCOURS_D0_ET_APPRENTISSAGE_IA.md`](SEPT_PHASES_PARCOURS_D0_ET_APPRENTISSAGE_IA.md)

## 6. Frontières, état et suite

### Décisions de travail retenues

1. Conserver les deux définitions de la section 1.
2. Traiter la Pratique comme un moyen d'apprentissage réutilisable, avec des instances adaptables et des réalisations effectives.
3. Traiter l'Expérience vécue comme un ensemble intégré, potentiellement partiel, de schèmes acquis ou modifiés et conservés.
4. Admettre les poids, exemples mémorisés, états persistants et autres structures comme supports possibles des schèmes et des expériences.
5. Ne pas exiger de détecteur universel de schèmes ni d'historique intégral pour représenter une Expérience vécue.

### Non-décisions

- Aucune nouvelle équation, métrique, condition d'existence, correspondance mathématique démontrée ou classe d'API normative.
- Aucun jugement automatique de conformité scientifique à partir de la seule exécution d'un apprentissage classique.
- Aucune modification de la définition des huit objets fondamentaux ni de la distinction entre Disciple, ressource, modèle, système TL et Tradition.

### Travaux d'implémentation à instruire

Examiner, au moment de développer `tllib`, les interfaces, providers, conventions C++20/Python, contrats exécutables ou structurels, et tests déjà présents. Préciser alors comment **définir et instancier une Pratique**, **associer et représenter une Expérience vécue**, **exposer les supports propres au modèle** et **tester séparément la représentation informatique et la conformité scientifique**.

**État final de cette note :** définition de travail arrêtée ; interface informatique et équivalence mathématique à établir ; aucune implémentation ni validation exécutée.
