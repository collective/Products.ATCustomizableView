# -*- coding: utf-8 -*-

from OFS.interfaces import IFolder

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
    
    def back_url(self):
        """Calc the back_url, so is less confusing"""
        context = self.context
        if context.hasProperty('default_page'):
            return context.absolute_url() + '/' + context.getProperty('default_page')
        return context.absolute_url() + '/view'
    
    def isFolder(self):
        return IFolder.providedBy(self.context)
  
    def values(self):
        """Get the values to be displayed in the form"""
        form = self.request.form
        context = self.context
        values = {
                  'fixed_layout': form.get('fixed_layout') or context.getProperty('fixed_layout') or False,
                  'fixed_additional_layouts': form.get('fixed_additional_layouts') or context.getProperty('fixed_additional_layouts') or [], 
                  'purge_basic_layouts': form.get('purge_basic_layouts') or context.getProperty('purge_basic_layouts') or False,
                  'layout': form.get('layout') or self.context.getProperty('layout') or '',
                  'default_page': form.get('default_page') or self.context.getProperty('default_page', '') or '',
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

        if form.get('layout'):
            if not context.hasProperty('layout'):
                context.manage_addProperty('layout', form.get('layout'), 'string')
            else:
                context.manage_changeProperties({'layout': form.get('layout')})
        else:
            if context.hasProperty('layout'):
                context.manage_delProperties(ids=['layout'])
            
        if form.get('default_page'):
            if not context.hasProperty('default_page'):
                context.manage_addProperty('default_page', form.get('default_page'), 'string')
            else:
                context.manage_changeProperties({'default_page': form.get('default_page')})
        else:
            if context.hasProperty('default_page'):
                context.manage_delProperties(ids=['default_page'])


        