nuke.pluginAddPath( '/Volumes/GBPROD01/Departments/.Nuke/gizmos' )
nuke.pluginAddPath( '/Volumes/GBPROD01/Departments/.Nuke/python' )
nuke.pluginAddPath( '/Volumes/GBPROD01/Departments/.Nuke/plugins' )
nuke.pluginAddPath('./X_Tools')
nuke.pluginAddPath('./X_Tools/Icons')
nuke.pluginAddPath('./X_Tools/Gizmos')
#nuke.pluginAddPath('/Users/msquires/Documents/gizmos2')

import collectFiles
import ReadFromWrite

nuke.ViewerProcess.register("Jag_XF", nuke.Node, ('JAG_XF_LUT_viewerprocess',''))
nuke.ViewerProcess.register("FLIP", nuke.Node, ('FLIP_viewerprocess',''))
nuke.ViewerProcess.register("LOG", nuke.Node, ('LOG_viewerprocess',''))
nuke.ViewerProcess.register("GrainCheck", nuke.Node, ('GrainCheck_viewerprocess.gizmo',''))
nuke.ViewerProcess.register("SAT10", nuke.Node, ('SAT10_viewerprocess.gizmo',''))

#DEFAULT SETTINGS
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}")
nuke.knobDefault("Roto.outputMask", "rgba.alpha")
nuke.knobDefault("Roto.format", "Tangerine")


#Project Settings

tang = '3200 1800 Tangerine'
nuke.addFormat( tang )
nuke.knobDefault("Root.format", "Tangerine")
nuke.knobDefault("Root.fps", "25")



#nuke.pluginAddPath('/Users/msquires/Downloads/pw_tools_latest_/pw_tools')

def createWriteDir(): 
  import nuke, os, errno
  file = nuke.filename(nuke.thisNode())
  dir = os.path.dirname( file )
  osdir = nuke.callbacks.filenameFilter( dir )
  # cope with the directory existing already by ignoring that exception
  try:
    os.makedirs( osdir )
  except OSError, e:
    if e.errno != errno.EEXIST:
      raise
nuke.addBeforeRender(createWriteDir)
