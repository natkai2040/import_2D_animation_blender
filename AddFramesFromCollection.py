import bpy
import sys


########## INPUTS ###########
frameobj_collection_name = "Frames" 
initial_frame = 0
frameobj_order = [0, 1, 2, 3]
frame_switches = [initial_frame, 5, 10, 15] #frame switches on 1

obj = bpy.context.object # selected object is targetted.
##################

frameobjs = bpy.data.collections.get(frame_collection_name) # get the collection by name

######## CHECKS ##########
if frameobjs: 
    print("found collection:", frameobjs.objects)
else: 
    print("did not find collection:", frame_collection_name)
    sys.exit()
if obj:
    print("found obj: ", obj)
else: 
    print("no object selected") 
    sys.exit()
if len(frameobj_order) != len(frame_switches):
    print("frameobj_order should be equal to frame_switches")
    sys.exit()

###################

def transfer_animation_data(source, target):
    if source and target: 
        if source.animation_data:
            target.animation_data_create() # create animation data in target
            
            target.animation_data.action = (source.animation_data.action).copy() # transfer action
            print("tranferring data from ", source, " to ", target)
        else: 
            print("source has no animation data")
    else: 
        print("source or target nonexistent")
        
def make_invisible(target, _frame): 
    
    bpy.context.scene.frame_set(_frame) # set frame to _frame
    
    target.hide_render = True # hide render at this frame
    target.keyframe_insert(data_path="hide_render", frame=_frame) # add keyframe
    
    target.hide_viewport = True # hide render at this frame
    target.keyframe_insert(data_path="hide_viewport", frame=_frame)
    
    print("made", target, "invisible at ", _frame)
    
def make_visible(target, _frame): 
    bpy.context.scene.frame_set(_frame) 
    
    target.hide_render = False # show render 
    target.keyframe_insert(data_path="hide_render", frame=_frame)
    
    target.hide_viewport = False # show render at this frame
    target.keyframe_insert(data_path="hide_viewport", frame=_frame)
    
    print("made", target, "visible at ", _frame)

def clear_animation_data(target):    
    if target.animation_data:
        target.animation_data_clear()
    print("cleared animation data for",target)

###################


for frameobj in frameobjs.objects:
    clear_animation_data(frameobj)
    transfer_animation_data(obj, frameobj)

# make everything but [0] invisible on frame [0], make everything but [1] invisible on frame [1]

for visible_idx in range(0, len(frameobj_order)): # 0,1,2,3...
    
    for frameobj in frameobjs.objects: 
        # gets the object at placement "place" in the order
        if frameobj == frameobjs.objects[frameobj_order[visible_idx]]: # this is the visible one
            make_visible(frameobj, frame_switches[visible_idx]) # make invisible this frame
        else: 
            make_invisible(frameobj, frame_switches[visible_idx])# make invisible this frame    
