# Sprig-PNG-To-Bitmap-Converter
 Converts 16x16 sprites in a png format to the bitmap string that Sprig uses to store sprite data. And don't worry, if a color on the sprite doesn't have a place in Sprig's color palette, the program will replace it with the closest color on the palette.

 <h1>INSTRUCTIONS</h1>
 <ul>
  <li> First, make sure you have the pypng package installed. Open the command prompt and enter the following: python -m pip install git+https://gitlab.com/drj11/pypng@pypng-0.20220715.0 </li>
  <li> After it's installed, place any 16x16 sprite pngs you would like to convert inside the "in" folder. </li>
  <li> Next, go back to the command prompt and open the directory that the main.py file is located. </li>
  <li> In the command prompt, type the following: python main.py </li>
  <li> The converted bitmap will then be in the "out" folder</li>
 </ul>
