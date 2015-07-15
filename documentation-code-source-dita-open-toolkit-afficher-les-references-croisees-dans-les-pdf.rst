.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: yes

.. _dita-open-toolkit-afficher-les-references-croisees-dans-les-pdf:

DITA Open Toolkit : afficher les références croisées dans les PDF
=================================================================

Les références croisées sont un élément important d'une |doc|
bien structurée. Elles permettent à l'utilisateur de naviguer
facilement dans les briques d'information et sont un élément crucial de
l'utilisabilité du document final. |dita-ot| les gère très bien, à
condition d'effectuer quelques réglages.

Vous avez placé des balises *related-links* correctement formatées dans vos
fichiers de contenu |dita|, ou mieux, une `reltable`_
dans votre
structure de table des matières *ditamap* (la *reltable* permet de
décontextualiser votre contenu et donc de mieux le réutiliser). Vous lancez
votre commande de génération du PDF et, mauvaise surprise, aucune section *Voir
aussi* [#]_ n'apparaît dans le fichier cible ! Vous essayez alors de générer une
version HTML de votre contenu et là, votre section *Voir aussi* est bien
présente. |dita-ot| ne supporterait-il pas les références croisées
dans les PDF ?

Fort heureusement, non. Par défaut (allez savoir pourquoi), les références
croisées ne sont pas générées dans les PDF par |dita-ot|. Pour les
afficher, attribuez la valeur *no* à la variable *disableRelatedLinks* du fichier
:file:`demo/fo/build_template.xml`. Si vous utilisez *ant*, il vous faudra
également passer le paramètre *args.fo.include.rellinks=all* comme suit :

.. code-block:: console

   $ ant -Dargs.input=samples/sequence.ditamap -Doutput.dir=out/ \
   -Dtranstype=pdf2 -Dargs.fo.include.rellinks=all

.. only:: html

   .. rubric:: Notes

.. [#] Pour des raisons de « décontextualisation », et pour se donner la
       possibilité de réutiliser le contenu ailleurs, les références croisées ne
       sont pas placées dans le corps du texte, mais en fin de section, dans une
       rubrique dédiée.

.. text review: yes
