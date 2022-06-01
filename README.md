# blender-automation

## introduction
Small proof of concept, how a generic 3d object modelled in Blender and the right UV map can be used, to apply shirts to it via script.

## requirements
To be able to use it, you have to have installed blender on your machine

## how to use it
```
blender -b models/shirt.blend --python change-image.py --render-output '/Users/manzked/workspaces/yoona/blender-automation/samples/output/shirt01-render##.png' --render-frame 1 -- -f '/Users/manzked/workspaces/yoona/blender-automation/samples/input/shirt01.png' -o 'Object'
```

### cli parameters
**-b** to run Blender in background

**--python** for the script to execute

**--render-output** full qualified path where the image is stored (should include ## to control the name ## -> zero'ed frame number)

**--render-frame** how many frames (default 1)

**--** as the separator for further parameters which are used by the script

**-f** full qualified path for the file to be used for the texture

**-o** name of the node, where the image has to be replaced (default 'Object')

**-t** True, for a transparent background (default False)

**-d** True, for denoising (default False)

**-c** if cpu only mode, should be used for rendering

alternative --cycles-device CPU to adress cycles engine directly

# further reading, what is possible
https://docs.blender.org/manual/en/latest/advanced/command_line/render.html

https://github.com/yuki-koyama/blender-cli-rendering
