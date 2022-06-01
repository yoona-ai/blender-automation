import sys
import argparse
import bpy

image_filename = ''
object_name = ''
cpu_only = False
transparent_background = False
denoise = False

if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', dest='filename', metavar='FILE')
    parser.add_argument('-o', '--object', dest='object', default='Object', required=False)
    parser.add_argument('-c', '--cpu', dest='use_cpu', type=bool, default=False, required=False)
    parser.add_argument('-t', '--transparent', dest='transparent_background', type=bool, default=False, required=False)
    parser.add_argument('-d', '--denoise', dest='denoise', type=bool, default=False, required=False)
    
    args = parser.parse_known_args(argv)[0]
    # print parameters
    print('filename: ', args.filename)
    print('object name: ', args.object)
    print('cpu only: ', args.use_cpu)
    print('transparent background: ', args.transparent_background)
    print('denoise: ', args.denoise)
    
    image_filename = args.filename
    object_name = args.object
    cpu_only = args.use_cpu
    transparent_background = args.transparent_background
    denoise = args.denoise

if not cpu_only:
    bpy.context.scene.cycles.device = "GPU"
    bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
else:
    print('using cpu only mode') 

# Call get_devices() to let Blender detects GPU device (if any)
bpy.context.preferences.addons["cycles"].preferences.get_devices()

# Let Blender use all available devices, include GPU and CPU
for d in bpy.context.preferences.addons["cycles"].preferences.devices:
    d["use"] = 1

# Display the devices to be used for rendering
print("----")
print("The following devices will be used for path tracing:")
for d in bpy.context.preferences.addons["cycles"].preferences.devices:
    print("- {}".format(d["name"]))
print("----")    

if denoise:
    bpy.context.scene.render.use_motion_blur = True
if transparent_background:
    bpy.context.scene.render.film_transparent = True

shirt = bpy.data.objects[object_name]
materials = shirt.data.materials
mat = materials[0]
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]

texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load(image_filename)
mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])