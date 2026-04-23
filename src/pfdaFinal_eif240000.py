import maya.cmds as cmds
import os

#def textures_path():
    #baseColor = ["basecolor", "albedo", "diffuse", "color"]
    #path = cmds.fileDialog2(dialogStyle=2, caption="Select texture directory", fileMode=3)
    #if not path:
       #cmds.warning("Operation cancelled")

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

def create_nodes(name):
    shader = cmds.shadingNode('aiStandardSurface', asShader=True, name=name)
    place_2d = cmds.shadingNode('place2dTexture', asUtility=True)
    diffuse_tex = cmds.shadingNode('file', asTexture=True, name="diffuse_TEX")
    
    cmds.connectAttr(place_2d + ".outUV", diffuse_tex + ".uvCoord")
    cmds.connectAttr(place_2d + ".outUvFilterSize", diffuse_tex + ".uvFilterSize")
    cmds.connectAttr(diffuse_tex + ".outColor", shader + ".baseColor")
    return create_nodes

def main():
   #user_path = textures_path()
   #if not user_path:
       #return None
   custom_name = dialog_box()
   if not custom_name:
        return None
   create_shader = create_nodes(custom_name)

    
if __name__ == "__main__":
    main()