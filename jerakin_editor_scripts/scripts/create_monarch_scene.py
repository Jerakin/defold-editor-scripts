from pathlib import Path
import sys

import deftree

gui_script_content = """local monarch = require "monarch.monarch"\n
function init(self)
	msg.post(".", "acquire_input_focus")
end\n
function final(self)
end\n
function update(self, dt)
end\n
function on_message(self, message_id, message, sender)
end\n
function on_input(self, action_id, action)
end\n
function on_reload(self)
end\n
"""

_anchor = Path("/").anchor
def _fix_path(path):
    """We have to remove the anchor if there is one"""
    if path.anchor == _anchor:
        path = Path(str(path)[1:])
    return Path().cwd() / path

def components(name, component):
    root = deftree.Element("components")
    root.add_attribute("id", name)
    root.add_attribute("component", component)
    root.append(vector("position"))
    root.append(vector("rotation", w=1.0))
    return root

def vector(name, x=0.0, y=0.0, z=0.0, w=None):
    root = deftree.Element(name)
    root.add_attribute("x", x)
    root.add_attribute("y", y)
    root.add_attribute("z", z)
    if w:
        root.add_attribute("w", w)
    return root

def embedded_instance(name):
    root = deftree.Element("embedded_instances")
    root.add_attribute("id", name)
    root.add_element("data")
    root.append(vector("position"))
    root.append(vector("rotation", w=1.0))
    root.append(vector("scale3", 1.0, 1.0, 1.0))
    return root

def collection(name, gui_scene):
    tree = deftree.DefTree()
    root = tree.get_root()
    root.add_attribute("name", name)
    root.add_attribute("scale_along_z", 0)
    go = embedded_instance("go")
    data = go.get_element("data")
    data.append(components(name, gui_scene))
    root.append(go)
    return tree

def set_gui_script_path(gui_path, script_path):
    tree = deftree.parse(gui_path)
    root = tree.get_root()
    root.set_attribute("script", script_path.as_posix())
    tree.write()

def main(path):
    path = Path(path)
    absolute_path = _fix_path(path)
    absolute_path.with_suffix(".gui_script").write_text(gui_script_content)
    set_gui_script_path(absolute_path, path.with_suffix(".gui_script"))
    new_collection = collection(path.stem, path.as_posix())
    new_collection.write(absolute_path.with_suffix(".collection"))

if __name__ == '__main__':
    main(sys.argv[-1])

