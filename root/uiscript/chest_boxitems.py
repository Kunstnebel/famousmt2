import uiScriptLocale

SIZE_X = 110
SIZE_Y = 240

WIDTH = (SCREEN_WIDTH/2) - (SIZE_X/2)
HEIGHT = (SCREEN_HEIGHT/2) - (SIZE_Y/2)


window = {
	"name" : "UiChestBoxItems",
	
	"x" : WIDTH,
	"y" : HEIGHT,	

	"width" : SIZE_X,
	"height" : SIZE_Y,
	
	"children" :
	(
		{"name": "CofresBoxItemsBg0","type": "image","x": 0-5,"y": 0-12,"image":"d:/ymir work/ui/ChestSystem/slot_icon_new.tga","children":(
		{"name": "CofresBoxItemsIcon0","type": "image","x": 11,"y": 20,"image":"icon/item/00010.tga",},
		{"name": "CofresBoxItemsName0","type": "text","x":55,"y":24,"text":"Cookie1337",},
		{"name": "CofresBoxItemsCount0","type": "text","x":136,"y":46,"text":"0",},),},

		{"name": "CofresBoxItemsBg1","type": "image","x": 0-5,"y": 128,"image":"d:/ymir work/ui/ChestSystem/slot_icon_new.tga","children":(
		{"name": "CofresBoxItemsIcon1","type": "image","x": 11,"y": 20,"image":"icon/item/00010.tga",},
		{"name": "CofresBoxItemsName1","type": "text","x":55,"y":24,"text":"Cookie1337",},
		{"name": "CofresBoxItemsCount1","type": "text","x":136,"y":46,"text":"0",},),},
		
	),
}