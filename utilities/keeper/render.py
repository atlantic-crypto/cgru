import json

import af

import cmd

WndInfo = None

from PyQt4 import QtCore, QtGui

def showInfo( tray = None):
	renders = af.Cmd().renderGetLocal()

	if renders is None or len( renders) == 0:
		if tray is not None: tray.showMessage('Render information:', 'No local render client founded.')
		return

	global WndInfo

	WndInfo = QtGui.QTextEdit()
	WndInfo.setPlainText( json.dumps( renders[0], sort_keys=True, indent=4))
	WndInfo.setReadOnly( True)
	WndInfo.resize( WndInfo.viewport().size())
	WndInfo.setWindowTitle('AFANASY Render Information:')
	WndInfo.show()

#def getParameter( data, parm, default):
#	if parm in data:#
#		return data[parm]
#	return default

def refresh():
	renders = af.Cmd().renderGetLocal()
	if renders is not None and len( renders):
		render = renders[0]
		#print( render)
#		online = not getParameter( render, 'offline', False)
#		nimby = getParameter( render, 'nimby', False)
#		NIMBY = getParameter( render, 'NIMBY', False)
#		busy = getParameter( render, 'busy', False)
		online = render["state"].find('OFF') == -1
		nimby  = render["state"].find('NbY') != -1
		NIMBY  = render["state"].find('NBY') != -1
		busy   = render["state"].find('RUN') != -1
		cmd.Tray.showRenderIcon( online, nimby or NIMBY, busy)
	else: cmd.Tray.showIcon()
