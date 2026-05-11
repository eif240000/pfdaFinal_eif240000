import maya.cmds as cmds
import os

def user_path():
    path = cmds.fileDialog2(dialogStyle=2, caption="Select texture directory", fileMode=3)
    if not path:
       cmds.warning("Operation cancelled")
    return path[0]
       
def find_textures(path, keywords):
    if not path:
        return None
    
    for file in os.listdir(path):
        lower = file.lower()
        for name in keywords:
            if name in lower:
                return os.path.join(path, file)
    return None
                
def find_diffuse(path):
    diffuse_names = ["basecolor", "albedo", "diffuse", "color"]
    return find_textures(path, diffuse_names)
    
def find_roughness(path):
    roughness_names = ["roughness", "rough", "gloss", "spec", "specular"]
    return find_textures(path, roughness_names)
    
def find_normal(path):
    normal_names = ["normal", "norm", "nrm"]
    return find_textures(path, normal_names)
    
def find_metalness(path):
    metalness_names = ["metalness","metal", "metallic"]
    return find_textures(path, metalness_names)

def dialog_box():
    shader_name = cmds.promptDialog(
		title='Specify Shader Name',
		button=['OK', 'Cancel'],
		cancelButton='Cancel',
		message='Enter Shader Name:'
    )

    if shader_name == 'OK':
        user_input = cmds.promptDialog(query=True, text=True)
        return user_input
    else:
        cmds.warning("Operation cancelled")

def create_nodes(name, diffuse_path, roughness_path, metalness_path, normal_path):
    shader = cmds.shadingNode('aiStandardSurface', asShader=True, name=name)
    place_2d = cmds.shadingNode('place2dTexture', asUtility=True)
    normal_map = cmds.shadingNode('aiNormalMap', asUtility=True)
    diffuse_tex = cmds.shadingNode('file', asTexture=True, name="diffuse_TEX")
    roughness_tex = cmds.shadingNode('file', asTexture=True, name="roughness_TEX")
    metal_tex = cmds.shadingNode('file', asTexture=True, name="metal_TEX")
    normal_tex = cmds.shadingNode('file', asTexture=True, name="normal_TEX")
    
    
    cmds.setAttr(diffuse_tex + ".fileTextureName", diffuse_path, type="string")
    cmds.setAttr(normal_tex + ".fileTextureName", normal_path, type="string")
    cmds.setAttr(roughness_tex + ".fileTextureName", roughness_path, type="string")
    cmds.setAttr(metal_tex + ".fileTextureName", metalness_path, type="string")
    
    cmds.connectAttr(place_2d + ".outUV", diffuse_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", diffuse_tex + ".uvFilterSize")
    
    cmds.connectAttr(place_2d + ".outUV", roughness_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", roughness_tex + ".uvFilterSize") 
  
    cmds.connectAttr(place_2d + ".outUV", metal_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", metal_tex + ".uvFilterSize")    
  
    cmds.connectAttr(place_2d + ".outUV", normal_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", normal_tex + ".uvFilterSize") 
  
    cmds.connectAttr(diffuse_tex + ".outColor", shader + ".baseColor")
    cmds.connectAttr(roughness_tex + ".outAlpha", shader + ".specularRoughness")
    cmds.connectAttr(metal_tex + ".outAlpha", shader + ".metalness")
    cmds.connectAttr(normal_tex + ".outColor", normal_map + ".input")
    cmds.connectAttr(normal_map + ".outValue", shader + ".normalCamera")
    
    return shader

def main():
   custom_name = dialog_box() 
   if not custom_name:
       return None
       
   custom_path = user_path()
   if not custom_path:
       return None
       
   diffuse_path = find_diffuse(custom_path)
   roughness_path = find_roughness(custom_path)
   metalness_path = find_metalness(custom_path)
   normal_path = find_normal(custom_path)     
   create_nodes(custom_name, diffuse_path, roughness_path, metalness_path, normal_path)

    
if __name__ == "__main__":
    main()