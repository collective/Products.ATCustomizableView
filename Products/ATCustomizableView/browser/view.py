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
    
    def _save(self, form):
        """Save customization chages"""
        