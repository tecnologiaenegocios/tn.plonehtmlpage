from five import grok
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


class ViewRaw(grok.View):
    grok.context(IHTMLPageSchema)
    grok.require('zope2.View')
    grok.name('view-raw')

    def render(self):
        return self.context.html


mode_adapter = widget.StaticWidgetAttribute(u'html',
                                            field=IHTMLPageSchema['html'])
