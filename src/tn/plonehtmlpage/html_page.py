from five import grok
from Products.CMFCore.utils import getToolByName
from plone.directives import form
from tn.ploneformwidget.sourcecode import SourceCodeFieldWidget
from tn.plonehtmlpage import _
from z3c.form import widget

import zope.interface
import zope.schema


class IHTMLPageSchema(form.Schema):

    title = zope.schema.TextLine(title=_(u'Name'))

    description = zope.schema.Text(
        title=_(u'Description'),
        required=False,
    )

    form.widget(html=SourceCodeFieldWidget)
    html = zope.schema.SourceText(
        title=_(u'Raw HTML code'),
    )


class ViewRawHTML(grok.View):
    grok.context(IHTMLPageSchema)
    grok.require('zope2.View')

    def render(self):
        return self.context.html


class View(grok.View):
    grok.context(IHTMLPageSchema)
    grok.require('zope2.View')

    def update(self):
        portal_url = getToolByName(self.context, 'portal_url')()
        base_resources_path = portal_url + '/++resource++tn.plonehtmlpage/'

        self.frame_id = u'frame-%s' % self.context.__name__
        self.iframe_height_js_url = base_resources_path + 'iframe-height.js'
        self.stylesheet_url = base_resources_path + 'default.css'


mode_adapter = widget.StaticWidgetAttribute(u'html',
                                            field=IHTMLPageSchema['html'])
