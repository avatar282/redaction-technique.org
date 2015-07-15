.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: yes

.. _utiliser-ide-nxml-pour-dita-xml:

Utiliser l'IDE nXML pour DITA XML
=================================

Le mode nXML propose de valider en temps réel les documents XML |db|,
XHTML ou autres. Plus la peine de connaître le schéma XML par cœur: votre
éditeur de texte vous propose l'autocomplétion des balises XML selon le
contexte. Il ne supporte cependant pas |dita| par défaut. Ce didacticiel vous
permettra d'utiliser ce mode Emacs pour |dita|.

.. rubric:: Prérequis

- Emacs

- La structure de répertoires de votre projet de documentation |dita| doit
  être la suivante :

  - répertoire de langue

    - concepts
    - faq
    - reference
    - tasks
    - topics

  où *<répertoire de langue>* a la valeur *en_US*, ou *fr_FR*, etc.

- Les instructions de ligne de commande sont conçues pour GNU/Linux ; elles
  doivent être adaptées pour être utilisées dans un autre environnement.

#.  Effectuez une sauvegarde de l'ensemble de votre projet de documentation
    |dita|.
#.  Ouvrez un terminal et collez la suite de commandes suivante :

    .. code-block:: console

       $ cd && \
       wget http://www.thaiopensource.com/download/nxml-mode-20041004.tar.gz && \
       tar xzvf nxml-mode-20041004.tar.gz && \
       wget http://www.redaction-technique.org/media/nxml-mode-environmment.txt && \
       cp .emacs .emacs.bak && \
       cat .emacs | sed '$a\' > .emacs.tmp && \
       mv .emacs.tmp .emacs && \
       cat nxml-mode-environmment.txt >> .emacs && \
       rm  nxml-mode-environmment.txt

    .. note::

       Si un message vous avertit que le fichier :file:`.emacs` n'existe pas, collez les
       commandes suivantes, puis recommencez l'opération :

       .. code-block:: console

          $ cd && touch .emacs

    Cette suite de commandes :

    - télécharge et décompresse le mode nXML,
    - crée une copie de sauvegarde du fichier :file:`.emacs` (:file:`.emacs.bak`),
    - écrit les variables d'environnement du mode nXML dans le fichier :file:`.emacs`.

#.  Téléchargez `l'archive des schémas RelaxNG pour DITA XML`_
    dans le répertoire
    racine de votre projet de documentation |dita|.

#.  Placez-vous dans le répertoire racine de votre projet de documentation |dita|,
    puis collez la commande suivante :

    .. code-block:: console

       $ tar xzvf rnc.tar.gz

    Cette commande crée un répertoire :file:`rnc` de même niveau que le
    *<répertoire de langue>*.

#.  Téléchargez `l'archive des fichiers schemas.xml`_
    dans le répertoire racine de votre projet de documentation |dita|, puis
    collez la suite de commandes ci-dessous en remplaçant *<répertoire de langue>*
    par la valeur appropriée, *en_US*, ou *fr_FR*, par exemple. Répétez cette étape
    pour tous vos répertoires de langue.

    .. code-block:: console

       $ tar xzvf schemas.redaction-technique.org.tar.gz && \
       cd <répertoire de langue> && \
       cp ../schemas.redaction-technique.org/concepts/schemas.xml concepts/ && \
       cp ../schemas.redaction-technique.org/faq/schemas.xml faq/ && \
       cp ../schemas.redaction-technique.org/reference/schemas.xml reference/ && \
       cp ../schemas.redaction-technique.org/tasks/schemas.xml tasks/ && \
       cp ../schemas.redaction-technique.org/tasks/schemas.xml tasks/ && \
       cp ../schemas.redaction-technique.org/topics/schemas.xml topics/ && \
       rm -rf ../schemas.redaction-technique.org/

    Vos répertoires de langue doivent maintenant comporter les fichiers
    :file:`schemas.xml` appropriés :

    - fr_FR

      - concepts

        - schemas.xml

      - concepts

       - schemas.xml

      - faq

       - schemas.xml

      - reference

       - schemas.xml

      - tasks

       - schemas.xml

      - topics

       - schemas.xml

#.  Ouvrez un fichier de contenu |dita| (:file:`.dita`) avec Emacs.  La
    syntaxe |dita| apparaît en couleurs. Les endroits où le schéma n'est pas
    respecté sont soulignés en rouge.

#.  Pour insérer une nouvelle balise entrez <, puis appuyez sur Ctrl+Entrée.  La
    liste des balises possibles apparaît.

#.  Sélectionnez une balise, puis appuyez sur Entrée. Appuyez sur Ctrl+Entrée
    pour afficher la liste des attributs autorisés.

#.  Pour insérer une balise fermante après du texte, entrez </, puis appuyez sur
    Ctrl+Entrée.

.. text review: yes
