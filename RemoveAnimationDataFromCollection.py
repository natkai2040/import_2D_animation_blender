import bpy
import sys

########## INPUTS ###########
collection_name = "Frames"
##################

collection = bpy.data.collections.get(collection_name) # get the collection by name

######## CHECKS ##########

if collection: 
    print("found collection:", collection_name)
else: 
    print("did not find collection:", collection_name)
    sys.exit()

###################

for obj in collection.objects:
    clear_animation_data(obj)

def clear_animation_data(target):    
    if target.animation_data:
        target.animation_data_clear()
    print("cleared animation data for",target)