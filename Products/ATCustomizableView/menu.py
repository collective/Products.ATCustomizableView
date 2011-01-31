# -*- coding: utf-8 -*-

from Acquisition import aq_inner, aq_parent
from zope.interface import implements
from zope.component import getMultiAdapter

from OFS.interfaces import IFolder

from plone.memoize.instance import memoize

from plone.app.contentmenu.menu import DisplayMenu as PloneDisplayMenu
from plone.app.contentmenu.menu import DisplaySubMenuItem as PloneDisplaySubMenuItem
from plone.app.contentmenu.interfaces import IDisplayMenu, IDisplaySubMenuItem

from Products.CMFCore.utils import getToolByName
from Products.ATCustomizableView import custommenuMessageFactory as _
from Products.ATCustomizableView.interfaces import ICustomViewMenuLayer

class DisplayMenu(PloneDisplayMenu):
    implements(IDisplayMenu)

    # Stolen from ploneview
    def isFolderOrFolderDefaultPage(self, context, request):
        context_state = getMultiAdapter((aq_inner(context), request), name=u'plone_context_state')
        return context_state.is_structural_folder() or context_state.is_default_page()

    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""
        results = PloneDisplayMenu.getMenuItems(self, context, request)

        if ICustomViewMenuLayer.providedBy(request):
    
            # First of all, get the real context of the menu
            if IFolder.providedBy(context):
                folder = context
            elif self.isFolderOrFolderDefaultPage(context, request):
                folder = aq_parent(aq_inner(context))
            else:
                # don't know how to handle this
                folder = context

            member = getToolByName(context, 'portal_membership').getAuthenticatedMember()
            if member.has_permission('Customize menu: view', context):
                results.append({ 'title' : _(u'label_customization', default=u'Customize menu'),
                         'description'   : _(u'help_customization', default=u'Freeze, change or add menu entries'),
                         'action'        : folder.absolute_url()+'/@@customize-viewmenu',
                         'selected'      : False,
                         'icon'          : None,
                         'extra'         : {'id': 'customizeViewMenu', 'separator': 'actionSeparator', 'class': ''},
                         'submenu'       : None,
                         })
        
        return results


class DisplaySubMenuItem(PloneDisplaySubMenuItem):
    implements(IDisplaySubMenuItem)
    
    @memoize
    def available(self):
        context = self.context
        member = getToolByName(context, 'portal_membership').getAuthenticatedMember()
        if member.has_permission('Customize menu: view', context):
            return True
    
        return PloneDisplaySubMenuItem.available(self)

