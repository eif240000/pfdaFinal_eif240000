import maya.cmds as cmds
import os

def dialog():
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
        return None

def createAiStand(name):
    createShader = cmds.shadingNode('aiStandardSurface', asShader=True, name=name)
    return createShader

def main():
    customName = dialog()
    createShader = createAiStand(customName)
    
if __name__ == "__main__":
    main()