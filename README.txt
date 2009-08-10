Products.ATCustomizableView
===========================

Overview
--------

A simple Plone product based on monkeypatch to enhance a little the basic Plone control
on the default view of contents.
Applying some Zope properties to contents you can enhance (or limit) the power of users
able to manage views.

For every content of the portal you can block the user ability to change layouts on a
single document/folder, instead of having this feature only for the whole content-class.
This is simply done adding a new boolean property (**fixed_layout**) set to *True*.
When this is done, users can't change the default view (or select folder contents as
default view) on this object.
Removing this property (or set this to **False**) will restore normal behaviour.

Again, you can add custom, addition view to a single content. You only need to a new
(lines) property called **fixed_additional_layouts** to the content. Every additional
views on this list will be added to basic views avaiable.

Of course you can block and not inherits default views but use only the news ones.
To do this just add another (boolean) property called **purge_basic_layouts** and set it
to *True*.

All those features can be very useful on many Plone sites.

* You can set a (non standard?) view to a single content and make the user not able
  to change your choice.
* You can force a stardard view on a content, but again make users not able to change
  this.
* You can develop a new view compatible with some content type, but can choice to not
  make it avaiable for all content types of the portal. Instead of force this new view
  to the content you can leave again the choice to the power user that normally manage
  the "views" menu.

Without this product, too often a Plone developer is forced to develop new, silly content
types just for only provide different views policy.

Requirements
------------

Monkeypatch approach is dangerous, `collective.monkeypatcher`__ is now required in
your buildout.

__ http://pypi.python.org/pypi/collective.monkeypatcher/

::

    [instance]
    ...
    eggs =
        ...
        Products.ATCustomizableView
        collective.monkeypatcher
        collective.monkeypatcherpanel
    ...
    
    zcml =
        ...
        Products.ATCustomizableView
        collective.monkeypatcher
        collective.monkeypatcherpanel
    ...

Tutorial
--------

This `first version`__ of the product has been written related to a
`tutorial on Plone.it`__ (italian language!).

__ http://pypi.python.org/pypi/Products.ATCustomizableView/0.1.0
__ http://www.plone.it/scopri/documentazione/how-to/controllo-at-default-view-in-plone

TODO
----

* What about leave the old ZMI property approach and move to some other technology
  like Zope3 interfaces, annotations, ?
* In any case give to the user a Plone form for managing per-object configuration.
