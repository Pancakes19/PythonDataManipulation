import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Painting practice
features = pd.read_csv('mondrian-painting-features.csv')
painting_info = pd.read_csv('mondrian-painting-info.csv')
print(painting_info)

b104_features = features.query('painting_id == "b104"')
# print(b104_features)

# ok now we are gonna draw a painting with the info from features df
# using a function




def draw_mondrian( painting_id):
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval("x + width").max()
    total_height = rects.eval("y + height").max()
    
    fig, ax = plt.subplots()
    
    for (idx, row) in rects.iterrows():
        x, y, w, h, rgb = row[['x','y','width','height','rgb']]
        patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
        ax.add_patch(patch)
    
    ax.axis([0, total_width, 0, total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.text(0.5, 0.01, painting_id, ha="center", fontsize=14)
    plt.show()
    
draw_mondrian("b294")
