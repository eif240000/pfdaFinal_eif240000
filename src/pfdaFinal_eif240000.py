import maya.cmds as cmds
import os

def texturesPath():
    path = cmds.fileDialog2(dialogStyle=2, caption="Select texture directory", fileMode=3)
    if not path:
        cmds.warning("Operation cancelled.")


def dialogBox():
    shaderName = cmds.promptDialog(
		title='Specify Shader Name',
		button=['OK', 'Cancel'],
		cancelButton='Cancel',
		message='Enter Shader Name:'
    )

    if shaderName == 'OK':
        userInput = cmds.promptDialog(query=True, text=True)
        return userInput
    else:
        cmds.warning("Operation cancelled.")
        
 
def createAiStand(name):
    createShader = cmds.shadingNode('aiStandardSurface', asShader=True, name=name)
    return createShader

def main():
    userPath = texturesPath()
    if not userPath:
        return None
    customName = dialogBox()
    if not customName:
        return None
    createShader = createAiStand(customName)

    
if __name__ == "__main__":
    main()