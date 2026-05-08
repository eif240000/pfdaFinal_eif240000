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
    diffuse_tex = cmds.shadingNode('file', asTexture=True, name="diffuse_TEX")
    
    cmds.setAttr(diffuse_tex + ".fileTextureName", diffuse_path, type="string")
    
    cmds.connectAttr(place_2d + ".outUV", diffuse_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", diffuse_tex + ".uvFilterSize")
    cmds.connectAttr(diffuse_tex + ".outColor", shader + ".baseColor")
    return shader

def main():
   custom_name = dialog_box()
   if not custom_name:
       return None
   custom_path = user_path()
   if not custom_path:
       return None
   user_diffuse = find_diffuse(custom_path)
   create_nodes(custom_name, user_diffuse)

    
if __name__ == "__main__":
    main()