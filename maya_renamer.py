"""
<> with <3 by Micha Grandel, talk@michagrandel.de
 
Maya Node Names Cleanup
=======================

This script helps you to cleanup your Node names according to a naming convention.
Currently, three naming conventions are supported:
 
* Prefix (T_Texture, SG_ShadingGroup etc)
* Suffix (Texture_tex, StandardSurface_Mat etc)
* UE Compatible (T_Texture, M_ShadingSurface etc)

Nodes that will be renamed include:

* Shading Groups
* Materials, e.g. StandardSurface
* Textures2D
* place2dTexture (will be called UvCoord)

"""

from pymel.core import *

material_types = ["standardSurface", "lambert"]
shadinggroup_types = ["shadingEngine"]
poly_mesh_types = ["mesh"]

filter_default_materials = lambda mat: True if mat not in ["lambert1", "particleCloud1", "standardSurface1"] else None

USE_PREFIX = "use_prefix"
USE_SUFFIX = "use_suffix"
UE_COMPATIBLE = "ue_compatible"

def Mi_list_all_of_type(types=["mesh"]):
    """ 
    Return a list of objects of type <types>
    
    :param types: list of types to select
    
    :return: list of nodes of the specificied type
    """
    # Ignore default Maya nodes
    ignore_list = ["lambert1", "standardSurface1", "particleCloud1", "shaderGlow1", "defaultRenderLayer", "frontShape", "perspShape", "sideShape", "topShape", "initialParticleSE", "initialShadingGroup"]
    object_list = []
    for node_type in types:
        objects = ls(type=node_type)
        for obj in objects:
            if obj.name() in ignore_list:
                continue
            object_list.append(obj)
    return object_list

def Mi_list_objects_types():
    """ return list of available types """
    return ls(showType=True)

def Mi_renamer(method=None):
    """
    Run to rename ShadingGroups, Textures, and Materials
    """
    # get shading groups
    # shading_groups = filter(lambda x: True if x else False, [obj if obj.name().endswith("SG") else None for obj in list_all_of_type(shadinggroup_types)])
    shading_groups = Mi_list_all_of_type(shadinggroup_types)
    
    # rename shading groups
    for shadinggroup in shading_groups:
        material = [shadinggroup.connections(type=type) for type in material_types][0]
        material = material[0]
        
        # Extract name of shading group
        if material.endswith("_Mat") or material.endswith("_mat"):
            material_name = material[:-4]
        elif material.startswith("M_"):
            material_name = material[2:]
        else:
            material_name = material.name()
        
        new_name = {
            USE_PREFIX: "SG_{}",
            UE_COMPATIBLE: "M_{}"
        }.get(method, "{}SG").format(material_name.capitalize())
        
        print("Rename {} to {}".format(shadinggroup.name(), new_name))
        shadinggroup.rename(new_name)
        
    
    # get materials
    materials = ls(materials=True)
    materials = filter(filter_default_materials, materials)
    materials = filter(lambda mat: not mat.endswith("_Mat"), materials)
    
    # rename materials
    for material in materials:
        material_name = material.name()
        if material.name().endswith("_Mat") or material.name().endswith("_mat"):
            material_name = material.name()[:-4]
        elif material.name().startswith("M_"):
            material_name = material.name()[2:]
            
        new_name = "M_{}".format(material_name.capitalize()) if method == USE_PREFIX else "{}_Mat".format(material_name.capitalize())
            
        print("Rename {} to {}".format(material.name(), new_name))
        print(material.rename(new_name))
    
    # get textures
    textures = ls(textures=True)
    
    # rename textures
    for texture in textures:
        texture_name = texture.name()
        if texture.name().endswith("_Tex") or texture.name().endswith("_tex"):
            texture_name = texture.name()[:-4]
        elif texture.name().startswith("T_"):
            texture_name = texture.name()[2:]
            
        new_name = "{}_Tex".format(texture_name.capitalize()) if method == USE_SUFFIX else "T_{}".format(texture_name.capitalize())
        
        print("Rename {} to {}".format(texture.name(), new_name))
        
    # get place2dTexture
    place2dTextures = Mi_list_all_of_type(types=["place2dTexture"])
    for place2d_texture in place2dTextures:
        new_name = "UvCoord"
        print("Rename {} to {}".format(place2d_texture.name(), new_name))

def main(method=USE_PREFIX):
    Mi_renamer(method)

if __name__ == '__main__':
    main(method=UE_COMPATIBLE)