import maya.cmds as cmds
import os

def user_path():
    path = cmds.fileDialog2(dialogStyle=2, caption="Select texture directory", fileMode=3)
    if not path:
       cmds.warning("Operation cancelled")
    return path[0]
       
def find_diffuse(path):
    diffuse_names = ["basecolor", "albedo", "diffuse", "color"]
    
    for file in os.listdir(path):
        lower = file.lower()
        
        for name in diffuse_names:
            if name in lower:
                return os.path.join(path, file)
    
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

def create_nodes(name, diffuse_path):
    shader = cmds.shadingNode('aiStandardSurface', asShader=True, name=name)
    place_2d = cmds.shadingNode('place2dTexture', asUtility=True)
    normal_map = cmds.shadingNode('aiNormalMap', asUtility=True)
    diffuse_tex = cmds.shadingNode('file', asTexture=True, name="diffuse_TEX")
    roughness_tex = cmds.shadingNode('file', asTexture=True, name="roughness_TEX")
    metal_tex = cmds.shadingNode('file', asTexture=True, name="metal_TEX")
    normal_tex = cmds.shadingNode('file', asTexture=True, name="normal_TEX")
    
    cmds.setAttr(diffuse_tex + ".fileTextureName", diffuse_path, type="string")
    
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
   user_diffuse = find_diffuse(custom_path)
   if not user_diffuse:
       cmds.warning("No diffuse texture found")
       return None
   create_nodes(custom_name, user_diffuse)

    
if __name__ == "__main__":
    main()