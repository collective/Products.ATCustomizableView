# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from Products.ATCustomizableView import custommenuMessageFactory as _

class CustomizeViewMenuView(BrowserView):
    """The view for customizing "View" menu"""

    template = ViewPageTemplateFile("customize-viewmenu.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.request.set('disable_border', True)

    def __call__(self, *args, **kw):
        request = self.request
        if request.get('save'):
            self._save(request.form)
            context = self.context
            putils = getToolByName(context, 'plone_utils')
            putils.addPortalMessage(_(u'Changes saved'))
            request.response.redirect(context.absolute_url() + '/@@customize-viewmenu')
            return
        return self.template()
    
    def values(self):
        """Get the values to be displayed in the form"""
        form = self.request.form
        context = self.context
        values = {
                  'fixed_layout': form.get('fixed_layout') or context.getProperty('fixed_layout') or False,
                  'fixed_additional_layouts': form.get('fixed_additional_layouts') or context.getProperty('fixed_additional_layouts') or [], 
                  'purge_basic_layouts': form.get('purge_basic_layouts') or context.getProperty('purge_basic_layouts') or False,
                  }
        return values
    
    def _save(self, form):
        """Save customization chages.
        This method remove empty values so the uninstallation of the product is simpler.
        """
        context = self.context
        if form.get('fixed_layout'):
            if not context.hasProperty('fixed_layout'):
                context.manage_addProperty('fixed_layout', True, 'boolean')
        else:
            if context.hasProperty('fixed_layout'):
                context.manage_delProperties(ids=['fixed_layout'])
        if [x for x in form.get('fixed_additional_layouts') if x]:
            if not context.hasProperty('fixed_additional_layouts'):
                context.manage_addProperty('fixed_additional_layouts', form.get('fixed_additional_layouts'), 'lines')
            else:
                context.manage_changeProperties({'fixed_additional_layouts': form.get('fixed_additional_layouts')})
        else:
            if context.hasProperty('fixed_additional_layouts'):
                context.manage_delProperties(ids=['fixed_additional_layouts'])
        if form.get('purge_basic_layouts'):
            if not context.hasProperty('purge_basic_layouts'):
                context.manage_addProperty('purge_basic_layouts', True, 'boolean')
        else:
            if context.hasProperty('purge_basic_layouts'):
                context.manage_delProperties(ids=['purge_basic_layouts'])
            


        