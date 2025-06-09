import os
import re

outline = '''
life_sim/
├── core/
│   ├── grid.py         # World and cell representation
│   ├── agent.py        # Biot logic and minimal scripting
│   ├── sim.py          # Simulation loop and updates
├── ui/
│   └── viewer_stub.py  # Placeholder; polls slices from sim
├── data/
│   └── saves/          # State dumps
├── run.py              # Entry point for the engine
└── config.py           # Constants and tweakables
'''

def parse_outline(outline_text):
    path_stack = []
    base_indent = None
    paths = []

    for line in outline_text.splitlines():
        if not line.strip():
            continue

        # Extract indentation level and path info
        match = re.match(r'^([ │├└─]*)[├└]──\s*(.+)$', line)
        if not match:
            match = re.match(r'^([ ]*)([^│├└─].+)$', line)
        if not match:
            continue

        indent, item = match.groups()
        item = item.strip().split(' ')[0]  # remove comment

        level = indent.count('│') + indent.count(' ') // 4
        if base_indent is None:
            base_indent = level
        level -= base_indent

        # Adjust path stack
        path_stack = path_stack[:level]
        path_stack.append(item)
        paths.append(os.path.join(*path_stack))

    return paths

def create_structure(paths, root_dir='.'):
    for path in paths:
        full_path = os.path.join(root_dir, path)
        if path.endswith('/'):
            os.makedirs(full_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(full_path, 'a').close()

# Usage
paths = parse_outline(outline)
create_structure(paths)



