import ui
import uiToolTip
import mouseModule
import player
import item
import chat
import net
import localeInfo
import grp 
from _weakref import proxy
import wndMgr
import uiScriptLocale

class UiChestLoader(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.curPage = 1
		self.MaxPage = 2
		self.use_item = 0
		self.items=[]
		self.count =[]

		self.vnum = None
		self.index = None
		self.pos = None
		self.slotpos = None
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.__OnLimpiar()

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/chest_window.py")
		except:
			import exception
			exception.Abort("UiChestLoader.LoadWindow")

		try:
			self.bg = self.GetChild("board")
			self.prev_button = self.GetChild("prev_button")
			self.last_prev_button = self.GetChild("last_prev_button")
			self.next_button = self.GetChild("next_button")
			self.last_next_button = self.GetChild("last_next_button")
			self.slot = self.GetChild("ItemSlot")
			self.item_name = self.GetChild("ItemName")
			self.aceptar = self.GetChild("AceptButton")
			self.abrir = self.GetChild("AbrirButton")
			self.abrir2 = self.GetChild("AbrirButton2")
			self.limpiar = self.GetChild("LimpiarButton")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
		except:
			import exception
			exception.Abort("UiChestElements.LoadWindow")

		self.prev_button.SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_RIGHT')
		self.last_prev_button.SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_RIGHT_LAST')
		self.next_button.SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_LEFT')
		self.last_next_button.SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_LEFT_LAST')
		self.slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.aceptar.SetEvent(self.__OnAcept)
		self.abrir.SetEvent(self.__OnAbrir)
		self.abrir2.SetEvent(self.__OnAbrir2)
		self.limpiar.SetEvent(self.__OnLimpiar)


		self.Box = UiChestBox()
		self.Box.Open(self.bg,175,50)
		self.Box.Show()
		self.ButtonsHide()

	def ButtonsHide(self):
		self.prev_button.Hide()
		self.last_prev_button.Hide()
		self.next_button.Hide()
		self.last_next_button.Hide()


	def Information(self,vnums,counts):
		self.items.append(int(vnums))
		self.count.append(int(counts))

	def Page(self):
		self.Box.Hide()		
		self.Box.ClearList()

		self.use_item = 1

		for a in xrange(min(self.MaxPage, len(self.items) - self.curPage * self.MaxPage +self.MaxPage)):
			curId = self.items[a + (self.curPage - 1)*self.MaxPage]
			curCount = self.count[a + (self.curPage - 1)*self.MaxPage]
			self.Box.SetContent(curId,curCount,a)
			self.Box.Show()

		if self.curPage *self.MaxPage >= len(self.items):
			self.next_button.Hide()
			self.last_next_button.Hide()
		else:
			self.next_button.Show()
			self.last_next_button.Show()

		if self.curPage > 1:
			self.prev_button.Show()
			self.last_prev_button.Show()
		else:
			self.prev_button.Hide()
			self.last_prev_button.Hide()

	def __OnClickArrow(self, arrow):
		Left_Last = self.WFunction(float(len(self.items))/float(self.MaxPage))

		if arrow == 'MOSTBOUGHT_LEFT':
			self.curPage += 1
			self.Page()
		elif arrow == 'MOSTBOUGHT_LEFT_LAST':
			self.curPage = Left_Last
			self.Page()
		elif arrow == 'MOSTBOUGHT_RIGHT':
			self.curPage -= 1
			self.Page()
		elif arrow == 'MOSTBOUGHT_RIGHT_LAST':
			self.curPage = 1
			self.Page()

	def WFunction(self, num):
		if (num + 1) != int(num+1):
			return int(num+1)
		else:
			return int(num)

	def __OnSelectEmptySlot(self, selectedSlotPos):
		self.index,self.pos=None,None
		self.__OnLimpiar()
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

			mouseModule.mouseController.DeattachObject()
			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
			count = player.GetItemCount(attachedInvenType, attachedSlotPos)
				
			itemVNum = player.GetItemIndex(attachedInvenType, attachedSlotPos)
			item.SelectItem(itemVNum)

		self.slot.ClearSlot(selectedSlotPos)
		self.slot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
		self.index = player.GetItemIndex(attachedSlotPos)
		self.pos = attachedSlotPos
		self.slotpos=selectedSlotPos
		self.vnum = player.GetItemIndex(attachedSlotPos)
		self.item_name.SetText(item.GetItemName())


	def __OnSelectItemSlot(self, selectedSlotPos):
		self.__OnLimpiar()		

	def __OnAcept(self):
		if self.pos == None:
			chat.AppendChat(1, uiScriptLocale.BOX_SEARCH_NOITEM)
			return
		if self.use_item == 1:
			return
		net.SendChatPacket("/search_cofres search %s"%(self.pos))

	def __OnAbrir(self):
		if self.pos == None:
			chat.AppendChat(1, uiScriptLocale.BOX_SEARCH_NOOPEN)
			return

		net.SendChatPacket("/search_cofres all %s"%(self.pos))
		
	def __OnAbrir2(self):
		if self.pos == None:
			chat.AppendChat(1, uiScriptLocale.BOX_SEARCH_NOOPEN)
			return

		net.SendChatPacket("/search_cofres open %s"%(self.pos))

	def RefreshOpen(self):
		self.slot.SetItemSlot(self.slotpos, player.GetItemIndex(self.pos), player.GetItemCount(self.pos))
		if player.GetItemCount(self.pos) == 0:
			self.__OnLimpiar()

	def __OnLimpiar(self):
		self.items=[]
		self.count =[]
		self.curPage = 1
		self.index,self.pos,self.vnum=None,None,None
		self.Box.Hide()		
		self.Box.ClearList()
		self.slot.ClearSlot(0)	
		self.item_name.SetText("")
		self.ButtonsHide()
		self.use_item = 0


	def OverInItem(self, slotIndex):
		if (mouseModule.mouseController.isAttached()):
			return
			
		if (self.tooltipItem != 0):
			self.tooltipItem.SetInventoryItem(self.pos)
			
	def OverOutItem(self):
		if (self.tooltipItem != 0):
			self.tooltipItem.HideToolTip()

	def Close(self):
		self.__OnLimpiar()
		wndMgr.Hide(self.hWnd)

	def OnPressEscapeKey(self):
		self.Close()
		return True



class UiChestBox(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.name_items = {}
		self.icon_items = {}
		self.bg_items = {}
		self.count_items = {}
		self.list_items = []

		self.tooltipItem = uiToolTip.ItemToolTip()
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/chest_boxitems.py")

		except:
			import exception
			exception.Abort("UiChestBox.LoadWindow")

		try:
			for i in xrange(0,2):
				self.bg_items[i] = self.GetChild("CofresBoxItemsBg%s"%i)
				self.name_items[i] = self.GetChild("CofresBoxItemsName%s"%i)
				self.icon_items[i] = self.GetChild("CofresBoxItemsIcon%s"%i)
				self.icon_items[i].OnMouseOverIn= lambda selfArg = self, index = i: selfArg.OverInItem(index)
				self.icon_items[i].OnMouseOverOut = lambda selfArg = self, index = i: selfArg.OverOutItem(index)
				self.count_items[i] = self.GetChild("CofresBoxItemsCount%s"%i)
				self.bg_items[i].Hide()
		except:
			import exception
			exception.Abort("UiChestBoxElement.LoadWindow")


	def SetContent(self, vnum, count, index):
		item.SelectItem(vnum)
		self.icon_items[index].LoadImage(item.GetIconImageFileName())
		self.list_items.append(vnum)
		self.bg_items[index].Show()

		if vnum == 1:
			self.name_items[index].SetText(item.GetItemName()+": "+str(count))
			self.count_items[index].SetText("1")
			return

		if vnum == 2:
			self.name_items[index].SetText("Exp: "+str(count))
			self.count_items[index].SetText("1")
			return
		
		self.name_items[index].SetText(item.GetItemName())
		self.count_items[index].SetText(str(count))


	def OverInItem(self,index):
		if int(self.list_items[index]) == 1 or int(self.list_items[index]) == 2:
			return

		self.tooltipItem.ClearToolTip()
		self.tooltipItem.AddItemData(int(self.list_items[index]),0,0,0,0,0,1)
			
	def OverOutItem(self,index):
		self.tooltipItem.Hide()

	def Open(self, parent, x, y):
		if FALSE == self.isLoaded:
			self.LoadWindow()

		self.SetParent(parent)
		self.SetPosition(x,y)
		self.Show()

	def ClearList(self):
		self.list_items=[]
		for i in xrange(0,2):
			self.bg_items[i].Hide()
