# Title
pfdaFinal_eif240000
## Repository
https://github.com/eif240000/pfdaFinal_eif240000

## Description
This program will be able to create an aiStandardSurface node and connect the 
relevant maps to their respective channels. It may assist artist as it will
remove the tedium of manually importing and connecting nodes.

## Features
- Feature 1
	- The ability to read and import the correct maps. I could use a for loop with
  elif, else, and if statements to find or omit maps that aren't found.
- Feature 2
	- The ability to send out a warning messages using try/except strings for 
  any maps that are missing.

## Challenges
- Learning Maya's commands necessary for texturing.
- Learning how to make Maya connect, delete, and create nodes.
- Making sure that Maya connects the correct maps to the correct channels.

## Outcomes
Ideal Outcome:
- The program creates an aiStandardSurface and potentially an aiNormalMap 
or displacementShader depending what maps are present in a directory and connects
then to the correct channels while also sending out warning messages for missing
maps.

Minimal Viable Outcome:
- The program can create an aiStandardSurface node and connect the base color to
the correct channel.

## Milestones

- Week 1
  1. Learn the commands Maya uses to create, delete and connect nodes as well
  as how Maya selects directory paths.
  2. Conduct tests to make sure I'm using Maya's commands correctly.
  3. Implement the ability for the program to find and read the correct maps.

- Week 2
  1. The program should be able to import maps based on their naming convention.
  2. Attempt to create nodes using Python.

- Week 3 
  1. Create the correct nodes for displacement and normal maps.
  2. Connect all maps to the correct channels on the correct nodes.

- Week 4 (Final)
  1. Delete unnecessary 'place2dtexture' nodes and connect all other maps to
  one main 'place2dtexture' node.
  2. Conduct final debugging, making sure the program works correctly.
