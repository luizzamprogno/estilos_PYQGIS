layers = iface.mapCanvas().layers()
diretorio =  'C:/Local/Dos/Estilos/estilos.qml'
nomesLayersEstilos = []

def define_styles(style):
	layer.loadNamedStyle(diretorio + style)
	renderer = layer.renderer()
	myRenderer = renderer.clone()
	layer.setRenderer(myRenderer)
	layer.triggerRepaint()

for nome in layers:
	nomesLayersEstilos.append(nome.name())

for layer, estilo in zip(layers, nomesLayersEstilos):
	define_styles(estilo + '.qml')
