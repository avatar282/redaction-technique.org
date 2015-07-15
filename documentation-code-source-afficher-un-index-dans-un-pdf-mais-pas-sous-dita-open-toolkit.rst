.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: no code

.. _afficher-un-index-dans-un-pdf-mais-pas-sous-dita-open-toolkit:

Afficher un index dans un PDF (mais pas sous DITA Open Toolkit)
===============================================================

Tout n'est pas parfait sous |dita-ot|, le moteur de publication libre
|dita|. Vous avez méticuleusement inséré vos entrées d'index dans vos fichiers
de contenu |dita|. Vous générez une sortie PDF et l'index n'apparaît pas. Un
message d'erreur de la compilation vous indique que, hélas, FOP ne supporte
actuellement pas la génération des index.

Face à cette situation, vous avez quatre solutions :

- attendre que FOP supporte les index ; sans date de disponibilité, ce choix
  sera difficile à faire accepter par votre direction ;

- abandonner |dita| ; avouez que ce serait dommage de renoncer aux formidables
  gains de productivité que permet ce format ;

- renoncer à afficher l'index dans le PDF ; les arguments en faveur d'un tel
  choix ont un certain poids : les index sont difficiles à maintenir et offre un
  surplus d'utilisabilité discutable dans un document qui ne sera consulté que
  marginalement sous forme imprimée ;

- abandonner |dita-ot| et se tourner vers une solution propriétaire ;
  les logiciels non open-source, XMetal, par exemple, on souvent recours au
  moteur de publication XEP de RenderX qui lui, supporte parfaitement les index.

Le problème de l'index n'est donc pas un obstacle à l'adoption de |dita|. Si
votre support final est un document imprimé, les solutions existent. S'il s'agit
d'un format électronique, l'absence d'un index est largement compensée par la
fonction de recherche en plein texte.

.. text review: yes
