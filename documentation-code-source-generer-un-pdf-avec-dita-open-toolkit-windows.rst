.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: yes

.. _generer-un-pdf-avec-dita-open-toolkit-windows:

Générer un PDF avec DITA Open Toolkit (Windows)
===============================================

Ce didacticiel |dita| est destiné à vous guider
dans la mise en place et l'utilisation de la chaîne de publication |dita-ot|
dans un environnement Windows (testé sur Windows XP).

.. rubric:: Prérequis

- Connexion Internet

#.  Téléchargez `Java`_,
    puis lancez le programme d'installation.

#.  Téléchargez `DITA Open Toolkit 1.5.4`_
    sur le
    bureau, puis décompressez :file:`DITA-OT1.5.4_full_easy_install_bin.zip`.

#.  Sélectionnez :guilabel:`Exécuter` dans le menu :guilabel:`Démarrer`, collez
    la commande suivante, puis appuyez sur **Entrée** :

    .. code-block:: console

       cmd

    Un terminal apparaît.

#. Collez la commande suivante dans le terminal :

   .. code-block:: console

      cd Bureau\DITA-OT1.5.4_full_easy_install_bin\DITA-OT1.5.4

#. Collez la commande suivante :

   .. code-block:: console

      startcmd.bat

   Un nouveau terminal apparaît.

#. Collez la commande suivante dans le nouveau terminal :

   .. code-block:: console

      $ java -jar lib/dost.jar /i:samples/taskbook.ditamap /outdir:. /transtype:pdf2

   Cette commande génère un fichier PDF à partir d'un projet |dita| d'exemple.

   Félicitations, vous avez compilé votre premier projet |dita| ! Vous
   trouverez le fichier cible :file:`taskbook.pdf` dans le répertoire
   :file:`Bureau\\DITA-OT1.5.4_full_easy_install_bin\\DITA-OT1.5.4`. Vous pouvez
   maintenant compiler d'autres projets en ignorant les étapes 1 et 2.

.. text review: yes
