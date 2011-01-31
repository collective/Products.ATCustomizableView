Introduction
============

This product can change the behaviour of the Plone's "*Display*" menu, making it a little
customizable. Those customization are *not* content type related, but are done for a
single content.

For every specific content of the portal:

* You can block ability of your authors to change content's layouts.
* You can add custom, additional, views to a content.
* You can hide all standard available layout for a content, leaving only the new customized
  ones.

.. image:: http://keul.it/images/plone/Products.ATCustomizableView-0.4.0-01.png
   :alt: The menu customization form

User cases
----------

 `Why freeze the content layout?`
     Sometimes you need to apply a new view to a single content, like a folder.
     For example: you have a folder where you know is used only for *News Item* contents
     and you have a quite good view for this folder.
     
     Registering this view for all Folder content types will give to your author the choice
     to use this view also in other section of the site, but you don't want it.
     A views pollution in the "*Display*" menu can be confusing.
 `Why adding new entry in the menu`
     Keep in mind that you are adding new views to a single content of your site.
     
     For example: you have developed a new view for the *Page* and you want optionally leave
     to your authors to use or not this view in the home-page sub-sections of your site.
     
     Like above, registering this view for the Page content types will leave to authors the
     choice to use this view for *all* page of the site but, for design choice, you want to
     use this view only for some specific pages. 
 `Why dropping base views`
     No much to say, may be you don't want to inherit the content types views and don't want
     that your authors are able to use them.

Simplification for developers
-----------------------------

Behaviour described above can be reach also developing additional content types. However I found
not very useful developing silly content type or marker interfaces only for obtaining additional
layout.

If you like more older versions of ATCustomizableView
-----------------------------------------------------

I got some (good) criticism about releases of ATCustomizableView that started to display Plone UI,
even if those changes were in the TODO for a long time.

If you liked older versions, where you were forced to go to ZMI, simply remove to *all user roles* the
*Customize menu: view* permission. Also to Manager.

After that you can continue working only using ZMI properties tab!

Installation
============

Add "Products.ATCustomizableView" to the egg section of your buildout configuration file.

For Plone versions 3.2 or lower, remember the zcml section::

    zcml =
        ...
        Products.ATCustomizableView
        Products.ATCustomizableView-overrides

TODO
====

* Thinking about moving to the approach used for `redturtle.custommenu.factories`__, as soon as
  the per-object menu customization will be moved out of the product.

__ http://plone.org/products/redturtle.custommenu.factories

