
# Defines the main GUI installer
class InstallerDefinition:	
	def __init__(self):
		self.tabs = []
		self.buttons = []
	
	def set_title(self, title, show=True):
		if show: self.title = title
		return self

	def set_logo(self, logo, show=True):
		#TODO validates file existence
		if show: self.logo = logo
		return self
		
	def tab(self, label, show = True):		
		tab = _Tab(label, self)
		if show:
			self.tabs.append(tab)
		return tab
		
	def button(self, label, img, callback):
		button = _Button(label, img, callback)
		self.buttons.append(button)
		return self
		
	# iteration
	def checkboxes(self):
		cbs = []
		for tab in self.tabs:
			for group in tab.groups:
				for checkbox in group.checkboxes:
					cbs.append(checkbox)
		return cbs
		
	def comboboxes(self):
		cbs = []
		for tab in self.tabs:
			for group in tab.groups:
				for combobox in group.comboboxes:
					cbs.append(combobox)
		return cbs
	
	def textfields(self):
		tfs = []
		for tab in self.tabs:
			for group in tab.groups:
				for textfield in group.textfields:
					tfs.append(textfield)
		return tfs
				
class _Tab:
	def __init__(self, label, program):
		self.label = label
		self.program = program
		self.groups = []
		
	def toptext(self, text, platform='all'):
		self.text = text
		return self
	
	def group(self, label, show=True):
		group = _Group(label, self)
		if show: self.groups.append(group)
		return group
		
	def done(self):
		return self.program

class _Group:
	def __init__(self, label, top):
		self.label = label
		self.top = top
		self.checkboxes = []
		self.comboboxes = []
		self.textfields = []
		self.orientation = 'vertical'

	def checkbox(self, label, command, checked=False, show=True):
		checkbox = _CheckBox(label, command, checked, self)
		if show: self.checkboxes.append(checkbox)
		return self
		
	def combobox(self, label, options, command, selected, show=True):
		combo = _ComboBox(label, options, command, selected)
		if show: self.comboboxes.append(combo)
		return self
		
	def textfield(self, label, value, command, show=True):
		t = _TextField(label, value, command)
		if show: self.textfields.append(t)
		return self
	
	def horizontal(self):
		self.orientation = 'horizontal'
		return self

	def vertical(self):
		self.orientation = 'vertical'
		return self
			
	def done(self):
		return self.top
		
class _CheckBox:
	def __init__(self, label, command, checked, top):
		self.label = label
		self.command = command
		self.checked = checked
		self.top = top
		
class _ComboBox:
	def __init__(self,label, options, command, selected):
		self.label = label
		self.options = options.split(' ')
		self.options.sort()
		self.selected = selected
		self.command = command
		
class _TextField:
	def __init__(self, label, value, command):
		self.label = label
		self.value = value
		self.command = command
		
class _Button:
	def __init__(self, label, img, callback):
		self.label = label
		self.img = img
		self.callback = callback
		
