from markdown.inlinepatterns import InlineProcessor
from markdown.treeprocessors import Treeprocessor
from markdown.blockprocessors import BlockProcessor
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
import xml.etree.ElementTree as etree
import re


class XNosPreprocessor(Preprocessor):
    def run(self, lines):
        
        r_prefix = re.compile(r'^# (\w+\.)')
        r_def = re.compile(r'#(fig|tbl|eq|sec):([\w-]+)')
        r_ref1 = re.compile(r'\\?([!+*]?)@(fig|tbl|eq|sec):([\w-]+)')
        r_ref2 = re.compile(r'{([!+*]?)@(fig|tbl|eq|sec):([\w-]+)}')
        
        # If the page heading is "# 12. Some Chapter" then "12." is used as a prefix.
        prefix = ''
        for i, s in enumerate(lines):
            m = r_prefix.match(s)
            if m != None:
                prefix = m.group(1)
                break
        # assert(prefix != None)
        
        # Find all defined figure IDs and assign them a figure number.
        
        counts = {
            'fig': 0,
            'tbl': 0,
            'eq': 0,
        }
        id_to_num = {} # e.g. "fig:foo": "12.1"
        
        for i, s in enumerate(lines):
            for match in r_def.finditer(s):
                kind = match.group(1)
                id = (kind + ':' + match.group(2))
                counts[kind] += 1
                id_to_num[id] = prefix + str(counts[kind])
        
        # Replace references to figure IDs with the appropriate figure number.
        
        plus_names = {
            'fig': 'fig',
            'tbl': 'table',
            'eq': 'eq',
        }
        star_names = {
            'fig': 'Fig',
            'tbl': 'Table',
            'eq': 'Eq',
        }
        
        clever_refs = True
        clever_names = plus_names
        
        def replacefigs(match):
            op = match.group(1)
            kind = match.group(2)
            id = (kind + ':' + match.group(3))
            if id in id_to_num:
                num = id_to_num[id]
                if clever_refs:
                    if op == '!': return num
                    elif op == '+': return plus_names[kind] + ' ' + num
                    elif op == '*': return star_names[kind] + ' ' + num
                    else: return clever_names[kind] + ' ' + num
                else:
                    if op == '+': return plus_names[kind] + ' ' + num
                    elif op == '*': return star_names[kind] + ' ' + num
                    else: return num
            else:
                return match.group(0) # fallback, don't do any replacement
            
            return id_to_num.get(id, fallback)
        
        for i, s in enumerate(lines):
            s = r_ref2.sub(replacefigs, s)
            s = r_ref1.sub(replacefigs, s)
            lines[i] = s
        
        return lines


# Extension which ties together all of the above.

class XNosExtension(Extension):
    def extendMarkdown(self, md):        
        md.preprocessors.register(XNosPreprocessor(md), name = 'xnos', priority = 179)
