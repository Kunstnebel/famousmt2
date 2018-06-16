import ui
import wndMgr

class SideBar(ui.Board):
	def __init__(self):
		ui.Board.__init__(self)
		
		self.ExpandBtn = ui.Button()
		self.ExpandBtn.SetParent(self)
		self.ExpandBtn.SetPosition(138, 0)
		self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga")
		self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga")
		self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga")
		self.ExpandBtn.SetEvent(self.ToggleMinimize)
		self.ExpandBtn.Show()
		
		self.btns = []
		self.minimized = 1
	
	def AddButton(self, text, event):
		height = len(self.btns) * 26
		wndHeight = max(108, 52 + height)
		self.SetSize(140, wndHeight)
		self.SetPosition(-126, (wndMgr.GetScreenHeight() - wndHeight) / 2)
		self.ExpandBtn.SetPosition(126, (wndHeight - 108) / 2)
		btn = ui.Button()
		btn.SetParent(self)
		btn.SetPosition(35, 15 + height)
		btn.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btn.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btn.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btn.SetText(text)
		btn.SetEvent(event)
		btn.Show()
		self.btns.append(btn)

	def __del__(self):
		ui.Board.__del__(self)

	def Destroy(self):
		self.Hide()
		for obj in self.btns:
			obj.Hide()
			obj = None
		del self.btns[:]
		self.btns = None

	def OnUpdate(self):
		if self.minimized == 1:
			(x, y) = self.GetGlobalPosition()
			if x > -126:
				self.SetPosition(max(-126, x - 4), (wndMgr.GetScreenHeight() - (30 + len(self.btns) * 26)) / 2)
		else:
			(x, y) = self.GetGlobalPosition()
			if x < -25:
				self.SetPosition(min(-25, x + 4), (wndMgr.GetScreenHeight() - (30 + len(self.btns) * 26)) / 2)

	def ToggleMinimize(self):
		if self.minimized == 1:
			self.minimized = 0
			self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga")
			self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga")
			self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga")
		else:
			self.minimized = 1
			self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga")
			self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga")
			self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga")

