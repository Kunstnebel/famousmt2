import uiScriptLocale

LOCALE_PATH = "d:/ymir work/ui/buttons_new/"

SIZE_X = 380
SIZE_Y = 329

WIDTH = (SCREEN_WIDTH/2) - (SIZE_X/2)
HEIGHT = (SCREEN_HEIGHT/2) - (SIZE_Y/2)

window = {
	"name" : uiScriptLocale.BOX_SEARCH_NAME,
	"style" : ("movable", "float",),
	
	"x" : WIDTH,
	"y" : HEIGHT,

	"width" : SIZE_X,
	"height" : SIZE_Y,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : SIZE_X,
			"height" : SIZE_Y,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 5,
					"y" : 5,

					"width" : SIZE_X-10,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-2, "text":uiScriptLocale.BOX_SEARCH_NAME, "all_align":"center" },
					),
				},
				{
					"name" : "thinboard_0",
					"type" : "thinboard_circle",
					"style" : ("attach",),
					"x" : 12,
					"y" : 32,

					"width" : 145,
					"height" : 150,
					"children":
					(
						{
							"name" : "bg_slots",
							"type" : "image",
							"x": 8,
							"y": 10,
							"image":"d:/ymir work/ui/ChestSystem/ChestSystemslot_bg.tga",
						},
						{
							"name" : "ItemSlot",
							"type" : "slot",
							"x" : 56,
							"y" : 63,
							"width": 32,
							"height": 32,
							"slot" : 
							(
								{
									"index":0, "x":0, "y":0, "width":32, "height":32,
								},
							),
						},
						{
							"name":"ItemName",
							"type": "text",
							"x":22,
							"y":22,
							"text":"",
						}
					),
				},
				{
					"name" : "thinboard_1",
					"type" : "thinboard_circle",
					"style" : ("attach",),
					"x" : 160,
					"y" : 32,
					"width" : 207,
					"height" : 283,
				},
				{
					"name" : "thinboard_2",
					"type" : "window",
					"x" : 12,
					"y" : 32+220,
					"width" : 145,
					"height" : 63,
					"children":
					(
						{
							"name" : "next_button", 
							"type" : "button",
							"x" : 100, "y" : 0-6,
							"default_image" : LOCALE_PATH + "private_next_btn_01.sub",
							"over_image" : LOCALE_PATH + "private_next_btn_02.sub",
							"down_image" : LOCALE_PATH + "private_next_btn_01.sub",
						},
						{
							"name" : "last_next_button", "type" : "button",
							"x" : 120, "y" : 0-6,

							"default_image" : LOCALE_PATH + "private_last_next_btn_01.sub",
							"over_image" : LOCALE_PATH + "private_last_next_btn_02.sub",
							"down_image" : LOCALE_PATH + "private_last_next_btn_01.sub",
						},
						{
							"name" : "prev_button", "type" : "button",
							"x" : 34, "y" : 0-6,

							"default_image" : LOCALE_PATH + "private_prev_btn_01.sub",
							"over_image" : LOCALE_PATH + "private_prev_btn_02.sub",
							"down_image" : LOCALE_PATH + "private_prev_btn_01.sub",
						},
						{
							"name" : "last_prev_button", "type" : "button",
							"x" : 12, "y" : 0-6,

							"default_image" : LOCALE_PATH + "private_first_prev_btn_01.sub",
							"over_image" : LOCALE_PATH + "private_first_prev_btn_02.sub",
							"down_image" : LOCALE_PATH + "private_first_prev_btn_01.sub",
						},
					),
				},
				{
					"name" : "AceptButton",
					"type" : "button",
					"x" : 9,
					"y" : 186,
					"text" : uiScriptLocale.BOX_SEARCH_SEARCH,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "LimpiarButton",
					"type" : "button",
					"x" : 9,
					"y" : 186+30,
					"text" : uiScriptLocale.BOX_SEARCH_CLEAN,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "AbrirButton2",
					"type" : "button",
					"x" : 9,
					"y" : 294-30,
					"text" : uiScriptLocale.BOX_SEARCH_OPEN,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "AbrirButton",
					"type" : "button",
					"x" : 9,
					"y" : 294,
					"text" : uiScriptLocale.BOX_SEARCH_OPEN_ALL,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
			),
		},
	),
}