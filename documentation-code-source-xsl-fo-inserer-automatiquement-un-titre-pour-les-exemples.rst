.. Copyright 2011-2015 Olivier Carrère
.. Cette œuvre est mise à disposition selon les termes de la licence Creative
.. Commons Attribution - Pas d'utilisation commerciale - Partage dans les mêmes
.. conditions 4.0 international.

.. code review: yes

.. _xsl-fo-inserer-automatiquement-un-titre-pour-les-exemples:

XSL-FO : insérer automatiquement un titre pour les exemples
===========================================================

Par défaut, |dita-ot| n'insère pas automatiquement dans les fichiers
PDF le texte *Exemple :* devant le titre d'un exemple contenu entre balises |dita|
:samp:`<example>`. La syntaxe `XSL-FO`_
offre cependant cette possibilité.

Supposons que le code source d'un de vos fichiers |dita| soit le suivant :

.. code-block:: xml

   <example>
     <title>
       XSL-FO
     </title>
     Voici mon exemple de chemin XPATH :
     <codeblock>
       ancestor-or-self
     </codeblock>
   </example>

Vous souhaitez que le fichier PDF généré affiche l'exemple structuré comme
suit :

   **Exemple : XSL-FO**

   Voici mon exemple de chemin XPATH :

   .. code-block:: xslt

      ancestor-or-self

et que si l'exemple ne contient pas de titre, il soit structuré comme suit :

   **Exemple :**

   Voici mon exemple de chemin XPATH :

   .. code-block:: xslt

      ancestor-or-self

Par défaut, cependant, ce contenu sera structuré comme suit dans le PDF par
|dita-ot| :

   **XSL-FO**

   Voici mon exemple de chemin XPATH :

   .. code-block:: xslt

      ancestor-or-self

Il est toujours possible d'entrer le texte entre les balises :samp:`<example>`, mais
XSL-FO offre une manière de procéder plus élégante et structurée.

Insérer automatiquement une variable de texte avant le titre des exemples
-------------------------------------------------------------------------

#. Remplacez dans la feuille de style
   :file:`plugins/org.dita.pdf2/xsl/fo/commons.xsl` (sous |dita-ot|
   1.7.)  le template suivant :

   .. code-block:: xslt

      <xsl:template match="*[contains(@class,' topic/example')]/*
      [contains(@class,' topic/title ')]>
        <fo:block xsl:use-attribute-sets="example.title>
          <xsl:call-template name="commonattributes"/>
          <xsl:apply-templates/>
        </fo:block>
      </xsl:template>

   par le code suivant :

   .. code-block:: xslt

      <xsl:template match="*[contains(@class,' topic/example ')]>
        <fo:block xsl:use-attribute-sets="example.title>
          <xsl:call-template name="insertVariable>
            <xsl:with-param name="theVariableID" select="'my-example-text'"/>
          </xsl:call-template>
          <xsl:apply-templates select="title"/>
        </fo:block>
        <fo:block>
          <xsl:apply-templates select="*[not(contains(@class, ' topic/title'))]
          |text()|processing-instruction()"/>
        </fo:block>
      </xsl:template>

#. Définissez dans les fichiers contenant les variables de langue, tels que
   :file:`plugins/org.dita.pdf2/cfg/common/vars/fr.xml`, les variables de texte
   à insérer automatiquement, par exemple :

   .. code-block:: xslt

      <variable id="my-example-text>Exemple :</variable>

Pour obtenir un comportement homogène, vous devez désactiver ce traitement
pour les exemples des types de *topics* spécifiques (*task*,
notamment).

.. text review: yes
