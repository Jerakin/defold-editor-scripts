These scripts have now been moved into their own repositories
https://github.com/Jerakin/editor-script-atlas
https://github.com/Jerakin/editor-script-components
https://github.com/Jerakin/editor-script-monarch

____

# Editor scripts
## Install
You can use the these editor scripts in your own project by adding this project as a [Defold library dependency](https://www.defold.com/manuals/libraries/). Open your game.project file and in the dependencies field under project add:  
https://github.com/Jerakin/defold-editor-scripts/archive/master.zip

### Dependencies
You also need to make sure you have python 3 and [deftree](https://github.com/Jerakin/DefTree) installed.  
You can easily install deftree with  
`pip install deftree`

## Asset Scripts
These scripts are all accessible through the context menu in the asset view, they are context sensitive and will only show when you are clicking on the relevant file.

### `add_to_atlas.editor_script`
This script requires exactly 1 atlas and arbitrary amount of .pngs, it will add all selected images to the selected atlas.

### `create_components.editor_script`
This script adds a few menu items, which shows up depends on the type of file selected. They all create a new resource depending on your selection. A wav or ogg creates a sound component, a selection of .png files will create an atlas containing the selection, a json will create a spine scene.
```
<name>.png          => NEW_ATLAS.atlas  
<name>.wav          => <name>.sound  
<name>.ogg          => <name>.sound  
<name>.json         => <name>.spinescene  
<name>.spinescene   => <name>.spinemodel  
```

### `make_monarch.editor_script`
This script adds a menu option when bringing up the context menu on a gui scene. When used it creates a collection and a gui_script (which adds the "require monarch" and "acquire_input_focus" automatically). It adds the gui_script to the selected gui scene and adds the gui scene to the newly created collection.
