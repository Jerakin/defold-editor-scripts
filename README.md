# Editor scripts

## Dependencies

python 3 exposed in your environment variables (being able to run `python` from the commandline)  
python package `deftree`, install it with `pip install deftree`

## Asset Scripts
Accessible through the context menu in the asset view.

### Add to Atlas
This script requires exactly 1 atlas and arbitrary amount of .pngs, it will add all selected images to the selected atlas.

### Create Component
This script takes a resource (filtered inside of the script, it will always be visble) and creates a component next to it.
```
<name>.png          => NEW_ATLAS.atlas  
<name>.wav          => <name>.sound  
<name>.json         => <name>.spinescene  
<name>.spinescene   => <name>.spinemodel  
```
