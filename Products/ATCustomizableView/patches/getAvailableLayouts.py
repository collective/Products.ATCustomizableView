# -*- coding: utf-8 -*-

import zope.component
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

originalGetAvailableLayouts = BrowserDefaultMixin.getAvailableLayouts

def cvGetAvailableLayouts(self):
    """Add any additional available layouts listed in the fixed_additional_layouts property
    Also ignore basic layout if the purge_basic_layouts property is set.
    """
    purge_basic_layouts = self.getProperty('purge_basic_layouts', False)
    fixed_additional_layouts = self.getProperty('fixed_additional_layouts', None)
    if fixed_additional_layouts is None:
        # Even if empty, I wanna fixed_additional_layouts to be required
        return originalGetAvailableLayouts(self)
    if purge_basic_layouts:
        basic_layouts = []
    else:
        basic_layouts = list(originalGetAvailableLayouts(self))
    return basic_layouts + _getViewMenuFormatLayouts(self, fixed_additional_layouts)

def _getViewMenuFormatLayouts(self, method_ids):
    """Code taken from the original getAvailableLayouts of browserdefault"""
    result = []
    for mid in method_ids:
        view = zope.component.queryMultiAdapter((self, self.REQUEST),
                                                zope.interface.Interface,
                                                name=mid)
        if view is not None:
            menu = zope.component.getUtility(
                IBrowserMenu, 'plone_displayviews')
            item = menu.getMenuItemByAction(self, self.REQUEST, mid)
            title = item and item.title or mid
            result.append((mid, title))
        else:
            method = getattr(self, mid, None)
            if method is not None:
                # a method might be a template, script or method
                try:
                    title = method.aq_inner.aq_explicit.title_or_id()
                except AttributeError:
                    title = mid
                result.append((mid, title))
    return result
