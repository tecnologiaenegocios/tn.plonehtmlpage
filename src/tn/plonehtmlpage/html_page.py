from plone.directives import form
from tn.plonehtmlpage import _

import zope.interface
import zope.schema


class IHTMLPageSchema(form.Schema):

    title = zope.schema.TextLine(title=_(u'Name'))

    description = zope.schema.Text(
        title=_(u'Description'),
        required=False,
    )

    html = zope.schema.SourceText(
        title=_(u'Raw HTML code'),
    )
