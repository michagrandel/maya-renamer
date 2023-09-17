# Maya Renamer

This script helps you to cleanup your Node names 
by renaming Maya Nodes automatically according to 
a naming convention.

## How it works

Currently, the following nodes are supported:

* Texture2D
* Materials (e.g. StandardSurface or lambert)
* ShadingGroups
* place2Dtextures

There are three different Naming conventions implemented:

* **Prefix**: T_Textures, M_Materials, SG_ShadingGroups, UvCoords
* **Suffix**: Texture_tex, Material_mat, ShadingGroup_SG, UvCoords
* **UE Compatible**: T_Textures, Materials_Mat, M_ShadingGroups, UvCoords

## Requirements

This script requires pymel installed.

## Installation

### Step 1

Copy the scripts into your Maya Script directory. After that, restart Maya. 
To find your maya script directory, open up the Script Editor in Maya and 
run the following MEL-command:

```internalVar -usd;```

**Default locations** *Replace &lt;version&gt; with your Maya Version*:

- Windows: `%USERPROFILE%\Documents\maya\<version>\scripts`
- Mac: `~/Library/Preferences/Autodesk/Maya/<version>/scripts`
- Linux: `~/Maya/<version>/scripts`

## Usage

### GUI

Press one of the rename buttons in the newly generated
Project-Shelf.

### Script Editor

Run the following script in your script editor:
```
import maya_renamer
renamer()  # default: PREFIX
```

To select the method, run one of the following commands:
```
import maya_renamer
renamer(maya_renamer.USE_PREFIX)     # using PREFIX naming convention
renamer(maya_renamer.USE_SUFFIX)     # using SUFFIX naming convention
renamer(maya_renamer.UE_COMPATIBLE)  # using UE Compatiblity naming convention
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first 
to discuss what you would like to change.

## License

Copyright 2023 Micha Grandel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
