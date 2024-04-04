import png
from png import Reader
import os
from math import inf

SPRIG_COLOR_PALETTE = [([25, 25, 26, 255],0), ([73, 80, 87, 255],'L'), ([145, 151, 156, 255],'1'), 
                       ([248, 249, 250, 255],2), ([235, 44, 71, 255],3), ([139, 65, 46, 255],'C'), 
                       ([25, 177, 248, 255],7), ([19, 21, 224, 255],'5'), ([254, 230, 16, 255],'6'), 
                       ([149, 140, 50, 255],'F'), ([45, 225, 62, 255],4), ([29, 148, 16, 255],'D'), 
                       ([245, 109, 187, 255],8), ([170, 58, 197, 255],'H'), ([245, 113, 23, 255],9), 
                       ([0, 0, 0, 0],'.')]


'''
    - Get the current absolute path
    - Get a list of all files in the "in" folder
    - Convert all files to readable [r,g,b,a] values using pypng and some magic
    - Iterate through each pixel, and find the closest color to the color palette and store its index
    - add the index to the bitmap string
    - place results in the "out" folder
'''

def main():
    main_path = os.path.abspath(__file__).removesuffix('\main.py')
    os.chdir(main_path+'\in')
    sprite_files = list(filter(lambda x : x.endswith('.png'), os.listdir()))
    sprite_colors = list(map(lambda x : convert_to_colors(Reader(x).read_flat()[2]), sprite_files))


    for jdx,s_color in enumerate(sprite_colors):
        bitmap = ''
        cnt = 0
        for idx,pixel in enumerate(s_color):
            n_idx = 0
            #Find index of color in palette
            n_idx = find_closest_color(pixel,SPRIG_COLOR_PALETTE)

            bitmap += str(n_idx)
            if (idx+1)%16 == 0 and idx+1 != 256:
                bitmap += '\n'
            cnt += 1
        
        f_name = sprite_files[jdx].removesuffix('.png')
        os.chdir(main_path+'\out')
        f = open(f'{f_name}.txt', 'w')
        f.write(bitmap)
        f.close()


def convert_to_colors(iterable:any):
    count = 0
    colors = []
    current_color = []
    for c in iterable:
        current_color.append(c)
        count+=1
        if count >= 4:
            colors.append(current_color.copy())
            current_color.clear()
            count = 0
    return colors

'''
Look for exact color match to the palette.
If an exact match doesn't exist, then calculate what the closest color is
and return the closest color
'''
def find_closest_color(cl:list, palette:list): 
    best_match_idx = -1
    best_error = inf
    for p_color in palette:
        same = True
        total_diff = 0
        for x,y in zip(cl, p_color[0]):
            diff = abs(y - x)
            total_diff += diff
            if x != y:
                same = False
        total_diff /= 4
        if same:
            best_match_idx = p_color[1]
            break
        elif total_diff < best_error:
            best_error = total_diff
            best_match_idx = p_color[1]
    return best_match_idx

if __name__ == '__main__':
    main()