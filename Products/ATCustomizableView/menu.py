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

    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""
        results = PloneDisplayMenu.getMenuItems(self, context, request)

        if ICustomViewMenuLayer.providedBy(request):
    
            # First of all, get the real context of the menu
            context_state = getMultiAdapter((aq_inner(context), request), name=u'plone_context_state')
            is_folder = context_state.is_structural_folder()
            is_folder_default_page = context_state.is_default_page()

            if is_folder:
                folder = context
            elif is_folder or is_folder_default_page:
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
        
                if is_folder_default_page:
                    # give a way to customize view menu for default page in the folder
                    results.append({ 'title' : _(u'label_customization_default_page', default=u'Customize menu (for default page)'),
                             'description'   : _(u'help_customization_default_page',
                                                 default=u'Freeze, change or add menu entries '
                                                         u"for the element used as default view"),
                             'action'        : context.absolute_url()+'/@@customize-viewmenu',
                             'selected'      : False,
                             'icon'          : None,
                             'extra'         : {'id': 'customizeViewMenu', 'separator': '', 'class': ''},
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

