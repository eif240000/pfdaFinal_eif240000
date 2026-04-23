import maya.cmds as cmds
import os

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
    customName = dialogBox()
    if not customName:
        return None
    createShader = createAiStand(customName)

    
if __name__ == "__main__":
    main()