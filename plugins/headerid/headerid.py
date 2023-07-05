from pelican import readers
from pelican.readers import PelicanHTMLTranslator
from pelican import signals
from docutils import nodes

LINK_CHAR = '*'


def init_headerid(sender):
    global LINK_CHAR
    char = sender.settings.get('HEADERID_LINK_CHAR')
    if char:
        LINK_CHAR = char

def register():
    signals.initialized.connect(init_headerid)

    class HeaderIDPatchedPelicanHTMLTranslator(PelicanHTMLTranslator):
        def visit_title(self, node):
            # print(self)
            parent = node.parent
            if (
                isinstance(parent, nodes.section) and
                parent.hasattr('ids') and
                parent['ids']
                # not node.hasattr('refid')
            ):
                #
                # Same as `PelicanHTMLTranslator.visit_title` for section nodes,
                # except it turns regular headers into links.
                #
                # It also intentially _does not_ generate links back to the table
                # of contents, since I don't want those.
                #
                h_level = self.section_level + self.initial_header_level - 1
                atts = {}
                if (len(node.parent) >= 2 and isinstance(node.parent[1], nodes.subtitle)):
                    atts['CLASS'] = 'with-subtitle'
                self.body.append(self.starttag(node, 'h%s' % h_level, '', **atts))
                anchor_name = parent['ids'][0]
                self.body.append('<a class="headerlink" href="#%s">' % (anchor_name))
                self.context.append('</a></h%s>\n' % (h_level))
            else:
                PelicanHTMLTranslator.visit_title(self, node)
        
        # def depart_title(self, node):
        #     self.visit_title(node)
        #     close_tag = self.context[-1]
        #     parent = node.parent
        #     if isinstance(parent, nodes.section) and parent.hasattr('ids') and parent['ids']:
        #         anchor_name = parent['ids'][0]
        #         # add permalink anchor
        #         if close_tag.startswith('</h'):
        #             self.body.append(
        #                 '<a class="headerlink" href="#%s" title="Permalink to this headline">%s</a>' %
        #                 (anchor_name, LINK_CHAR))
        #     PelicanHTMLTranslator.depart_title(self, node)
    
    readers.PelicanHTMLTranslator = HeaderIDPatchedPelicanHTMLTranslator
