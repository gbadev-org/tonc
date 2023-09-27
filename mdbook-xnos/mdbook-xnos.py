import json
import re
import sys

r_prefix = re.compile(r'^# (\w+\.)', flags=re.MULTILINE)
# XXX: mdBook doesn't support attributes on arbitrary elements
# r_def1 = re.compile(r'#(fig|tbl|eq|sec):([\w-]+)')            # Matches #fig:foo
r_def2 = re.compile(r'id="(fig|tbl|eq|sec):([\w-]+)"')          # Matches id="fig:foo"
r_ref1 = re.compile(r'\\?([!+*]?)@(fig|tbl|eq|sec):([\w-]+)')   # Matches @fig:foo
# XXX: mdBook seems to escape bare *
r_ref2 = re.compile(r'{\\?([!+*]?)@(fig|tbl|eq|sec):([\w-]+)}') # Matches {@fig:foo}

def run(section):
    # Other book item (part title or separator)
    if 'Chapter' not in section:
        return

    content = section['Chapter']['content']
    
    prefix = ''

    if section['Chapter']['number'] == None:
        m = r_prefix.search(content)
        if m != None:
            prefix = m.group(1)
    else:
        prefix = str(section['Chapter']['number'][0]) + '.'

    counts = { 'fig': 0, 'tbl': 0, 'eq': 0, 'sec': 0 }

    id_to_num = {}

    def add_id(match):
        kind = match.group(1)
        id = (kind + ':' + match.group(2))
        counts[kind] += 1
        id_to_num[id] = prefix + str(counts[kind])
        
    # for match in r_def1.finditer(content): add_id(match)
    for match in r_def2.finditer(content): add_id(match)

    plus_names = { 'fig': 'fig', 'tbl': 'table', 'eq': 'eq', 'sec': 'section' }
    star_names = { 'fig': 'Fig', 'tbl': 'Table', 'eq': 'Eq', 'sec': 'Section' }

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
        
        # XXX: dead code in original xnos.py?
        # return id_to_num.get(id, fallback)
    
    content = r_ref2.sub(replacefigs, content)
    content = r_ref1.sub(replacefigs, content)

    section['Chapter']['content'] = content

if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)

    for chapter in book['sections']:
        run(chapter)

    print(json.dumps(book))
