.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: no code

Intégrer la documentation aux processus de développement
--------------------------------------------------------

La documentation fait partie du logiciel. Fournie avec le produit, elle doit :

- sortir en même temps,
- suivre les mêmes cycles de vie, et
- faire l'objet des mêmes processus de
  production et de contrôle qualité.

.. figure:: graphics/integration-doc-dev.svg

   *Sources de documentation modulaires au format texte*

Elle doit répondre idéalement aux critères suivants :

- pas de *vendor lock-in* (indépendance du format et de l'éditeur de contenu),
- chaînes de publication libres et gratuites,
- mise en page totalement automatisée.

Il y a quelques années encore, les seuls outils permettant de fournir des
livrables de qualité au format PDF ou HTML reposaient sur des formats binaires
et propriétaires qui s'intégraient mal aux systèmes de gestion de versions des
équipes de développement.

Résultat : réalisée à part, la documentation technique répondait difficilement
aux mêmes exigences de qualité et de délai de mise sur le marché que les
produits.

|db|, puis |dita| et |rst| ont changé la donne : ces formats texte peuvent être
modifiés avec tout type de programme, du simple éditeur de texte à l'|ide|
graphique, et s'intègrent parfaitement sous Subversion, Git ou tout autre
système de gestion de versions.

.. text review: yes
