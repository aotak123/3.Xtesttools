window.skins=window.skins||{};
                var __extends = this && this.__extends|| function (d, b) {
                    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
                        function __() {
                            this.constructor = d;
                        }
                    __.prototype = b.prototype;
                    d.prototype = new __();
                };
                window.generateEUI = window.generateEUI||{};
                generateEUI.paths = generateEUI.paths||{};
                generateEUI.styles = undefined;
                generateEUI.skins = {"eui.Button":"resource/eui_skins/ButtonSkin.exml","eui.CheckBox":"resource/eui_skins/CheckBoxSkin.exml","eui.HScrollBar":"resource/eui_skins/HScrollBarSkin.exml","eui.HSlider":"resource/eui_skins/HSliderSkin.exml","eui.Panel":"resource/eui_skins/PanelSkin.exml","eui.TextInput":"resource/eui_skins/TextInputSkin.exml","eui.ProgressBar":"resource/eui_skins/ProgressBarSkin.exml","eui.RadioButton":"resource/eui_skins/RadioButtonSkin.exml","eui.Scroller":"resource/eui_skins/ScrollerSkin.exml","eui.ToggleSwitch":"resource/eui_skins/ToggleSwitchSkin.exml","eui.VScrollBar":"resource/eui_skins/VScrollBarSkin.exml","eui.VSlider":"resource/eui_skins/VSliderSkin.exml","eui.ItemRenderer":"resource/eui_skins/ItemRendererSkin.exml","HeadItem":"resource/eui_skins/HeadItem.exml","StartItem":"resource/eui_skins/StartItem.exml","OverItem":"resource/eui_skins/OverItem.exml","SignItem":"resource/eui_skins/SignItem.exml","MissionItem":"resource/eui_skins/MissionItem.exml","SoundDialog":"resource/eui_skins/SoundDialog.exml","ErrorView":"resource/eui_skins/ErrorView.exml","PictureItem":"resource/eui_skins/PictureItem.exml","BubbleItem":"resource/eui_skins/BubbleItem.exml","GuessLevelItem":"resource/eui_skins/GuessLevelItem.exml","GuessOverItem":"resource/eui_skins/GuessOverItem.exml","RankItem":"resource/eui_skins/RankItem.exml","TreeGetDialog":"resource/eui_skins/TreeGetDialog.exml","LevelGroupItem":"resource/eui_skins/LevelGroupItem.exml","GuessGroupItem":"resource/eui_skins/GuessGroupItem.exml","RankItemRenderer":"resource/eui_skins/RankItemRenderer.exml","CardTypeItem":"resource/eui_skins/CardTypeItem.exml","RobotITipItem":"resource/eui_skins/RobotITipItem.exml","CardImageItem":"resource/eui_skins/CardImageItem.exml","PKGameUI":"resource/eui_skins/PKGameUI.exml","PKWord":"resource/eui_skins/PKWord.exml","PKMenuUI":"resource/eui_skins/PKMenuUI.exml","PKMatchUI":"resource/eui_skins/PKMatchUI.exml","PKBonusView":"resource/eui_skins/PKBonusView.exml","ConfirmView":"resource/eui_skins/ConfirmView.exml","EqualView":"resource/eui_skins/EqualView.exml","PKFriendUI":"resource/eui_skins/PKFriendUI.exml","InvitePKTip":"resource/eui_skins/InvitePKTip.exml"};generateEUI.paths['resource/eui_skins/ButtonSkin.exml'] = window.skins.ButtonSkin = (function (_super) {
	__extends(ButtonSkin, _super);
	function ButtonSkin() {
		_super.call(this);
		this.skinParts = ["labelDisplay","iconDisplay"];
		
		this.minHeight = 50;
		this.minWidth = 100;
		this.elementsContent = [this._Image1_i(),this.labelDisplay_i(),this.iconDisplay_i()];
		this.states = [
			new eui.State ("up",
				[
				])
			,
			new eui.State ("down",
				[
					new eui.SetProperty("_Image1","source","button_down_png")
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("_Image1","alpha",0.5)
				])
		];
	}
	var _proto = ButtonSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(1,3,8,8);
		t.source = "button_up_png";
		t.percentWidth = 100;
		return t;
	};
	_proto.labelDisplay_i = function () {
		var t = new eui.Label();
		this.labelDisplay = t;
		t.bottom = 8;
		t.left = 8;
		t.right = 8;
		t.size = 20;
		t.textAlign = "center";
		t.textColor = 0xFFFFFF;
		t.top = 8;
		t.verticalAlign = "middle";
		return t;
	};
	_proto.iconDisplay_i = function () {
		var t = new eui.Image();
		this.iconDisplay = t;
		t.horizontalCenter = 0;
		t.verticalCenter = 0;
		return t;
	};
	return ButtonSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/CheckBoxSkin.exml'] = window.skins.CheckBoxSkin = (function (_super) {
	__extends(CheckBoxSkin, _super);
	function CheckBoxSkin() {
		_super.call(this);
		this.skinParts = ["labelDisplay"];
		
		this.elementsContent = [this._Group1_i()];
		this.states = [
			new eui.State ("up",
				[
				])
			,
			new eui.State ("down",
				[
					new eui.SetProperty("_Image1","alpha",0.7)
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("_Image1","alpha",0.5)
				])
			,
			new eui.State ("upAndSelected",
				[
					new eui.SetProperty("_Image1","source","checkbox_select_up_png")
				])
			,
			new eui.State ("downAndSelected",
				[
					new eui.SetProperty("_Image1","source","checkbox_select_down_png")
				])
			,
			new eui.State ("disabledAndSelected",
				[
					new eui.SetProperty("_Image1","source","checkbox_select_disabled_png")
				])
		];
	}
	var _proto = CheckBoxSkin.prototype;

	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.percentHeight = 100;
		t.percentWidth = 100;
		t.layout = this._HorizontalLayout1_i();
		t.elementsContent = [this._Image1_i(),this.labelDisplay_i()];
		return t;
	};
	_proto._HorizontalLayout1_i = function () {
		var t = new eui.HorizontalLayout();
		t.verticalAlign = "middle";
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.alpha = 1;
		t.fillMode = "scale";
		t.source = "checkbox_unselect_png";
		return t;
	};
	_proto.labelDisplay_i = function () {
		var t = new eui.Label();
		this.labelDisplay = t;
		t.fontFamily = "Tahoma";
		t.size = 20;
		t.textAlign = "center";
		t.textColor = 0x707070;
		t.verticalAlign = "middle";
		return t;
	};
	return CheckBoxSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/HScrollBarSkin.exml'] = window.skins.HScrollBarSkin = (function (_super) {
	__extends(HScrollBarSkin, _super);
	function HScrollBarSkin() {
		_super.call(this);
		this.skinParts = ["thumb"];
		
		this.minHeight = 8;
		this.minWidth = 20;
		this.elementsContent = [this.thumb_i()];
	}
	var _proto = HScrollBarSkin.prototype;

	_proto.thumb_i = function () {
		var t = new eui.Image();
		this.thumb = t;
		t.height = 8;
		t.scale9Grid = new egret.Rectangle(3,3,2,2);
		t.source = "roundthumb_png";
		t.verticalCenter = 0;
		t.width = 30;
		return t;
	};
	return HScrollBarSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/HSliderSkin.exml'] = window.skins.HSliderSkin = (function (_super) {
	__extends(HSliderSkin, _super);
	function HSliderSkin() {
		_super.call(this);
		this.skinParts = ["track","thumb"];
		
		this.minHeight = 8;
		this.minWidth = 20;
		this.elementsContent = [this.track_i(),this.thumb_i()];
	}
	var _proto = HSliderSkin.prototype;

	_proto.track_i = function () {
		var t = new eui.Image();
		this.track = t;
		t.height = 6;
		t.scale9Grid = new egret.Rectangle(1,1,4,4);
		t.source = "track_sb_png";
		t.verticalCenter = 0;
		t.percentWidth = 100;
		return t;
	};
	_proto.thumb_i = function () {
		var t = new eui.Image();
		this.thumb = t;
		t.source = "thumb_png";
		t.verticalCenter = 0;
		return t;
	};
	return HSliderSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/ItemRendererSkin.exml'] = window.skins.ItemRendererSkin = (function (_super) {
	__extends(ItemRendererSkin, _super);
	function ItemRendererSkin() {
		_super.call(this);
		this.skinParts = ["labelDisplay"];
		
		this.minHeight = 50;
		this.minWidth = 100;
		this.elementsContent = [this._Image1_i(),this.labelDisplay_i()];
		this.states = [
			new eui.State ("up",
				[
				])
			,
			new eui.State ("down",
				[
					new eui.SetProperty("_Image1","source","button_down_png")
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("_Image1","alpha",0.5)
				])
		];
		
		eui.Binding.$bindProperties(this, ["hostComponent.data"],[0],this.labelDisplay,"text");
	}
	var _proto = ItemRendererSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(1,3,8,8);
		t.source = "button_up_png";
		t.percentWidth = 100;
		return t;
	};
	_proto.labelDisplay_i = function () {
		var t = new eui.Label();
		this.labelDisplay = t;
		t.bottom = 8;
		t.fontFamily = "Tahoma";
		t.left = 8;
		t.right = 8;
		t.size = 20;
		t.textAlign = "center";
		t.textColor = 0xFFFFFF;
		t.top = 8;
		t.verticalAlign = "middle";
		return t;
	};
	return ItemRendererSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/PanelSkin.exml'] = window.skins.PanelSkin = (function (_super) {
	__extends(PanelSkin, _super);
	function PanelSkin() {
		_super.call(this);
		this.skinParts = ["titleDisplay","moveArea","closeButton"];
		
		this.minHeight = 230;
		this.minWidth = 450;
		this.elementsContent = [this._Image1_i(),this.moveArea_i(),this.closeButton_i()];
	}
	var _proto = PanelSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.bottom = 0;
		t.left = 0;
		t.right = 0;
		t.scale9Grid = new egret.Rectangle(2,2,12,12);
		t.source = "border_png";
		t.top = 0;
		return t;
	};
	_proto.moveArea_i = function () {
		var t = new eui.Group();
		this.moveArea = t;
		t.height = 45;
		t.left = 0;
		t.right = 0;
		t.top = 0;
		t.elementsContent = [this._Image2_i(),this.titleDisplay_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.bottom = 0;
		t.left = 0;
		t.right = 0;
		t.source = "header_png";
		t.top = 0;
		return t;
	};
	_proto.titleDisplay_i = function () {
		var t = new eui.Label();
		this.titleDisplay = t;
		t.fontFamily = "Tahoma";
		t.left = 15;
		t.right = 5;
		t.size = 20;
		t.textColor = 0xFFFFFF;
		t.verticalCenter = 0;
		t.wordWrap = false;
		return t;
	};
	_proto.closeButton_i = function () {
		var t = new eui.Button();
		this.closeButton = t;
		t.bottom = 5;
		t.horizontalCenter = 0;
		t.label = "close";
		return t;
	};
	return PanelSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/ProgressBarSkin.exml'] = window.skins.ProgressBarSkin = (function (_super) {
	__extends(ProgressBarSkin, _super);
	function ProgressBarSkin() {
		_super.call(this);
		this.skinParts = ["thumb","labelDisplay"];
		
		this.minHeight = 18;
		this.minWidth = 30;
		this.elementsContent = [this._Image1_i(),this.thumb_i(),this.labelDisplay_i()];
	}
	var _proto = ProgressBarSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(1,1,4,4);
		t.source = "track_pb_png";
		t.verticalCenter = 0;
		t.percentWidth = 100;
		return t;
	};
	_proto.thumb_i = function () {
		var t = new eui.Image();
		this.thumb = t;
		t.percentHeight = 100;
		t.source = "thumb_pb_png";
		t.percentWidth = 100;
		return t;
	};
	_proto.labelDisplay_i = function () {
		var t = new eui.Label();
		this.labelDisplay = t;
		t.fontFamily = "Tahoma";
		t.horizontalCenter = 0;
		t.size = 15;
		t.textAlign = "center";
		t.textColor = 0x707070;
		t.verticalAlign = "middle";
		t.verticalCenter = 0;
		return t;
	};
	return ProgressBarSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/RadioButtonSkin.exml'] = window.skins.RadioButtonSkin = (function (_super) {
	__extends(RadioButtonSkin, _super);
	function RadioButtonSkin() {
		_super.call(this);
		this.skinParts = ["labelDisplay"];
		
		this.elementsContent = [this._Group1_i()];
		this.states = [
			new eui.State ("up",
				[
				])
			,
			new eui.State ("down",
				[
					new eui.SetProperty("_Image1","alpha",0.7)
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("_Image1","alpha",0.5)
				])
			,
			new eui.State ("upAndSelected",
				[
					new eui.SetProperty("_Image1","source","radiobutton_select_up_png")
				])
			,
			new eui.State ("downAndSelected",
				[
					new eui.SetProperty("_Image1","source","radiobutton_select_down_png")
				])
			,
			new eui.State ("disabledAndSelected",
				[
					new eui.SetProperty("_Image1","source","radiobutton_select_disabled_png")
				])
		];
	}
	var _proto = RadioButtonSkin.prototype;

	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.percentHeight = 100;
		t.percentWidth = 100;
		t.layout = this._HorizontalLayout1_i();
		t.elementsContent = [this._Image1_i(),this.labelDisplay_i()];
		return t;
	};
	_proto._HorizontalLayout1_i = function () {
		var t = new eui.HorizontalLayout();
		t.verticalAlign = "middle";
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.alpha = 1;
		t.fillMode = "scale";
		t.source = "radiobutton_unselect_png";
		return t;
	};
	_proto.labelDisplay_i = function () {
		var t = new eui.Label();
		this.labelDisplay = t;
		t.fontFamily = "Tahoma";
		t.size = 20;
		t.textAlign = "center";
		t.textColor = 0x707070;
		t.verticalAlign = "middle";
		return t;
	};
	return RadioButtonSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/ScrollerSkin.exml'] = window.skins.ScrollerSkin = (function (_super) {
	__extends(ScrollerSkin, _super);
	function ScrollerSkin() {
		_super.call(this);
		this.skinParts = ["horizontalScrollBar","verticalScrollBar"];
		
		this.minHeight = 20;
		this.minWidth = 20;
		this.elementsContent = [this.horizontalScrollBar_i(),this.verticalScrollBar_i()];
	}
	var _proto = ScrollerSkin.prototype;

	_proto.horizontalScrollBar_i = function () {
		var t = new eui.HScrollBar();
		this.horizontalScrollBar = t;
		t.bottom = 0;
		t.percentWidth = 100;
		return t;
	};
	_proto.verticalScrollBar_i = function () {
		var t = new eui.VScrollBar();
		this.verticalScrollBar = t;
		t.percentHeight = 100;
		t.right = 0;
		return t;
	};
	return ScrollerSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/TextInputSkin.exml'] = window.skins.TextInputSkin = (function (_super) {
	__extends(TextInputSkin, _super);
	function TextInputSkin() {
		_super.call(this);
		this.skinParts = ["textDisplay","promptDisplay"];
		
		this.minHeight = 40;
		this.minWidth = 300;
		this.elementsContent = [this._Image1_i(),this._Rect1_i(),this.textDisplay_i()];
		this.promptDisplay_i();
		
		this.states = [
			new eui.State ("normal",
				[
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("textDisplay","textColor",0xff0000)
				])
			,
			new eui.State ("normalWithPrompt",
				[
					new eui.AddItems("promptDisplay","",1,"")
				])
			,
			new eui.State ("disabledWithPrompt",
				[
					new eui.AddItems("promptDisplay","",1,"")
				])
		];
	}
	var _proto = TextInputSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(1,3,8,8);
		t.source = "button_up_png";
		t.percentWidth = 100;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.fillColor = 0xffffff;
		t.percentHeight = 100;
		t.percentWidth = 100;
		return t;
	};
	_proto.textDisplay_i = function () {
		var t = new eui.EditableText();
		this.textDisplay = t;
		t.height = 24;
		t.left = "10";
		t.right = "10";
		t.size = 20;
		t.textColor = 0x000000;
		t.verticalCenter = "0";
		t.percentWidth = 100;
		return t;
	};
	_proto.promptDisplay_i = function () {
		var t = new eui.Label();
		this.promptDisplay = t;
		t.height = 24;
		t.left = 10;
		t.right = 10;
		t.size = 20;
		t.textColor = 0xa9a9a9;
		t.touchEnabled = false;
		t.verticalCenter = 0;
		t.percentWidth = 100;
		return t;
	};
	return TextInputSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/ToggleSwitchSkin.exml'] = window.skins.ToggleSwitchSkin = (function (_super) {
	__extends(ToggleSwitchSkin, _super);
	function ToggleSwitchSkin() {
		_super.call(this);
		this.skinParts = [];
		
		this.elementsContent = [this._Image1_i(),this._Image2_i()];
		this.states = [
			new eui.State ("up",
				[
					new eui.SetProperty("_Image1","source","off_png")
				])
			,
			new eui.State ("down",
				[
					new eui.SetProperty("_Image1","source","off_png")
				])
			,
			new eui.State ("disabled",
				[
					new eui.SetProperty("_Image1","source","off_png")
				])
			,
			new eui.State ("upAndSelected",
				[
					new eui.SetProperty("_Image2","horizontalCenter",18)
				])
			,
			new eui.State ("downAndSelected",
				[
					new eui.SetProperty("_Image2","horizontalCenter",18)
				])
			,
			new eui.State ("disabledAndSelected",
				[
					new eui.SetProperty("_Image2","horizontalCenter",18)
				])
		];
	}
	var _proto = ToggleSwitchSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.source = "on_png";
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.horizontalCenter = -18;
		t.source = "handle_png";
		t.verticalCenter = 0;
		return t;
	};
	return ToggleSwitchSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/VScrollBarSkin.exml'] = window.skins.VScrollBarSkin = (function (_super) {
	__extends(VScrollBarSkin, _super);
	function VScrollBarSkin() {
		_super.call(this);
		this.skinParts = ["thumb"];
		
		this.minHeight = 20;
		this.minWidth = 8;
		this.elementsContent = [this.thumb_i()];
	}
	var _proto = VScrollBarSkin.prototype;

	_proto.thumb_i = function () {
		var t = new eui.Image();
		this.thumb = t;
		t.height = 30;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(3,3,2,2);
		t.source = "roundthumb_png";
		t.width = 8;
		return t;
	};
	return VScrollBarSkin;
})(eui.Skin);generateEUI.paths['resource/eui_skins/VSliderSkin.exml'] = window.skins.VSliderSkin = (function (_super) {
	__extends(VSliderSkin, _super);
	function VSliderSkin() {
		_super.call(this);
		this.skinParts = ["track","thumb"];
		
		this.minHeight = 30;
		this.minWidth = 25;
		this.elementsContent = [this.track_i(),this.thumb_i()];
	}
	var _proto = VSliderSkin.prototype;

	_proto.track_i = function () {
		var t = new eui.Image();
		this.track = t;
		t.percentHeight = 100;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(1,1,4,4);
		t.source = "track_png";
		t.width = 7;
		return t;
	};
	_proto.thumb_i = function () {
		var t = new eui.Image();
		this.thumb = t;
		t.horizontalCenter = 0;
		t.source = "thumb_png";
		return t;
	};
	return VSliderSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/AchieveItem.exml'] = window.AchieveItemSkin = (function (_super) {
	__extends(AchieveItemSkin, _super);
	function AchieveItemSkin() {
		_super.call(this);
		this.skinParts = ["titleImg","titleTxt","getTimeTxt","progressBar","progressTxt","progressGrp","coinIcon","coinTxt","getBtn","btnLabel"];
		
		this.height = 315;
		this.width = 242;
		this.elementsContent = [this._Rect1_i(),this.titleImg_i(),this.titleTxt_i(),this.getBtn_i(),this.btnLabel_i()];
		this.getTimeTxt_i();
		
		this.progressGrp_i();
		
		this.coinIcon_i();
		
		this.coinTxt_i();
		
		this.states = [
			new eui.State ("2",
				[
					new eui.AddItems("getTimeTxt","",2,"getBtn")
				])
			,
			new eui.State ("0",
				[
					new eui.AddItems("progressGrp","",2,"getBtn"),
					new eui.AddItems("coinIcon","",2,"getBtn"),
					new eui.AddItems("coinTxt","",2,"getBtn"),
					new eui.SetProperty("titleTxt","y",168),
					new eui.SetProperty("titleTxt","textAlign","center"),
					new eui.SetProperty("titleTxt","x",5),
					new eui.SetProperty("titleTxt","width",195),
					new eui.SetProperty("_Rect2","x",15),
					new eui.SetProperty("progressBar","x",15),
					new eui.SetProperty("progressTxt","x",-7),
					new eui.SetProperty("progressTxt","anchorOffsetX",0),
					new eui.SetProperty("progressTxt","width",137),
					new eui.SetProperty("progressTxt","y",0),
					new eui.SetProperty("progressTxt","textAlign","center"),
					new eui.SetProperty("coinIcon","y",200),
					new eui.SetProperty("coinIcon","x",48),
					new eui.SetProperty("coinTxt","y",210),
					new eui.SetProperty("coinTxt","x",84),
					new eui.SetProperty("coinTxt","anchorOffsetX",0),
					new eui.SetProperty("coinTxt","width",84),
					new eui.SetProperty("coinTxt","textAlign","center"),
					new eui.SetProperty("getBtn","source","viewpage_json.btndoing"),
					new eui.SetProperty("getBtn","y",243),
					new eui.SetProperty("getBtn","x",38),
					new eui.SetProperty("btnLabel","text","去完成"),
					new eui.SetProperty("btnLabel","y",260),
					new eui.SetProperty("btnLabel","x",40)
				])
			,
			new eui.State ("1",
				[
					new eui.AddItems("progressGrp","",2,"getBtn"),
					new eui.AddItems("coinIcon","",2,"getBtn"),
					new eui.AddItems("coinTxt","",2,"getBtn"),
					new eui.SetProperty("titleTxt","y",168),
					new eui.SetProperty("titleTxt","textAlign","center"),
					new eui.SetProperty("titleTxt","x",1),
					new eui.SetProperty("_Rect2","x",12),
					new eui.SetProperty("progressBar","x",12),
					new eui.SetProperty("progressTxt","textAlign","center"),
					new eui.SetProperty("progressTxt","anchorOffsetX",0),
					new eui.SetProperty("progressTxt","width",155),
					new eui.SetProperty("progressTxt","x",-16),
					new eui.SetProperty("progressTxt","y",0),
					new eui.SetProperty("coinIcon","y",200),
					new eui.SetProperty("coinIcon","x",46),
					new eui.SetProperty("coinTxt","y",210),
					new eui.SetProperty("coinTxt","x",78),
					new eui.SetProperty("coinTxt","textAlign","center"),
					new eui.SetProperty("coinTxt","anchorOffsetX",0),
					new eui.SetProperty("coinTxt","width",97),
					new eui.SetProperty("getBtn","source","viewpage_json.btnget"),
					new eui.SetProperty("getBtn","y",243),
					new eui.SetProperty("getBtn","width",156),
					new eui.SetProperty("getBtn","x",31),
					new eui.SetProperty("btnLabel","text","立即领取"),
					new eui.SetProperty("btnLabel","y",260),
					new eui.SetProperty("btnLabel","x",41)
				])
		];
	}
	var _proto = AchieveItemSkin.prototype;

	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.alpha = 0.1;
		t.fillColor = 0x9D1111;
		t.height = 120;
		t.visible = false;
		t.width = 120;
		t.x = 25;
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.height = 120;
		t.source = "achieve_json.achieve_30";
		t.width = 120;
		t.x = 35;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 24;
		t.text = "小有成就";
		t.textAlign = "center";
		t.textColor = 0x985300;
		t.width = 199;
		t.x = -1;
		t.y = 136;
		return t;
	};
	_proto.getTimeTxt_i = function () {
		var t = new eui.Label();
		this.getTimeTxt = t;
		t.anchorOffsetX = 0;
		t.bold = false;
		t.rotation = 359.91;
		t.size = 22;
		t.text = "2019-01-01获得";
		t.textAlign = "left";
		t.textColor = 0xC0A067;
		t.width = 212;
		t.x = 20;
		t.y = 166;
		return t;
	};
	_proto.progressGrp_i = function () {
		var t = new eui.Group();
		this.progressGrp = t;
		t.touchEnabled = false;
		t.x = 35;
		t.y = 137;
		t.elementsContent = [this._Rect2_i(),this.progressBar_i(),this.progressTxt_i()];
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		this._Rect2 = t;
		t.ellipseHeight = 12;
		t.ellipseWidth = 12;
		t.fillColor = 0xffe096;
		t.height = 12;
		t.width = 96;
		t.x = -1;
		t.y = -18;
		return t;
	};
	_proto.progressBar_i = function () {
		var t = new eui.Rect();
		this.progressBar = t;
		t.ellipseHeight = 12;
		t.ellipseWidth = 12;
		t.fillColor = 0xff8c38;
		t.height = 12;
		t.width = 96;
		t.x = -1;
		t.y = -18;
		return t;
	};
	_proto.progressTxt_i = function () {
		var t = new eui.Label();
		this.progressTxt = t;
		t.size = 22;
		t.text = "1000/4000";
		t.textColor = 0xff8c38;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.coinIcon_i = function () {
		var t = new eui.Image();
		this.coinIcon = t;
		t.height = 38;
		t.source = "menuover_json.coin";
		t.width = 38;
		t.x = 44;
		t.y = 167;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.size = 26;
		t.text = "2000";
		t.textColor = 0xff8c38;
		t.x = 86;
		t.y = 177;
		return t;
	};
	_proto.getBtn_i = function () {
		var t = new eui.Image();
		this.getBtn = t;
		t.source = "viewpage_json.btnget";
		t.width = 136;
		t.x = 29;
		t.y = 200;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.text = "炫耀";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 131;
		t.x = 31;
		t.y = 217;
		return t;
	};
	return AchieveItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/AchievePopup.exml'] = window.AchievePopupSkin = (function (_super) {
	__extends(AchievePopupSkin, _super);
	function AchievePopupSkin() {
		_super.call(this);
		this.skinParts = ["bgImg","closeBtn","titleLabel","titleImg","descTxt","titleTxt","coinTxt","getBtn","moreBtn","starImg0","starImg1","starImg2","starImg3","starImg4"];
		
		this.height = 1334;
		this.width = 750;
		this.elementsContent = [this._Rect1_i(),this.bgImg_i(),this._Image1_i(),this.closeBtn_i(),this.titleLabel_i(),this._Rect2_i(),this.titleImg_i(),this.descTxt_i(),this.titleTxt_i(),this.coinTxt_i(),this._Image2_i(),this.getBtn_i(),this._Label1_i(),this.starImg0_i(),this.starImg1_i(),this.starImg2_i(),this.starImg3_i(),this.starImg4_i()];
		this.moreBtn_i();
		
		this._Label2_i();
		
		this.states = [
			new eui.State ("28",
				[
					new eui.AddItems("moreBtn","",2,"starImg0"),
					new eui.AddItems("_Label2","",2,"starImg0"),
					new eui.SetProperty("titleTxt","text","初出茅庐")
				])
			,
			new eui.State ("32",
				[
					new eui.AddItems("moreBtn","",2,"starImg0"),
					new eui.AddItems("_Label2","",2,"starImg0"),
					new eui.SetProperty("titleTxt","text","初生牛犊")
				])
			,
			new eui.State ("-1",
				[
					new eui.SetProperty("coinTxt","textAlign","right"),
					new eui.SetProperty("coinTxt","anchorOffsetX",0),
					new eui.SetProperty("coinTxt","width",194),
					new eui.SetProperty("coinTxt","x",175),
					new eui.SetProperty("getBtn","x",260.36),
					new eui.SetProperty("_Label1","x",315.5),
					new eui.SetProperty("_Label1","y",889)
				])
		];
	}
	var _proto = AchievePopupSkin.prototype;

	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.height = 1334;
		t.width = 750;
		return t;
	};
	_proto.bgImg_i = function () {
		var t = new eui.Image();
		this.bgImg = t;
		t.anchorOffsetX = 256;
		t.anchorOffsetY = 262.67;
		t.height = 523;
		t.scale9Grid = new egret.Rectangle(23,24,20,16);
		t.source = "redeff_json.lightbox";
		t.width = 523;
		t.x = 378.31;
		t.y = 500.38;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 114;
		t.scale9Grid = new egret.Rectangle(23,24,20,16);
		t.source = "viewpage_json.common_title_bg";
		t.visible = false;
		t.width = 640;
		t.x = 55;
		t.y = 313;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.close_btn";
		t.touchEnabled = true;
		t.x = 597;
		t.y = 243;
		return t;
	};
	_proto.titleLabel_i = function () {
		var t = new eui.Label();
		this.titleLabel = t;
		t.bold = true;
		t.height = 40;
		t.size = 40;
		t.stroke = 2;
		t.strokeColor = 0xf9e9b5;
		t.text = "成就达成";
		t.textAlign = "center";
		t.textColor = 0xbb5c00;
		t.verticalAlign = "justify";
		t.visible = false;
		t.width = 640;
		t.x = 55;
		t.y = 353;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.alpha = 0.1;
		t.ellipseHeight = 24;
		t.ellipseWidth = 24;
		t.fillColor = 0x9D1111;
		t.height = 177;
		t.visible = false;
		t.width = 177;
		t.x = 289;
		t.y = 488;
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.height = 250;
		t.source = "achieve_json.achieve_28";
		t.width = 250;
		t.x = 250;
		t.y = 375;
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.bold = true;
		t.height = 40;
		t.size = 34;
		t.text = "恭喜获得“小有斩获”称号";
		t.textAlign = "center";
		t.textColor = 0xffffff;
		t.verticalAlign = "justify";
		t.width = 640;
		t.x = 55;
		t.y = 706;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.bold = true;
		t.height = 40;
		t.size = 34;
		t.text = "小有斩获";
		t.textAlign = "center";
		t.textColor = 0xff8c38;
		t.verticalAlign = "justify";
		t.visible = false;
		t.x = 339.86;
		t.y = 706;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.bold = true;
		t.size = 36;
		t.text = "+100";
		t.textColor = 0xE7AE00;
		t.x = 287;
		t.y = 775;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.coins_icon";
		t.x = 381;
		t.y = 759;
		return t;
	};
	_proto.getBtn_i = function () {
		var t = new eui.Image();
		this.getBtn = t;
		t.height = 98;
		t.scale9Grid = new egret.Rectangle(28,21,97,23);
		t.source = "viewpage_json.btnget";
		t.touchEnabled = true;
		t.width = 264;
		t.x = 91;
		t.y = 858;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 36;
		t.stroke = 0.1;
		t.strokeColor = 0xadf4be;
		t.text = "炫耀";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 131;
		t.x = 156;
		t.y = 891;
		return t;
	};
	_proto.moreBtn_i = function () {
		var t = new eui.Image();
		this.moreBtn = t;
		t.height = 98;
		t.scale9Grid = new egret.Rectangle(28,21,97,23);
		t.source = "viewpage_json.btndoing";
		t.touchEnabled = true;
		t.width = 264;
		t.x = 392;
		t.y = 858;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 36;
		t.stroke = 2;
		t.strokeColor = 0x1b8bf2;
		t.text = "完成更多成就";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 259;
		t.x = 394;
		t.y = 889;
		return t;
	};
	_proto.starImg0_i = function () {
		var t = new eui.Image();
		this.starImg0 = t;
		t.alpha = 0.05;
		t.anchorOffsetX = 41.33;
		t.anchorOffsetY = 48;
		t.source = "redeff_json.star_0";
		t.x = 88.64;
		t.y = 114;
		return t;
	};
	_proto.starImg1_i = function () {
		var t = new eui.Image();
		this.starImg1 = t;
		t.alpha = 0.05;
		t.anchorOffsetX = 40;
		t.anchorOffsetY = 46.67;
		t.source = "redeff_json.star_0";
		t.x = 252;
		t.y = 87.17;
		return t;
	};
	_proto.starImg2_i = function () {
		var t = new eui.Image();
		this.starImg2 = t;
		t.alpha = 0.05;
		t.anchorOffsetX = 40;
		t.anchorOffsetY = 46.67;
		t.source = "redeff_json.star_0";
		t.x = 371.5;
		t.y = 127.67;
		return t;
	};
	_proto.starImg3_i = function () {
		var t = new eui.Image();
		this.starImg3 = t;
		t.alpha = 0.05;
		t.anchorOffsetX = 40;
		t.anchorOffsetY = 46.67;
		t.source = "redeff_json.star_0";
		t.x = 371.5;
		t.y = 127.67;
		return t;
	};
	_proto.starImg4_i = function () {
		var t = new eui.Image();
		this.starImg4 = t;
		t.alpha = 0.05;
		t.anchorOffsetX = 40;
		t.anchorOffsetY = 46.67;
		t.source = "redeff_json.star_0";
		t.x = 371.5;
		t.y = 127.67;
		return t;
	};
	return AchievePopupSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/BeastViewSkin.exml'] = window.BeastViewSkin = (function (_super) {
	__extends(BeastViewSkin, _super);
	function BeastViewSkin() {
		_super.call(this);
		this.skinParts = ["effImage","titleImg","titleTxt","commonBtn","btnLabel","doubleTxt","treeCoinTxt","giveTxt","distanceTxt","closeBtn","thousandImg0","thousandImg1","shareTxt","goldTxt","viewGrp"];
		
		this.currentState = "status_get";
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this.viewGrp_i()];
		this.effImage_i();
		
		this.titleTxt_i();
		
		this._Image3_i();
		
		this.doubleTxt_i();
		
		this.treeCoinTxt_i();
		
		this.giveTxt_i();
		
		this.distanceTxt_i();
		
		this.closeBtn_i();
		
		this._Label1_i();
		
		this._Label2_i();
		
		this.thousandImg0_i();
		
		this.thousandImg1_i();
		
		this.shareTxt_i();
		
		this.goldTxt_i();
		
		this._Label3_i();
		
		this._Image4_i();
		
		this._Label4_i();
		
		this._Image5_i();
		
		this._Label5_i();
		
		this._Image6_i();
		
		this._Label6_i();
		
		this._Image7_i();
		
		this._Label7_i();
		
		this._Image8_i();
		
		this._Label8_i();
		
		this._Image9_i();
		
		this._Label9_i();
		
		this._Label10_i();
		
		this._Label11_i();
		
		this.states = [
			new eui.State ("status_get",
				[
					new eui.AddItems("effImage","",0,""),
					new eui.AddItems("titleTxt","viewGrp",2,"commonBtn"),
					new eui.AddItems("_Image3","viewGrp",2,"commonBtn"),
					new eui.SetProperty("_Image1","anchorOffsetY",0),
					new eui.SetProperty("_Image1","height",712),
					new eui.SetProperty("_Image2","x",0),
					new eui.SetProperty("_Image2","y",34),
					new eui.SetProperty("titleImg","x",111),
					new eui.SetProperty("titleImg","y",36),
					new eui.SetProperty("titleTxt","width",640),
					new eui.SetProperty("titleTxt","y",205),
					new eui.SetProperty("_Image3","source","viewpage_json.beastonly"),
					new eui.SetProperty("_Image3","y",267),
					new eui.SetProperty("_Image3","x",195),
					new eui.SetProperty("commonBtn","x",138),
					new eui.SetProperty("commonBtn","y",623),
					new eui.SetProperty("btnLabel","x",153),
					new eui.SetProperty("btnLabel","y",653),
					new eui.SetProperty("giveTxt","x",0)
				])
			,
			new eui.State ("status_try",
				[
					new eui.AddItems("effImage","",0,""),
					new eui.AddItems("titleTxt","viewGrp",2,"commonBtn"),
					new eui.AddItems("_Image3","viewGrp",2,"commonBtn"),
					new eui.AddItems("_Image4","viewGrp",1,""),
					new eui.AddItems("_Label4","viewGrp",1,""),
					new eui.AddItems("_Image5","viewGrp",1,""),
					new eui.AddItems("_Label5","viewGrp",1,""),
					new eui.AddItems("_Image6","viewGrp",1,""),
					new eui.AddItems("_Label6","viewGrp",1,""),
					new eui.AddItems("_Image7","viewGrp",1,""),
					new eui.AddItems("_Label7","viewGrp",1,""),
					new eui.AddItems("_Image8","viewGrp",1,""),
					new eui.AddItems("_Label8","viewGrp",1,""),
					new eui.AddItems("_Image9","viewGrp",1,""),
					new eui.AddItems("_Label9","viewGrp",1,""),
					new eui.AddItems("_Label10","viewGrp",1,""),
					new eui.AddItems("_Label11","viewGrp",1,""),
					new eui.SetProperty("effImage","y",448.49),
					new eui.SetProperty("_Image1","height",800),
					new eui.SetProperty("_Image2","x",0),
					new eui.SetProperty("titleImg","x",111),
					new eui.SetProperty("titleImg","y",36),
					new eui.SetProperty("titleTxt","text","恭喜获得分红神兽限时体验\n期间产生的收益真实到账"),
					new eui.SetProperty("titleTxt","lineSpacing",10),
					new eui.SetProperty("titleTxt","width",640),
					new eui.SetProperty("titleTxt","y",196.66),
					new eui.SetProperty("_Image3","y",306),
					new eui.SetProperty("_Image3","source","viewpage_json.beastonly"),
					new eui.SetProperty("_Image3","x",195),
					new eui.SetProperty("commonBtn","y",718.99),
					new eui.SetProperty("commonBtn","x",138),
					new eui.SetProperty("btnLabel","y",752.99),
					new eui.SetProperty("btnLabel","text","去体验"),
					new eui.SetProperty("btnLabel","x",155),
					new eui.SetProperty("giveTxt","x",0)
				])
			,
			new eui.State ("status_result",
				[
					new eui.AddItems("titleTxt","viewGrp",2,"commonBtn"),
					new eui.AddItems("goldTxt","viewGrp",1,""),
					new eui.AddItems("_Label3","viewGrp",1,""),
					new eui.SetProperty("_Image1","y",286),
					new eui.SetProperty("_Image1","height",560),
					new eui.SetProperty("_Image1","anchorOffsetY",0),
					new eui.SetProperty("_Image2","x",0),
					new eui.SetProperty("_Image2","y",280),
					new eui.SetProperty("titleImg","source","viewpage_json.beastresulttitle"),
					new eui.SetProperty("titleImg","y",28),
					new eui.SetProperty("titleImg","x",111),
					new eui.SetProperty("titleTxt","y",454),
					new eui.SetProperty("titleTxt","text","本次限时体验共分红"),
					new eui.SetProperty("titleTxt","width",640),
					new eui.SetProperty("titleTxt","x",0),
					new eui.SetProperty("_Image3","x",158),
					new eui.SetProperty("_Image3","y",427.76),
					new eui.SetProperty("commonBtn","y",699),
					new eui.SetProperty("commonBtn","x",138),
					new eui.SetProperty("btnLabel","y",733),
					new eui.SetProperty("btnLabel","text","了解更多"),
					new eui.SetProperty("btnLabel","x",155),
					new eui.SetProperty("giveTxt","x",0),
					new eui.SetProperty("viewGrp","y",0)
				])
			,
			new eui.State ("status_share",
				[
					new eui.AddItems("_Image3","viewGrp",2,"commonBtn"),
					new eui.AddItems("distanceTxt","viewGrp",1,""),
					new eui.AddItems("closeBtn","viewGrp",1,""),
					new eui.AddItems("shareTxt","viewGrp",1,""),
					new eui.SetProperty("_Image1","height",750),
					new eui.SetProperty("titleImg","source","viewpage_json.getsuccesstitle"),
					new eui.SetProperty("titleImg","x",111),
					new eui.SetProperty("titleImg","y",36),
					new eui.SetProperty("titleTxt","text","恭喜获得200金币"),
					new eui.SetProperty("_Image3","source","viewpage_json.beastonly"),
					new eui.SetProperty("_Image3","y",265),
					new eui.SetProperty("_Image3","scaleX",-1),
					new eui.SetProperty("_Image3","x",446),
					new eui.SetProperty("commonBtn","width",331),
					new eui.SetProperty("commonBtn","height",101),
					new eui.SetProperty("commonBtn","scale9Grid",new egret.Rectangle(74,26,10,7)),
					new eui.SetProperty("commonBtn","y",667),
					new eui.SetProperty("commonBtn","source","menuover_json.nextbtn"),
					new eui.SetProperty("commonBtn","x",156),
					new eui.SetProperty("btnLabel","text","加速合成神兽"),
					new eui.SetProperty("btnLabel","y",701),
					new eui.SetProperty("btnLabel","bold",true),
					new eui.SetProperty("btnLabel","x",156),
					new eui.SetProperty("giveTxt","x",0),
					new eui.SetProperty("closeBtn","y",38),
					new eui.SetProperty("closeBtn","x",584)
				])
			,
			new eui.State ("status_tree",
				[
					new eui.AddItems("doubleTxt","viewGrp",1,""),
					new eui.AddItems("treeCoinTxt","viewGrp",1,""),
					new eui.AddItems("giveTxt","viewGrp",1,""),
					new eui.AddItems("closeBtn","viewGrp",1,""),
					new eui.AddItems("_Label1","viewGrp",1,""),
					new eui.SetProperty("_Image1","height",560),
					new eui.SetProperty("titleImg","source","viewpage_json.getsuccesstitle"),
					new eui.SetProperty("titleImg","x",111),
					new eui.SetProperty("titleImg","y",36),
					new eui.SetProperty("commonBtn","source","menuover_json.nextbtn"),
					new eui.SetProperty("commonBtn","width",331),
					new eui.SetProperty("commonBtn","height",101),
					new eui.SetProperty("commonBtn","y",479),
					new eui.SetProperty("commonBtn","x",156),
					new eui.SetProperty("btnLabel","text","我也要当师傅"),
					new eui.SetProperty("btnLabel","bold",true),
					new eui.SetProperty("btnLabel","y",513),
					new eui.SetProperty("btnLabel","x",156),
					new eui.SetProperty("doubleTxt","width",640),
					new eui.SetProperty("doubleTxt","y",210),
					new eui.SetProperty("treeCoinTxt","text","+188"),
					new eui.SetProperty("treeCoinTxt","textAlign","right"),
					new eui.SetProperty("treeCoinTxt","anchorOffsetX",0),
					new eui.SetProperty("treeCoinTxt","width",315),
					new eui.SetProperty("treeCoinTxt","y",284),
					new eui.SetProperty("treeCoinTxt","x",77),
					new eui.SetProperty("giveTxt","x",0),
					new eui.SetProperty("giveTxt","width",640),
					new eui.SetProperty("giveTxt","y",423),
					new eui.SetProperty("closeBtn","x",584),
					new eui.SetProperty("closeBtn","y",38)
				])
			,
			new eui.State ("status_pay",
				[
					new eui.AddItems("effImage","",0,""),
					new eui.AddItems("doubleTxt","viewGrp",1,""),
					new eui.AddItems("treeCoinTxt","viewGrp",1,""),
					new eui.AddItems("giveTxt","viewGrp",1,""),
					new eui.AddItems("closeBtn","viewGrp",1,""),
					new eui.AddItems("_Label2","viewGrp",1,""),
					new eui.AddItems("thousandImg0","viewGrp",1,""),
					new eui.AddItems("thousandImg1","viewGrp",1,""),
					new eui.SetProperty("effImage","x",325),
					new eui.SetProperty("effImage","y",83),
					new eui.SetProperty("effImage","alpha",0.5),
					new eui.SetProperty("_Image1","height",640),
					new eui.SetProperty("_Image1","width",640),
					new eui.SetProperty("titleImg","source","redeff_json.giveinvitetitle"),
					new eui.SetProperty("titleImg","y",-76),
					new eui.SetProperty("titleImg","x",106),
					new eui.SetProperty("commonBtn","source","menuover_json.nextbtn"),
					new eui.SetProperty("commonBtn","width",524),
					new eui.SetProperty("commonBtn","height",101),
					new eui.SetProperty("commonBtn","y",549),
					new eui.SetProperty("commonBtn","scale9Grid",new egret.Rectangle(145,44,18,11)),
					new eui.SetProperty("commonBtn","x",58),
					new eui.SetProperty("btnLabel","text","邀请好友，躺收进贡"),
					new eui.SetProperty("btnLabel","bold",true),
					new eui.SetProperty("btnLabel","x",81),
					new eui.SetProperty("btnLabel","y",583),
					new eui.SetProperty("btnLabel","textAlign","left"),
					new eui.SetProperty("btnLabel","width",355),
					new eui.SetProperty("doubleTxt","width",640),
					new eui.SetProperty("doubleTxt","text","获得好友进贡奖励体验"),
					new eui.SetProperty("doubleTxt","y",200),
					new eui.SetProperty("treeCoinTxt","text","+188"),
					new eui.SetProperty("treeCoinTxt","textAlign","right"),
					new eui.SetProperty("treeCoinTxt","anchorOffsetX",0),
					new eui.SetProperty("treeCoinTxt","width",319),
					new eui.SetProperty("treeCoinTxt","x",88),
					new eui.SetProperty("treeCoinTxt","y",274),
					new eui.SetProperty("giveTxt","width",416),
					new eui.SetProperty("giveTxt","anchorOffsetX",0),
					new eui.SetProperty("giveTxt","text","邀请过来的好友，每天都可以给\n你进贡10次，也就是2000金币！"),
					new eui.SetProperty("giveTxt","y",434),
					new eui.SetProperty("giveTxt","textAlign","left"),
					new eui.SetProperty("giveTxt","lineSpacing",10),
					new eui.SetProperty("giveTxt","x",122),
					new eui.SetProperty("closeBtn","x",584),
					new eui.SetProperty("closeBtn","y",38)
				])
		];
	}
	var _proto = BeastViewSkin.prototype;

	_proto.effImage_i = function () {
		var t = new eui.Image();
		this.effImage = t;
		t.anchorOffsetX = 204;
		t.anchorOffsetY = 204;
		t.height = 408;
		t.source = "redeff_json.lightbox";
		t.width = 408;
		t.x = 279;
		t.y = 378;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.height = 640;
		t.scale9Grid = new egret.Rectangle(30,31,2,2);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 60;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 58;
		return t;
	};
	_proto.viewGrp_i = function () {
		var t = new eui.Group();
		this.viewGrp = t;
		t.cacheAsBitmap = true;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this.titleImg_i(),this.commonBtn_i(),this.btnLabel_i()];
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.source = "viewpage_json.beastruntitle";
		t.y = 0;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.anchorOffsetX = 0;
		t.size = 36;
		t.text = "恭喜获得分红神兽";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 566;
		t.x = 0;
		t.y = 154;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.height = 304;
		t.source = "viewpage_json.beast";
		t.width = 250;
		t.y = 209.76;
		return t;
	};
	_proto.commonBtn_i = function () {
		var t = new eui.Image();
		this.commonBtn = t;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.y = 555;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.anchorOffsetX = 0;
		t.size = 34;
		t.text = "领取";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 331;
		t.y = 589;
		return t;
	};
	_proto.doubleTxt_i = function () {
		var t = new eui.Label();
		this.doubleTxt = t;
		t.size = 36;
		t.text = "恭喜获得5倍奖励";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 566;
		t.x = 0;
		t.y = 160;
		return t;
	};
	_proto.treeCoinTxt_i = function () {
		var t = new eui.Label();
		this.treeCoinTxt = t;
		t.size = 100;
		t.text = "+188金币";
		t.textAlign = "center";
		t.textColor = 0xff6038;
		t.width = 566;
		t.x = 0;
		t.y = 271;
		return t;
	};
	_proto.giveTxt_i = function () {
		var t = new eui.Label();
		this.giveTxt = t;
		t.size = 26;
		t.text = "本次额外向师父进贡了200金币";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 566;
		t.y = 417;
		return t;
	};
	_proto.distanceTxt_i = function () {
		var t = new eui.Label();
		this.distanceTxt = t;
		t.size = 26;
		t.text = "您距离合成分红神兽还差80%";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 640;
		t.x = 0;
		t.y = 610;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 582;
		t.y = 47;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.size = 38;
		t.text = "金币";
		t.textColor = 0xff6038;
		t.x = 401;
		t.y = 335;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.size = 38;
		t.text = "金币";
		t.textColor = 0xff6038;
		t.x = 417;
		t.y = 327;
		return t;
	};
	_proto.thousandImg0_i = function () {
		var t = new eui.Image();
		this.thousandImg0 = t;
		t.alpha = 0;
		t.source = "viewpage_json.twothoundadd";
		t.x = 402;
		t.y = 611;
		return t;
	};
	_proto.thousandImg1_i = function () {
		var t = new eui.Image();
		this.thousandImg1 = t;
		t.alpha = 0;
		t.source = "viewpage_json.twothoundadd";
		t.x = 402;
		t.y = 611;
		return t;
	};
	_proto.shareTxt_i = function () {
		var t = new eui.Label();
		this.shareTxt = t;
		t.size = 36;
		t.text = "Label";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 640;
		t.x = 0;
		t.y = 192;
		return t;
	};
	_proto.goldTxt_i = function () {
		var t = new eui.Label();
		this.goldTxt = t;
		t.size = 80;
		t.text = "0.34元";
		t.textColor = 0xff5a37;
		t.x = 202;
		t.y = 527;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.text = "已存入钱包";
		t.textColor = 0xccb197;
		t.x = 245;
		t.y = 617;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		this._Image4 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 205.01;
		t.y = 638;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		this._Label4 = t;
		t.size = 32;
		t.text = "0";
		t.x = 211.05;
		t.y = 642;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		this._Image5 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 237.01;
		t.y = 638;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		this._Label5 = t;
		t.size = 32;
		t.text = "0";
		t.x = 242.01;
		t.y = 642;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		this._Image6 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 286.01;
		t.y = 638;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		this._Label6 = t;
		t.size = 32;
		t.text = "0";
		t.x = 293.86;
		t.y = 642;
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		this._Image7 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 319.34;
		t.y = 638;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		this._Label7 = t;
		t.size = 32;
		t.text = "5";
		t.x = 325.34;
		t.y = 642;
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		this._Image8 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 368.34;
		t.y = 638;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		this._Label8 = t;
		t.size = 32;
		t.text = "0";
		t.x = 373.34;
		t.y = 642;
		return t;
	};
	_proto._Image9_i = function () {
		var t = new eui.Image();
		this._Image9 = t;
		t.source = "viewpage_json.numberbg";
		t.x = 400.34;
		t.y = 638;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		this._Label9 = t;
		t.size = 32;
		t.text = "0";
		t.x = 405.34;
		t.y = 642;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		this._Label10 = t;
		t.size = 32;
		t.text = ":";
		t.textColor = 0x242424;
		t.x = 275.34;
		t.y = 638;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		this._Label11 = t;
		t.size = 32;
		t.text = ":";
		t.textColor = 0x242424;
		t.x = 356.34;
		t.y = 638;
		return t;
	};
	return BeastViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/BlackNormalViewSkin.exml'] = window.BlackNormalViewSkin = (function (_super) {
	__extends(BlackNormalViewSkin, _super);
	function BlackNormalViewSkin() {
		_super.call(this);
		this.skinParts = ["effectImg","successTitle","ctitleTxt","avatarImg","xbutton","lvlupCoinImg","closeBtn","xLabel","videoGrp","getBtnGrp","xlightEff1","effect1","scaleEffect11","scaleEffect12","selectCard1","cardGrp1","xlightEff2","effect2","scaleEffect21","scaleEffect22","selectCard2","cardGrp2","xlightEff3","effect3","scaleEffect31","scaleEffect32","selectCard3","cardGrp3","levelupNameTxt","cardTxt","lvlGoldTxt","viewGrp"];
		
		this.currentState = "status_levelup";
		this.width = 750;
		this.elementsContent = [this.effectImg_i(),this.viewGrp_i()];
		this._Image1_i();
		
		this._Image2_i();
		
		this.successTitle_i();
		
		this.ctitleTxt_i();
		
		this.avatarImg_i();
		
		this._Image3_i();
		
		this.xbutton_i();
		
		this.lvlupCoinImg_i();
		
		this.xLabel_i();
		
		this._Image5_i();
		
		this.videoGrp_i();
		
		this._Image6_i();
		
		this.getBtnGrp_i();
		
		this.effect1_i();
		
		this.selectCard1_i();
		
		this.cardGrp1_i();
		
		this.xlightEff2_i();
		
		this.effect2_i();
		
		this.selectCard2_i();
		
		this.cardGrp2_i();
		
		this.xlightEff3_i();
		
		this.effect3_i();
		
		this.selectCard3_i();
		
		this.cardGrp3_i();
		
		this.levelupNameTxt_i();
		
		this.cardTxt_i();
		
		this.lvlGoldTxt_i();
		
		this.states = [
			new eui.State ("status_levelup",
				[
					new eui.AddItems("_Image1","",0,""),
					new eui.AddItems("_Image2","",2,"effectImg"),
					new eui.AddItems("avatarImg","viewGrp",2,"closeBtn"),
					new eui.AddItems("_Image3","viewGrp",2,"closeBtn"),
					new eui.AddItems("xbutton","viewGrp",2,"closeBtn"),
					new eui.AddItems("lvlupCoinImg","viewGrp",2,"closeBtn"),
					new eui.AddItems("xLabel","viewGrp",1,""),
					new eui.AddItems("levelupNameTxt","viewGrp",1,""),
					new eui.AddItems("lvlGoldTxt","viewGrp",1,""),
					new eui.SetProperty("effectImg","horizontalCenter",0),
					new eui.SetProperty("effectImg","y",396),
					new eui.SetProperty("xbutton","y",793),
					new eui.SetProperty("xbutton","x",193),
					new eui.SetProperty("xLabel","touchEnabled",false),
					new eui.SetProperty("xLabel","y",827),
					new eui.SetProperty("xLabel","width",364),
					new eui.SetProperty("xLabel","x",193),
					new eui.SetProperty("xLabel","text","炫耀一下"),
					new eui.SetProperty("_Image4","y",629),
					new eui.SetProperty("_Image4","x",193),
					new eui.SetProperty("_Label1","touchEnabled",false),
					new eui.SetProperty("_Label1","y",663),
					new eui.SetProperty("_Label1","width",364),
					new eui.SetProperty("_Label1","x",193),
					new eui.SetProperty("_Label1","text","炫耀一下")
				])
			,
			new eui.State ("status_getcard",
				[
					new eui.AddItems("successTitle","viewGrp",0,""),
					new eui.AddItems("ctitleTxt","viewGrp",2,"closeBtn"),
					new eui.AddItems("_Image5","videoGrp",1,""),
					new eui.AddItems("videoGrp","viewGrp",1,""),
					new eui.AddItems("_Image6","getBtnGrp",0,""),
					new eui.AddItems("getBtnGrp","viewGrp",1,""),
					new eui.AddItems("effect1","cardGrp1",2,"scaleEffect11"),
					new eui.AddItems("selectCard1","cardGrp1",1,""),
					new eui.AddItems("cardGrp1","viewGrp",1,""),
					new eui.AddItems("xlightEff2","cardGrp2",0,""),
					new eui.AddItems("effect2","cardGrp2",2,"scaleEffect21"),
					new eui.AddItems("selectCard2","cardGrp2",1,""),
					new eui.AddItems("cardGrp2","viewGrp",1,""),
					new eui.AddItems("xlightEff3","cardGrp3",0,""),
					new eui.AddItems("effect3","cardGrp3",2,"scaleEffect31"),
					new eui.AddItems("selectCard3","cardGrp3",1,""),
					new eui.AddItems("cardGrp3","viewGrp",1,""),
					new eui.AddItems("cardTxt","viewGrp",1,""),
					new eui.SetProperty("effectImg","y",392),
					new eui.SetProperty("effectImg","scaleX",1),
					new eui.SetProperty("effectImg","scaleY",1),
					new eui.SetProperty("effectImg","horizontalCenter",-0.5),
					new eui.SetProperty("effectImg","width",154),
					new eui.SetProperty("effectImg","height",154),
					new eui.SetProperty("effectImg","anchorOffsetX",77),
					new eui.SetProperty("effectImg","anchorOffsetY",77),
					new eui.SetProperty("effectImg","source","redeff_json.lightcircle"),
					new eui.SetProperty("avatarImg","y",299),
					new eui.SetProperty("xbutton","y",760),
					new eui.SetProperty("xbutton","scale9Grid",new egret.Rectangle(170,43,18,12)),
					new eui.SetProperty("xbutton","width",400),
					new eui.SetProperty("xbutton","x",175),
					new eui.SetProperty("xLabel","text","看视频再翻一张"),
					new eui.SetProperty("xLabel","touchEnabled",false),
					new eui.SetProperty("xLabel","y",790),
					new eui.SetProperty("xLabel","width",279),
					new eui.SetProperty("xLabel","x",264),
					new eui.SetProperty("xLabel","size",38),
					new eui.SetProperty("xLabel","anchorOffsetX",0),
					new eui.SetProperty("_Image4","y",0),
					new eui.SetProperty("_Image4","scale9Grid",new egret.Rectangle(170,43,18,12)),
					new eui.SetProperty("_Image4","width",400),
					new eui.SetProperty("_Image4","x",0),
					new eui.SetProperty("_Label1","text","免费再翻一张"),
					new eui.SetProperty("_Label1","touchEnabled",false),
					new eui.SetProperty("_Label1","y",30),
					new eui.SetProperty("_Label1","width",279),
					new eui.SetProperty("_Label1","x",89),
					new eui.SetProperty("_Label1","size",38),
					new eui.SetProperty("_Label1","anchorOffsetX",0)
				])
		];
	}
	var _proto = BlackNormalViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.anchorOffsetX = 74;
		t.anchorOffsetY = 74;
		t.scaleX = 4;
		t.scaleY = 4;
		t.source = "viewpage_json.lightadded";
		t.x = 375;
		t.y = 398;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.anchorOffsetX = 74;
		t.anchorOffsetY = 74;
		t.scaleX = 4;
		t.scaleY = 4;
		t.source = "viewpage_json.lightadded";
		t.x = 375;
		t.y = 398;
		return t;
	};
	_proto.effectImg_i = function () {
		var t = new eui.Image();
		this.effectImg = t;
		t.anchorOffsetX = 248;
		t.anchorOffsetY = 248;
		t.horizontalCenter = 0;
		t.source = "redeff_json.lightbox";
		t.y = 360;
		return t;
	};
	_proto.viewGrp_i = function () {
		var t = new eui.Group();
		this.viewGrp = t;
		t.width = 750;
		t.x = 0;
		t.y = -1;
		t.elementsContent = [this.closeBtn_i()];
		return t;
	};
	_proto.successTitle_i = function () {
		var t = new eui.Image();
		this.successTitle = t;
		t.source = "viewpage_json.successtitlejudge";
		t.width = 562;
		t.x = 94;
		t.y = -120;
		return t;
	};
	_proto.ctitleTxt_i = function () {
		var t = new eui.Label();
		this.ctitleTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 42;
		t.text = "请抽取您的奖励";
		t.textAlign = "center";
		t.width = 300;
		t.x = 225;
		t.y = 185;
		return t;
	};
	_proto.avatarImg_i = function () {
		var t = new eui.Image();
		this.avatarImg = t;
		t.anchorOffsetX = 82;
		t.anchorOffsetY = 110;
		t.source = "viewpage_json.notget";
		t.x = 375;
		t.y = 386;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "viewpage_json.leveluptitle";
		t.x = 167;
		t.y = 0;
		return t;
	};
	_proto.xbutton_i = function () {
		var t = new eui.Image();
		this.xbutton = t;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.y = 565;
		return t;
	};
	_proto.lvlupCoinImg_i = function () {
		var t = new eui.Image();
		this.lvlupCoinImg = t;
		t.source = "viewpage_json.mocoin";
		t.x = 410;
		t.y = 714;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.blackclosebtn";
		t.x = 630;
		t.y = 30;
		return t;
	};
	_proto.xLabel_i = function () {
		var t = new eui.Label();
		this.xLabel = t;
		t.size = 34;
		t.text = "炫耀一下";
		t.textAlign = "center";
		t.width = 330;
		t.x = 210;
		t.y = 603;
		return t;
	};
	_proto.videoGrp_i = function () {
		var t = new eui.Group();
		this.videoGrp = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 175;
		t.y = 760;
		t.elementsContent = [this._Image4_i(),this._Label1_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		this._Image4 = t;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.y = 565;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.size = 34;
		t.text = "炫耀一下";
		t.textAlign = "center";
		t.width = 330;
		t.x = 210;
		t.y = 603;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		this._Image5 = t;
		t.source = "guessgame_json.video4";
		t.x = 59;
		t.y = 30;
		return t;
	};
	_proto.getBtnGrp_i = function () {
		var t = new eui.Group();
		this.getBtnGrp = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.visible = false;
		t.x = 175;
		t.y = 760;
		t.elementsContent = [this._Label2_i()];
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		this._Image6 = t;
		t.scale9Grid = new egret.Rectangle(170,43,18,12);
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.width = 400;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.size = 34;
		t.text = "收下";
		t.x = 166;
		t.y = 30;
		return t;
	};
	_proto.cardGrp1_i = function () {
		var t = new eui.Group();
		this.cardGrp1 = t;
		t.touchChildren = true;
		t.touchEnabled = false;
		t.touchThrough = true;
		t.x = 120;
		t.y = 407;
		t.elementsContent = [this.xlightEff1_i(),this.scaleEffect11_i(),this.scaleEffect12_i()];
		return t;
	};
	_proto.xlightEff1_i = function () {
		var t = new eui.Image();
		this.xlightEff1 = t;
		t.anchorOffsetX = 250;
		t.anchorOffsetY = 250;
		t.height = 500;
		t.source = "redeff_json.xlight";
		t.touchEnabled = false;
		t.width = 500;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.effect1_i = function () {
		var t = new eui.Image();
		this.effect1 = t;
		t.alpha = 0.5;
		t.anchorOffsetX = 180;
		t.anchorOffsetY = 180;
		t.height = 360;
		t.source = "redeff_json.light2";
		t.touchEnabled = false;
		t.width = 360;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect11_i = function () {
		var t = new eui.Image();
		this.scaleEffect11 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect12_i = function () {
		var t = new eui.Image();
		this.scaleEffect12 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.selectCard1_i = function () {
		var t = new eui.Image();
		this.selectCard1 = t;
		t.anchorOffsetX = 100;
		t.anchorOffsetY = 132;
		t.source = "viewpage_json.jcardkbg";
		t.touchEnabled = true;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.cardGrp2_i = function () {
		var t = new eui.Group();
		this.cardGrp2 = t;
		t.touchChildren = true;
		t.touchEnabled = false;
		t.touchThrough = true;
		t.x = 375;
		t.y = 407;
		t.elementsContent = [this.scaleEffect21_i(),this.scaleEffect22_i()];
		return t;
	};
	_proto.xlightEff2_i = function () {
		var t = new eui.Image();
		this.xlightEff2 = t;
		t.anchorOffsetX = 250;
		t.anchorOffsetY = 250;
		t.height = 500;
		t.source = "redeff_json.xlight";
		t.touchEnabled = false;
		t.width = 500;
		t.x = 1;
		t.y = 0;
		return t;
	};
	_proto.effect2_i = function () {
		var t = new eui.Image();
		this.effect2 = t;
		t.alpha = 0.5;
		t.anchorOffsetX = 180;
		t.anchorOffsetY = 180;
		t.height = 360;
		t.source = "redeff_json.light2";
		t.touchEnabled = false;
		t.width = 360;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect21_i = function () {
		var t = new eui.Image();
		this.scaleEffect21 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect22_i = function () {
		var t = new eui.Image();
		this.scaleEffect22 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.selectCard2_i = function () {
		var t = new eui.Image();
		this.selectCard2 = t;
		t.anchorOffsetX = 100;
		t.anchorOffsetY = 132;
		t.source = "viewpage_json.jcardkbg";
		t.touchEnabled = true;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.cardGrp3_i = function () {
		var t = new eui.Group();
		this.cardGrp3 = t;
		t.touchChildren = true;
		t.touchEnabled = false;
		t.touchThrough = true;
		t.x = 630;
		t.y = 407;
		t.elementsContent = [this.scaleEffect31_i(),this.scaleEffect32_i()];
		return t;
	};
	_proto.xlightEff3_i = function () {
		var t = new eui.Image();
		this.xlightEff3 = t;
		t.anchorOffsetX = 250;
		t.anchorOffsetY = 250;
		t.height = 500;
		t.source = "redeff_json.xlight";
		t.touchEnabled = false;
		t.width = 500;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.effect3_i = function () {
		var t = new eui.Image();
		this.effect3 = t;
		t.alpha = 0.5;
		t.anchorOffsetX = 180;
		t.anchorOffsetY = 180;
		t.height = 360;
		t.source = "redeff_json.light2";
		t.touchEnabled = false;
		t.width = 360;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect31_i = function () {
		var t = new eui.Image();
		this.scaleEffect31 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.scaleEffect32_i = function () {
		var t = new eui.Image();
		this.scaleEffect32 = t;
		t.anchorOffsetX = 150;
		t.anchorOffsetY = 150;
		t.height = 300;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "redeff_json.lightwave";
		t.touchEnabled = false;
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.selectCard3_i = function () {
		var t = new eui.Image();
		this.selectCard3 = t;
		t.anchorOffsetX = 100;
		t.anchorOffsetY = 132;
		t.source = "viewpage_json.jcardkbg";
		t.touchEnabled = true;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.levelupNameTxt_i = function () {
		var t = new eui.Label();
		this.levelupNameTxt = t;
		t.bold = true;
		t.size = 36;
		t.text = "官升一级";
		t.textAlign = "center";
		t.width = 332;
		t.x = 209;
		t.y = 706;
		return t;
	};
	_proto.cardTxt_i = function () {
		var t = new eui.Label();
		this.cardTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 72;
		t.text = "鸡";
		t.textAlign = "center";
		t.textColor = 0xcb2620;
		t.width = 309;
		t.x = 221;
		t.y = 590;
		return t;
	};
	_proto.lvlGoldTxt_i = function () {
		var t = new eui.Label();
		this.lvlGoldTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 60;
		t.text = "+100";
		t.textAlign = "right";
		t.textColor = 0xffeb46;
		t.width = 225;
		t.x = 173;
		t.y = 714;
		return t;
	};
	return BlackNormalViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/BoxRewardViewSkin.exml'] = window.BoxRewardViewSkin = (function (_super) {
	__extends(BoxRewardViewSkin, _super);
	function BoxRewardViewSkin() {
		_super.call(this);
		this.skinParts = ["closeBtn"];
		
		this.height = 857;
		this.width = 750;
		this.elementsContent = [this.closeBtn_i()];
	}
	var _proto = BoxRewardViewSkin.prototype;

	_proto.closeBtn_i = function () {
		var t = new eui.Group();
		this.closeBtn = t;
		t.name = "closeBtn";
		t.touchChildren = false;
		t.x = 218;
		t.y = 739;
		t.elementsContent = [this._Image1_i(),this._Label1_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_btn_0";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 42;
		t.text = "收下";
		t.x = 131;
		t.y = 38;
		return t;
	};
	return BoxRewardViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/BubbleItem.exml'] = window.BubbleItemSkin = (function (_super) {
	__extends(BubbleItemSkin, _super);
	function BubbleItemSkin() {
		_super.call(this);
		this.skinParts = ["bubbleImg","coinTxt","lifeTxt"];
		
		this.elementsContent = [this.bubbleImg_i(),this.coinTxt_i(),this.lifeTxt_i()];
	}
	var _proto = BubbleItemSkin.prototype;

	_proto.bubbleImg_i = function () {
		var t = new eui.Image();
		this.bubbleImg = t;
		t.source = "menuover_json.bubblecoin";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 32;
		t.text = "66";
		t.textAlign = "center";
		t.textColor = 0xfdf42e;
		t.width = 71;
		t.x = 16;
		t.y = 37;
		return t;
	};
	_proto.lifeTxt_i = function () {
		var t = new eui.Label();
		this.lifeTxt = t;
		t.bold = true;
		t.size = 24;
		t.stroke = 3;
		t.strokeColor = 0x428bcb;
		t.text = "x3";
		t.x = 60;
		t.y = 68;
		return t;
	};
	return BubbleItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/CardImageItem.exml'] = window.CardImageItemSkin = (function (_super) {
	__extends(CardImageItemSkin, _super);
	function CardImageItemSkin() {
		_super.call(this);
		this.skinParts = ["avatarImg","nameTxt"];
		
		this.minHeight = 50;
		this.minWidth = 100;
		this.elementsContent = [this.avatarImg_i(),this.nameTxt_i()];
	}
	var _proto = CardImageItemSkin.prototype;

	_proto.avatarImg_i = function () {
		var t = new eui.Image();
		this.avatarImg = t;
		t.height = 204;
		t.source = "viewpage_json.notget";
		t.width = 152;
		t.y = 0;
		return t;
	};
	_proto.nameTxt_i = function () {
		var t = new eui.Label();
		this.nameTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.size = 25;
		t.text = "龙";
		t.textAlign = "center";
		t.textColor = 0xb1afac;
		t.width = 152;
		t.x = 0;
		t.y = 170;
		return t;
	};
	return CardImageItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/CardTypeItem.exml'] = window.CardTypeItemSkin = (function (_super) {
	__extends(CardTypeItemSkin, _super);
	function CardTypeItemSkin() {
		_super.call(this);
		this.skinParts = ["getBtn","coinImg","titleTxt","descTxt","btnLabel","imgList","xScroller"];
		
		this.elementsContent = [this.getBtn_i(),this.coinImg_i(),this.titleTxt_i(),this.descTxt_i(),this.btnLabel_i(),this.xScroller_i()];
	}
	var _proto = CardTypeItemSkin.prototype;

	_proto.getBtn_i = function () {
		var t = new eui.Image();
		this.getBtn = t;
		t.height = 68;
		t.scale9Grid = new egret.Rectangle(74,29,7,6);
		t.source = "viewpage_json.btnget";
		t.width = 254;
		t.x = 469;
		t.y = 66;
		return t;
	};
	_proto.coinImg_i = function () {
		var t = new eui.Image();
		this.coinImg = t;
		t.source = "judgegame_json.jcoin";
		t.touchEnabled = false;
		t.x = 654;
		t.y = 78;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 40;
		t.size = 34;
		t.text = "十二生肖(1/12)";
		t.textColor = 0x000000;
		t.verticalAlign = "bottom";
		t.x = 24;
		t.y = 56;
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.size = 26;
		t.text = "集齐可以兑换10000金币";
		t.textColor = 0x656462;
		t.x = 24;
		t.y = 112;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.anchorOffsetX = 0;
		t.size = 32;
		t.text = "兑换10000";
		t.textAlign = "right";
		t.touchEnabled = false;
		t.width = 179;
		t.x = 467;
		t.y = 86;
		return t;
	};
	_proto.xScroller_i = function () {
		var t = new eui.Scroller();
		this.xScroller = t;
		t.anchorOffsetX = 0;
		t.height = 220;
		t.scrollPolicyH = "auto";
		t.scrollPolicyV = "off";
		t.width = 710;
		t.x = 12;
		t.y = 162;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.y = 1;
		t.elementsContent = [this.imgList_i()];
		return t;
	};
	_proto.imgList_i = function () {
		var t = new eui.List();
		this.imgList = t;
		t.x = 0;
		t.y = 0;
		return t;
	};
	return CardTypeItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/CommonViewSkin.exml'] = window.CommonViewSkin = (function (_super) {
	__extends(CommonViewSkin, _super);
	function CommonViewSkin() {
		_super.call(this);
		this.skinParts = ["closeBtn","secondImg","titleTxt","midImage","descTxt","confirmBtn","btnLabel","numTxt"];
		
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this.closeBtn_i(),this.secondImg_i(),this.titleTxt_i(),this.midImage_i(),this.descTxt_i(),this.confirmBtn_i(),this.btnLabel_i(),this.numTxt_i()];
	}
	var _proto = CommonViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 680;
		t.scale9Grid = new egret.Rectangle(33,32,5,7);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 42;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 42;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 580;
		t.y = 38;
		return t;
	};
	_proto.secondImg_i = function () {
		var t = new eui.Image();
		this.secondImg = t;
		t.horizontalCenter = 0;
		t.source = "viewpage_json.viewsecondalphabg";
		t.y = 253.84;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 72;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xf9e9b5;
		t.text = "恭喜升级";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 640;
		t.x = 0;
		t.y = 69;
		return t;
	};
	_proto.midImage_i = function () {
		var t = new eui.Image();
		this.midImage = t;
		t.anchorOffsetX = 78;
		t.anchorOffsetY = 113;
		t.scaleX = 0.6;
		t.scaleY = 0.6;
		t.source = "viewpage_json.lamb";
		t.x = 264;
		t.y = 356;
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.size = 26;
		t.text = "返回首页可以升级哦~";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 640;
		t.x = 0;
		t.y = 525;
		return t;
	};
	_proto.confirmBtn_i = function () {
		var t = new eui.Image();
		this.confirmBtn = t;
		t.source = "viewpage_json.commonbtn";
		t.width = 331;
		t.x = 155;
		t.y = 587.31;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.size = 34;
		t.text = "继续";
		t.touchEnabled = false;
		t.x = 286;
		t.y = 620.31;
		return t;
	};
	_proto.numTxt_i = function () {
		var t = new eui.Label();
		this.numTxt = t;
		t.bold = true;
		t.size = 56;
		t.stroke = 3;
		t.strokeColor = 0x8c4e03;
		t.text = "+3";
		t.textColor = 0xffffff;
		t.x = 354;
		t.y = 333;
		return t;
	};
	return CommonViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/comp/RewardPreViewSkin.exml'] = window.RewardPreViewSkin = (function (_super) {
	__extends(RewardPreViewSkin, _super);
	function RewardPreViewSkin() {
		_super.call(this);
		this.skinParts = ["reward1Lbl","reward2Lbl","reward3Lbl"];
		
		this.height = 202;
		this.width = 216;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this._Image4_i(),this.reward1Lbl_i(),this.reward2Lbl_i(),this.reward3Lbl_i()];
	}
	var _proto = RewardPreViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 215;
		t.rotation = 90;
		t.scale9Grid = new egret.Rectangle(12,64,29,2);
		t.source = "dispelPk_json.dpk_arrowframe";
		t.width = 201;
		t.x = 215;
		t.y = 1;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.pk_item_coin";
		t.x = 5;
		t.y = 12;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.pk_item_0";
		t.x = 19;
		t.y = 77;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.pk_item_help";
		t.x = 7;
		t.y = 123;
		return t;
	};
	_proto.reward1Lbl_i = function () {
		var t = new eui.Label();
		this.reward1Lbl = t;
		t.size = 26;
		t.text = "金币X50";
		t.textColor = 0xEDE661;
		t.x = 67;
		t.y = 29;
		return t;
	};
	_proto.reward2Lbl_i = function () {
		var t = new eui.Label();
		this.reward2Lbl = t;
		t.size = 26;
		t.text = "入场券x1";
		t.textColor = 0xede661;
		t.x = 66;
		t.y = 83;
		return t;
	};
	_proto.reward3Lbl_i = function () {
		var t = new eui.Label();
		this.reward3Lbl = t;
		t.size = 26;
		t.text = "随机道具x6";
		t.textColor = 0xede661;
		t.x = 66;
		t.y = 139;
		return t;
	};
	return RewardPreViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/ConfirmView.exml'] = window.ConfirmViewSkin = (function (_super) {
	__extends(ConfirmViewSkin, _super);
	function ConfirmViewSkin() {
		_super.call(this);
		this.skinParts = ["descTxt","confirmBtn","cancelBtn"];
		
		this.elementsContent = [this._Image1_i(),this.descTxt_i(),this.confirmBtn_i(),this.cancelBtn_i(),this._Label1_i(),this._Label2_i()];
	}
	var _proto = ConfirmViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 440;
		t.scale9Grid = new egret.Rectangle(31,29,61,64);
		t.source = "dispelPk_json.dpk_dlg_0";
		t.width = 660;
		t.x = 0;
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.bold = true;
		t.lineSpacing = 14;
		t.size = 34;
		t.text = "小主，认输将无法获得本局的 金币奖励哦~";
		t.textColor = 0x222222;
		t.touchEnabled = false;
		t.width = 440;
		t.x = 110;
		t.y = 99;
		return t;
	};
	_proto.confirmBtn_i = function () {
		var t = new eui.Image();
		this.confirmBtn = t;
		t.source = "dispelPk_json.dpk_confirmbtn";
		t.touchEnabled = true;
		t.x = 92;
		t.y = 265;
		return t;
	};
	_proto.cancelBtn_i = function () {
		var t = new eui.Image();
		this.cancelBtn = t;
		t.source = "dispelPk_json.dpk_cancelbtn";
		t.touchEnabled = true;
		t.x = 354;
		t.y = 265;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 42;
		t.text = "确定";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 218;
		t.x = 92;
		t.y = 300;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 42;
		t.text = "取消";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 218;
		t.x = 354;
		t.y = 300;
		return t;
	};
	return ConfirmViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/EqualView.exml'] = window.EqualViewSkin = (function (_super) {
	__extends(EqualViewSkin, _super);
	function EqualViewSkin() {
		_super.call(this);
		this.skinParts = ["confirmBtn","closeBtn","btnLabel"];
		
		this.currentState = "status_moneytree";
		this.elementsContent = [this._Image1_i(),this.confirmBtn_i(),this._Image2_i(),this.closeBtn_i(),this.btnLabel_i(),this._Label1_i(),this._Label2_i(),this._Label3_i(),this._Label4_i(),this._Label5_i()];
		this._Image3_i();
		
		this.states = [
			new eui.State ("status_moneytree",
				[
					new eui.AddItems("_Image3","",2,"btnLabel"),
					new eui.SetProperty("confirmBtn","y",522.31),
					new eui.SetProperty("confirmBtn","x",156),
					new eui.SetProperty("btnLabel","y",551.31),
					new eui.SetProperty("btnLabel","x",271),
					new eui.SetProperty("_Label5","y",431),
					new eui.SetProperty("_Label5","size",48),
					new eui.SetProperty("_Label5","x",213)
				])
		];
	}
	var _proto = EqualViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 680;
		t.scale9Grid = new egret.Rectangle(33,32,5,7);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.confirmBtn_i = function () {
		var t = new eui.Image();
		this.confirmBtn = t;
		t.source = "viewpage_json.commonbtn";
		t.width = 331;
		t.x = 155;
		t.y = 514.31;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 581;
		t.y = -17;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "viewpage_json.mocoin";
		t.x = 338.5;
		t.y = 423;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.size = 34;
		t.text = "好";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 100;
		t.x = 270;
		t.y = 547.31;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 72;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xF9E9B5;
		t.text = "摇钱树赚钱秘籍";
		t.textAlign = "center";
		t.textColor = 0x8F5007;
		t.verticalAlign = "middle";
		t.width = 640;
		t.x = 0;
		t.y = 27;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetY = 0;
		t.height = 113;
		t.lineSpacing = 10;
		t.size = 30;
		t.strokeColor = 0xF9E9B5;
		t.text = "摇钱树等级越高\n每次领取的金币就越多\n升级物件也可以领取金币";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 640;
		t.x = 0;
		t.y = 160;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.anchorOffsetY = 0;
		t.height = 42;
		t.lineSpacing = 10;
		t.size = 30;
		t.strokeColor = 0xF9E9B5;
		t.text = "只要观看短短广告";
		t.textAlign = "center";
		t.textColor = 0x8F5007;
		t.verticalAlign = "middle";
		t.width = 640;
		t.x = 0;
		t.y = 329;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.anchorOffsetY = 0;
		t.height = 42;
		t.lineSpacing = 10;
		t.size = 30;
		t.strokeColor = 0xF9E9B5;
		t.text = "满级每天最高可领取";
		t.textAlign = "center";
		t.textColor = 0x5ba924;
		t.verticalAlign = "middle";
		t.width = 640;
		t.x = 0;
		t.y = 371;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		this._Label5 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.lineSpacing = 10;
		t.size = 30;
		t.strokeColor = 0xF9E9B5;
		t.text = "1800";
		t.textAlign = "center";
		t.textColor = 0x5BA924;
		t.verticalAlign = "middle";
		t.x = 232;
		t.y = 419;
		return t;
	};
	return EqualViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/ErrorView.exml'] = window.ErrorViewSkin = (function (_super) {
	__extends(ErrorViewSkin, _super);
	function ErrorViewSkin() {
		_super.call(this);
		this.skinParts = ["groupView"];
		
		this.elementsContent = [this.groupView_i()];
	}
	var _proto = ErrorViewSkin.prototype;

	_proto.groupView_i = function () {
		var t = new eui.Group();
		this.groupView = t;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this._Label1_i(),this._Label2_i(),this._Image2_i(),this._Label3_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 344;
		t.scale9Grid = new egret.Rectangle(33,31,4,6);
		t.source = "viewpage_json.viewbg";
		t.width = 540;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 36;
		t.text = "提示";
		t.textColor = 0x914e00;
		t.x = 233;
		t.y = 64;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.text = "网络异常，请重试";
		t.textColor = 0x914e00;
		t.x = 150;
		t.y = 147;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.nextbtn";
		t.x = 117;
		t.y = 210;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.text = "重试";
		t.x = 239;
		t.y = 249;
		return t;
	};
	return ErrorViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/ExplainViewSkin.exml'] = window.ExplainViewSkin = (function (_super) {
	__extends(ExplainViewSkin, _super);
	function ExplainViewSkin() {
		_super.call(this);
		this.skinParts = ["viewbg","titleTxt","pinyinLbl","descTxt","xscroller","btnNameLbl","addToBtn","feedbackLbl"];
		
		this.elementsContent = [this.viewbg_i(),this._Image1_i(),this.titleTxt_i(),this.pinyinLbl_i(),this.xscroller_i(),this._Rect1_i(),this._Label1_i(),this.addToBtn_i(),this.feedbackLbl_i()];
	}
	var _proto = ExplainViewSkin.prototype;

	_proto.viewbg_i = function () {
		var t = new eui.Image();
		this.viewbg = t;
		t.anchorOffsetY = 0;
		t.height = 680;
		t.scale9Grid = new egret.Rectangle(34,34,3,5);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 46.64;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xf9e9b5;
		t.text = "富可敌国";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.width = 640;
		t.x = 0;
		t.y = 38.38;
		return t;
	};
	_proto.pinyinLbl_i = function () {
		var t = new eui.Label();
		this.pinyinLbl = t;
		t.size = 26;
		t.stroke = 1;
		t.strokeColor = 0xF9E9B5;
		t.text = "pinyin";
		t.textAlign = "center";
		t.textColor = 0x8F5007;
		t.width = 640;
		t.x = 0;
		t.y = 129;
		return t;
	};
	_proto.xscroller_i = function () {
		var t = new eui.Scroller();
		this.xscroller = t;
		t.height = 340;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "on";
		t.width = 540;
		t.x = 48;
		t.y = 183;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.anchorOffsetX = 0;
		t.elementsContent = [this.descTxt_i()];
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.lineSpacing = 14;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "\n成语解释：${data.idiom_explain} 成语出处：${data.idiom_from} 成语例句：${data.idiom_eg} 成语故事：${data.idiom_story} 近义词：${data.idiom_similar} 反义词：${data.idiom_opposite}";
		t.textColor = 0x914e00;
		t.width = 536;
		t.x = 2;
		t.y = 5;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 16;
		t.ellipseWidth = 16;
		t.fillColor = 0xffeecd;
		t.height = 40;
		t.width = 66;
		t.x = 44;
		t.y = 164.99;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 24;
		t.text = "译义";
		t.textColor = 0xfea910;
		t.x = 51;
		t.y = 172.99;
		return t;
	};
	_proto.addToBtn_i = function () {
		var t = new eui.Group();
		this.addToBtn = t;
		t.touchChildren = false;
		t.x = 138;
		t.y = 559.32;
		t.elementsContent = [this._Image2_i(),this.btnNameLbl_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.btnNameLbl_i = function () {
		var t = new eui.Label();
		this.btnNameLbl = t;
		t.anchorOffsetX = 0;
		t.size = 34;
		t.text = "加入生词本";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 361;
		t.x = 3;
		t.y = 33;
		return t;
	};
	_proto.feedbackLbl_i = function () {
		var t = new eui.Label();
		this.feedbackLbl = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.border = false;
		t.height = 37;
		t.italic = false;
		t.size = 25;
		t.text = "有错误？点我反馈";
		t.textAlign = "center";
		t.textColor = 0xC19F7D;
		t.touchEnabled = true;
		t.verticalAlign = "middle";
		t.width = 244;
		t.x = 198;
		t.y = 668;
		return t;
	};
	return ExplainViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/FirstAddNewViewSkin.exml'] = window.FirstAddNewViewSkin = (function (_super) {
	__extends(FirstAddNewViewSkin, _super);
	function FirstAddNewViewSkin() {
		_super.call(this);
		this.skinParts = ["confirmBtn"];
		
		this.height = 752;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Label1_i(),this._Label2_i(),this._Label3_i(),this.confirmBtn_i(),this._Label4_i(),this._Image3_i(),this._Label5_i()];
	}
	var _proto = FirstAddNewViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.anchorOffsetY = 0;
		t.height = 694;
		t.scale9Grid = new egret.Rectangle(30,30,3,3);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 58;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.cypostip";
		t.x = 40;
		t.y = 300.68;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.horizontalCenter = 0;
		t.text = "大人，您的生词可在";
		t.textColor = 0x914e00;
		t.y = 186.34;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.text = "打页右上角-成语词典-生词本";
		t.textColor = 0x5fa92c;
		t.x = 101;
		t.y = 233.34;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.text = "查看";
		t.textColor = 0x914e00;
		t.x = 483;
		t.y = 233.34;
		return t;
	};
	_proto.confirmBtn_i = function () {
		var t = new eui.Image();
		this.confirmBtn = t;
		t.height = 90;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.width = 320;
		t.x = 160;
		t.y = 620.35;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.size = 34;
		t.text = "确定";
		t.touchEnabled = false;
		t.x = 286;
		t.y = 649.35;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xf9e9b5;
		t.text = "生词本";
		t.textColor = 0x8f5007;
		t.x = 259;
		t.y = 38;
		return t;
	};
	return FirstAddNewViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendApplyItemSkin.exml'] = window.FriendApplyItemSkin = (function (_super) {
	__extends(FriendApplyItemSkin, _super);
	function FriendApplyItemSkin() {
		_super.call(this);
		this.skinParts = ["headImg","maskRect","nameLbl","codeLbl"];
		
		this.height = 120;
		this.width = 590;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this._Image4_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i()];
	}
	var _proto = FriendApplyItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_cdlgbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.name = "agreeBtn";
		t.source = "dispelPk_json.dpk_agree";
		t.x = 471;
		t.y = 27;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.name = "refuseBtn";
		t.source = "dispelPk_json.dpk_refuse";
		t.x = 341;
		t.y = 27;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 25;
		t.y = 19;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 24;
		t.text = "卖火柴的小女孩";
		t.x = 130;
		t.y = 22;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 24;
		t.text = "邀请码:100";
		t.x = 130;
		t.y = 72;
		return t;
	};
	return FriendApplyItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendBattleDetailViewSkin.exml'] = window.FriendBattleDetailViewSkin = (function (_super) {
	__extends(FriendBattleDetailViewSkin, _super);
	function FriendBattleDetailViewSkin() {
		_super.call(this);
		this.skinParts = ["headImg","maskRect","nameLbl","codeLbl","victoryLbl","failLbl","ratioLbl"];
		
		this.height = 534;
		this.width = 660;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i(),this.victoryLbl_i(),this.failLbl_i(),this.ratioLbl_i(),this._Label1_i(),this._Label2_i(),this._Label3_i()];
	}
	var _proto = FriendBattleDetailViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_hydetailbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 605;
		t.y = -25;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 90;
		t.anchorOffsetY = 90;
		t.height = 180;
		t.source = "menuover_json.headimg";
		t.width = 180;
		t.x = 134;
		t.y = 138;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 90;
		t.anchorOffsetY = 90;
		t.height = 180;
		t.source = "";
		t.width = 180;
		t.x = 134;
		t.y = 138;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 156;
		t.ellipseWidth = 156;
		t.height = 156;
		t.width = 156;
		t.x = 57;
		t.y = 61;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 38;
		t.text = "卖火柴的小女孩";
		t.x = 280;
		t.y = 82;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 25;
		t.text = "邀请码:100";
		t.x = 288;
		t.y = 152;
		return t;
	};
	_proto.victoryLbl_i = function () {
		var t = new eui.Label();
		this.victoryLbl = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 48;
		t.text = "胜利";
		t.textAlign = "center";
		t.textColor = 0xa9f78f;
		t.width = 179;
		t.x = 18;
		t.y = 377;
		return t;
	};
	_proto.failLbl_i = function () {
		var t = new eui.Label();
		this.failLbl = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 48;
		t.text = "失败";
		t.textAlign = "center";
		t.textColor = 0xff576c;
		t.width = 187;
		t.x = 237;
		t.y = 377;
		return t;
	};
	_proto.ratioLbl_i = function () {
		var t = new eui.Label();
		this.ratioLbl = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 48;
		t.text = "胜率";
		t.textAlign = "center";
		t.textColor = 0xa9f78f;
		t.width = 198;
		t.x = 460;
		t.y = 377;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.text = "胜利";
		t.x = 76;
		t.y = 457;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.text = "失败";
		t.x = 301;
		t.y = 457;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.text = "胜率";
		t.x = 527;
		t.y = 457;
		return t;
	};
	return FriendBattleDetailViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendDeleteAlertSkin.exml'] = window.FriendDeleteAlertSkin = (function (_super) {
	__extends(FriendDeleteAlertSkin, _super);
	function FriendDeleteAlertSkin() {
		_super.call(this);
		this.skinParts = [];
		
		this.height = 472;
		this.width = 660;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this._Image4_i(),this._Image5_i(),this._Label1_i()];
	}
	var _proto = FriendDeleteAlertSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(33,34,31,33);
		t.source = "dispelPk_json.dpk_commonbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 296;
		t.scale9Grid = new egret.Rectangle(30,32,32,16);
		t.source = "dispelPk_json.dpk_secondbg";
		t.width = 620;
		t.x = 20;
		t.y = 35;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.name = "confirmBtn";
		t.source = "dispelPk_json.dpk_delconfirm";
		t.x = 26;
		t.y = 350;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_fcancelbtn";
		t.x = 388;
		t.y = 353;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 605;
		t.y = -25;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 36;
		t.stroke = 2;
		t.strokeColor = 0x2D417D;
		t.text = "确定要删除好友吗？";
		t.textColor = 0xffffff;
		t.x = 163;
		t.y = 152;
		return t;
	};
	return FriendDeleteAlertSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendDeleteItemSkin.exml'] = window.FriendDeleteItemSkin = (function (_super) {
	__extends(FriendDeleteItemSkin, _super);
	function FriendDeleteItemSkin() {
		_super.call(this);
		this.skinParts = ["headImg","maskRect","nameLbl","codeLbl"];
		
		this.height = 120;
		this.width = 590;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i()];
	}
	var _proto = FriendDeleteItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_cdlgbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.name = "deleteBtn";
		t.source = "dispelPk_json.dpk_deletenow";
		t.x = 491;
		t.y = 27;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 25;
		t.y = 19;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 24;
		t.text = "卖火柴的小女孩";
		t.x = 130;
		t.y = 22;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 24;
		t.text = "邀请码:100";
		t.x = 130;
		t.y = 72;
		return t;
	};
	return FriendDeleteItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendDetailItemSkin.exml'] = window.FriendDetailItemSkin = (function (_super) {
	__extends(FriendDetailItemSkin, _super);
	function FriendDetailItemSkin() {
		_super.call(this);
		this.skinParts = ["headImg","maskRect","nameLbl","codeLbl"];
		
		this.height = 120;
		this.width = 590;
		this.elementsContent = [this._Image1_i(),this._Rect1_i(),this._Rect2_i(),this._Rect3_i(),this._Image2_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i()];
	}
	var _proto = FriendDetailItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_cdlgbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 10;
		t.ellipseWidth = 10;
		t.fillColor = 0x0F2357;
		t.height = 10;
		t.width = 10;
		t.x = 512;
		t.y = 54;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 10;
		t.ellipseWidth = 10;
		t.fillColor = 0x0F2357;
		t.height = 10;
		t.width = 10;
		t.x = 554;
		t.y = 54;
		return t;
	};
	_proto._Rect3_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 10;
		t.ellipseWidth = 10;
		t.fillColor = 0x0F2357;
		t.height = 10;
		t.width = 10;
		t.x = 532;
		t.y = 54;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 25;
		t.y = 19;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 24;
		t.text = "卖火柴的小女孩";
		t.x = 130;
		t.y = 22;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 24;
		t.text = "邀请码:100";
		t.x = 130;
		t.y = 72;
		return t;
	};
	return FriendDetailItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendListItemSkin.exml'] = window.FriendListItemSkin = (function (_super) {
	__extends(FriendListItemSkin, _super);
	function FriendListItemSkin() {
		_super.call(this);
		this.skinParts = ["headImg","maskRect","nameLbl","codeLbl"];
		
		this.height = 120;
		this.width = 590;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i()];
	}
	var _proto = FriendListItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_cdlgbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.name = "invitePkBtn";
		t.source = "dispelPk_json.dpk_invitepk";
		t.x = 411;
		t.y = 27;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "";
		t.width = 90;
		t.x = 64;
		t.y = 58;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 25;
		t.y = 19;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 24;
		t.text = "卖火柴的小女孩";
		t.x = 130;
		t.y = 22;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 24;
		t.text = "邀请码:100";
		t.x = 130;
		t.y = 72;
		return t;
	};
	return FriendListItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendOnlineViewSkin.exml'] = window.FriendOnlineViewSkin = (function (_super) {
	__extends(FriendOnlineViewSkin, _super);
	function FriendOnlineViewSkin() {
		_super.call(this);
		this.skinParts = ["inviteBtn","arrowImg","listEmptyLbl","dataProvider"];
		
		this.height = 880;
		this.width = 660;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this.inviteBtn_i(),this._Label1_i(),this.listEmptyLbl_i(),this._Scroller1_i()];
		this.states = [
			new eui.State ("normal",
				[
				])
			,
			new eui.State ("ios",
				[
					new eui.SetProperty("_Image2","height",761),
					new eui.SetProperty("_Image2","anchorOffsetY",0),
					new eui.SetProperty("_Image2","horizontalCenter",0),
					new eui.SetProperty("inviteBtn","visible",false),
					new eui.SetProperty("_Label3","visible",false),
					new eui.SetProperty("arrowImg","visible",false),
					new eui.SetProperty("_Scroller1","anchorOffsetY",0),
					new eui.SetProperty("_Scroller1","height",720)
				])
		];
	}
	var _proto = FriendOnlineViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(33,34,31,33);
		t.source = "dispelPk_json.dpk_commonbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.height = 640;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(28,31,39,28);
		t.source = "dispelPk_json.dpk_secondbg";
		t.width = 620;
		t.y = 88;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 604;
		t.y = -26;
		return t;
	};
	_proto.inviteBtn_i = function () {
		var t = new eui.Image();
		this.inviteBtn = t;
		t.horizontalCenter = 0;
		t.name = "inviteBtn";
		t.source = "dispelPk_json.dpk_yqwxhy";
		t.y = 752;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.horizontalCenter = 0.5;
		t.size = 36;
		t.stroke = 2;
		t.strokeColor = 0x2D417D;
		t.text = "在线好友";
		t.y = 25;
		return t;
	};
	_proto.listEmptyLbl_i = function () {
		var t = new eui.Group();
		this.listEmptyLbl = t;
		t.x = 126;
		t.y = 358;
		t.elementsContent = [this._Label2_i(),this._Label3_i(),this.arrowImg_i()];
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.lineSpacing = 16;
		t.size = 30;
		t.stroke = 1;
		t.strokeColor = 0x2D417D;
		t.text = "暂无好友";
		t.textAlign = "center";
		t.textColor = 0x448ff9;
		t.width = 392;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.bold = true;
		t.lineSpacing = 16;
		t.size = 30;
		t.stroke = 1;
		t.strokeColor = 0x2D417D;
		t.text = "点击下方按钮邀请吧~";
		t.textAlign = "center";
		t.textColor = 0x448ff9;
		t.width = 392;
		t.y = 48;
		return t;
	};
	_proto.arrowImg_i = function () {
		var t = new eui.Image();
		this.arrowImg = t;
		t.source = "dispelPk_json.dpk_arrowtip";
		t.x = 180;
		t.y = 180;
		return t;
	};
	_proto._Scroller1_i = function () {
		var t = new eui.Scroller();
		this._Scroller1 = t;
		t.height = 590;
		t.scrollPolicyH = "off";
		t.width = 590;
		t.x = 36;
		t.y = 106;
		t.viewport = this._List1_i();
		return t;
	};
	_proto._List1_i = function () {
		var t = new eui.List();
		t.itemRenderer = FriendListItem;
		t.itemRendererSkinName = FriendListItemSkin;
		t.layout = this._VerticalLayout1_i();
		t.dataProvider = this.dataProvider_i();
		return t;
	};
	_proto._VerticalLayout1_i = function () {
		var t = new eui.VerticalLayout();
		t.gap = 14;
		return t;
	};
	_proto.dataProvider_i = function () {
		var t = new eui.ArrayCollection();
		this.dataProvider = t;
		t.source = [];
		return t;
	};
	return FriendOnlineViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendSearchViewSkin.exml'] = window.FriendSearchViewSkin = (function (_super) {
	__extends(FriendSearchViewSkin, _super);
	function FriendSearchViewSkin() {
		_super.call(this);
		this.skinParts = ["inputLbl","headImg","maskRect","nameLbl","codeLbl","friendGroup"];
		
		this.height = 402;
		this.width = 660;
		this.elementsContent = [this._Image1_i(),this._Label1_i(),this._Image2_i(),this._Image3_i(),this.inputLbl_i(),this.friendGroup_i(),this._Image8_i()];
	}
	var _proto = FriendSearchViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(33,34,31,33);
		t.source = "dispelPk_json.dpk_commonbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.horizontalCenter = 0.5;
		t.size = 36;
		t.stroke = 2;
		t.strokeColor = 0x2D417D;
		t.text = "搜索好友";
		t.y = 25;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.name = "searchBtn";
		t.source = "dispelPk_json.dpk_search";
		t.x = 486;
		t.y = 93;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_textbg";
		t.x = 25;
		t.y = 97;
		return t;
	};
	_proto.inputLbl_i = function () {
		var t = new eui.EditableText();
		this.inputLbl = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 54;
		t.inputType = "tel";
		t.maxChars = 9;
		t.prompt = "请输入对方邀请码";
		t.restrict = "0-9";
		t.size = 28;
		t.text = "";
		t.textAlign = "left";
		t.verticalAlign = "middle";
		t.width = 388;
		t.x = 60;
		t.y = 107;
		return t;
	};
	_proto.friendGroup_i = function () {
		var t = new eui.Group();
		this.friendGroup = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 124;
		t.visible = false;
		t.width = 583;
		t.x = 39;
		t.y = 231;
		t.elementsContent = [this._Image4_i(),this._Group1_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(28,31,39,28);
		t.source = "dispelPk_json.dpk_secondbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 95;
		t.width = 550;
		t.x = 16;
		t.y = 16;
		t.elementsContent = [this._Image5_i(),this._Image6_i(),this.headImg_i(),this.maskRect_i(),this.nameLbl_i(),this.codeLbl_i(),this._Image7_i()];
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,27,42,28);
		t.source = "dispelPk_json.dpk_cdlgbg";
		t.percentWidth = 100;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 64;
		t.y = 47;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "";
		t.width = 90;
		t.x = 64;
		t.y = 47;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 25;
		t.y = 8;
		return t;
	};
	_proto.nameLbl_i = function () {
		var t = new eui.Label();
		this.nameLbl = t;
		t.size = 24;
		t.text = "卖火柴的小女孩";
		t.x = 130;
		t.y = 16;
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 24;
		t.text = "邀请码:100";
		t.x = 130;
		t.y = 60;
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		t.name = "addFriendBtn";
		t.source = "dispelPk_json.dpk_addfriend";
		t.x = 383;
		t.y = 16;
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 596;
		t.y = -26;
		return t;
	};
	return FriendSearchViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/friend/FriendViewSkin.exml'] = window.FriendViewSkin = (function (_super) {
	__extends(FriendViewSkin, _super);
	function FriendViewSkin() {
		_super.call(this);
		this.skinParts = ["tabLabel1","tabGrp1","tabLabel2","applyCountLbl","applyGroup","tabGrp2","mainGrp","codeLbl","copyLbl","revokeBtn","deleteBtn","friendCountLbl","friendGroup","scrollerbg","dataProvider","list","scroller","noFriendImg","listEmptyLbl","closeBtn"];
		
		this.currentState = "friendstate";
		this.width = 660;
		this.elementsContent = [this.mainGrp_i(),this._Group1_i(),this.friendGroup_i(),this.scrollerbg_i(),this.scroller_i(),this.noFriendImg_i(),this.listEmptyLbl_i(),this.closeBtn_i()];
		this.states = [
			new eui.State ("friendstate",
				[
					new eui.SetProperty("_Image2","source","dispelPk_json.dpk_selected"),
					new eui.SetProperty("tabLabel1","x",6),
					new eui.SetProperty("tabLabel1","y",40),
					new eui.SetProperty("tabLabel1","textColor",0xffffff),
					new eui.SetProperty("tabLabel1","stroke",2),
					new eui.SetProperty("tabLabel1","strokeColor",0x2D417D),
					new eui.SetProperty("tabGrp1","y",14)
				])
			,
			new eui.State ("applystate",
				[
					new eui.SetProperty("_Image3","source","dispelPk_json.dpk_selected"),
					new eui.SetProperty("tabLabel2","x",24),
					new eui.SetProperty("tabLabel2","y",36),
					new eui.SetProperty("tabLabel2","textColor",0xffffff),
					new eui.SetProperty("tabLabel2","stroke",2),
					new eui.SetProperty("tabLabel2","strokeColor",0x2D417D),
					new eui.SetProperty("tabGrp2","y",14)
				])
		];
	}
	var _proto = FriendViewSkin.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.elementsContent = [this._Image1_i(),this.tabGrp1_i(),this.tabGrp2_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 800;
		t.scale9Grid = new egret.Rectangle(33,34,31,33);
		t.source = "dispelPk_json.dpk_commonbg";
		t.width = 660;
		t.y = 80;
		return t;
	};
	_proto.tabGrp1_i = function () {
		var t = new eui.Group();
		this.tabGrp1 = t;
		t.name = "tabBtn1";
		t.touchChildren = false;
		t.y = 27;
		t.elementsContent = [this._Image2_i(),this.tabLabel1_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.source = "dispelPk_json.dpk_notselected";
		return t;
	};
	_proto.tabLabel1_i = function () {
		var t = new eui.Label();
		this.tabLabel1 = t;
		t.bold = true;
		t.size = 30;
		t.text = "游戏好友";
		t.textAlign = "center";
		t.textColor = 0x6F89D3;
		t.width = 306;
		t.y = 31;
		return t;
	};
	_proto.tabGrp2_i = function () {
		var t = new eui.Group();
		this.tabGrp2 = t;
		t.name = "tabBtn2";
		t.touchChildren = false;
		t.x = 330;
		t.y = 27;
		t.elementsContent = [this._Image3_i(),this.tabLabel2_i(),this.applyGroup_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "dispelPk_json.dpk_notselected";
		return t;
	};
	_proto.tabLabel2_i = function () {
		var t = new eui.Label();
		this.tabLabel2 = t;
		t.bold = true;
		t.size = 30;
		t.text = "好友申请";
		t.textAlign = "center";
		t.textColor = 0x6F89D3;
		t.width = 293;
		t.x = 5;
		t.y = 31;
		return t;
	};
	_proto.applyGroup_i = function () {
		var t = new eui.Group();
		this.applyGroup = t;
		t.visible = false;
		t.x = 217.32;
		t.y = 2;
		t.elementsContent = [this._Rect1_i(),this.applyCountLbl_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 33;
		t.ellipseWidth = 43;
		t.fillColor = 0xfa572b;
		t.height = 32;
		t.strokeColor = 0xe0a650;
		t.strokeWeight = 0;
		t.touchEnabled = false;
		t.width = 52;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.applyCountLbl_i = function () {
		var t = new eui.Label();
		this.applyCountLbl = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 17;
		t.size = 22;
		t.text = "99+";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 39;
		t.x = 7;
		t.y = 7;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.anchorOffsetY = 0;
		t.height = 42;
		t.name = "copyBtn";
		t.touchChildren = false;
		t.x = 20;
		t.y = 117;
		t.elementsContent = [this.codeLbl_i(),this.copyLbl_i()];
		return t;
	};
	_proto.codeLbl_i = function () {
		var t = new eui.Label();
		this.codeLbl = t;
		t.size = 26;
		t.text = "您的邀请码:01234551000";
		t.x = 0;
		t.y = 8;
		return t;
	};
	_proto.copyLbl_i = function () {
		var t = new eui.Label();
		this.copyLbl = t;
		t.bold = true;
		t.size = 26;
		t.text = "(点击复制)";
		t.textColor = 0x1B43A3;
		t.x = 302;
		t.y = 7;
		return t;
	};
	_proto.friendGroup_i = function () {
		var t = new eui.Group();
		this.friendGroup = t;
		t.x = 26;
		t.y = 783;
		t.elementsContent = [this._Image4_i(),this.revokeBtn_i(),this.deleteBtn_i(),this._Rect2_i(),this._Image5_i(),this.friendCountLbl_i(),this._Label1_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.name = "searchBtn";
		t.source = "dispelPk_json.dpk_searchhy";
		t.y = 2;
		return t;
	};
	_proto.revokeBtn_i = function () {
		var t = new eui.Image();
		this.revokeBtn = t;
		t.name = "revokeBtn";
		t.source = "dispelPk_json.dpk_cancel";
		t.x = 530;
		t.y = -3;
		return t;
	};
	_proto.deleteBtn_i = function () {
		var t = new eui.Image();
		this.deleteBtn = t;
		t.name = "deleteBtn";
		t.source = "dispelPk_json.dpk_deletebtn";
		t.x = 530;
		t.y = -3;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 40;
		t.ellipseWidth = 40;
		t.fillColor = 0x1B43A3;
		t.height = 40;
		t.width = 144;
		t.x = 361;
		t.y = 8;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_txl";
		t.x = 380;
		t.y = 17;
		return t;
	};
	_proto.friendCountLbl_i = function () {
		var t = new eui.Label();
		this.friendCountLbl = t;
		t.anchorOffsetX = 0;
		t.size = 24;
		t.text = "2/100";
		t.width = 80;
		t.x = 418;
		t.y = 17;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "游戏内好友,非微信好友";
		t.x = 262;
		t.y = 56;
		return t;
	};
	_proto.scrollerbg_i = function () {
		var t = new eui.Image();
		this.scrollerbg = t;
		t.height = 600;
		t.scale9Grid = new egret.Rectangle(37,30,30,14);
		t.source = "dispelPk_json.dpk_secondbg";
		t.width = 620;
		t.x = 20;
		t.y = 168;
		return t;
	};
	_proto.scroller_i = function () {
		var t = new eui.Scroller();
		this.scroller = t;
		t.anchorOffsetY = 0;
		t.height = 580;
		t.width = 600;
		t.x = 30;
		t.y = 177;
		t.viewport = this.list_i();
		return t;
	};
	_proto.list_i = function () {
		var t = new eui.List();
		this.list = t;
		t.dataProvider = this.dataProvider_i();
		t.layout = this._VerticalLayout1_i();
		return t;
	};
	_proto.dataProvider_i = function () {
		var t = new eui.ArrayCollection();
		this.dataProvider = t;
		return t;
	};
	_proto._VerticalLayout1_i = function () {
		var t = new eui.VerticalLayout();
		t.gap = 10;
		return t;
	};
	_proto.noFriendImg_i = function () {
		var t = new eui.Image();
		this.noFriendImg = t;
		t.source = "dispelPk_json.dpk_blankhy";
		t.visible = false;
		t.x = 239;
		t.y = 310;
		return t;
	};
	_proto.listEmptyLbl_i = function () {
		var t = new eui.Label();
		this.listEmptyLbl = t;
		t.bold = true;
		t.horizontalCenter = 1;
		t.size = 30;
		t.stroke = 1;
		t.strokeColor = 0x2D417D;
		t.text = "暂无好友申请";
		t.textAlign = "center";
		t.textColor = 0x448ff9;
		t.visible = false;
		t.width = 392;
		t.y = 465.53;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.name = "closeBtn";
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 602;
		t.y = -4;
		return t;
	};
	return FriendViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/getedPuzzle.exml'] = window.getedPuzzle = (function (_super) {
	__extends(getedPuzzle, _super);
	function getedPuzzle() {
		_super.call(this);
		this.skinParts = ["receiveBtn","btnNameLbl","puzzleImg","puzzleTxt","unownSp","puzzle2Img","puzzle2Txt","coin2Txt","subLbl","ownSp","tips","firstCoinImg"];
		
		this.height = 720;
		this.width = 640;
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Image3_i(),this.receiveBtn_i(),this._Label1_i(),this.btnNameLbl_i(),this.unownSp_i(),this.ownSp_i(),this.firstCoinImg_i()];
		this._Image5_i();
		
		this.tips_i();
		
		this.states = [
			new eui.State ("getUnown",
				[
					new eui.AddItems("tips","",2,"firstCoinImg"),
					new eui.SetProperty("receiveBtn","horizontalCenter",0),
					new eui.SetProperty("receiveBtn","y",601),
					new eui.SetProperty("btnNameLbl","horizontalCenter",0),
					new eui.SetProperty("btnNameLbl","y",628),
					new eui.SetProperty("puzzleTxt","y",316),
					new eui.SetProperty("ownSp","visible",false),
					new eui.SetProperty("firstCoinImg","source","viewpage_json.mocoin"),
					new eui.SetProperty("firstCoinImg","y",522),
					new eui.SetProperty("firstCoinImg","x",481)
				])
			,
			new eui.State ("getOwned",
				[
					new eui.AddItems("_Image5","ownSp",1,""),
					new eui.SetProperty("unownSp","visible",false)
				])
		];
	}
	var _proto = getedPuzzle.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.bottom = 0;
		t.left = 0;
		t.right = 0;
		t.scale9Grid = new egret.Rectangle(26,28,31,36);
		t.source = "puzzle_json.puzzleBg";
		t.top = 0;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "puzzle_json.puzzleColorDot";
		t.x = 422;
		t.y = 53;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 90;
		t.anchorOffsetY = 0;
		t.scaleX = -1;
		t.source = "puzzle_json.puzzleColorDot";
		t.x = 129;
		t.y = 53;
		return t;
	};
	_proto.receiveBtn_i = function () {
		var t = new eui.Image();
		this.receiveBtn = t;
		t.horizontalCenter = 0;
		t.source = "puzzle_json.puzzleBtn";
		t.y = 616;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.horizontalCenter = 0;
		t.size = 40;
		t.text = "恭喜获得";
		t.textColor = 0x000000;
		t.y = 48;
		return t;
	};
	_proto.btnNameLbl_i = function () {
		var t = new eui.Label();
		this.btnNameLbl = t;
		t.bold = true;
		t.horizontalCenter = 0;
		t.size = 40;
		t.text = "收下";
		t.textColor = 0xffffff;
		t.touchEnabled = false;
		t.y = 643;
		return t;
	};
	_proto.unownSp_i = function () {
		var t = new eui.Group();
		this.unownSp = t;
		t.x = 170;
		t.y = 150;
		t.elementsContent = [this.puzzleImg_i(),this.puzzleTxt_i()];
		return t;
	};
	_proto.puzzleImg_i = function () {
		var t = new eui.Image();
		this.puzzleImg = t;
		t.height = 300;
		t.source = "puzzle_json.puzzle_1";
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.puzzleTxt_i = function () {
		var t = new eui.Label();
		this.puzzleTxt = t;
		t.bold = true;
		t.size = 38;
		t.text = "Label";
		t.textAlign = "center";
		t.textColor = 0xF15841;
		t.width = 300;
		t.x = 0;
		t.y = 323;
		return t;
	};
	_proto.ownSp_i = function () {
		var t = new eui.Group();
		this.ownSp = t;
		t.x = 60;
		t.y = 200;
		t.elementsContent = [this.puzzle2Img_i(),this._Image4_i(),this.puzzle2Txt_i(),this.coin2Txt_i(),this.subLbl_i()];
		return t;
	};
	_proto.puzzle2Img_i = function () {
		var t = new eui.Image();
		this.puzzle2Img = t;
		t.height = 220;
		t.source = "puzzle_json.puzzle_1";
		t.width = 220;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "puzzle_json.puzzleCoinIcon";
		t.x = 300;
		t.y = 0;
		return t;
	};
	_proto.puzzle2Txt_i = function () {
		var t = new eui.Label();
		this.puzzle2Txt = t;
		t.bold = true;
		t.size = 38;
		t.text = "Label";
		t.textAlign = "center";
		t.textColor = 0xf15841;
		t.width = 220;
		t.x = 0;
		t.y = 250;
		return t;
	};
	_proto.coin2Txt_i = function () {
		var t = new eui.Label();
		this.coin2Txt = t;
		t.bold = true;
		t.size = 38;
		t.text = "Label";
		t.textAlign = "center";
		t.textColor = 0xeca214;
		t.width = 220;
		t.x = 300;
		t.y = 250;
		return t;
	};
	_proto.subLbl_i = function () {
		var t = new eui.Label();
		this.subLbl = t;
		t.size = 28;
		t.text = "已拥有，自动转换成金币";
		t.textColor = 0x999999;
		t.x = 106;
		t.y = 312;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		this._Image5 = t;
		t.source = "puzzle_json.puzzleArrow";
		t.x = 238;
		t.y = 95;
		return t;
	};
	_proto.tips_i = function () {
		var t = new eui.Label();
		this.tips = t;
		t.anchorOffsetX = 0;
		t.height = 28;
		t.horizontalCenter = 0;
		t.size = 28;
		t.text = "tips";
		t.textAlign = "center";
		t.textColor = 0x666666;
		t.width = 462;
		t.y = 542;
		return t;
	};
	_proto.firstCoinImg_i = function () {
		var t = new eui.Image();
		this.firstCoinImg = t;
		return t;
	};
	return getedPuzzle;
})(eui.Skin);generateEUI.paths['resource/game_skins/GuessGroupItem.exml'] = window.GuessGroupItemSkin = (function (_super) {
	__extends(GuessGroupItemSkin, _super);
	function GuessGroupItemSkin() {
		_super.call(this);
		this.skinParts = ["levelGrp0","levelGrp1","levelGrp2","levelGrp3","levelGrp4","levelGrp5","levelGrp6","levelGrp7","levelGrp8","levelGrp9","levelGrp10","levelGrp11","mainGrp"];
		
		this.minHeight = 50;
		this.minWidth = 100;
		this.elementsContent = [this.mainGrp_i()];
	}
	var _proto = GuessGroupItemSkin.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.levelGrp0_i(),this.levelGrp1_i(),this.levelGrp2_i(),this.levelGrp3_i(),this.levelGrp4_i(),this.levelGrp5_i(),this.levelGrp6_i(),this.levelGrp7_i(),this.levelGrp8_i(),this.levelGrp9_i(),this.levelGrp10_i(),this.levelGrp11_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "glvlbg_png";
		t.touchEnabled = false;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.levelGrp0_i = function () {
		var t = new eui.Group();
		this.levelGrp0 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 160;
		t.y = 1190;
		t.elementsContent = [this._Image2_i(),this._Label1_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xb25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xfffaf1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp1_i = function () {
		var t = new eui.Group();
		this.levelGrp1 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 337;
		t.y = 1159;
		t.elementsContent = [this._Image3_i(),this._Label2_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp2_i = function () {
		var t = new eui.Group();
		this.levelGrp2 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 500;
		t.y = 1099;
		t.elementsContent = [this._Image4_i(),this._Label3_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp3_i = function () {
		var t = new eui.Group();
		this.levelGrp3 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 485;
		t.y = 936;
		t.elementsContent = [this._Image5_i(),this._Label4_i()];
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp4_i = function () {
		var t = new eui.Group();
		this.levelGrp4 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 354;
		t.y = 820;
		t.elementsContent = [this._Image6_i(),this._Label5_i()];
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp5_i = function () {
		var t = new eui.Group();
		this.levelGrp5 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 215;
		t.y = 677;
		t.elementsContent = [this._Image7_i(),this._Label6_i()];
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp6_i = function () {
		var t = new eui.Group();
		this.levelGrp6 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 367;
		t.y = 576;
		t.elementsContent = [this._Image8_i(),this._Label7_i()];
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp7_i = function () {
		var t = new eui.Group();
		this.levelGrp7 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 512;
		t.y = 464;
		t.elementsContent = [this._Image9_i(),this._Label8_i()];
		return t;
	};
	_proto._Image9_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp8_i = function () {
		var t = new eui.Group();
		this.levelGrp8 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 458;
		t.y = 291;
		t.elementsContent = [this._Image10_i(),this._Label9_i()];
		return t;
	};
	_proto._Image10_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp9_i = function () {
		var t = new eui.Group();
		this.levelGrp9 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 284;
		t.y = 234;
		t.elementsContent = [this._Image11_i(),this._Label10_i()];
		return t;
	};
	_proto._Image11_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp10_i = function () {
		var t = new eui.Group();
		this.levelGrp10 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 117;
		t.y = 177;
		t.elementsContent = [this._Image12_i(),this._Label11_i()];
		return t;
	};
	_proto._Image12_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	_proto.levelGrp11_i = function () {
		var t = new eui.Group();
		this.levelGrp11 = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 79;
		t.y = 12;
		t.elementsContent = [this._Image13_i(),this._Label12_i()];
		return t;
	};
	_proto._Image13_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.levellock";
		t.x = 10;
		t.y = 0;
		return t;
	};
	_proto._Label12_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 50;
		t.size = 46;
		t.stroke = 4;
		t.strokeColor = 0xB25303;
		t.text = "12";
		t.textAlign = "center";
		t.textColor = 0xFFFAF1;
		t.verticalAlign = "middle";
		t.width = 160;
		t.x = 0;
		t.y = 93;
		return t;
	};
	return GuessGroupItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/GuessOverItem.exml'] = window.GuessOverItemSkin = (function (_super) {
	__extends(GuessOverItemSkin, _super);
	function GuessOverItemSkin() {
		_super.call(this);
		this.skinParts = ["titleTxt","backBtn","nextBtn","nextTxt","explainBg","idiomTxt","addNewBtn","explainTxt","exScroller","videoIcon"];
		
		this.elementsContent = [this._Group3_i()];
	}
	var _proto = GuessOverItemSkin.prototype;

	_proto._Group3_i = function () {
		var t = new eui.Group();
		t.cacheAsBitmap = true;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Rect1_i(),this._Image1_i(),this.titleTxt_i(),this.backBtn_i(),this.nextBtn_i(),this.nextTxt_i(),this._Group1_i(),this.exScroller_i(),this.videoIcon_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 64;
		t.ellipseWidth = 64;
		t.fillColor = 0xFFFEFA;
		t.height = 580;
		t.width = 664;
		t.x = 0;
		t.y = 65;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.overtitlebg";
		t.x = 57;
		t.y = 0;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.bold = true;
		t.size = 36;
		t.text = "恭喜通过第 600 关";
		t.textAlign = "center";
		t.width = 481;
		t.x = 92;
		t.y = 28;
		return t;
	};
	_proto.backBtn_i = function () {
		var t = new eui.Image();
		this.backBtn = t;
		t.height = 100;
		t.source = "guessgame_json.backbtn";
		t.touchEnabled = true;
		t.width = 100;
		t.x = 75;
		t.y = 524;
		return t;
	};
	_proto.nextBtn_i = function () {
		var t = new eui.Image();
		this.nextBtn = t;
		t.source = "menuover_json.nextbtn";
		t.touchEnabled = true;
		t.x = 221;
		t.y = 525;
		return t;
	};
	_proto.nextTxt_i = function () {
		var t = new eui.Label();
		this.nextTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 36;
		t.text = "下一关";
		t.touchEnabled = false;
		t.x = 320;
		t.y = 559;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.anchorOffsetY = 0;
		t.x = 78;
		t.y = 146;
		t.elementsContent = [this.explainBg_i(),this._Rect2_i(),this.idiomTxt_i(),this.addNewBtn_i()];
		return t;
	};
	_proto.explainBg_i = function () {
		var t = new eui.Image();
		this.explainBg = t;
		t.anchorOffsetY = 0;
		t.height = 346.67;
		t.scale9Grid = new egret.Rectangle(7,7,2,2);
		t.source = "guessgame_json.overidiombg";
		t.width = 508;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 16;
		t.ellipseWidth = 16;
		t.fillColor = 0xffeecd;
		t.height = 42;
		t.width = 128;
		t.x = 190.5;
		t.y = 22;
		return t;
	};
	_proto.idiomTxt_i = function () {
		var t = new eui.Label();
		this.idiomTxt = t;
		t.size = 28;
		t.text = "富可敌国";
		t.textAlign = "center";
		t.textColor = 0xe28d00;
		t.width = 128;
		t.x = 190.5;
		t.y = 30;
		return t;
	};
	_proto.addNewBtn_i = function () {
		var t = new eui.Image();
		this.addNewBtn = t;
		t.source = "menuover_json.addidiombtn";
		t.touchEnabled = true;
		t.x = 328;
		t.y = 15;
		return t;
	};
	_proto.exScroller_i = function () {
		var t = new eui.Scroller();
		this.exScroller = t;
		t.height = 244;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "auto";
		t.width = 456;
		t.x = 104;
		t.y = 230;
		t.viewport = this._Group2_i();
		return t;
	};
	_proto._Group2_i = function () {
		var t = new eui.Group();
		t.elementsContent = [this.explainTxt_i()];
		return t;
	};
	_proto.explainTxt_i = function () {
		var t = new eui.Label();
		this.explainTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.lineSpacing = 10;
		t.multiline = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.scrollV = 2;
		t.text = "私人拥有的财富可与国家的资财相匹敌；sdfgasdgasdgasdgsdagsdagsdagsdagsdagiu会跟随阿贡火山大概就哦适当i哦感觉死哦大概就哦四大金刚四大给司机大哥iOS打进欧冠决赛到国际赛道i给给i静安寺滴哦关键是带哦关键是带哦感觉形容极为富有。";
		t.textColor = 0x914e00;
		t.width = 456;
		t.wordWrap = false;
		t.x = 0;
		t.y = 10;
		return t;
	};
	_proto.videoIcon_i = function () {
		var t = new eui.Image();
		this.videoIcon = t;
		t.source = "guessgame_json.video4";
		t.x = 257;
		t.y = 557;
		return t;
	};
	return GuessOverItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/GuessRewardViewSkin.exml'] = window.GuessRewardViewSkin = (function (_super) {
	__extends(GuessRewardViewSkin, _super);
	function GuessRewardViewSkin() {
		_super.call(this);
		this.skinParts = ["effectImg","titleImg","getDbBtn","videoTxt","getLowBtn","coinTxt","finCoinTxt","viewGrp"];
		
		this.elementsContent = [this.viewGrp_i()];
	}
	var _proto = GuessRewardViewSkin.prototype;

	_proto.viewGrp_i = function () {
		var t = new eui.Group();
		this.viewGrp = t;
		t.touchChildren = true;
		t.x = 5;
		t.y = 2;
		t.elementsContent = [this.effectImg_i(),this.titleImg_i(),this._Group1_i()];
		return t;
	};
	_proto.effectImg_i = function () {
		var t = new eui.Image();
		this.effectImg = t;
		t.alpha = 0.7;
		t.anchorOffsetX = 248;
		t.anchorOffsetY = 248;
		t.source = "redeff_json.lightbox";
		t.x = 247;
		t.y = 395;
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.anchorOffsetX = 167;
		t.anchorOffsetY = 220;
		t.source = "redeff_json.openred";
		t.touchEnabled = true;
		t.x = 247;
		t.y = 395;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.cacheAsBitmap = true;
		t.touchThrough = true;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.getDbBtn_i(),this._Image2_i(),this.videoTxt_i(),this.getLowBtn_i(),this.coinTxt_i(),this.finCoinTxt_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "redeff_json.successtitle";
		t.x = -3.5;
		t.y = 0;
		return t;
	};
	_proto.getDbBtn_i = function () {
		var t = new eui.Image();
		this.getDbBtn = t;
		t.height = 101;
		t.scale9Grid = new egret.Rectangle(73,21,134,43);
		t.source = "guessgame_json.deletebtn";
		t.touchEnabled = true;
		t.width = 493;
		t.x = 0;
		t.y = 662;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "guessgame_json.video1";
		t.touchEnabled = false;
		t.x = 379;
		t.y = 693.5;
		return t;
	};
	_proto.videoTxt_i = function () {
		var t = new eui.Label();
		this.videoTxt = t;
		t.bold = true;
		t.size = 36;
		t.text = "领取100金币奖励";
		t.touchEnabled = false;
		t.x = 89;
		t.y = 695;
		return t;
	};
	_proto.getLowBtn_i = function () {
		var t = new eui.Rect();
		this.getLowBtn = t;
		t.ellipseHeight = 32;
		t.ellipseWidth = 32;
		t.fillAlpha = 0.1;
		t.height = 80;
		t.strokeColor = 0xffbe19;
		t.strokeWeight = 2;
		t.touchEnabled = true;
		t.width = 482;
		t.x = 9;
		t.y = 809;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.text = "领取10金币";
		t.textAlign = "center";
		t.textColor = 0xffcc21;
		t.touchEnabled = false;
		t.width = 482;
		t.x = 9;
		t.y = 837;
		return t;
	};
	_proto.finCoinTxt_i = function () {
		var t = new eui.Label();
		this.finCoinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 72;
		t.text = "+72";
		t.textAlign = "center";
		t.textColor = 0xffd200;
		t.width = 220;
		t.x = 126;
		t.y = 106;
		return t;
	};
	return GuessRewardViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/GuessSingleRewardViewSkin.exml'] = window.GuessSingleRewardViewSkin = (function (_super) {
	__extends(GuessSingleRewardViewSkin, _super);
	function GuessSingleRewardViewSkin() {
		_super.call(this);
		this.skinParts = ["effImg","getBtn","coinTxt"];
		
		this.elementsContent = [this.effImg_i(),this._Image1_i(),this._Image2_i(),this._Image3_i(),this.getBtn_i(),this._Label1_i(),this._Label2_i(),this._Label3_i(),this.coinTxt_i()];
	}
	var _proto = GuessSingleRewardViewSkin.prototype;

	_proto.effImg_i = function () {
		var t = new eui.Image();
		this.effImg = t;
		t.anchorOffsetX = 248;
		t.anchorOffsetY = 248;
		t.scaleX = 0.6;
		t.scaleY = 0.6;
		t.source = "redeff_json.lightbox";
		t.x = 321;
		t.y = 149;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 390;
		t.scale9Grid = new egret.Rectangle(33,33,5,5);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 1;
		t.y = 161;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 130;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "redeff_json.guessredbag";
		t.x = 105;
		t.y = 0;
		return t;
	};
	_proto.getBtn_i = function () {
		var t = new eui.Image();
		this.getBtn = t;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.x = 139;
		t.y = 417;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 34;
		t.text = "立即领取";
		t.touchEnabled = false;
		t.x = 253;
		t.y = 451;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 48;
		t.text = "+";
		t.textColor = 0xfea910;
		t.x = 201.5;
		t.y = 324;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 48;
		t.text = "金币";
		t.textColor = 0xFEA910;
		t.x = 328;
		t.y = 318;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 80;
		t.text = "77";
		t.textAlign = "center";
		t.textColor = 0xFEA910;
		t.width = 115;
		t.x = 220;
		t.y = 293;
		return t;
	};
	return GuessSingleRewardViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/HeadItem.exml'] = window.HeadItemSkin = (function (_super) {
	__extends(HeadItemSkin, _super);
	function HeadItemSkin() {
		_super.call(this);
		this.skinParts = ["headMask","coinTxt","cashBtn","coinGrp","headImg","soundBtn","lifeImg","timeTxt","numTxt","redPoint","lifeGrp","expTxt"];
		
		this.elementsContent = [this.headMask_i(),this.coinGrp_i(),this.headImg_i(),this.soundBtn_i(),this.lifeGrp_i(),this._Image4_i(),this.expTxt_i()];
	}
	var _proto = HeadItemSkin.prototype;

	_proto.headMask_i = function () {
		var t = new eui.Rect();
		this.headMask = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.ellipseWidth = 88;
		t.height = 88;
		t.width = 88;
		t.x = 0;
		t.y = 8;
		return t;
	};
	_proto.coinGrp_i = function () {
		var t = new eui.Group();
		this.coinGrp = t;
		t.x = 72;
		t.y = 23;
		t.elementsContent = [this._Image1_i(),this._Image2_i(),this.coinTxt_i(),this.cashBtn_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.scale9Grid = new egret.Rectangle(78,6,8,40);
		t.source = "menuover_json.hnamebg";
		t.width = 229;
		t.x = -3;
		t.y = 5;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 20;
		t.anchorOffsetY = 20;
		t.height = 40;
		t.source = "menuover_json.coin";
		t.width = 40;
		t.x = 50;
		t.y = 32;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.fontFamily = "Montserrat-Bold";
		t.size = 24;
		t.text = "3687";
		t.textAlign = "center";
		t.width = 155;
		t.x = 39;
		t.y = 21;
		return t;
	};
	_proto.cashBtn_i = function () {
		var t = new eui.Image();
		this.cashBtn = t;
		t.source = "menuover_json.smallbtn";
		t.x = 178;
		t.y = 5;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.height = 100;
		t.source = "menuover_json.headimg";
		t.width = 100;
		t.x = -6;
		t.y = 2;
		return t;
	};
	_proto.soundBtn_i = function () {
		var t = new eui.Image();
		this.soundBtn = t;
		t.name = "soundBtnName";
		t.source = "menuover_json.soundbtn";
		t.x = 666;
		t.y = 24;
		return t;
	};
	_proto.lifeGrp_i = function () {
		var t = new eui.Group();
		this.lifeGrp = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 377;
		t.y = 21;
		t.elementsContent = [this._Image3_i(),this.lifeImg_i(),this.timeTxt_i(),this.numTxt_i(),this.redPoint_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.scale9Grid = new egret.Rectangle(78,6,8,40);
		t.source = "menuover_json.hnamebg";
		t.width = 136;
		t.x = 7;
		t.y = 7;
		return t;
	};
	_proto.lifeImg_i = function () {
		var t = new eui.Image();
		this.lifeImg = t;
		t.source = "menuover_json.lifeB";
		t.x = 0;
		t.y = 3;
		return t;
	};
	_proto.timeTxt_i = function () {
		var t = new eui.Label();
		this.timeTxt = t;
		t.anchorOffsetX = 0;
		t.border = false;
		t.borderColor = 0x04f4ef;
		t.fontFamily = "Montserrat-Bold";
		t.size = 20;
		t.stroke = 3;
		t.strokeColor = 0x428bcb;
		t.text = "00:00";
		t.x = 0;
		t.y = 40;
		return t;
	};
	_proto.numTxt_i = function () {
		var t = new eui.Label();
		this.numTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.fontFamily = "Montserrat-Bold";
		t.size = 24;
		t.text = "10/20";
		t.textAlign = "center";
		t.width = 105;
		t.x = 40;
		t.y = 22;
		return t;
	};
	_proto.redPoint_i = function () {
		var t = new eui.Image();
		this.redPoint = t;
		t.source = "menuover_json.redpoint";
		t.x = 127;
		t.y = 0;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.expbg";
		t.x = 8;
		t.y = 78;
		return t;
	};
	_proto.expTxt_i = function () {
		var t = new eui.Label();
		this.expTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 22;
		t.size = 18;
		t.text = "阅历值: 20000";
		t.textAlign = "center";
		t.touchEnabled = true;
		t.verticalAlign = "middle";
		t.width = 150;
		t.x = 9;
		t.y = 79;
		return t;
	};
	return HeadItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/InvitePromotionCountdownSkin.exml'] = window.InvitePromotionCountdownSkin = (function (_super) {
	__extends(InvitePromotionCountdownSkin, _super);
	function InvitePromotionCountdownSkin() {
		_super.call(this);
		this.skinParts = ["rpImg","countdownLabel"];
		
		this.width = 130;
		this.elementsContent = [this._Image1_i(),this.rpImg_i(),this._Label1_i(),this._Label2_i(),this.countdownLabel_i()];
	}
	var _proto = InvitePromotionCountdownSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 72;
		t.source = "menuover_json.countdown_bg";
		t.visible = false;
		t.width = 178;
		t.x = 23;
		t.y = 9;
		return t;
	};
	_proto.rpImg_i = function () {
		var t = new eui.Image();
		this.rpImg = t;
		t.height = 83;
		t.source = "menuover_json.redpack_0";
		t.width = 66;
		t.x = 31;
		t.y = 1.5;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 22;
		t.stroke = 4;
		t.strokeColor = 0xe7643b;
		t.text = "后过期";
		t.textColor = 0xFFFFFF;
		t.x = 30.5;
		t.y = 100;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 22;
		t.text = "￥2.5";
		t.textColor = 0xFFEFC7;
		t.visible = false;
		t.x = 34;
		t.y = 53.5;
		return t;
	};
	_proto.countdownLabel_i = function () {
		var t = new eui.Label();
		this.countdownLabel = t;
		t.size = 24;
		t.stroke = 4;
		t.strokeColor = 0xe7643b;
		t.text = "00:00:00";
		t.textColor = 0xFFFFFF;
		t.x = 19.5;
		t.y = 73.5;
		return t;
	};
	return InvitePromotionCountdownSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/InvitePromotionSkin.exml'] = window.InvitePromotionSkin = (function (_super) {
	__extends(InvitePromotionSkin, _super);
	function InvitePromotionSkin() {
		_super.call(this);
		this.skinParts = ["viewbg","titleImg","closeBtn","coinNumLabel","rpImg1","rpImg2","rpImg3","rpImg4","btnImg","btnLabel"];
		
		this.currentState = "no_coins";
		this.height = 1344;
		this.width = 750;
		this.elementsContent = [this.viewbg_i(),this.titleImg_i(),this.closeBtn_i(),this._Label1_i(),this.coinNumLabel_i(),this._Label2_i(),this._Label3_i(),this._Label4_i(),this._Rect1_i(),this._Rect2_i(),this.rpImg1_i(),this.rpImg2_i(),this.rpImg3_i(),this.rpImg4_i(),this._Label5_i(),this._Label6_i(),this._Label7_i(),this._Label8_i(),this._Rect3_i(),this._Label9_i(),this._Rect4_i(),this._Label10_i(),this._Rect5_i(),this._Label11_i(),this._Group1_i()];
		this.states = [
			new eui.State ("no_coins",
				[
				])
			,
			new eui.State ("has_coins",
				[
					new eui.SetProperty("btnLabel","text","收下，去提现")
				])
		];
	}
	var _proto = InvitePromotionSkin.prototype;

	_proto.viewbg_i = function () {
		var t = new eui.Image();
		this.viewbg = t;
		t.anchorOffsetY = 0;
		t.height = 680;
		t.scale9Grid = new egret.Rectangle(34,34,3,5);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 55;
		t.y = 295;
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.source = "viewpage_json.invite_reward_title";
		t.x = 150;
		t.y = 125;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.touchEnabled = true;
		t.x = 647;
		t.y = 269;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 34;
		t.text = "恭喜获得邀请好友奖励";
		t.textColor = 0x914e00;
		t.x = 206;
		t.y = 377;
		return t;
	};
	_proto.coinNumLabel_i = function () {
		var t = new eui.Label();
		this.coinNumLabel = t;
		t.fontFamily = "Montserrat-Bold";
		t.size = 100;
		t.text = "+25000";
		t.textAlign = "left";
		t.textColor = 0xff6038;
		t.verticalAlign = "middle";
		t.x = 141;
		t.y = 450;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.size = 38;
		t.text = "金币";
		t.textColor = 0xff6038;
		t.x = 535;
		t.y = 485;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.height = 55;
		t.size = 22;
		t.text = "成功邀请一名好友，即可存入钱包，具体金额以实际到账为准";
		t.textColor = 0xccb090;
		t.width = 416;
		t.x = 157;
		t.y = 547;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.size = 30;
		t.text = "更多奖励";
		t.textColor = 0x914E00;
		t.x = 316;
		t.y = 647;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 19;
		t.fillColor = 0xeee7d6;
		t.height = 18;
		t.width = 484;
		t.x = 133;
		t.y = 737;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 19;
		t.fillColor = 0x64C50C;
		t.height = 18;
		t.width = 88;
		t.x = 133;
		t.y = 737;
		return t;
	};
	_proto.rpImg1_i = function () {
		var t = new eui.Image();
		this.rpImg1 = t;
		t.height = 40;
		t.source = "redeff_json.redpack";
		t.width = 33;
		t.x = 153;
		t.y = 715;
		return t;
	};
	_proto.rpImg2_i = function () {
		var t = new eui.Image();
		this.rpImg2 = t;
		t.height = 44;
		t.source = "redeff_json.redpack";
		t.width = 36;
		t.x = 278;
		t.y = 711;
		return t;
	};
	_proto.rpImg3_i = function () {
		var t = new eui.Image();
		this.rpImg3 = t;
		t.height = 54;
		t.source = "redeff_json.redpack";
		t.width = 44;
		t.x = 398;
		t.y = 701;
		return t;
	};
	_proto.rpImg4_i = function () {
		var t = new eui.Image();
		this.rpImg4 = t;
		t.height = 64;
		t.source = "redeff_json.redpack";
		t.width = 50;
		t.x = 566;
		t.y = 691;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "3元";
		t.textColor = 0xFF6038;
		t.x = 144;
		t.y = 770;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "20元";
		t.textColor = 0xFF6038;
		t.x = 255;
		t.y = 770;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "25元";
		t.textColor = 0xFF6038;
		t.x = 389;
		t.y = 770;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "9999元+";
		t.textColor = 0xFF6038;
		t.x = 545;
		t.y = 770;
		return t;
	};
	_proto._Rect3_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 10;
		t.fillColor = 0xfef9e3;
		t.height = 24;
		t.strokeColor = 0xFF6038;
		t.strokeWeight = 1;
		t.width = 42;
		t.x = 181;
		t.y = 769;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		t.height = 24;
		t.size = 18;
		t.text = "新人";
		t.textAlign = "center";
		t.textColor = 0xFF6038;
		t.verticalAlign = "middle";
		t.width = 42;
		t.x = 182;
		t.y = 770;
		return t;
	};
	_proto._Rect4_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 10;
		t.fillColor = 0xfef9e3;
		t.height = 24;
		t.strokeColor = 0xFF6038;
		t.strokeWeight = 1;
		t.width = 61;
		t.x = 306;
		t.y = 769;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.height = 24;
		t.rotation = 0.22;
		t.size = 18;
		t.text = "可提现";
		t.textAlign = "center";
		t.textColor = 0xFF6038;
		t.verticalAlign = "middle";
		t.width = 56;
		t.x = 309;
		t.y = 771;
		return t;
	};
	_proto._Rect5_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 10;
		t.fillColor = 0xfef9e3;
		t.height = 24;
		t.strokeColor = 0xFF6038;
		t.strokeWeight = 1;
		t.width = 61;
		t.x = 441;
		t.y = 769;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.height = 24;
		t.size = 18;
		t.text = "邀10人";
		t.textAlign = "center";
		t.textColor = 0xFF6038;
		t.verticalAlign = "middle";
		t.width = 59;
		t.x = 444;
		t.y = 771;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.height = 90;
		t.width = 480;
		t.x = 135;
		t.y = 836;
		t.elementsContent = [this.btnImg_i(),this.btnLabel_i()];
		return t;
	};
	_proto.btnImg_i = function () {
		var t = new eui.Image();
		this.btnImg = t;
		t.height = 90;
		t.scale9Grid = new egret.Rectangle(20,22,323,56);
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.width = 480;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.bold = true;
		t.height = 90;
		t.size = 34;
		t.text = "邀请好友";
		t.textAlign = "center";
		t.textColor = 0xffffff;
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 480;
		return t;
	};
	return InvitePromotionSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/JudgeDialogSkin.exml'] = window.JudgeDialogSkin = (function (_super) {
	__extends(JudgeDialogSkin, _super);
	function JudgeDialogSkin() {
		_super.call(this);
		this.skinParts = ["jcoinTxt","coinEffImg","btnGetCoin","titleTxt","effImg","cardImg","btnGetCard","cardNameTxt","notExitBtn","exitBtn","idxTxt1","idxTxt2","idxTxt3","idxTxt4","explainTxt","btnContinue","closeBtn"];
		
		this.currentState = "status_fail";
		this.elementsContent = [this._Image1_i()];
		this._Image2_i();
		
		this._Label1_i();
		
		this._Image3_i();
		
		this.jcoinTxt_i();
		
		this._Label2_i();
		
		this._Image4_i();
		
		this.coinEffImg_i();
		
		this._Image5_i();
		
		this.btnGetCoin_i();
		
		this._Label3_i();
		
		this._Image6_i();
		
		this.titleTxt_i();
		
		this.effImg_i();
		
		this.cardImg_i();
		
		this.btnGetCard_i();
		
		this._Label4_i();
		
		this.cardNameTxt_i();
		
		this._Label5_i();
		
		this._Label6_i();
		
		this.notExitBtn_i();
		
		this.exitBtn_i();
		
		this._Label7_i();
		
		this._Label8_i();
		
		this._Image7_i();
		
		this._Image8_i();
		
		this._Image9_i();
		
		this._Image10_i();
		
		this.idxTxt1_i();
		
		this.idxTxt2_i();
		
		this.idxTxt3_i();
		
		this.idxTxt4_i();
		
		this._Rect1_i();
		
		this._Label9_i();
		
		this.explainTxt_i();
		
		this.btnContinue_i();
		
		this._Label10_i();
		
		this.closeBtn_i();
		
		this.states = [
			new eui.State ("status_fail",
				[
					new eui.AddItems("_Image2","",1,""),
					new eui.AddItems("_Label1","",1,""),
					new eui.AddItems("_Image7","",1,""),
					new eui.AddItems("_Image8","",1,""),
					new eui.AddItems("_Image9","",1,""),
					new eui.AddItems("_Image10","",1,""),
					new eui.AddItems("idxTxt1","",1,""),
					new eui.AddItems("idxTxt2","",1,""),
					new eui.AddItems("idxTxt3","",1,""),
					new eui.AddItems("idxTxt4","",1,""),
					new eui.AddItems("_Rect1","",1,""),
					new eui.AddItems("_Label9","",1,""),
					new eui.AddItems("explainTxt","",1,""),
					new eui.AddItems("btnContinue","",1,""),
					new eui.AddItems("_Label10","",1,""),
					new eui.AddItems("closeBtn","",1,""),
					new eui.SetProperty("_Image1","height",680),
					new eui.SetProperty("closeBtn","y",-20)
				])
			,
			new eui.State ("status_confirm",
				[
					new eui.AddItems("_Image3","",1,""),
					new eui.AddItems("_Label5","",1,""),
					new eui.AddItems("_Label6","",1,""),
					new eui.AddItems("notExitBtn","",1,""),
					new eui.AddItems("exitBtn","",1,""),
					new eui.AddItems("_Label7","",1,""),
					new eui.AddItems("_Label8","",1,""),
					new eui.SetProperty("_Image1","height",440)
				])
			,
			new eui.State ("status_card",
				[
					new eui.AddItems("_Image3","",1,""),
					new eui.AddItems("_Label2","",1,""),
					new eui.AddItems("_Image6","",1,""),
					new eui.AddItems("titleTxt","",1,""),
					new eui.AddItems("effImg","",1,""),
					new eui.AddItems("cardImg","",1,""),
					new eui.AddItems("btnGetCard","",1,""),
					new eui.AddItems("_Label4","",1,""),
					new eui.AddItems("cardNameTxt","",1,""),
					new eui.AddItems("closeBtn","",1,""),
					new eui.SetProperty("_Image1","y",57),
					new eui.SetProperty("closeBtn","y",-20)
				])
			,
			new eui.State ("status_coin",
				[
					new eui.AddItems("_Image3","",1,""),
					new eui.AddItems("jcoinTxt","",1,""),
					new eui.AddItems("_Image4","",1,""),
					new eui.AddItems("coinEffImg","",1,""),
					new eui.AddItems("_Image5","",1,""),
					new eui.AddItems("btnGetCoin","",1,""),
					new eui.AddItems("_Label3","",1,""),
					new eui.AddItems("closeBtn","",1,""),
					new eui.SetProperty("_Image1","y",57),
					new eui.SetProperty("_Image1","anchorOffsetY",0),
					new eui.SetProperty("_Image1","height",640),
					new eui.SetProperty("closeBtn","y",-20)
				])
		];
	}
	var _proto = JudgeDialogSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.height = 640;
		t.scale9Grid = new egret.Rectangle(30,30,3,4);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.bold = true;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xF9E9B5;
		t.text = "正确答案";
		t.textColor = 0x8F5007;
		t.x = 238;
		t.y = 38;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.jcoinTxt_i = function () {
		var t = new eui.Label();
		this.jcoinTxt = t;
		t.size = 36;
		t.text = "恭喜获得50金币";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.touchEnabled = true;
		t.width = 640;
		t.x = 0;
		t.y = 151;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.size = 34;
		t.text = "收下";
		t.touchEnabled = false;
		t.x = 249.5;
		t.y = 564;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		this._Image4 = t;
		t.source = "judgegame_json.jsuccess";
		t.x = 112;
		t.y = 0;
		return t;
	};
	_proto.coinEffImg_i = function () {
		var t = new eui.Image();
		this.coinEffImg = t;
		t.anchorOffsetX = 248;
		t.anchorOffsetY = 248;
		t.scaleX = 0.8;
		t.scaleY = 0.8;
		t.source = "redeff_json.lightbox";
		t.x = 320;
		t.y = 355;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		this._Image5 = t;
		t.source = "viewpage_json.coinbagicom";
		t.x = 173;
		t.y = 255;
		return t;
	};
	_proto.btnGetCoin_i = function () {
		var t = new eui.Image();
		this.btnGetCoin = t;
		t.source = "guessgame_json.deletebtn";
		t.touchEnabled = true;
		t.x = 188;
		t.y = 536;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.anchorOffsetY = 0;
		t.height = 32;
		t.size = 34;
		t.text = "收下";
		t.touchEnabled = false;
		t.x = 286;
		t.y = 565;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		this._Image6 = t;
		t.source = "judgegame_json.jsuccess";
		t.x = 112;
		t.y = -11;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.size = 36;
		t.text = "恭喜获得“鼠”卡";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 640;
		t.x = 0;
		t.y = 151;
		return t;
	};
	_proto.effImg_i = function () {
		var t = new eui.Image();
		this.effImg = t;
		t.anchorOffsetX = 248;
		t.anchorOffsetY = 248;
		t.scaleX = 0.8;
		t.scaleY = 0.8;
		t.source = "redeff_json.lightbox";
		t.x = 320;
		t.y = 348;
		return t;
	};
	_proto.cardImg_i = function () {
		var t = new eui.Image();
		this.cardImg = t;
		t.height = 220;
		t.source = "viewpage_json.notget";
		t.width = 165;
		t.x = 238;
		t.y = 264;
		return t;
	};
	_proto.btnGetCard_i = function () {
		var t = new eui.Image();
		this.btnGetCard = t;
		t.source = "guessgame_json.deletebtn";
		t.x = 188;
		t.y = 536;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		this._Label4 = t;
		t.size = 34;
		t.text = "收下";
		t.touchEnabled = false;
		t.x = 286;
		t.y = 564;
		return t;
	};
	_proto.cardNameTxt_i = function () {
		var t = new eui.Label();
		this.cardNameTxt = t;
		t.text = "虎";
		t.textAlign = "center";
		t.textColor = 0xcb2620;
		t.width = 165;
		t.x = 238;
		t.y = 446.56;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		this._Label5 = t;
		t.bold = true;
		t.size = 38;
		t.stroke = 3;
		t.strokeColor = 0xf9e9b5;
		t.text = "确认退出？";
		t.textColor = 0x914e00;
		t.x = 230;
		t.y = 43;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		this._Label6 = t;
		t.anchorOffsetX = 0;
		t.lineSpacing = 10;
		t.size = 34;
		t.text = "此时退出不会保存进度，且无任何奖励";
		t.textColor = 0x914e00;
		t.width = 451;
		t.x = 94.5;
		t.y = 161;
		return t;
	};
	_proto.notExitBtn_i = function () {
		var t = new eui.Image();
		this.notExitBtn = t;
		t.height = 90;
		t.source = "menuover_json.nextbtn";
		t.touchEnabled = true;
		t.width = 246;
		t.x = 91;
		t.y = 302;
		return t;
	};
	_proto.exitBtn_i = function () {
		var t = new eui.Image();
		this.exitBtn = t;
		t.source = "guessgame_json.deletebtn";
		t.touchEnabled = true;
		t.width = 180;
		t.x = 357;
		t.y = 302;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		this._Label7 = t;
		t.size = 34;
		t.text = "暂不退出";
		t.touchEnabled = false;
		t.x = 145;
		t.y = 331;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		this._Label8 = t;
		t.size = 34;
		t.text = "退出";
		t.touchEnabled = false;
		t.x = 413;
		t.y = 331;
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		this._Image7 = t;
		t.height = 104;
		t.source = "judgegame_json.bigwordbg";
		t.width = 104;
		t.x = 80;
		t.y = 145;
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		this._Image8 = t;
		t.height = 104;
		t.source = "judgegame_json.bigwordbg";
		t.width = 104;
		t.x = 203;
		t.y = 145;
		return t;
	};
	_proto._Image9_i = function () {
		var t = new eui.Image();
		this._Image9 = t;
		t.height = 104;
		t.source = "judgegame_json.bigwordbg";
		t.width = 104;
		t.x = 448;
		t.y = 145;
		return t;
	};
	_proto._Image10_i = function () {
		var t = new eui.Image();
		this._Image10 = t;
		t.height = 104;
		t.source = "judgegame_json.bigwordbg";
		t.width = 104;
		t.x = 325;
		t.y = 145;
		return t;
	};
	_proto.idxTxt1_i = function () {
		var t = new eui.Label();
		this.idxTxt1 = t;
		t.bold = true;
		t.height = 104;
		t.size = 75;
		t.text = "掉";
		t.textAlign = "center";
		t.textColor = 0x000000;
		t.verticalAlign = "middle";
		t.width = 104;
		t.x = 80;
		t.y = 150;
		return t;
	};
	_proto.idxTxt2_i = function () {
		var t = new eui.Label();
		this.idxTxt2 = t;
		t.bold = true;
		t.height = 104;
		t.size = 75;
		t.text = "掉";
		t.textAlign = "center";
		t.textColor = 0x000000;
		t.verticalAlign = "middle";
		t.width = 104;
		t.x = 203;
		t.y = 150;
		return t;
	};
	_proto.idxTxt3_i = function () {
		var t = new eui.Label();
		this.idxTxt3 = t;
		t.bold = true;
		t.height = 104;
		t.size = 75;
		t.text = "掉";
		t.textAlign = "center";
		t.textColor = 0x000000;
		t.verticalAlign = "middle";
		t.width = 104;
		t.x = 325;
		t.y = 150;
		return t;
	};
	_proto.idxTxt4_i = function () {
		var t = new eui.Label();
		this.idxTxt4 = t;
		t.bold = true;
		t.height = 104;
		t.size = 75;
		t.text = "掉";
		t.textAlign = "center";
		t.textColor = 0x000000;
		t.verticalAlign = "middle";
		t.width = 104;
		t.x = 448;
		t.y = 150;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		this._Rect1 = t;
		t.ellipseHeight = 16;
		t.ellipseWidth = 16;
		t.fillColor = 0xffeecd;
		t.height = 40;
		t.width = 66;
		t.x = 47;
		t.y = 288;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		this._Label9 = t;
		t.size = 24;
		t.text = "译义";
		t.textColor = 0xfea910;
		t.x = 56;
		t.y = 297;
		return t;
	};
	_proto.explainTxt_i = function () {
		var t = new eui.Label();
		this.explainTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 152.97;
		t.size = 28;
		t.text = "掉：原意为摇摆；现只表示一种动作；无实义；轻心：漫不经心。对事情采取轻率的漫不经心的态度；不认真当回事。";
		t.textColor = 0x914e00;
		t.width = 541.12;
		t.x = 50;
		t.y = 347;
		return t;
	};
	_proto.btnContinue_i = function () {
		var t = new eui.Image();
		this.btnContinue = t;
		t.source = "viewpage_json.btnvideo";
		t.touchEnabled = true;
		t.x = 155;
		t.y = 540;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		this._Label10 = t;
		t.size = 34;
		t.text = "继续答题";
		t.touchEnabled = false;
		t.x = 222;
		t.y = 573;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 580;
		t.y = -3;
		return t;
	};
	return JudgeDialogSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/JudgeStartViewSkin.exml'] = window.JudgeStartViewSkin = (function (_super) {
	__extends(JudgeStartViewSkin, _super);
	function JudgeStartViewSkin() {
		_super.call(this);
		this.skinParts = ["startBtn","startLabel","myCardImg","closeBtn"];
		
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this._Label1_i(),this.startBtn_i(),this.startLabel_i(),this._Label2_i(),this._Rect1_i(),this._Label3_i(),this._Label4_i(),this.myCardImg_i(),this._Label5_i(),this._Image3_i(),this.closeBtn_i()];
	}
	var _proto = JudgeStartViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 691;
		t.scale9Grid = new egret.Rectangle(30,31,2,3);
		t.source = "viewpage_json.viewbg";
		t.width = 600;
		t.x = 0;
		t.y = 196;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.tjudgetitle";
		t.x = 144;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.bold = true;
		t.left = 0;
		t.lineSpacing = 10;
		t.size = 32;
		t.text = "挑战集卡赢100000金币";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 600;
		t.y = 311;
		return t;
	};
	_proto.startBtn_i = function () {
		var t = new eui.Image();
		this.startBtn = t;
		t.height = 122;
		t.scale9Grid = new egret.Rectangle(116,38,21,6);
		t.source = "guessgame_json.deletebtn";
		t.touchEnabled = true;
		t.width = 448;
		t.x = 76;
		t.y = 422;
		return t;
	};
	_proto.startLabel_i = function () {
		var t = new eui.Label();
		this.startLabel = t;
		t.size = 26;
		t.text = "今日还有3次挑战机会";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.touchEnabled = false;
		t.width = 300;
		t.x = 150;
		t.y = 571;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 48;
		t.text = "开始挑战";
		t.touchEnabled = false;
		t.x = 202;
		t.y = 459;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 32;
		t.fillAlpha = 0.1;
		t.fillColor = 0xb16e48;
		t.height = 191;
		t.width = 449;
		t.x = 76;
		t.y = 668;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.size = 26;
		t.text = "集齐一套卡片可兑换";
		t.textColor = 0x914e00;
		t.x = 118;
		t.y = 693;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.size = 26;
		t.text = "超高额奖励";
		t.textColor = 0xeb3516;
		t.x = 354;
		t.y = 693;
		return t;
	};
	_proto.myCardImg_i = function () {
		var t = new eui.Image();
		this.myCardImg = t;
		t.scale9Grid = new egret.Rectangle(147,49,13,7);
		t.source = "menuover_json.nextbtn";
		t.touchEnabled = true;
		t.width = 365;
		t.x = 118;
		t.y = 738;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.size = 32;
		t.text = "我的卡片";
		t.touchEnabled = false;
		t.x = 261;
		t.y = 772;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.cardeximg";
		t.touchEnabled = false;
		t.x = 195;
		t.y = 768;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.commonclosebtn";
		t.x = 536;
		t.y = 226;
		return t;
	};
	return JudgeStartViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/LifeExplainView.exml'] = window.LifeExplainViewSkin = (function (_super) {
	__extends(LifeExplainViewSkin, _super);
	function LifeExplainViewSkin() {
		_super.call(this);
		this.skinParts = ["viewbg","lifeImg","expImg","btnConfirm"];
		
		this.currentState = "life_status";
		this.elementsContent = [this.viewbg_i(),this._Image1_i(),this._Group1_i(),this._Label2_i(),this._Label3_i(),this._Label4_i(),this._Label5_i(),this._Label6_i(),this._Label7_i(),this.btnConfirm_i()];
		this.lifeImg_i();
		
		this.expImg_i();
		
		this._Label8_i();
		
		this._Label9_i();
		
		this._Label10_i();
		
		this._Label11_i();
		
		this.states = [
			new eui.State ("life_status",
				[
					new eui.AddItems("lifeImg","_Group1",0,""),
					new eui.AddItems("_Label8","",2,"btnConfirm"),
					new eui.AddItems("_Label9","",2,"btnConfirm"),
					new eui.AddItems("_Label10","",2,"btnConfirm"),
					new eui.AddItems("_Label11","",2,"btnConfirm"),
					new eui.SetProperty("_Group1","horizontalCenter",0.5),
					new eui.SetProperty("_Group1","y",32),
					new eui.SetProperty("_Label3","text","            体力值领取存储上限为25点(常规倒计时体力上限为10点)"),
					new eui.SetProperty("_Label5","text","            当体力槽没有达到上限(10点)时，系统每20分钟会自动回复1点体力值"),
					new eui.SetProperty("_Label7","text","            当体力值耗尽，完整观看1次小视频，即可自动回复3点体力值")
				])
			,
			new eui.State ("exp_status",
				[
					new eui.AddItems("expImg","_Group1",1,""),
					new eui.SetProperty("viewbg","anchorOffsetY",0),
					new eui.SetProperty("viewbg","height",692),
					new eui.SetProperty("_Label1","text","阅历值说明"),
					new eui.SetProperty("_Label1","x",76),
					new eui.SetProperty("_Group1","horizontalCenter",0),
					new eui.SetProperty("_Group1","y",32),
					new eui.SetProperty("_Label2","y",159),
					new eui.SetProperty("_Label3","text","            玩家通过成语接龙、看图猜成语可以获得阅历值经验"),
					new eui.SetProperty("_Label5","text","            通关以上游戏模式任意关卡后可获得阅历值+1，重复通过不会获得额外的经验值奖励"),
					new eui.SetProperty("_Label6","y",402),
					new eui.SetProperty("_Label7","text","            当阅历值达到对应的等级后，可点击升级解锁新的人物图鉴"),
					new eui.SetProperty("_Label7","horizontalCenter",0),
					new eui.SetProperty("_Label7","y",401),
					new eui.SetProperty("btnConfirm","horizontalCenter",0.5),
					new eui.SetProperty("btnConfirm","y",532),
					new eui.SetProperty("","height",692)
				])
		];
	}
	var _proto = LifeExplainViewSkin.prototype;

	_proto.viewbg_i = function () {
		var t = new eui.Image();
		this.viewbg = t;
		t.height = 822;
		t.scale9Grid = new egret.Rectangle(34,34,3,5);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		this._Group1 = t;
		t.height = 55;
		t.horizontalCenter = 0;
		t.y = 54;
		t.elementsContent = [this._Label1_i()];
		return t;
	};
	_proto.lifeImg_i = function () {
		var t = new eui.Image();
		this.lifeImg = t;
		t.anchorOffsetX = 44;
		t.height = 55;
		t.scaleX = 1;
		t.scaleY = 1;
		t.source = "viewpage_json.biglife";
		t.width = 44;
		t.x = -15;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.bold = true;
		t.height = 55;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xf9e9b5;
		t.text = "体力获取方式";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.x = 0;
		return t;
	};
	_proto.expImg_i = function () {
		var t = new eui.Image();
		this.expImg = t;
		t.source = "viewpage_json.expicon";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.fontFamily = "xnumberMedium";
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "（1）";
		t.textColor = 0xf89c35;
		t.x = 59;
		t.y = 158;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.anchorOffsetX = 0;
		t.fontFamily = "xnumberMedium";
		t.horizontalCenter = 0;
		t.lineSpacing = 10;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "            体力值领取存储上限为25点(常规倒计时体力上限为10点)；";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.width = 500;
		t.y = 158;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.fontFamily = "xnumberMedium";
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "（2）";
		t.textColor = 0xF89C35;
		t.x = 59;
		t.y = 260;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		this._Label5 = t;
		t.anchorOffsetX = 0;
		t.fontFamily = "xnumberMedium";
		t.horizontalCenter = 8.5;
		t.lineSpacing = 10;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "            当体力槽没有达到上限(10点)时，系统每20分钟会自动回复1点体力值；";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.width = 517;
		t.y = 260;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		this._Label6 = t;
		t.fontFamily = "xnumberMedium";
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "（3）";
		t.textColor = 0xF89C35;
		t.x = 59;
		t.y = 360;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		this._Label7 = t;
		t.fontFamily = "xnumberMedium";
		t.horizontalCenter = 0;
		t.lineSpacing = 10;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "            当体力值耗尽，完整观看1次小视频，即可自动回复3点体力值；";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.width = 500;
		t.y = 359;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		this._Label8 = t;
		t.fontFamily = "xnumberMedium";
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "（4）";
		t.textColor = 0xF89C35;
		t.x = 59;
		t.y = 461;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		this._Label9 = t;
		t.fontFamily = "xnumberMedium";
		t.horizontalCenter = 0;
		t.lineSpacing = 10;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "            每日登录可进行免费抽奖活动，可获得金币和体力奖励";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.width = 500;
		t.y = 461;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		this._Label10 = t;
		t.fontFamily = "xnumberMedium";
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "（5）";
		t.textColor = 0xF89C35;
		t.x = 59;
		t.y = 563;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		this._Label11 = t;
		t.fontFamily = "xnumberMedium";
		t.horizontalCenter = 0;
		t.lineSpacing = 10;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "            首次登录用户，体力耗尽时会免费赠送3点体力值";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.width = 500;
		t.y = 563;
		return t;
	};
	_proto.btnConfirm_i = function () {
		var t = new eui.Group();
		this.btnConfirm = t;
		t.height = 101;
		t.horizontalCenter = 0;
		t.y = 682;
		t.elementsContent = [this._Image2_i(),this._Label12_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 101;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(147,42,31,19);
		t.scaleX = 1;
		t.scaleY = 1;
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.width = 493;
		t.y = 0;
		return t;
	};
	_proto._Label12_i = function () {
		var t = new eui.Label();
		t.height = 101;
		t.horizontalCenter = 0;
		t.size = 34;
		t.text = "知道了";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.verticalCenter = 0;
		t.width = 493;
		return t;
	};
	return LifeExplainViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/MailItemRenderer.exml'] = window.MailItemRendererSkin = (function (_super) {
	__extends(MailItemRendererSkin, _super);
	function MailItemRendererSkin() {
		_super.call(this);
		this.skinParts = ["redpointImg","titleLabel","timeLabel","touchGrp","checkboxImg","onCheckboxImg"];
		
		this.currentState = "not-selected";
		this.height = 128;
		this.width = 600;
		this.elementsContent = [this._Group1_i()];
		this.states = [
			new eui.State ("not-selected",
				[
				])
			,
			new eui.State ("selected",
				[
				])
		];
	}
	var _proto = MailItemRendererSkin.prototype;

	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.height = 120;
		t.width = 600;
		t.x = 0;
		t.y = 4;
		t.elementsContent = [this._Rect1_i(),this.touchGrp_i(),this.checkboxImg_i(),this.onCheckboxImg_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 4;
		t.fillColor = 0xF6F0D7;
		t.height = 120;
		t.strokeColor = 0xf5dcb4;
		t.strokeWeight = 1;
		t.width = 600;
		return t;
	};
	_proto.touchGrp_i = function () {
		var t = new eui.Group();
		this.touchGrp = t;
		t.height = 120;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 600;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.redpointImg_i(),this.titleLabel_i(),this.timeLabel_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.mail_item_icon";
		t.x = 24;
		t.y = 38;
		return t;
	};
	_proto.redpointImg_i = function () {
		var t = new eui.Image();
		this.redpointImg = t;
		t.source = "menuover_json.redpoint";
		t.x = 71;
		t.y = 29;
		return t;
	};
	_proto.titleLabel_i = function () {
		var t = new eui.Label();
		this.titleLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.text = "主题";
		t.textColor = 0x8f5007;
		t.width = 403;
		t.x = 95;
		t.y = 45;
		return t;
	};
	_proto.timeLabel_i = function () {
		var t = new eui.Label();
		this.timeLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 20;
		t.text = "时间";
		t.textAlign = "right";
		t.textColor = 0xc6ac8a;
		t.width = 268;
		t.x = 322;
		t.y = 48;
		return t;
	};
	_proto.checkboxImg_i = function () {
		var t = new eui.Image();
		this.checkboxImg = t;
		t.source = "viewpage_json.mail_checkbox";
		t.x = 566;
		t.y = 0;
		return t;
	};
	_proto.onCheckboxImg_i = function () {
		var t = new eui.Image();
		this.onCheckboxImg = t;
		t.source = "viewpage_json.successnumber";
		t.x = 566;
		t.y = 0;
		return t;
	};
	return MailItemRendererSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/MailViewSkin.exml'] = window.MailViewSkin = (function (_super) {
	__extends(MailViewSkin, _super);
	function MailViewSkin() {
		_super.call(this);
		this.skinParts = ["headImg","tabRect1","tabLabel1","tabGrp1","tabRect2","tabLabel2","tabGrp2","unreadRect1","unreadLabel1","unreadRect2","unreadLabel2","curTabBGImg","noticeRedpointImg","noticeGrp","activityRedpointImg","activityGrp","updateRedpointImg","updateGrp","closeBtn","readGrp","selectAllGrp","deleteGrp","emptyLabel","emptyGrp","mainGrp","scroller","detailRect","titleLabel","detailLabel","detailImg","detailScroller","senderLabel","dateLabel","comfirmLabel","confirmGrp","closeDetailBtn","detailGrp"];
		
		this.elementsContent = [this.mainGrp_i(),this.scroller_i(),this.detailGrp_i()];
		this._Rect3_i();
		
		this.curTabBGImg_i();
		
		this.noticeGrp_i();
		
		this.activityGrp_i();
		
		this.updateGrp_i();
		
		this.states = [
			new eui.State ("system_msg_status",
				[
					new eui.AddItems("_Rect3","mainGrp",2,"closeBtn"),
					new eui.AddItems("curTabBGImg","mainGrp",2,"closeBtn"),
					new eui.AddItems("noticeGrp","mainGrp",2,"closeBtn"),
					new eui.AddItems("activityGrp","mainGrp",2,"closeBtn"),
					new eui.AddItems("updateGrp","mainGrp",2,"closeBtn"),
					new eui.SetProperty("_Rect2","height",646),
					new eui.SetProperty("tabRect1","y",0),
					new eui.SetProperty("tabLabel1","y",0),
					new eui.SetProperty("tabLabel1","width",301),
					new eui.SetProperty("tabLabel1","height",70),
					new eui.SetProperty("tabGrp1","anchorOffsetY",0),
					new eui.SetProperty("tabGrp1","height",70),
					new eui.SetProperty("tabGrp1","y",52),
					new eui.SetProperty("tabGrp1","anchorOffsetX",0),
					new eui.SetProperty("tabGrp1","width",301),
					new eui.SetProperty("tabRect2","x",0),
					new eui.SetProperty("tabRect2","y",0),
					new eui.SetProperty("tabLabel2","x",0),
					new eui.SetProperty("tabLabel2","y",0),
					new eui.SetProperty("tabLabel2","width",301),
					new eui.SetProperty("tabLabel2","height",70),
					new eui.SetProperty("tabGrp2","anchorOffsetX",0),
					new eui.SetProperty("tabGrp2","width",301),
					new eui.SetProperty("tabGrp2","x",322),
					new eui.SetProperty("tabGrp2","y",52),
					new eui.SetProperty("tabGrp2","anchorOffsetY",0),
					new eui.SetProperty("tabGrp2","height",70)
				])
			,
			new eui.State ("private_msg_status",
				[
					new eui.SetProperty("_Rect2","anchorOffsetY",0),
					new eui.SetProperty("_Rect2","height",809),
					new eui.SetProperty("_Rect2","x",12),
					new eui.SetProperty("_Rect2","y",123),
					new eui.SetProperty("tabRect1","y",0),
					new eui.SetProperty("tabRect1","x",0),
					new eui.SetProperty("tabLabel1","y",0),
					new eui.SetProperty("tabLabel1","x",0),
					new eui.SetProperty("tabLabel1","anchorOffsetX",0),
					new eui.SetProperty("tabLabel1","anchorOffsetY",0),
					new eui.SetProperty("tabLabel1","height",70),
					new eui.SetProperty("tabLabel1","verticalAlign","middle"),
					new eui.SetProperty("tabLabel1","width",301),
					new eui.SetProperty("tabGrp1","y",52),
					new eui.SetProperty("tabGrp1","height",70),
					new eui.SetProperty("tabGrp1","width",301),
					new eui.SetProperty("tabRect2","y",0),
					new eui.SetProperty("tabRect2","x",0),
					new eui.SetProperty("tabLabel2","y",0),
					new eui.SetProperty("tabLabel2","x",0),
					new eui.SetProperty("tabLabel2","anchorOffsetX",0),
					new eui.SetProperty("tabLabel2","anchorOffsetY",0),
					new eui.SetProperty("tabLabel2","height",70),
					new eui.SetProperty("tabLabel2","verticalAlign","middle"),
					new eui.SetProperty("tabLabel2","width",301),
					new eui.SetProperty("tabGrp2","anchorOffsetX",0),
					new eui.SetProperty("tabGrp2","width",301),
					new eui.SetProperty("tabGrp2","x",322),
					new eui.SetProperty("tabGrp2","y",52),
					new eui.SetProperty("tabGrp2","anchorOffsetY",0),
					new eui.SetProperty("tabGrp2","height",70),
					new eui.SetProperty("closeBtn","touchEnabled",true),
					new eui.SetProperty("scroller","y",128),
					new eui.SetProperty("scroller","height",726),
					new eui.SetProperty("scroller","scrollPolicyH","off"),
					new eui.SetProperty("scroller","scrollPolicyV","auto"),
					new eui.SetProperty("scroller","anchorOffsetY",0)
				])
		];
	}
	var _proto = MailViewSkin.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.x = 35;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.headImg_i(),this._Rect1_i(),this._Rect2_i(),this.tabGrp1_i(),this.tabGrp2_i(),this.unreadRect1_i(),this.unreadLabel1_i(),this.unreadRect2_i(),this.unreadLabel2_i(),this.closeBtn_i(),this.readGrp_i(),this.selectAllGrp_i(),this.deleteGrp_i(),this.emptyGrp_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 906;
		t.scale9Grid = new egret.Rectangle(32,30,3,4);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 55;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.source = "viewpage_json.mail_head";
		t.visible = false;
		t.x = -33.75;
		t.y = 31;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 53;
		t.fillColor = 0xffd983;
		t.height = 100;
		t.width = 638;
		t.x = 1;
		t.y = 31;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		this._Rect2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.ellipseWidth = 0;
		t.fillColor = 0xfef9e3;
		t.height = 740;
		t.touchEnabled = false;
		t.width = 617;
		t.x = 23;
		t.y = 200;
		return t;
	};
	_proto.tabGrp1_i = function () {
		var t = new eui.Group();
		this.tabGrp1 = t;
		t.x = 22;
		t.y = 25;
		t.elementsContent = [this.tabRect1_i(),this.tabLabel1_i()];
		return t;
	};
	_proto.tabRect1_i = function () {
		var t = new eui.Rect();
		this.tabRect1 = t;
		t.ellipseWidth = 12;
		t.fillColor = 0xe0a650;
		t.height = 66;
		t.strokeColor = 0xe0a650;
		t.strokeWeight = 2;
		t.width = 301;
		t.x = -1;
		t.y = 31;
		return t;
	};
	_proto.tabLabel1_i = function () {
		var t = new eui.Label();
		this.tabLabel1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 66;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 30;
		t.text = "通知消息";
		t.textAlign = "center";
		t.textColor = 0xfef9e3;
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 306;
		t.x = 0;
		t.y = 31;
		return t;
	};
	_proto.tabGrp2_i = function () {
		var t = new eui.Group();
		this.tabGrp2 = t;
		t.x = 22;
		t.y = 25;
		t.elementsContent = [this.tabRect2_i(),this.tabLabel2_i()];
		return t;
	};
	_proto.tabRect2_i = function () {
		var t = new eui.Rect();
		this.tabRect2 = t;
		t.ellipseWidth = 12;
		t.fillColor = 0xe0a650;
		t.height = 66;
		t.strokeColor = 0xe0a650;
		t.strokeWeight = 2;
		t.width = 301;
		t.x = 300;
		t.y = 31;
		return t;
	};
	_proto.tabLabel2_i = function () {
		var t = new eui.Label();
		this.tabLabel2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 67;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 30;
		t.text = "我的消息";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 293;
		t.x = 305;
		t.y = 31;
		return t;
	};
	_proto.unreadRect1_i = function () {
		var t = new eui.Rect();
		this.unreadRect1 = t;
		t.ellipseHeight = 33;
		t.ellipseWidth = 43;
		t.fillColor = 0xfa572b;
		t.height = 32;
		t.strokeColor = 0xe0a650;
		t.strokeWeight = 0;
		t.touchEnabled = false;
		t.width = 52;
		t.x = 230;
		t.y = 64;
		return t;
	};
	_proto.unreadLabel1_i = function () {
		var t = new eui.Label();
		this.unreadLabel1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 17;
		t.size = 22;
		t.text = "1";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 39;
		t.x = 237;
		t.y = 71;
		return t;
	};
	_proto.unreadRect2_i = function () {
		var t = new eui.Rect();
		this.unreadRect2 = t;
		t.ellipseHeight = 33;
		t.ellipseWidth = 43;
		t.fillColor = 0xfa572b;
		t.height = 32;
		t.strokeColor = 0xe0a650;
		t.strokeWeight = 0;
		t.touchEnabled = false;
		t.width = 52;
		t.x = 528.32;
		t.y = 64;
		return t;
	};
	_proto.unreadLabel2_i = function () {
		var t = new eui.Label();
		this.unreadLabel2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 17;
		t.size = 22;
		t.text = "99+";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 39;
		t.x = 535.32;
		t.y = 71;
		return t;
	};
	_proto._Rect3_i = function () {
		var t = new eui.Rect();
		this._Rect3 = t;
		t.ellipseWidth = 0;
		t.fillColor = 0xffd983;
		t.height = 72;
		t.width = 632;
		t.x = 3;
		t.y = 130;
		return t;
	};
	_proto.curTabBGImg_i = function () {
		var t = new eui.Image();
		this.curTabBGImg = t;
		t.source = "viewpage_json.mail_cur_tab_bg";
		t.x = 21;
		t.y = 127;
		return t;
	};
	_proto.noticeGrp_i = function () {
		var t = new eui.Group();
		this.noticeGrp = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 72;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 200;
		t.x = 21;
		t.y = 127;
		t.elementsContent = [this._Label1_i(),this.noticeRedpointImg_i()];
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.bold = true;
		t.height = 72;
		t.text = "公告";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 115;
		t.x = 42.5;
		t.y = 3;
		return t;
	};
	_proto.noticeRedpointImg_i = function () {
		var t = new eui.Image();
		this.noticeRedpointImg = t;
		t.source = "menuover_json.redpoint";
		t.x = 125;
		t.y = 12;
		return t;
	};
	_proto.activityGrp_i = function () {
		var t = new eui.Group();
		this.activityGrp = t;
		t.anchorOffsetX = 0;
		t.height = 72;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 200;
		t.x = 223;
		t.y = 127;
		t.elementsContent = [this._Label2_i(),this.activityRedpointImg_i()];
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.height = 72;
		t.text = "活动";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 115;
		t.x = 36;
		t.y = 3;
		return t;
	};
	_proto.activityRedpointImg_i = function () {
		var t = new eui.Image();
		this.activityRedpointImg = t;
		t.source = "menuover_json.redpoint";
		t.x = 125;
		t.y = 12;
		return t;
	};
	_proto.updateGrp_i = function () {
		var t = new eui.Group();
		this.updateGrp = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 72;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 200;
		t.x = 424.48;
		t.y = 127;
		t.elementsContent = [this._Label3_i(),this.updateRedpointImg_i()];
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.bold = true;
		t.height = 72;
		t.text = "版本更新";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 200.33;
		t.x = 0;
		t.y = 3;
		return t;
	};
	_proto.updateRedpointImg_i = function () {
		var t = new eui.Image();
		this.updateRedpointImg = t;
		t.source = "menuover_json.redpoint";
		t.x = 160;
		t.y = 12;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 589;
		t.y = 5;
		return t;
	};
	_proto.readGrp_i = function () {
		var t = new eui.Group();
		this.readGrp = t;
		t.height = 66;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 148;
		t.x = 228;
		t.y = 865;
		t.elementsContent = [this._Image2_i(),this._Label4_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 66;
		t.source = "viewpage_json.mail_op_btn";
		t.width = 148;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.height = 66;
		t.size = 26;
		t.text = "标记已读";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 148;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.selectAllGrp_i = function () {
		var t = new eui.Group();
		this.selectAllGrp = t;
		t.height = 66;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 112;
		t.x = 386;
		t.y = 865;
		t.elementsContent = [this._Image3_i(),this._Label5_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.height = 66;
		t.source = "viewpage_json.mail_op_btn";
		t.width = 112;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.height = 66;
		t.size = 26;
		t.text = "全选";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 112;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.deleteGrp_i = function () {
		var t = new eui.Group();
		this.deleteGrp = t;
		t.height = 66;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 112;
		t.x = 508;
		t.y = 865;
		t.elementsContent = [this._Image4_i(),this._Label6_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.height = 66;
		t.source = "viewpage_json.mail_op_btn";
		t.width = 112;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.height = 66;
		t.size = 26;
		t.text = "删除";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 112;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.emptyGrp_i = function () {
		var t = new eui.Group();
		this.emptyGrp = t;
		t.height = 170;
		t.touchChildren = false;
		t.touchEnabled = false;
		t.width = 350;
		t.x = 151.38;
		t.y = 356.19;
		t.elementsContent = [this._Image5_i(),this.emptyLabel_i()];
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.height = 163;
		t.horizontalCenter = 0;
		t.source = "viewpage_json.blankmail";
		t.width = 306;
		t.y = 0;
		return t;
	};
	_proto.emptyLabel_i = function () {
		var t = new eui.Label();
		this.emptyLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.height = 66;
		t.horizontalCenter = -0.5;
		t.size = 30;
		t.text = "暂无私信";
		t.textAlign = "center";
		t.textColor = 0xdab25e;
		t.verticalAlign = "middle";
		t.width = 165.33;
		t.y = 160;
		return t;
	};
	_proto.scroller_i = function () {
		var t = new eui.Scroller();
		this.scroller = t;
		t.anchorOffsetY = 0;
		t.height = 652;
		t.touchEnabled = false;
		t.width = 600;
		t.x = 57;
		t.y = 204;
		return t;
	};
	_proto.detailGrp_i = function () {
		var t = new eui.Group();
		this.detailGrp = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 914.68;
		t.visible = false;
		t.width = 678;
		t.x = 0;
		t.y = 37.31;
		t.elementsContent = [this.detailRect_i(),this._Image6_i(),this.titleLabel_i(),this.detailScroller_i(),this.senderLabel_i(),this.dateLabel_i(),this.confirmGrp_i(),this.closeDetailBtn_i()];
		return t;
	};
	_proto.detailRect_i = function () {
		var t = new eui.Image();
		this.detailRect = t;
		t.height = 640;
		t.horizontalCenter = 15;
		t.scale9Grid = new egret.Rectangle(32,30,3,4);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.y = 140;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.height = 114;
		t.source = "viewpage_json.common_title_bg";
		t.width = 640;
		t.x = 34;
		t.y = 75;
		return t;
	};
	_proto.titleLabel_i = function () {
		var t = new eui.Label();
		this.titleLabel = t;
		t.bold = true;
		t.height = 40;
		t.size = 36;
		t.text = "邮件标题";
		t.textAlign = "center";
		t.textColor = 0xbb5c00;
		t.verticalAlign = "justify";
		t.width = 640;
		t.x = 35;
		t.y = 111;
		return t;
	};
	_proto.detailScroller_i = function () {
		var t = new eui.Scroller();
		this.detailScroller = t;
		t.anchorOffsetY = 0;
		t.height = 270;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "on";
		t.touchEnabled = true;
		t.width = 484;
		t.x = 116;
		t.y = 238;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.height = 270;
		t.scrollEnabled = false;
		t.width = 484;
		t.elementsContent = [this.detailLabel_i(),this.detailImg_i()];
		return t;
	};
	_proto.detailLabel_i = function () {
		var t = new eui.Label();
		this.detailLabel = t;
		t.anchorOffsetY = 0;
		t.lineSpacing = 18;
		t.size = 28;
		t.text = "大师发生大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大大www.baidu.c大大大大大大大大大大若点击使用“我的消息”类型时，则需要填写收件人（用户手机号或accid）逻辑2：点击发送后，后台默认2分钟后才生效逻辑3：当类型选择“活动”时，可配置对应跳转的活动链大大www.baidu.c大大大大大大大大大大大大大大大大www.baidu.c大大发生大\",\"gowhere\": \"1\",\"url\": \"www.baidu.comff";
		t.textAlign = "left";
		t.textColor = 0x8f5007;
		t.touchEnabled = true;
		t.verticalAlign = "justify";
		t.width = 485;
		t.x = 0;
		t.y = 5.32;
		return t;
	};
	_proto.detailImg_i = function () {
		var t = new eui.Image();
		this.detailImg = t;
		t.height = 300;
		t.horizontalCenter = 0;
		t.width = 300;
		return t;
	};
	_proto.senderLabel_i = function () {
		var t = new eui.Label();
		this.senderLabel = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = false;
		t.height = 50.66;
		t.size = 28;
		t.text = "发信人";
		t.textAlign = "right";
		t.textColor = 0x8f5007;
		t.verticalAlign = "middle";
		t.width = 450.66;
		t.x = 152;
		t.y = 538.24;
		return t;
	};
	_proto.dateLabel_i = function () {
		var t = new eui.Label();
		this.dateLabel = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = false;
		t.height = 50.66;
		t.size = 28;
		t.text = "日期";
		t.textAlign = "right";
		t.textColor = 0xc6ac8a;
		t.verticalAlign = "middle";
		t.width = 464;
		t.x = 138.66;
		t.y = 584.86;
		return t;
	};
	_proto.confirmGrp_i = function () {
		var t = new eui.Group();
		this.confirmGrp = t;
		t.height = 90;
		t.horizontalCenter = 17;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.width = 360;
		t.y = 671;
		t.elementsContent = [this._Image7_i(),this.comfirmLabel_i()];
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		t.height = 90;
		t.source = "viewpage_json.commonbtn";
		t.width = 360;
		t.x = 0;
		t.y = 8;
		return t;
	};
	_proto.comfirmLabel_i = function () {
		var t = new eui.Label();
		this.comfirmLabel = t;
		t.bold = true;
		t.height = 90;
		t.size = 34;
		t.text = "确定";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 360;
		t.x = 0;
		t.y = 8;
		return t;
	};
	_proto.closeDetailBtn_i = function () {
		var t = new eui.Image();
		this.closeDetailBtn = t;
		t.source = "viewpage_json.closebtn";
		t.touchEnabled = true;
		t.x = 624;
		t.y = 49;
		return t;
	};
	return MailViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/MissionItem.exml'] = window.MissionItemSkin = (function (_super) {
	__extends(MissionItemSkin, _super);
	function MissionItemSkin() {
		_super.call(this);
		this.skinParts = ["titleTxt","coinTxt","itemImg1","itemTxt1","itemNumTxt1","itemGrp1","itemImg2","itemTxt2","itemNumTxt2","itemGrp2","itemImg3","itemTxt3","itemNumTxt3","itemGrp3","getBtn","btnLabel","progressBar","progressTxt","progressGrp"];
		
		this.currentState = "common";
		this.elementsContent = [this._Rect1_i(),this.titleTxt_i(),this._Image1_i(),this.coinTxt_i(),this.itemGrp1_i(),this.itemGrp2_i(),this.itemGrp3_i(),this.getBtn_i(),this.btnLabel_i(),this.progressGrp_i()];
		this.states = [
			new eui.State ("special",
				[
					new eui.SetProperty("_Rect1","strokeColor",0xefa74f),
					new eui.SetProperty("_Rect1","strokeWeight",2),
					new eui.SetProperty("_Rect1","fillColor",0xfdffe2)
				])
			,
			new eui.State ("common",
				[
				])
			,
			new eui.State ("battle",
				[
					new eui.SetProperty("_Rect1","width",680),
					new eui.SetProperty("_Rect1","fillColor",0x4670dc),
					new eui.SetProperty("_Rect1","y",-1),
					new eui.SetProperty("titleTxt","textColor",0xffffff),
					new eui.SetProperty("titleTxt","strokeColor",0x223483),
					new eui.SetProperty("titleTxt","stroke",2),
					new eui.SetProperty("titleTxt","x",18),
					new eui.SetProperty("_Image1","x",19),
					new eui.SetProperty("coinTxt","bold",true),
					new eui.SetProperty("coinTxt","textColor",0xffde1a),
					new eui.SetProperty("coinTxt","strokeColor",0x223483),
					new eui.SetProperty("coinTxt","stroke",2),
					new eui.SetProperty("coinTxt","x",61),
					new eui.SetProperty("itemTxt1","textColor",0xffffff),
					new eui.SetProperty("itemTxt1","strokeColor",0x223483),
					new eui.SetProperty("itemTxt1","stroke",2),
					new eui.SetProperty("itemTxt1","x",35),
					new eui.SetProperty("itemNumTxt1","textColor",0xffde1a),
					new eui.SetProperty("itemNumTxt1","strokeColor",0x223483),
					new eui.SetProperty("itemNumTxt1","stroke",2),
					new eui.SetProperty("itemNumTxt1","x",100),
					new eui.SetProperty("itemGrp1","x",108),
					new eui.SetProperty("itemTxt2","strokeColor",0x223483),
					new eui.SetProperty("itemTxt2","stroke",2),
					new eui.SetProperty("itemTxt2","textColor",0xffffff),
					new eui.SetProperty("itemTxt2","x",32),
					new eui.SetProperty("itemNumTxt2","textColor",0xffde1a),
					new eui.SetProperty("itemNumTxt2","strokeColor",0x223483),
					new eui.SetProperty("itemNumTxt2","stroke",2),
					new eui.SetProperty("itemNumTxt2","x",100),
					new eui.SetProperty("itemGrp2","x",247),
					new eui.SetProperty("itemTxt3","strokeColor",0x223483),
					new eui.SetProperty("itemTxt3","stroke",2),
					new eui.SetProperty("itemTxt3","textColor",0xffffff),
					new eui.SetProperty("itemTxt3","x",33),
					new eui.SetProperty("itemNumTxt3","textColor",0xffde1a),
					new eui.SetProperty("itemNumTxt3","strokeColor",0x223483),
					new eui.SetProperty("itemNumTxt3","stroke",2),
					new eui.SetProperty("itemNumTxt3","x",98),
					new eui.SetProperty("itemGrp3","x",377),
					new eui.SetProperty("getBtn","source","dispelPk_json.dpk_mget"),
					new eui.SetProperty("getBtn","y",61),
					new eui.SetProperty("getBtn","x",505),
					new eui.SetProperty("btnLabel","y",80),
					new eui.SetProperty("btnLabel","x",505),
					new eui.SetProperty("_Rect2","fillColor",0x2c419d),
					new eui.SetProperty("progressBar","fillColor",0xabff92),
					new eui.SetProperty("progressTxt","textColor",0xffffff),
					new eui.SetProperty("progressTxt","text","3/3"),
					new eui.SetProperty("progressGrp","x",512)
				])
		];
	}
	var _proto = MissionItemSkin.prototype;

	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		this._Rect1 = t;
		t.ellipseHeight = 24;
		t.ellipseWidth = 24;
		t.fillColor = 0xfffaca;
		t.height = 148;
		t.width = 700;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.bold = true;
		t.size = 32;
		t.text = "首次登陆";
		t.textColor = 0x914e00;
		t.x = 30;
		t.y = 32;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.height = 38;
		t.source = "menuover_json.coin";
		t.width = 38;
		t.x = 31;
		t.y = 86;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.size = 26;
		t.text = "20";
		t.textColor = 0xff8c38;
		t.x = 73;
		t.y = 96;
		return t;
	};
	_proto.itemGrp1_i = function () {
		var t = new eui.Group();
		this.itemGrp1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 39;
		t.width = 128;
		t.x = 127;
		t.y = 88;
		t.elementsContent = [this.itemImg1_i(),this.itemTxt1_i(),this.itemNumTxt1_i()];
		return t;
	};
	_proto.itemImg1_i = function () {
		var t = new eui.Image();
		this.itemImg1 = t;
		t.anchorOffsetX = 19;
		t.anchorOffsetY = 19;
		t.height = 38;
		t.source = "";
		t.width = 38;
		t.x = 19;
		t.y = 19;
		return t;
	};
	_proto.itemTxt1_i = function () {
		var t = new eui.Label();
		this.itemTxt1 = t;
		t.bold = true;
		t.size = 22;
		t.text = "入场券";
		t.textColor = 0x914e00;
		t.touchEnabled = false;
		t.x = 30;
		t.y = 9;
		return t;
	};
	_proto.itemNumTxt1_i = function () {
		var t = new eui.Label();
		this.itemNumTxt1 = t;
		t.bold = true;
		t.size = 26;
		t.text = "x1";
		t.textColor = 0xff8c38;
		t.touchEnabled = false;
		t.x = 90;
		t.y = 5;
		return t;
	};
	_proto.itemGrp2_i = function () {
		var t = new eui.Group();
		this.itemGrp2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 39;
		t.width = 126;
		t.x = 257;
		t.y = 88;
		t.elementsContent = [this.itemImg2_i(),this.itemTxt2_i(),this.itemNumTxt2_i()];
		return t;
	};
	_proto.itemImg2_i = function () {
		var t = new eui.Image();
		this.itemImg2 = t;
		t.anchorOffsetX = 19;
		t.anchorOffsetY = 19;
		t.height = 38;
		t.source = "";
		t.width = 38;
		t.x = 15;
		t.y = 19;
		return t;
	};
	_proto.itemTxt2_i = function () {
		var t = new eui.Label();
		this.itemTxt2 = t;
		t.bold = true;
		t.size = 22;
		t.text = "入场券";
		t.textColor = 0x914e00;
		t.touchEnabled = false;
		t.x = 29;
		t.y = 9;
		return t;
	};
	_proto.itemNumTxt2_i = function () {
		var t = new eui.Label();
		this.itemNumTxt2 = t;
		t.bold = true;
		t.size = 26;
		t.text = "x1";
		t.textColor = 0xff8c38;
		t.touchEnabled = false;
		t.x = 90;
		t.y = 5;
		return t;
	};
	_proto.itemGrp3_i = function () {
		var t = new eui.Group();
		this.itemGrp3 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 39;
		t.width = 128;
		t.x = 381;
		t.y = 88;
		t.elementsContent = [this.itemImg3_i(),this.itemTxt3_i(),this.itemNumTxt3_i()];
		return t;
	};
	_proto.itemImg3_i = function () {
		var t = new eui.Image();
		this.itemImg3 = t;
		t.anchorOffsetX = 19;
		t.anchorOffsetY = 19;
		t.height = 38;
		t.source = "";
		t.width = 38;
		t.x = 17;
		t.y = 19;
		return t;
	};
	_proto.itemTxt3_i = function () {
		var t = new eui.Label();
		this.itemTxt3 = t;
		t.bold = true;
		t.size = 22;
		t.text = "入场券";
		t.textColor = 0x914e00;
		t.touchEnabled = false;
		t.x = 30;
		t.y = 9;
		return t;
	};
	_proto.itemNumTxt3_i = function () {
		var t = new eui.Label();
		this.itemNumTxt3 = t;
		t.bold = true;
		t.size = 26;
		t.text = "x1";
		t.textColor = 0xff8c38;
		t.touchEnabled = false;
		t.x = 91;
		t.y = 5;
		return t;
	};
	_proto.getBtn_i = function () {
		var t = new eui.Image();
		this.getBtn = t;
		t.source = "viewpage_json.btnget";
		t.x = 513;
		t.y = 42;
		return t;
	};
	_proto.btnLabel_i = function () {
		var t = new eui.Label();
		this.btnLabel = t;
		t.bold = true;
		t.text = "领取奖励";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 156;
		t.x = 513;
		t.y = 61;
		return t;
	};
	_proto.progressGrp_i = function () {
		var t = new eui.Group();
		this.progressGrp = t;
		t.touchEnabled = false;
		t.x = 490;
		t.y = 26;
		t.elementsContent = [this._Rect2_i(),this.progressBar_i(),this.progressTxt_i()];
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		this._Rect2 = t;
		t.ellipseHeight = 12;
		t.ellipseWidth = 12;
		t.fillColor = 0xffe096;
		t.height = 12;
		t.width = 96;
		t.x = 0;
		t.y = 3;
		return t;
	};
	_proto.progressBar_i = function () {
		var t = new eui.Rect();
		this.progressBar = t;
		t.ellipseHeight = 12;
		t.ellipseWidth = 12;
		t.fillColor = 0xff8c38;
		t.height = 12;
		t.width = 96;
		t.x = 0;
		t.y = 3;
		return t;
	};
	_proto.progressTxt_i = function () {
		var t = new eui.Label();
		this.progressTxt = t;
		t.size = 22;
		t.text = "1000/4000";
		t.textColor = 0xff8c38;
		t.x = 100;
		t.y = 0;
		return t;
	};
	return MissionItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/MissionViewSkin.exml'] = window.MissionViewSkin = (function (_super) {
	__extends(MissionViewSkin, _super);
	function MissionViewSkin() {
		_super.call(this);
		this.skinParts = ["btnSel1","btnSel2","btnTab2","btnTab1","tabLabel1","tabLabel2","closeBtn","noticeRedpointImg","progressRect","signGrp","refImg","cdTxt","cdGrp","overallMissionGrp","scroller","readyRect","readyExpandBtn","readyContentGrp","readyGrp","tryRect","tryExpandBtn","tryContentGrp","tryGrp","gotRect","gotExpandBtn","gotContentGrp","gotGrp","aContainer","aScroller"];
		
		this.elementsContent = [this._Group1_i()];
		this.cdGrp_i();
		
		this.overallMissionGrp_i();
		
		this.scroller_i();
		
		this.aScroller_i();
		
		this.states = [
			new eui.State ("missions",
				[
					new eui.AddItems("cdGrp","_Group1",1,""),
					new eui.AddItems("overallMissionGrp","_Group1",1,""),
					new eui.AddItems("scroller","",1,""),
					new eui.SetProperty("noticeRedpointImg","y",74),
					new eui.SetProperty("noticeRedpointImg","x",583),
					new eui.SetProperty("overallMissionGrp","x",25)
				])
			,
			new eui.State ("achieves",
				[
					new eui.AddItems("aScroller","",1,""),
					new eui.SetProperty("noticeRedpointImg","x",593),
					new eui.SetProperty("noticeRedpointImg","y",63)
				])
		];
	}
	var _proto = MissionViewSkin.prototype;

	_proto._Group1_i = function () {
		var t = new eui.Group();
		this._Group1 = t;
		t.cacheAsBitmap = true;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Rect1_i(),this.btnSel1_i(),this.btnSel2_i(),this.btnTab2_i(),this.btnTab1_i(),this.tabLabel1_i(),this.tabLabel2_i(),this.closeBtn_i(),this.noticeRedpointImg_i(),this.signGrp_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.fillColor = 0xffd982;
		t.height = 1108;
		t.width = 750;
		t.x = 0;
		t.y = 92;
		return t;
	};
	_proto.btnSel1_i = function () {
		var t = new eui.Image();
		this.btnSel1 = t;
		t.source = "viewpage_json.labelA";
		t.x = 0;
		t.y = 42;
		return t;
	};
	_proto.btnSel2_i = function () {
		var t = new eui.Image();
		this.btnSel2 = t;
		t.scaleX = -1;
		t.source = "viewpage_json.labelA";
		t.width = 376;
		t.x = 750;
		t.y = 42;
		return t;
	};
	_proto.btnTab2_i = function () {
		var t = new eui.Image();
		this.btnTab2 = t;
		t.source = "viewpage_json.labelB";
		t.touchEnabled = true;
		t.x = 375;
		t.y = 61;
		return t;
	};
	_proto.btnTab1_i = function () {
		var t = new eui.Image();
		this.btnTab1 = t;
		t.scaleX = -1;
		t.source = "viewpage_json.labelB";
		t.touchEnabled = true;
		t.x = 375;
		t.y = 61;
		return t;
	};
	_proto.tabLabel1_i = function () {
		var t = new eui.Label();
		this.tabLabel1 = t;
		t.bold = true;
		t.size = 40;
		t.text = "每日任务";
		t.touchEnabled = false;
		t.x = 108;
		t.y = 69;
		return t;
	};
	_proto.tabLabel2_i = function () {
		var t = new eui.Label();
		this.tabLabel2 = t;
		t.bold = true;
		t.size = 40;
		t.text = "成就榜";
		t.touchEnabled = false;
		t.x = 480;
		t.y = 69;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.touchEnabled = true;
		t.x = 678;
		t.y = 22;
		return t;
	};
	_proto.noticeRedpointImg_i = function () {
		var t = new eui.Image();
		this.noticeRedpointImg = t;
		t.source = "menuover_json.redpoint";
		t.x = 596;
		t.y = 67;
		return t;
	};
	_proto.signGrp_i = function () {
		var t = new eui.Group();
		this.signGrp = t;
		t.x = 27;
		t.y = 150;
		t.elementsContent = [this._Rect2_i(),this.progressRect_i()];
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.fillColor = 0xffe6ac;
		t.height = 6;
		t.scaleX = 1;
		t.scaleY = 1;
		t.width = 600;
		t.x = 32;
		t.y = 72;
		return t;
	};
	_proto.progressRect_i = function () {
		var t = new eui.Rect();
		this.progressRect = t;
		t.fillColor = 0xff7b2b;
		t.height = 6;
		t.width = 600;
		t.x = 32;
		t.y = 72;
		return t;
	};
	_proto.cdGrp_i = function () {
		var t = new eui.Group();
		this.cdGrp = t;
		t.touchEnabled = false;
		t.elementsContent = [this._Rect3_i(),this.refImg_i(),this.cdTxt_i()];
		return t;
	};
	_proto._Rect3_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 24;
		t.ellipseWidth = 24;
		t.fillColor = 0xefa74f;
		t.height = 65;
		t.width = 424;
		t.x = 165;
		t.y = 316;
		return t;
	};
	_proto.refImg_i = function () {
		var t = new eui.Image();
		this.refImg = t;
		t.anchorOffsetX = 20;
		t.anchorOffsetY = 19;
		t.source = "viewpage_json.refresh_icon";
		t.x = 199.5;
		t.y = 350;
		return t;
	};
	_proto.cdTxt_i = function () {
		var t = new eui.Label();
		this.cdTxt = t;
		t.bold = true;
		t.size = 28;
		t.text = "距离任务刷新还剩15:40:22";
		t.textColor = 0xffffff;
		t.x = 231;
		t.y = 336.5;
		return t;
	};
	_proto.overallMissionGrp_i = function () {
		var t = new eui.Group();
		this.overallMissionGrp = t;
		t.x = 0;
		t.y = 370;
		return t;
	};
	_proto.scroller_i = function () {
		var t = new eui.Scroller();
		this.scroller = t;
		t.anchorOffsetY = 0;
		t.height = 631;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "auto";
		t.width = 710;
		t.x = 25;
		t.y = 529;
		t.viewport = this._Group2_i();
		return t;
	};
	_proto._Group2_i = function () {
		var t = new eui.Group();
		return t;
	};
	_proto.aScroller_i = function () {
		var t = new eui.Scroller();
		this.aScroller = t;
		t.height = 840;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "auto";
		t.width = 750;
		t.x = 25;
		t.y = 320;
		t.viewport = this.aContainer_i();
		return t;
	};
	_proto.aContainer_i = function () {
		var t = new eui.Group();
		this.aContainer = t;
		t.touchEnabled = false;
		t.layout = this._VerticalLayout1_i();
		t.elementsContent = [this.readyGrp_i(),this.tryGrp_i(),this.gotGrp_i()];
		return t;
	};
	_proto._VerticalLayout1_i = function () {
		var t = new eui.VerticalLayout();
		t.gap = -70;
		return t;
	};
	_proto.readyGrp_i = function () {
		var t = new eui.Group();
		this.readyGrp = t;
		t.touchEnabled = false;
		t.elementsContent = [this._Group3_i(),this.readyContentGrp_i()];
		return t;
	};
	_proto._Group3_i = function () {
		var t = new eui.Group();
		t.touchEnabled = false;
		t.elementsContent = [this.readyRect_i(),this._Label1_i(),this.readyExpandBtn_i()];
		return t;
	};
	_proto.readyRect_i = function () {
		var t = new eui.Image();
		this.readyRect = t;
		t.anchorOffsetY = 0;
		t.height = 88;
		t.scale9Grid = new egret.Rectangle(27,30,36,36);
		t.source = "viewpage_json.achieve_bg";
		t.width = 700;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 34;
		t.text = "待领取";
		t.textColor = 0x914E00;
		t.x = 22;
		t.y = 27;
		return t;
	};
	_proto.readyExpandBtn_i = function () {
		var t = new eui.Image();
		this.readyExpandBtn = t;
		t.source = "viewpage_json.up_arrow";
		t.touchEnabled = true;
		t.x = 608;
		t.y = 3.5;
		return t;
	};
	_proto.readyContentGrp_i = function () {
		var t = new eui.Group();
		this.readyContentGrp = t;
		t.width = 710;
		t.y = 85;
		t.layout = this._TileLayout1_i();
		return t;
	};
	_proto._TileLayout1_i = function () {
		var t = new eui.TileLayout();
		t.horizontalGap = -10;
		t.verticalGap = 12;
		return t;
	};
	_proto.tryGrp_i = function () {
		var t = new eui.Group();
		this.tryGrp = t;
		t.touchEnabled = false;
		t.elementsContent = [this._Group4_i(),this.tryContentGrp_i()];
		return t;
	};
	_proto._Group4_i = function () {
		var t = new eui.Group();
		t.touchEnabled = false;
		t.y = 99;
		t.elementsContent = [this.tryRect_i(),this._Label2_i(),this.tryExpandBtn_i()];
		return t;
	};
	_proto.tryRect_i = function () {
		var t = new eui.Image();
		this.tryRect = t;
		t.anchorOffsetY = 0;
		t.height = 88;
		t.scale9Grid = new egret.Rectangle(27,30,36,36);
		t.source = "viewpage_json.achieve_bg";
		t.width = 700;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 34;
		t.text = "未获得";
		t.textColor = 0x914E00;
		t.x = 22;
		t.y = 27;
		return t;
	};
	_proto.tryExpandBtn_i = function () {
		var t = new eui.Image();
		this.tryExpandBtn = t;
		t.source = "viewpage_json.up_arrow";
		t.touchEnabled = true;
		t.x = 608;
		t.y = 3.5;
		return t;
	};
	_proto.tryContentGrp_i = function () {
		var t = new eui.Group();
		this.tryContentGrp = t;
		t.width = 710;
		t.y = 184;
		t.layout = this._VerticalLayout2_i();
		return t;
	};
	_proto._VerticalLayout2_i = function () {
		var t = new eui.VerticalLayout();
		t.gap = 20;
		return t;
	};
	_proto.gotGrp_i = function () {
		var t = new eui.Group();
		this.gotGrp = t;
		t.touchEnabled = false;
		t.y = 100;
		t.elementsContent = [this._Group5_i(),this.gotContentGrp_i()];
		return t;
	};
	_proto._Group5_i = function () {
		var t = new eui.Group();
		t.touchEnabled = false;
		t.y = 9;
		t.elementsContent = [this.gotRect_i(),this._Label3_i(),this.gotExpandBtn_i()];
		return t;
	};
	_proto.gotRect_i = function () {
		var t = new eui.Image();
		this.gotRect = t;
		t.height = 88;
		t.scale9Grid = new egret.Rectangle(27,30,36,36);
		t.source = "viewpage_json.achieve_bg";
		t.width = 700;
		t.x = 0;
		t.y = 91;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 34;
		t.text = "已获得";
		t.textColor = 0x914E00;
		t.x = 22;
		t.y = 118;
		return t;
	};
	_proto.gotExpandBtn_i = function () {
		var t = new eui.Image();
		this.gotExpandBtn = t;
		t.source = "viewpage_json.up_arrow";
		t.touchEnabled = true;
		t.x = 605;
		t.y = 91;
		return t;
	};
	_proto.gotContentGrp_i = function () {
		var t = new eui.Group();
		this.gotContentGrp = t;
		t.width = 750;
		t.y = 186;
		t.layout = this._TileLayout2_i();
		return t;
	};
	_proto._TileLayout2_i = function () {
		var t = new eui.TileLayout();
		t.verticalGap = -15;
		return t;
	};
	return MissionViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/NewUserRedpackSkin.exml'] = window.NewUserReadpackSkin = (function (_super) {
	__extends(NewUserReadpackSkin, _super);
	function NewUserReadpackSkin() {
		_super.call(this);
		this.skinParts = ["rpImg"];
		
		this.height = 83;
		this.width = 200;
		this.elementsContent = [this._Image1_i(),this.rpImg_i(),this._Label1_i()];
	}
	var _proto = NewUserReadpackSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 72;
		t.source = "menuover_json.countdown_bg";
		t.width = 178;
		t.x = 23;
		t.y = 9;
		return t;
	};
	_proto.rpImg_i = function () {
		var t = new eui.Image();
		this.rpImg = t;
		t.height = 77;
		t.source = "redeff_json.redpack";
		t.width = 60;
		t.x = 0;
		t.y = 5;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "次日领取";
		t.textColor = 0xFFFFFF;
		t.x = 72;
		t.y = 32;
		return t;
	};
	return NewUserReadpackSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/OverItem.exml'] = window.OverItemSkin = (function (_super) {
	__extends(OverItemSkin, _super);
	function OverItemSkin() {
		_super.call(this);
		this.skinParts = ["titleTxt","lvlTxt1","lvlTxt2","lvlbarImg","lvlImg1","imgGrp1","lvlImg2","imgGrp2","proGrp","homeBtn","nextBtn","lifeImg","levelTxt","scroller"];
		
		this.elementsContent = [this._Group1_i(),this.scroller_i()];
	}
	var _proto = OverItemSkin.prototype;

	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.cacheAsBitmap = true;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Rect1_i(),this._Image1_i(),this.titleTxt_i(),this.lvlTxt1_i(),this.lvlTxt2_i(),this.proGrp_i(),this.homeBtn_i(),this.nextBtn_i(),this._Label1_i(),this.lifeImg_i(),this.levelTxt_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseHeight = 64;
		t.ellipseWidth = 64;
		t.fillColor = 0xfffefa;
		t.height = 580;
		t.width = 700;
		t.x = 0;
		t.y = 65;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.overtitlebg";
		t.x = 75;
		t.y = 0;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.bold = true;
		t.size = 36;
		t.text = "恭喜通过第 600 关";
		t.textAlign = "center";
		t.width = 481;
		t.x = 110;
		t.y = 28;
		return t;
	};
	_proto.lvlTxt1_i = function () {
		var t = new eui.Label();
		this.lvlTxt1 = t;
		t.size = 22;
		t.text = "第3关";
		t.textColor = 0xbd8f63;
		t.x = 339;
		t.y = 334;
		return t;
	};
	_proto.lvlTxt2_i = function () {
		var t = new eui.Label();
		this.lvlTxt2 = t;
		t.size = 22;
		t.text = "第5关";
		t.textColor = 0xBD8F63;
		t.x = 538;
		t.y = 334;
		return t;
	};
	_proto.proGrp_i = function () {
		var t = new eui.Group();
		this.proGrp = t;
		t.x = 87;
		t.y = 365;
		t.elementsContent = [this._Rect2_i(),this.lvlbarImg_i(),this.imgGrp1_i(),this.imgGrp2_i()];
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 10;
		t.fillColor = 0xfae2c0;
		t.height = 14;
		t.width = 502;
		t.x = 6;
		t.y = 6;
		return t;
	};
	_proto.lvlbarImg_i = function () {
		var t = new eui.Image();
		this.lvlbarImg = t;
		t.height = 25;
		t.scale9Grid = new egret.Rectangle(82,10,14,2);
		t.source = "menuover_json.lvlbar";
		t.width = 200;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.imgGrp1_i = function () {
		var t = new eui.Group();
		this.imgGrp1 = t;
		t.x = 233;
		t.y = 19;
		t.elementsContent = [this._Image2_i(),this.lvlImg1_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.lvltipbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.lvlImg1_i = function () {
		var t = new eui.Image();
		this.lvlImg1 = t;
		t.anchorOffsetX = 25;
		t.anchorOffsetY = 25;
		t.height = 50;
		t.source = "menuover_json.coin";
		t.width = 50;
		t.x = 46;
		t.y = 38;
		return t;
	};
	_proto.imgGrp2_i = function () {
		var t = new eui.Group();
		this.imgGrp2 = t;
		t.x = 435;
		t.y = 19;
		t.elementsContent = [this._Image3_i(),this.lvlImg2_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.lvltipbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.lvlImg2_i = function () {
		var t = new eui.Image();
		this.lvlImg2 = t;
		t.anchorOffsetX = 25;
		t.anchorOffsetY = 25;
		t.height = 50;
		t.source = "menuover_json.coin";
		t.width = 50;
		t.x = 47;
		t.y = 38;
		return t;
	};
	_proto.homeBtn_i = function () {
		var t = new eui.Image();
		this.homeBtn = t;
		t.source = "menuover_json.ghomebtn";
		t.touchEnabled = true;
		t.x = 101;
		t.y = 525;
		return t;
	};
	_proto.nextBtn_i = function () {
		var t = new eui.Image();
		this.nextBtn = t;
		t.source = "menuover_json.nextbtn";
		t.touchEnabled = true;
		t.x = 247;
		t.y = 525;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 36;
		t.text = "下一关";
		t.touchEnabled = false;
		t.x = 328;
		t.y = 559;
		return t;
	};
	_proto.lifeImg_i = function () {
		var t = new eui.Image();
		this.lifeImg = t;
		t.source = "menuover_json.lifeC";
		t.touchEnabled = false;
		t.x = 450;
		t.y = 552;
		return t;
	};
	_proto.levelTxt_i = function () {
		var t = new eui.Label();
		this.levelTxt = t;
		t.size = 24;
		t.text = "还差1关解锁新房子";
		t.textAlign = "center";
		t.textColor = 0x914e00;
		t.width = 308;
		t.x = 239;
		t.y = 473;
		return t;
	};
	_proto.scroller_i = function () {
		var t = new eui.Scroller();
		this.scroller = t;
		t.height = 180;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "on";
		t.width = 520;
		t.x = 90;
		t.y = 146;
		t.viewport = this._Group2_i();
		return t;
	};
	_proto._Group2_i = function () {
		var t = new eui.Group();
		return t;
	};
	return OverItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PictureItem.exml'] = window.PictureItemSkin = (function (_super) {
	__extends(PictureItemSkin, _super);
	function PictureItemSkin() {
		_super.call(this);
		this.skinParts = ["bgRect","titleBg","maskShape","titleLabel","avatarImg"];
		
		this.currentState = "status_normal";
		this.elementsContent = [this.bgRect_i(),this.titleBg_i(),this.maskShape_i(),this.titleLabel_i(),this.avatarImg_i()];
		this._Image1_i();
		
		this._Label1_i();
		
		this.states = [
			new eui.State ("status_selected",
				[
					new eui.AddItems("_Image1","",1,""),
					new eui.AddItems("_Label1","",1,""),
					new eui.SetProperty("bgRect","strokeColor",0xb16e48),
					new eui.SetProperty("bgRect","strokeWeight",6),
					new eui.SetProperty("titleBg","fillColor",0xb16e48),
					new eui.SetProperty("titleLabel","textColor",0xffffff)
				])
			,
			new eui.State ("status_normal",
				[
				])
		];
	}
	var _proto = PictureItemSkin.prototype;

	_proto.bgRect_i = function () {
		var t = new eui.Rect();
		this.bgRect = t;
		t.ellipseHeight = 32;
		t.ellipseWidth = 32;
		t.fillColor = 0xfffdf6;
		t.height = 270;
		t.strokeColor = 0xeed3b6;
		t.strokeWeight = 1;
		t.width = 180;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.titleBg_i = function () {
		var t = new eui.Rect();
		this.titleBg = t;
		t.ellipseHeight = 24;
		t.ellipseWidth = 24;
		t.fillColor = 0xf6e6d3;
		t.height = 48;
		t.width = 160;
		t.x = 10;
		t.y = 14;
		return t;
	};
	_proto.maskShape_i = function () {
		var t = new eui.Rect();
		this.maskShape = t;
		t.fillColor = 0xdcd7cc;
		t.height = 160;
		t.width = 160;
		t.x = 10;
		t.y = 80;
		return t;
	};
	_proto.titleLabel_i = function () {
		var t = new eui.Label();
		this.titleLabel = t;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 47;
		t.size = 26;
		t.text = "捉襟见肘";
		t.textAlign = "center";
		t.textColor = 0xb16e48;
		t.verticalAlign = "middle";
		t.width = 180;
		t.x = 0;
		t.y = 15;
		return t;
	};
	_proto.avatarImg_i = function () {
		var t = new eui.Image();
		this.avatarImg = t;
		t.source = "viewpage_json.right";
		t.x = 90;
		t.y = 160;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.source = "viewpage_json.usetipbg";
		t.x = 92;
		t.y = 228;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.bold = true;
		t.size = 22;
		t.text = "使用中";
		t.x = 100;
		t.y = 238;
		return t;
	};
	return PictureItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PictureViewSkin.exml'] = window.NewFile = (function (_super) {
	__extends(NewFile, _super);
	function NewFile() {
		_super.call(this);
		this.skinParts = ["titleImage","pScroller","titleTxt","closeBtn","beastGrp","mainGrp"];
		
		this.currentState = "normal_status";
		this.elementsContent = [this.mainGrp_i()];
		this.titleTxt_i();
		
		this._Rect1_i();
		
		this._Image2_i();
		
		this._Label1_i();
		
		this.beastGrp_i();
		
		this.states = [
			new eui.State ("normal_status",
				[
					new eui.AddItems("titleTxt","mainGrp",2,"closeBtn"),
					new eui.SetProperty("titleImage","anchorOffsetX",0),
					new eui.SetProperty("titleImage","anchorOffsetY",0),
					new eui.SetProperty("titleImage","y",0),
					new eui.SetProperty("titleImage","x",0)
				])
			,
			new eui.State ("pets_status",
				[
					new eui.AddItems("_Rect1","beastGrp",0,""),
					new eui.AddItems("_Image2","beastGrp",2,"_Label2"),
					new eui.AddItems("_Label1","beastGrp",2,"_Label2"),
					new eui.AddItems("beastGrp","mainGrp",1,""),
					new eui.SetProperty("titleImage","x",0),
					new eui.SetProperty("titleImage","y",0),
					new eui.SetProperty("titleImage","anchorOffsetX",0),
					new eui.SetProperty("titleImage","anchorOffsetY",0),
					new eui.SetProperty("pScroller","height",616),
					new eui.SetProperty("pScroller","x",20),
					new eui.SetProperty("pScroller","y",388)
				])
		];
	}
	var _proto = NewFile.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.titleImage_i(),this.pScroller_i(),this.closeBtn_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 970;
		t.scale9Grid = new egret.Rectangle(30,31,3,2);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 48;
		return t;
	};
	_proto.titleImage_i = function () {
		var t = new eui.Image();
		this.titleImage = t;
		t.anchorOffsetX = 320;
		t.anchorOffsetY = 40;
		t.source = "viewpage_json.housetitle";
		t.x = 320;
		t.y = 39;
		return t;
	};
	_proto.pScroller_i = function () {
		var t = new eui.Scroller();
		this.pScroller = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 890;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "on";
		t.width = 600;
		t.x = 20;
		t.y = 116;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.x = -144;
		t.y = 80;
		return t;
	};
	_proto.titleTxt_i = function () {
		var t = new eui.Label();
		this.titleTxt = t;
		t.bold = true;
		t.size = 42;
		t.text = "";
		t.x = 320;
		t.y = 39;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 572;
		t.y = -20;
		return t;
	};
	_proto.beastGrp_i = function () {
		var t = new eui.Group();
		this.beastGrp = t;
		t.cacheAsBitmap = true;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 42;
		t.y = 126;
		t.elementsContent = [this._Label2_i(),this._Image3_i(),this._Label3_i(),this._Image4_i(),this._Label4_i()];
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		this._Rect1 = t;
		t.ellipseHeight = 32;
		t.ellipseWidth = 32;
		t.fillColor = 0xfffdf6;
		t.height = 256;
		t.width = 556;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.source = "viewpage_json.beast";
		t.x = 36;
		t.y = 32;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.text = "分红神兽";
		t.textColor = 0xb16e48;
		t.x = 215;
		t.y = 49;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.size = 24;
		t.text = "每天获得平台广告收益的20%";
		t.textColor = 0xef5e38;
		t.x = 215;
		t.y = 97;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.height = 58;
		t.source = "menuover_json.nextbtn";
		t.touchEnabled = false;
		t.width = 156;
		t.x = 219;
		t.y = 152;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.size = 26;
		t.text = "如何获得？";
		t.touchEnabled = false;
		t.x = 238;
		t.y = 168;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.xhighestbg";
		t.x = 330;
		t.y = 22;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.size = 20;
		t.text = "限量10万只";
		t.x = 336.63;
		t.y = 26;
		return t;
	};
	return NewFile;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKBonusView.exml'] = window.PKBonusViewSkin = (function (_super) {
	__extends(PKBonusViewSkin, _super);
	function PKBonusViewSkin() {
		_super.call(this);
		this.skinParts = ["titleImg","videoBtn","cancelTxt"];
		
		this.elementsContent = [this._Image1_i(),this.titleImg_i(),this.videoBtn_i(),this._Image2_i(),this._Image3_i(),this._Label1_i(),this.cancelTxt_i(),this._Label2_i()];
	}
	var _proto = PKBonusViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 520;
		t.scale9Grid = new egret.Rectangle(31,29,61,64);
		t.source = "dispelPk_json.dpk_dlg_0";
		t.width = 660;
		t.x = 0;
		t.y = 39;
		return t;
	};
	_proto.titleImg_i = function () {
		var t = new eui.Image();
		this.titleImg = t;
		t.height = 91;
		t.source = "dispelPk_json.dpk_bonus_title";
		t.width = 389;
		t.x = 136;
		t.y = -1;
		return t;
	};
	_proto.videoBtn_i = function () {
		var t = new eui.Image();
		this.videoBtn = t;
		t.height = 101;
		t.source = "dispelPk_json.dpk_cancelbtn";
		t.width = 227;
		t.x = 367;
		t.y = 370;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 47;
		t.source = "dispelPk_json.dpk_video_0";
		t.touchEnabled = false;
		t.width = 49;
		t.x = 512;
		t.y = 393.5;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.height = 101;
		t.source = "dispelPk_json.dpk_confirmbtn";
		t.touchEnabled = false;
		t.width = 227;
		t.x = 70;
		t.y = 370;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 42;
		t.text = "翻倍";
		t.textColor = 0xffffff;
		t.touchEnabled = false;
		t.x = 416;
		t.y = 396.5;
		return t;
	};
	_proto.cancelTxt_i = function () {
		var t = new eui.Label();
		this.cancelTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 101;
		t.size = 42;
		t.text = "不翻倍";
		t.textAlign = "center";
		t.textColor = 0xffffff;
		t.touchEnabled = true;
		t.verticalAlign = "middle";
		t.width = 227;
		t.x = 70;
		t.y = 370;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 181;
		t.lineSpacing = 14;
		t.size = 34;
		t.text = "如果本场比赛获得胜利，您获得的 奖励将会翻倍，是否选择翻倍奖励？";
		t.textColor = 0x222222;
		t.verticalAlign = "middle";
		t.width = 563;
		t.x = 64;
		t.y = 135;
		return t;
	};
	return PKBonusViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKFriendUI.exml'] = window.PKFriendUISkin = (function (_super) {
	__extends(PKFriendUISkin, _super);
	function PKFriendUISkin() {
		_super.call(this);
		this.skinParts = ["backBtn","readyImg","myfriendBtn","chatBtn","startBtn","startTxt","inviteBtn","headImg1","maskRect1","headImg2","maskRect2","tipsTxt","myNameTxt","friendNameTxt","nowTxt","playGrp"];
		
		this.elementsContent = [this._Image1_i(),this.backBtn_i(),this._Image2_i(),this._Image3_i(),this._Image4_i(),this._Image5_i(),this.readyImg_i(),this.myfriendBtn_i(),this.chatBtn_i(),this.startBtn_i(),this.startTxt_i(),this.inviteBtn_i(),this.headImg1_i(),this.maskRect1_i(),this.headImg2_i(),this.maskRect2_i(),this.tipsTxt_i(),this.myNameTxt_i(),this.friendNameTxt_i(),this.nowTxt_i(),this.playGrp_i()];
	}
	var _proto = PKFriendUISkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 680;
		t.scale9Grid = new egret.Rectangle(45,42,7,7);
		t.source = "dispelPk_json.dpk_hysbg";
		t.width = 700;
		t.x = 0;
		t.y = 174;
		return t;
	};
	_proto.backBtn_i = function () {
		var t = new eui.Image();
		this.backBtn = t;
		t.source = "dispelPk_json.dpk_homebtn";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_friendtitle";
		t.x = 86;
		t.y = 105;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_fleftbg";
		t.x = 22;
		t.y = 265;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_frightbg";
		t.x = 486;
		t.y = 265;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_vshy";
		t.x = 223;
		t.y = 362;
		return t;
	};
	_proto.readyImg_i = function () {
		var t = new eui.Image();
		this.readyImg = t;
		t.source = "dispelPk_json.dpk_isready";
		t.x = 596;
		t.y = 244;
		return t;
	};
	_proto.myfriendBtn_i = function () {
		var t = new eui.Image();
		this.myfriendBtn = t;
		t.source = "dispelPk_json.dpk_friend";
		t.x = 585;
		t.y = 911;
		return t;
	};
	_proto.chatBtn_i = function () {
		var t = new eui.Image();
		this.chatBtn = t;
		t.anchorOffsetY = 24;
		t.scaleY = -1;
		t.source = "dispelPk_json.dpk_tlistbg";
		t.x = 200;
		t.y = 595;
		return t;
	};
	_proto.startBtn_i = function () {
		var t = new eui.Image();
		this.startBtn = t;
		t.source = "dispelPk_json.dpk_btn_0";
		t.x = 181;
		t.y = 655;
		return t;
	};
	_proto.startTxt_i = function () {
		var t = new eui.Label();
		this.startTxt = t;
		t.bold = true;
		t.size = 48;
		t.stroke = 3;
		t.strokeColor = 0x8f3728;
		t.text = "开始对战";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 338;
		t.x = 181;
		t.y = 688;
		return t;
	};
	_proto.inviteBtn_i = function () {
		var t = new eui.Image();
		this.inviteBtn = t;
		t.source = "dispelPk_json.dpk_invitebtn";
		t.x = 170;
		t.y = 654;
		return t;
	};
	_proto.headImg1_i = function () {
		var t = new eui.Image();
		this.headImg1 = t;
		t.height = 130;
		t.source = "menuover_json.headimg";
		t.width = 130;
		t.x = 52;
		t.y = 289;
		return t;
	};
	_proto.maskRect1_i = function () {
		var t = new eui.Rect();
		this.maskRect1 = t;
		t.ellipseHeight = 120;
		t.ellipseWidth = 120;
		t.height = 120;
		t.width = 120;
		t.x = 57;
		t.y = 294;
		return t;
	};
	_proto.headImg2_i = function () {
		var t = new eui.Image();
		this.headImg2 = t;
		t.height = 130;
		t.source = "menuover_json.headimg";
		t.width = 130;
		t.x = 517.5;
		t.y = 289;
		return t;
	};
	_proto.maskRect2_i = function () {
		var t = new eui.Rect();
		this.maskRect2 = t;
		t.ellipseHeight = 120;
		t.ellipseWidth = 120;
		t.height = 120;
		t.width = 120;
		t.x = 522.5;
		t.y = 294;
		return t;
	};
	_proto.tipsTxt_i = function () {
		var t = new eui.Label();
		this.tipsTxt = t;
		t.bold = true;
		t.text = "等待好友加入...";
		t.textAlign = "center";
		t.textColor = 0xffe646;
		t.width = 220;
		t.x = 240;
		t.y = 463;
		return t;
	};
	_proto.myNameTxt_i = function () {
		var t = new eui.Label();
		this.myNameTxt = t;
		t.bold = true;
		t.height = 25;
		t.multiline = false;
		t.size = 24;
		t.text = "";
		t.textAlign = "center";
		t.width = 175;
		t.x = 29;
		t.y = 463;
		return t;
	};
	_proto.friendNameTxt_i = function () {
		var t = new eui.Label();
		this.friendNameTxt = t;
		t.bold = true;
		t.height = 25;
		t.multiline = false;
		t.size = 24;
		t.text = "";
		t.textAlign = "center";
		t.width = 175;
		t.x = 493;
		t.y = 463;
		return t;
	};
	_proto.nowTxt_i = function () {
		var t = new eui.Label();
		this.nowTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.size = 24;
		t.text = "一起battle一下吧";
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 211;
		t.y = 576;
		return t;
	};
	_proto.playGrp_i = function () {
		var t = new eui.Group();
		this.playGrp = t;
		t.visible = false;
		t.x = 200;
		t.y = 617;
		t.elementsContent = [this._Image6_i(),this._Label1_i(),this._Label2_i(),this._Label3_i(),this._Label4_i(),this._Label5_i(),this._Label6_i()];
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 276;
		t.scale9Grid = new egret.Rectangle(15,15,3,4);
		t.source = "dispelPk_json.dpk_xlistbg";
		t.width = 252;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_0";
		t.size = 24;
		t.text = "一起battle一下吧";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 8;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_1";
		t.size = 24;
		t.text = "输家晚上请吃饭";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 52;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_2";
		t.size = 24;
		t.text = "分数低的发红包";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 96;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_3";
		t.size = 24;
		t.text = "输的人罚三杯";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 139;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_4";
		t.size = 24;
		t.text = "谁输谁来做家务";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 183;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 42;
		t.name = "playtxt_5";
		t.size = 24;
		t.text = "输的人罚做俯卧撑";
		t.verticalAlign = "middle";
		t.width = 239;
		t.x = 11;
		t.y = 227;
		return t;
	};
	return PKFriendUISkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKGameUI.exml'] = window.PKGameUISkin = (function (_super) {
	__extends(PKGameUISkin, _super);
	function PKGameUISkin() {
		_super.call(this);
		this.skinParts = ["headMask1","headMask2","headImg1","headImg2","progress1","progress2","prgmask1","prgmask2","timeTxt","scoreTxt1","scoreTxt2","toastTxt1","toastTxt2","topGrp","pkbgImg","wordGrp","tipBtn","itemBtn1","itemBtn2","itemBtn3","itemBtn4","idiomBg0","idiomBg1","idiomBg2","idiomBg3","idiomBg4","idiomBg5","giveupBtn","chatBtn","idiomTxt0","idiomTxt1","idiomTxt2","idiomTxt3","idiomTxt4","idiomTxt5","itemLabel1","itemCnt1","itemLabel2","itemCnt2","itemLabel3","itemCnt3","itemLabel4","itemCnt4","tipsTxt","tipMask","bottomGrp","chatDlgGrp","chatBubbleGrp1","chatBubbleGrp2"];
		
		this.elementsContent = [this.topGrp_i(),this.pkbgImg_i(),this.wordGrp_i(),this.bottomGrp_i(),this.chatDlgGrp_i(),this.chatBubbleGrp1_i(),this.chatBubbleGrp2_i()];
	}
	var _proto = PKGameUISkin.prototype;

	_proto.topGrp_i = function () {
		var t = new eui.Group();
		this.topGrp = t;
		t.x = 23;
		t.y = 73;
		t.elementsContent = [this.headMask1_i(),this.headMask2_i(),this.headImg1_i(),this.headImg2_i(),this._Image1_i(),this._Image2_i(),this._Image3_i(),this.progress1_i(),this.progress2_i(),this.prgmask1_i(),this.prgmask2_i(),this._Label1_i(),this.timeTxt_i(),this.scoreTxt1_i(),this.scoreTxt2_i(),this.toastTxt1_i(),this.toastTxt2_i()];
		return t;
	};
	_proto.headMask1_i = function () {
		var t = new eui.Rect();
		this.headMask1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.ellipseWidth = 108;
		t.height = 108;
		t.width = 108;
		t.x = 10;
		t.y = 6;
		return t;
	};
	_proto.headMask2_i = function () {
		var t = new eui.Rect();
		this.headMask2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.ellipseWidth = 108;
		t.height = 108;
		t.width = 108;
		t.x = 581;
		t.y = 6;
		return t;
	};
	_proto.headImg1_i = function () {
		var t = new eui.Image();
		this.headImg1 = t;
		t.height = 120;
		t.source = "menuover_json.headimg";
		t.width = 120;
		t.x = 4;
		t.y = 0;
		return t;
	};
	_proto.headImg2_i = function () {
		var t = new eui.Image();
		this.headImg2 = t;
		t.height = 120;
		t.source = "menuover_json.headimg";
		t.width = 120;
		t.x = 575;
		t.y = 0;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_leftbg";
		t.x = 0;
		t.y = 90;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_rightbg";
		t.x = 569;
		t.y = 90;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_pgrbg";
		t.x = 157;
		t.y = 68;
		return t;
	};
	_proto.progress1_i = function () {
		var t = new eui.Image();
		this.progress1 = t;
		t.anchorOffsetY = 1;
		t.scale9Grid = new egret.Rectangle(121,22,11,3);
		t.scaleX = 1;
		t.source = "dispelPk_json.dpk_pgr1";
		t.x = 164;
		t.y = 76;
		return t;
	};
	_proto.progress2_i = function () {
		var t = new eui.Image();
		this.progress2 = t;
		t.anchorOffsetX = 174;
		t.anchorOffsetY = 24;
		t.scale9Grid = new egret.Rectangle(64,6,8,36);
		t.source = "dispelPk_json.dpk_pgr2";
		t.x = 513;
		t.y = 99;
		return t;
	};
	_proto.prgmask1_i = function () {
		var t = new eui.Rect();
		this.prgmask1 = t;
		t.height = 40;
		t.width = 174;
		t.x = 163;
		t.y = 69;
		return t;
	};
	_proto.prgmask2_i = function () {
		var t = new eui.Rect();
		this.prgmask2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 40;
		t.scaleX = -1;
		t.width = 174;
		t.x = 513;
		t.y = 69;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.scaleX = 1;
		t.scaleY = 1;
		t.text = "倒计时";
		t.x = 293;
		t.y = -31;
		return t;
	};
	_proto.timeTxt_i = function () {
		var t = new eui.Label();
		this.timeTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 52;
		t.size = 48;
		t.text = "00:39";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 191;
		t.x = 243;
		t.y = 14;
		return t;
	};
	_proto.scoreTxt1_i = function () {
		var t = new eui.Label();
		this.scoreTxt1 = t;
		t.bold = true;
		t.size = 24;
		t.text = "得分：500";
		t.textAlign = "center";
		t.textColor = 0x7d4700;
		t.width = 130;
		t.x = 0;
		t.y = 98;
		return t;
	};
	_proto.scoreTxt2_i = function () {
		var t = new eui.Label();
		this.scoreTxt2 = t;
		t.bold = true;
		t.size = 24;
		t.text = "得分：500";
		t.textAlign = "center";
		t.textColor = 0x1e2d7c;
		t.width = 130;
		t.x = 569;
		t.y = 98;
		return t;
	};
	_proto.toastTxt1_i = function () {
		var t = new eui.Label();
		this.toastTxt1 = t;
		t.size = 34;
		t.text = "+200";
		t.textColor = 0xffdb89;
		t.x = 25.5;
		t.y = 0;
		return t;
	};
	_proto.toastTxt2_i = function () {
		var t = new eui.Label();
		this.toastTxt2 = t;
		t.size = 34;
		t.text = "+200";
		t.textColor = 0xFFDB89;
		t.x = 594.5;
		t.y = 0;
		return t;
	};
	_proto.pkbgImg_i = function () {
		var t = new eui.Image();
		this.pkbgImg = t;
		t.height = 560;
		t.scale9Grid = new egret.Rectangle(44,45,8,8);
		t.scaleX = 1;
		t.scaleY = 1;
		t.source = "dispelPk_json.dpk_pkbg";
		t.width = 700;
		t.x = 22;
		t.y = 230;
		return t;
	};
	_proto.wordGrp_i = function () {
		var t = new eui.Group();
		this.wordGrp = t;
		t.cacheAsBitmap = true;
		t.touchChildren = true;
		t.x = 41;
		t.y = 253;
		return t;
	};
	_proto.bottomGrp_i = function () {
		var t = new eui.Group();
		this.bottomGrp = t;
		t.cacheAsBitmap = false;
		t.x = 30;
		t.y = 740;
		t.elementsContent = [this.tipBtn_i(),this._Image4_i(),this._Image5_i(),this._Image6_i(),this.itemBtn1_i(),this.itemBtn2_i(),this.itemBtn3_i(),this.itemBtn4_i(),this.idiomBg0_i(),this.idiomBg1_i(),this.idiomBg2_i(),this.idiomBg3_i(),this.idiomBg4_i(),this.idiomBg5_i(),this.giveupBtn_i(),this.chatBtn_i(),this.idiomTxt0_i(),this.idiomTxt1_i(),this.idiomTxt2_i(),this.idiomTxt3_i(),this.idiomTxt4_i(),this.idiomTxt5_i(),this.itemLabel1_i(),this.itemCnt1_i(),this.itemLabel2_i(),this.itemCnt2_i(),this.itemLabel3_i(),this.itemCnt3_i(),this.itemLabel4_i(),this.itemCnt4_i(),this._Label2_i(),this.tipsTxt_i(),this._Label3_i(),this.tipMask_i()];
		return t;
	};
	_proto.tipBtn_i = function () {
		var t = new eui.Image();
		this.tipBtn = t;
		t.height = 80;
		t.scale9Grid = new egret.Rectangle(48,32,4,2);
		t.source = "dispelPk_json.dpk_wordbg";
		t.touchEnabled = true;
		t.width = 628;
		t.x = 26;
		t.y = 1;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_refresh";
		t.touchEnabled = false;
		t.x = 44;
		t.y = 24;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.anchorOffsetY = 0;
		t.height = 148;
		t.scale9Grid = new egret.Rectangle(21,20,2,2);
		t.source = "dispelPk_json.dpk_listbg";
		t.width = 690;
		t.x = 0;
		t.y = 123;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 39;
		t.source = "dispelPk_json.dpk_item";
		t.width = 73;
		t.x = 2;
		t.y = 125;
		return t;
	};
	_proto.itemBtn1_i = function () {
		var t = new eui.Image();
		this.itemBtn1 = t;
		t.source = "dispelPk_json.dpk_bigglass";
		t.x = 46;
		t.y = 148;
		return t;
	};
	_proto.itemBtn2_i = function () {
		var t = new eui.Image();
		this.itemBtn2 = t;
		t.source = "dispelPk_json.dpk_ink";
		t.x = 213;
		t.y = 154;
		return t;
	};
	_proto.itemBtn3_i = function () {
		var t = new eui.Image();
		this.itemBtn3 = t;
		t.source = "dispelPk_json.dpk_reset";
		t.x = 376;
		t.y = 152;
		return t;
	};
	_proto.itemBtn4_i = function () {
		var t = new eui.Image();
		this.itemBtn4 = t;
		t.source = "dispelPk_json.dpk_protect";
		t.x = 552;
		t.y = 152;
		return t;
	};
	_proto.idiomBg0_i = function () {
		var t = new eui.Image();
		this.idiomBg0 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 0;
		t.y = 296;
		return t;
	};
	_proto.idiomBg1_i = function () {
		var t = new eui.Image();
		this.idiomBg1 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 235;
		t.y = 296;
		return t;
	};
	_proto.idiomBg2_i = function () {
		var t = new eui.Image();
		this.idiomBg2 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 470;
		t.y = 296;
		return t;
	};
	_proto.idiomBg3_i = function () {
		var t = new eui.Image();
		this.idiomBg3 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 0;
		t.y = 375;
		return t;
	};
	_proto.idiomBg4_i = function () {
		var t = new eui.Image();
		this.idiomBg4 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 235;
		t.y = 375;
		return t;
	};
	_proto.idiomBg5_i = function () {
		var t = new eui.Image();
		this.idiomBg5 = t;
		t.height = 72;
		t.scale9Grid = new egret.Rectangle(21,19,3,3);
		t.source = "dispelPk_json.dpk_answerbg";
		t.width = 220;
		t.x = 470;
		t.y = 375;
		return t;
	};
	_proto.giveupBtn_i = function () {
		var t = new eui.Image();
		this.giveupBtn = t;
		t.source = "dispelPk_json.dpk_giveupbtn";
		t.touchEnabled = true;
		t.x = 545;
		t.y = 515;
		return t;
	};
	_proto.chatBtn_i = function () {
		var t = new eui.Image();
		this.chatBtn = t;
		t.source = "dispelPk_json.dpk_chatbtn";
		t.x = 3;
		t.y = 518;
		return t;
	};
	_proto.idiomTxt0_i = function () {
		var t = new eui.Label();
		this.idiomTxt0 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 0;
		t.y = 297;
		return t;
	};
	_proto.idiomTxt1_i = function () {
		var t = new eui.Label();
		this.idiomTxt1 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 235;
		t.y = 297;
		return t;
	};
	_proto.idiomTxt2_i = function () {
		var t = new eui.Label();
		this.idiomTxt2 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 470;
		t.y = 297;
		return t;
	};
	_proto.idiomTxt3_i = function () {
		var t = new eui.Label();
		this.idiomTxt3 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 0;
		t.y = 376;
		return t;
	};
	_proto.idiomTxt4_i = function () {
		var t = new eui.Label();
		this.idiomTxt4 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 235;
		t.y = 376;
		return t;
	};
	_proto.idiomTxt5_i = function () {
		var t = new eui.Label();
		this.idiomTxt5 = t;
		t.height = 72;
		t.size = 34;
		t.text = "大鹏展翅";
		t.textAlign = "center";
		t.verticalAlign = "middle";
		t.width = 220;
		t.x = 470;
		t.y = 376;
		return t;
	};
	_proto.itemLabel1_i = function () {
		var t = new eui.Label();
		this.itemLabel1 = t;
		t.bold = true;
		t.size = 28;
		t.stroke = 2;
		t.text = "放大镜";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 100;
		t.x = 36;
		t.y = 218;
		return t;
	};
	_proto.itemCnt1_i = function () {
		var t = new eui.Label();
		this.itemCnt1 = t;
		t.bold = true;
		t.size = 24;
		t.text = "(0)";
		t.textColor = 0x51edff;
		t.touchEnabled = false;
		t.x = 119;
		t.y = 154;
		return t;
	};
	_proto.itemLabel2_i = function () {
		var t = new eui.Label();
		this.itemLabel2 = t;
		t.bold = true;
		t.size = 28;
		t.stroke = 2;
		t.text = "墨汁";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 100;
		t.x = 193;
		t.y = 218;
		return t;
	};
	_proto.itemCnt2_i = function () {
		var t = new eui.Label();
		this.itemCnt2 = t;
		t.bold = true;
		t.size = 24;
		t.text = "(0)";
		t.textColor = 0x51EDFF;
		t.touchEnabled = false;
		t.x = 286;
		t.y = 154;
		return t;
	};
	_proto.itemLabel3_i = function () {
		var t = new eui.Label();
		this.itemLabel3 = t;
		t.bold = true;
		t.size = 28;
		t.stroke = 2;
		t.text = "重排";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 100;
		t.x = 360;
		t.y = 218;
		return t;
	};
	_proto.itemCnt3_i = function () {
		var t = new eui.Label();
		this.itemCnt3 = t;
		t.bold = true;
		t.size = 24;
		t.text = "(0)";
		t.textColor = 0x51EDFF;
		t.touchEnabled = false;
		t.x = 449;
		t.y = 153;
		return t;
	};
	_proto.itemLabel4_i = function () {
		var t = new eui.Label();
		this.itemLabel4 = t;
		t.bold = true;
		t.size = 28;
		t.stroke = 2;
		t.text = "保护卡";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 100;
		t.x = 534;
		t.y = 217;
		return t;
	};
	_proto.itemCnt4_i = function () {
		var t = new eui.Label();
		this.itemCnt4 = t;
		t.bold = true;
		t.size = 24;
		t.text = "(0)";
		t.textColor = 0x51EDFF;
		t.touchEnabled = false;
		t.x = 626;
		t.y = 153;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 36;
		t.text = "认输";
		t.textColor = 0x8d3f00;
		t.touchEnabled = false;
		t.x = 580;
		t.y = 534;
		return t;
	};
	_proto.tipsTxt_i = function () {
		var t = new eui.Label();
		this.tipsTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 41;
		t.size = 28;
		t.text = "形容一件很难做的事情地方打人";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.x = 168;
		t.y = 22;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "提示：";
		t.textColor = 0xffec47;
		t.x = 87;
		t.y = 30;
		return t;
	};
	_proto.tipMask_i = function () {
		var t = new eui.Rect();
		this.tipMask = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 67;
		t.width = 476;
		t.x = 161;
		t.y = 9;
		return t;
	};
	_proto.chatDlgGrp_i = function () {
		var t = new eui.Group();
		this.chatDlgGrp = t;
		t.anchorOffsetY = 416;
		t.cacheAsBitmap = true;
		t.visible = false;
		t.x = 30;
		t.y = 1254;
		t.elementsContent = [this._Image7_i(),this._Label4_i(),this._Label5_i(),this._Label6_i(),this._Label7_i(),this._Label8_i(),this._Label9_i(),this._Label10_i()];
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		t.height = 416;
		t.scale9Grid = new egret.Rectangle(52,12,5,3);
		t.source = "dispelPk_json.dpk_chatbg";
		t.width = 354;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.anchorOffsetY = 0;
		t.height = 40;
		t.name = "chat_0";
		t.size = 26;
		t.text = "你也太厉害了吧！";
		t.x = 25;
		t.y = 29;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_1";
		t.size = 26;
		t.text = "大佬，求轻虐~";
		t.x = 25;
		t.y = 81;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_2";
		t.size = 26;
		t.text = "谢谢，过奖啦~";
		t.x = 25;
		t.y = 134;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_3";
		t.size = 26;
		t.text = "让你一分钟";
		t.x = 25;
		t.y = 186;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_4";
		t.size = 26;
		t.text = "是时候展现真正的实力了！";
		t.x = 25;
		t.y = 238;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_5";
		t.size = 26;
		t.text = "答慢点，让让我啊~";
		t.x = 25;
		t.y = 291;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		t.height = 40;
		t.name = "chat_6";
		t.size = 26;
		t.text = "感觉要凉凉了";
		t.x = 25;
		t.y = 343;
		return t;
	};
	_proto.chatBubbleGrp1_i = function () {
		var t = new eui.Group();
		this.chatBubbleGrp1 = t;
		t.x = 137;
		t.y = 101;
		t.elementsContent = [this._Image8_i(),this._Label11_i()];
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(46,33,4,8);
		t.source = "dispelPk_json.dpk_singlechat";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		t.text = "这也太厉害了";
		t.x = 19;
		t.y = 23;
		return t;
	};
	_proto.chatBubbleGrp2_i = function () {
		var t = new eui.Group();
		this.chatBubbleGrp2 = t;
		t.x = 406;
		t.y = 101;
		t.elementsContent = [this._Image9_i(),this._Label12_i()];
		return t;
	};
	_proto._Image9_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(46,33,4,8);
		t.scaleX = -1;
		t.source = "dispelPk_json.dpk_singlechat";
		t.x = 199.5;
		t.y = 0;
		return t;
	};
	_proto._Label12_i = function () {
		var t = new eui.Label();
		t.text = "这也太厉害了";
		t.x = 19;
		t.y = 23;
		return t;
	};
	return PKGameUISkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKHelpView.exml'] = window.PKBonusViewSkin = (function (_super) {
	__extends(PKBonusViewSkin, _super);
	function PKBonusViewSkin() {
		_super.call(this);
		this.skinParts = ["closeBtn"];
		
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this.closeBtn_i(),this._Label1_i(),this._Label2_i(),this._Label3_i(),this._Label4_i(),this._Label5_i(),this._Label6_i(),this._Label7_i(),this._Label8_i(),this._Label9_i(),this._Label10_i(),this._Label11_i(),this._Label12_i(),this._Label13_i(),this._Label14_i()];
	}
	var _proto = PKBonusViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 952;
		t.scale9Grid = new egret.Rectangle(31,29,61,64);
		t.source = "dispelPk_json.dpk_dlg_0";
		t.width = 660;
		t.x = 0;
		t.y = 40;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 91;
		t.source = "dispelPk_json.dpk_help_title";
		t.width = 389;
		t.x = 111;
		t.y = 0;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "dispelPk_json.dpk_close_btn";
		t.x = 595;
		t.y = 11;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "（1）玩家开始对战匹配需要支付入场门票，每次对战需要消耗1张入场券，新用户免费赠送3张门票；";
		t.textColor = 0x343434;
		t.width = 523;
		t.x = 67;
		t.y = 118;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "（2）当玩家在入场券和道具消耗完毕时，需观看视频广告后获取免费的入场券和道具；";
		t.textColor = 0x343434;
		t.width = 523;
		t.x = 67;
		t.y = 252;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "（3）用户需要按照成语的顺序点击对应的文字进行消除，优先完成所有成语的玩家即为胜利；";
		t.textColor = 0x343434;
		t.width = 523;
		t.x = 67;
		t.y = 382;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "（4）连续消除和使用道具都会有额外的得分，合理的运用道具，有助于比赛的胜利哦；";
		t.textColor = 0x343434;
		t.width = 523;
		t.x = 67;
		t.y = 514;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "（5）道具说明:";
		t.textColor = 0x4670DC;
		t.x = 67;
		t.y = 638;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "墨汁：";
		t.textColor = 0x343434;
		t.x = 65;
		t.y = 682;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "使对手的棋盘被墨汁覆盖持续10秒";
		t.textColor = 0x343434;
		t.x = 139.68;
		t.y = 682;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "放大镜：";
		t.textColor = 0x343434;
		t.x = 65;
		t.y = 725;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "直接提示并消除一个成语";
		t.textColor = 0x343434;
		t.x = 169.01;
		t.y = 725.33;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "重排：";
		t.textColor = 0x343434;
		t.x = 65;
		t.y = 769;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "使对手的棋盘进行重新排列";
		t.textColor = 0x343434;
		t.x = 143.68;
		t.y = 768;
		return t;
	};
	_proto._Label12_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "保护卡：";
		t.textColor = 0x343434;
		t.x = 65;
		t.y = 812;
		return t;
	};
	_proto._Label13_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "在60s内可抵御一次对手的攻击";
		t.textColor = 0x343434;
		t.width = 428.33;
		t.x = 169;
		t.y = 812;
		return t;
	};
	_proto._Label14_i = function () {
		var t = new eui.Label();
		t.lineSpacing = 12;
		t.size = 28;
		t.text = "（6）最终解释权归疯狂猜成语所有，如有问题请联系客服。";
		t.textColor = 0x343434;
		t.width = 523;
		t.x = 67;
		t.y = 853.68;
		return t;
	};
	return PKBonusViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKMatchUI.exml'] = window.PKMatchUISkin = (function (_super) {
	__extends(PKMatchUISkin, _super);
	function PKMatchUISkin() {
		_super.call(this);
		this.skinParts = ["wave1","wave2","headImg1","nameTxt1","headMask1","playerGrp1","headImg2","nameTxt2","headMask2","playerGrp2"];
		
		this.elementsContent = [this._Image1_i(),this._Image2_i(),this.playerGrp1_i(),this.playerGrp2_i()];
	}
	var _proto = PKMatchUISkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.horizontalCenter = 0.5;
		t.source = "dispelPk_json.dpk_vstitle";
		t.y = 0;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.horizontalCenter = 0.5;
		t.source = "dispelPk_json.dpk_VS";
		t.y = 446;
		return t;
	};
	_proto.playerGrp1_i = function () {
		var t = new eui.Group();
		this.playerGrp1 = t;
		t.x = 66;
		t.y = 212;
		t.elementsContent = [this._Image3_i(),this.wave1_i(),this.wave2_i(),this.headImg1_i(),this.nameTxt1_i(),this.headMask1_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_enemybg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.wave1_i = function () {
		var t = new eui.Image();
		this.wave1 = t;
		t.anchorOffsetX = 101;
		t.anchorOffsetY = 101;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "dispelPk_json.dpk_whitecircle";
		t.x = 89;
		t.y = 87;
		return t;
	};
	_proto.wave2_i = function () {
		var t = new eui.Image();
		this.wave2 = t;
		t.anchorOffsetX = 101;
		t.anchorOffsetY = 101;
		t.scaleX = 0.5;
		t.scaleY = 0.5;
		t.source = "dispelPk_json.dpk_whitecircle";
		t.x = 89;
		t.y = 87;
		return t;
	};
	_proto.headImg1_i = function () {
		var t = new eui.Image();
		this.headImg1 = t;
		t.source = "menuover_json.headimg";
		t.x = 23;
		t.y = 21;
		return t;
	};
	_proto.nameTxt1_i = function () {
		var t = new eui.Label();
		this.nameTxt1 = t;
		t.size = 32;
		t.text = "正在匹配中（90%）...";
		t.x = 184;
		t.y = 73;
		return t;
	};
	_proto.headMask1_i = function () {
		var t = new eui.Rect();
		this.headMask1 = t;
		t.ellipseWidth = 132;
		t.height = 132;
		t.width = 132;
		t.x = 23;
		t.y = 21;
		return t;
	};
	_proto.playerGrp2_i = function () {
		var t = new eui.Group();
		this.playerGrp2 = t;
		t.x = 115;
		t.y = 725;
		t.elementsContent = [this._Image4_i(),this.headImg2_i(),this.nameTxt2_i(),this.headMask2_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_mybg";
		t.x = 91;
		t.y = 0;
		return t;
	};
	_proto.headImg2_i = function () {
		var t = new eui.Image();
		this.headImg2 = t;
		t.source = "menuover_json.headimg";
		t.x = 398.48;
		t.y = 34.2;
		return t;
	};
	_proto.nameTxt2_i = function () {
		var t = new eui.Label();
		this.nameTxt2 = t;
		t.anchorOffsetX = 0;
		t.size = 32;
		t.stroke = 2;
		t.text = "卖火柴的小女孩";
		t.textAlign = "right";
		t.width = 353;
		t.x = 0;
		t.y = 85;
		return t;
	};
	_proto.headMask2_i = function () {
		var t = new eui.Rect();
		this.headMask2 = t;
		t.ellipseWidth = 132;
		t.height = 132;
		t.width = 132;
		t.x = 398.48;
		t.y = 35;
		return t;
	};
	return PKMatchUISkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKRewardProgressItemSkin.exml'] = window.PKRewardProgressItemSkin = (function (_super) {
	__extends(PKRewardProgressItemSkin, _super);
	function PKRewardProgressItemSkin() {
		_super.call(this);
		this.skinParts = ["boxImg","stateLbl"];
		
		this.height = 215;
		this.width = 159;
		this.elementsContent = [this._Image1_i(),this.boxImg_i(),this._Image2_i(),this.stateLbl_i()];
	}
	var _proto = PKRewardProgressItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.scaleY = -1;
		t.source = "dispelPk_json.dpk_arrowtip1";
		t.touchEnabled = false;
		t.x = 69;
		t.y = 100;
		return t;
	};
	_proto.boxImg_i = function () {
		var t = new eui.Image();
		this.boxImg = t;
		t.name = "rewardBox";
		t.source = "";
		t.x = 27;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_arrowtip1";
		t.touchEnabled = false;
		t.x = 69;
		t.y = 156;
		return t;
	};
	_proto.stateLbl_i = function () {
		var t = new eui.Label();
		this.stateLbl = t;
		t.anchorOffsetX = 0;
		t.size = 28;
		t.stroke = 2;
		t.strokeColor = 0x0;
		t.text = "已完成";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 157;
		t.x = 1;
		t.y = 180;
		return t;
	};
	return PKRewardProgressItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKMenuUI.exml'] = window.PKMenuUISkin = (function (_super) {
	__extends(PKMenuUISkin, _super);
	function PKMenuUISkin() {
		_super.call(this);
		this.skinParts = ["homeBtn","addBtn","helpBtn","itemBtn1","itemBtn2","itemBtn3","itemBtn4","rewardBtn","rewardGroup","mScroller","coinTxt","ticketTxt","cntTxt0","cntTxt1","cntTxt2","cntTxt3","itemTimeTxt","toastTxt0","toastTxt1","toastTxt2","toastTxt3","ticketTimeTxt","mainGrp","itemTipGrp","raceBtn2","raceBtn1","achieve0","achieve1","achieve2","recordGroup"];
		
		this.height = 1334;
		this.width = 750;
		this.elementsContent = [this.mainGrp_i(),this.itemTipGrp_i(),this.raceBtn2_i(),this.raceBtn1_i(),this.recordGroup_i(),this._Image24_i(),this._Image25_i()];
	}
	var _proto = PKMenuUISkin.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.anchorOffsetY = 0;
		t.height = 706;
		t.x = 14;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this.homeBtn_i(),this._Image2_i(),this._Image3_i(),this._Image4_i(),this.addBtn_i(),this.helpBtn_i(),this._Image5_i(),this._Image6_i(),this.itemBtn1_i(),this.itemBtn2_i(),this.itemBtn3_i(),this.itemBtn4_i(),this._Image7_i(),this.rewardBtn_i(),this.rewardGroup_i(),this._Group2_i(),this._Label1_i(),this.coinTxt_i(),this.ticketTxt_i(),this.cntTxt0_i(),this.cntTxt1_i(),this.cntTxt2_i(),this.cntTxt3_i(),this.itemTimeTxt_i(),this.toastTxt0_i(),this.toastTxt1_i(),this.toastTxt2_i(),this.toastTxt3_i(),this.ticketTimeTxt_i(),this._Image15_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(61,16,55,6);
		t.source = "dispelPk_json.dpk_txtbg";
		t.touchEnabled = false;
		t.width = 172;
		t.x = 181;
		t.y = 39;
		return t;
	};
	_proto.homeBtn_i = function () {
		var t = new eui.Image();
		this.homeBtn = t;
		t.height = 88;
		t.source = "dispelPk_json.dpk_homebtn";
		t.width = 88;
		t.x = 18;
		t.y = 18;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(61,16,55,6);
		t.source = "dispelPk_json.dpk_txtbg";
		t.width = 150;
		t.x = 399;
		t.y = 39;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_coin";
		t.touchEnabled = false;
		t.x = 137;
		t.y = 29;
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_quan";
		t.touchEnabled = false;
		t.x = 363;
		t.y = 23;
		return t;
	};
	_proto.addBtn_i = function () {
		var t = new eui.Image();
		this.addBtn = t;
		t.source = "dispelPk_json.dpk_addbtn";
		t.touchEnabled = true;
		t.x = 508;
		t.y = 27;
		return t;
	};
	_proto.helpBtn_i = function () {
		var t = new eui.Image();
		this.helpBtn = t;
		t.source = "dispelPk_json.dpk_help";
		t.x = 593;
		t.y = 38;
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.height = 160;
		t.scale9Grid = new egret.Rectangle(23,55,8,10);
		t.source = "dispelPk_json.dpk_layerbg";
		t.touchEnabled = false;
		t.width = 690;
		t.x = 15;
		t.y = 305;
		return t;
	};
	_proto._Image6_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_item";
		t.touchEnabled = false;
		t.x = 15;
		t.y = 308;
		return t;
	};
	_proto.itemBtn1_i = function () {
		var t = new eui.Image();
		this.itemBtn1 = t;
		t.source = "dispelPk_json.dpk_pfdj";
		t.touchEnabled = true;
		t.x = 173;
		t.y = 323;
		return t;
	};
	_proto.itemBtn2_i = function () {
		var t = new eui.Image();
		this.itemBtn2 = t;
		t.source = "dispelPk_json.dpk_pmz";
		t.touchEnabled = true;
		t.x = 302;
		t.y = 323;
		return t;
	};
	_proto.itemBtn3_i = function () {
		var t = new eui.Image();
		this.itemBtn3 = t;
		t.source = "dispelPk_json.dpk_pcp";
		t.touchEnabled = true;
		t.x = 432;
		t.y = 323;
		return t;
	};
	_proto.itemBtn4_i = function () {
		var t = new eui.Image();
		this.itemBtn4 = t;
		t.source = "dispelPk_json.dpk_pbhk";
		t.touchEnabled = true;
		t.x = 560;
		t.y = 323;
		return t;
	};
	_proto._Image7_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_itemctime";
		t.x = 25;
		t.y = 384;
		return t;
	};
	_proto.rewardBtn_i = function () {
		var t = new eui.Image();
		this.rewardBtn = t;
		t.anchorOffsetX = 69;
		t.anchorOffsetY = 30;
		t.source = "dispelPk_json.dpk_creward";
		t.visible = false;
		t.x = 94;
		t.y = 411;
		return t;
	};
	_proto.rewardGroup_i = function () {
		var t = new eui.Group();
		this.rewardGroup = t;
		t.anchorOffsetX = 0;
		t.height = 241;
		t.width = 700;
		t.x = 10;
		t.y = 490;
		t.elementsContent = [this._Image8_i(),this._Image9_i(),this._Image10_i(),this._Image11_i(),this._Rect1_i(),this._Image12_i(),this._Component1_i(),this._Component2_i(),this._Component3_i(),this._Component4_i()];
		return t;
	};
	_proto._Image8_i = function () {
		var t = new eui.Image();
		t.percentHeight = 100;
		t.scale9Grid = new egret.Rectangle(23,61,4,14);
		t.source = "dispelPk_json.dpk_layerbg";
		t.touchEnabled = false;
		t.percentWidth = 100;
		return t;
	};
	_proto._Image9_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_oil";
		return t;
	};
	_proto._Image10_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_progress_bg";
		t.x = 21;
		t.y = 104;
		return t;
	};
	_proto._Image11_i = function () {
		var t = new eui.Image();
		t.name = "progress";
		t.source = "dispelPk_json.dpk_progress";
		t.x = 25;
		t.y = 108;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.fillColor = 0x888888;
		t.height = 50;
		t.name = "maskImg";
		t.width = 636;
		t.x = 25;
		t.y = 104;
		return t;
	};
	_proto._Image12_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_progress_split";
		t.x = 25;
		t.y = 107;
		return t;
	};
	_proto._Component1_i = function () {
		var t = new eui.Component();
		t.name = "reward0";
		t.skinName = "PKRewardProgressItemSkin";
		t.x = 105;
		t.y = 3;
		return t;
	};
	_proto._Component2_i = function () {
		var t = new eui.Component();
		t.name = "reward1";
		t.skinName = "PKRewardProgressItemSkin";
		t.x = 263;
		t.y = 3;
		return t;
	};
	_proto._Component3_i = function () {
		var t = new eui.Component();
		t.name = "reward2";
		t.skinName = "PKRewardProgressItemSkin";
		t.x = 421;
		t.y = 3;
		return t;
	};
	_proto._Component4_i = function () {
		var t = new eui.Component();
		t.name = "reward3";
		t.skinName = "PKRewardProgressItemSkin";
		t.x = 563;
		t.y = 3;
		return t;
	};
	_proto._Group2_i = function () {
		var t = new eui.Group();
		t.visible = false;
		t.x = 0;
		t.y = 563.5;
		t.elementsContent = [this._Image13_i(),this._Image14_i(),this.mScroller_i()];
		return t;
	};
	_proto._Image13_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_oil";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image14_i = function () {
		var t = new eui.Image();
		t.height = 480;
		t.scale9Grid = new egret.Rectangle(19,17,4,8);
		t.source = "dispelPk_json.dpk_alphabg";
		t.touchEnabled = false;
		t.width = 700;
		t.x = 10;
		t.y = 27.5;
		return t;
	};
	_proto.mScroller_i = function () {
		var t = new eui.Scroller();
		this.mScroller = t;
		t.height = 460;
		t.scaleX = 1;
		t.scaleY = 1;
		t.scrollPolicyH = "off";
		t.scrollPolicyV = "auto";
		t.width = 695;
		t.x = 20;
		t.y = 40.5;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.scaleX = 1;
		t.scaleY = 1;
		t.text = "玩法";
		t.touchEnabled = false;
		t.x = 632;
		t.y = 47;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "23503200";
		t.textAlign = "center";
		t.width = 160;
		t.x = 192;
		t.y = 45;
		return t;
	};
	_proto.ticketTxt_i = function () {
		var t = new eui.Label();
		this.ticketTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 28;
		t.text = "20/20";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 160;
		t.x = 387;
		t.y = 45;
		return t;
	};
	_proto.cntTxt0_i = function () {
		var t = new eui.Label();
		this.cntTxt0 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 26;
		t.stroke = 3;
		t.text = "20";
		t.textAlign = "right";
		t.textColor = 0xfff047;
		t.touchEnabled = false;
		t.width = 81;
		t.x = 207;
		t.y = 324;
		return t;
	};
	_proto.cntTxt1_i = function () {
		var t = new eui.Label();
		this.cntTxt1 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 26;
		t.stroke = 3;
		t.text = "20";
		t.textAlign = "right";
		t.textColor = 0xFFF047;
		t.touchEnabled = false;
		t.width = 92;
		t.x = 324;
		t.y = 324;
		return t;
	};
	_proto.cntTxt2_i = function () {
		var t = new eui.Label();
		this.cntTxt2 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 26;
		t.stroke = 3;
		t.text = "20";
		t.textAlign = "right";
		t.textColor = 0xFFF047;
		t.touchEnabled = false;
		t.width = 95;
		t.x = 452;
		t.y = 324;
		return t;
	};
	_proto.cntTxt3_i = function () {
		var t = new eui.Label();
		this.cntTxt3 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 26;
		t.stroke = 3;
		t.text = "20";
		t.textAlign = "right";
		t.textColor = 0xFFF047;
		t.touchEnabled = false;
		t.width = 97;
		t.x = 578;
		t.y = 324;
		return t;
	};
	_proto.itemTimeTxt_i = function () {
		var t = new eui.Label();
		this.itemTimeTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 28;
		t.text = "20:00";
		t.textAlign = "center";
		t.width = 139;
		t.x = 25;
		t.y = 399;
		return t;
	};
	_proto.toastTxt0_i = function () {
		var t = new eui.Label();
		this.toastTxt0 = t;
		t.bold = true;
		t.size = 52;
		t.stroke = 4;
		t.text = "+2";
		t.textColor = 0xfff047;
		t.visible = false;
		t.x = 204;
		t.y = 296;
		return t;
	};
	_proto.toastTxt1_i = function () {
		var t = new eui.Label();
		this.toastTxt1 = t;
		t.bold = true;
		t.size = 52;
		t.stroke = 4;
		t.text = "+2";
		t.textColor = 0xFFF047;
		t.visible = false;
		t.x = 334;
		t.y = 296;
		return t;
	};
	_proto.toastTxt2_i = function () {
		var t = new eui.Label();
		this.toastTxt2 = t;
		t.bold = true;
		t.size = 52;
		t.stroke = 4;
		t.text = "+2";
		t.textColor = 0xFFF047;
		t.visible = false;
		t.x = 467;
		t.y = 296;
		return t;
	};
	_proto.toastTxt3_i = function () {
		var t = new eui.Label();
		this.toastTxt3 = t;
		t.bold = true;
		t.size = 52;
		t.stroke = 4;
		t.text = "+2";
		t.textColor = 0xFFF047;
		t.visible = false;
		t.x = 595;
		t.y = 296;
		return t;
	};
	_proto.ticketTimeTxt_i = function () {
		var t = new eui.Label();
		this.ticketTimeTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 29;
		t.size = 26;
		t.stroke = 3;
		t.text = "02:00";
		t.textAlign = "center";
		t.textColor = 0x97ff73;
		t.verticalAlign = "middle";
		t.width = 84;
		t.x = 497;
		t.y = 44;
		return t;
	};
	_proto._Image15_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_menutitle";
		t.x = 129;
		t.y = 172;
		return t;
	};
	_proto.itemTipGrp_i = function () {
		var t = new eui.Group();
		this.itemTipGrp = t;
		t.anchorOffsetX = 191;
		t.anchorOffsetY = 98;
		t.visible = false;
		t.x = 261;
		t.y = 280;
		t.elementsContent = [this._Image16_i(),this._Label2_i()];
		return t;
	};
	_proto._Image16_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(70,34,15,12);
		t.source = "dispelPk_json.dpk_tipbubblebg";
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 85;
		t.lineSpacing = 10;
		t.size = 28;
		t.text = "对手棋盘喷上墨汁干扰";
		t.textAlign = "center";
		t.textColor = 0x51edff;
		t.verticalAlign = "middle";
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.raceBtn2_i = function () {
		var t = new eui.Image();
		this.raceBtn2 = t;
		t.bottom = 120;
		t.horizontalCenter = 0;
		t.source = "dispelPk_json.dpk_friendpk";
		return t;
	};
	_proto.raceBtn1_i = function () {
		var t = new eui.Image();
		this.raceBtn1 = t;
		t.bottom = 254;
		t.horizontalCenter = 0;
		t.source = "dispelPk_json.dpk_ppsbtn";
		return t;
	};
	_proto.recordGroup_i = function () {
		var t = new eui.Group();
		this.recordGroup = t;
		t.anchorOffsetX = 559;
		t.bottom = 77;
		t.scaleX = 1;
		t.visible = false;
		t.x = 632;
		t.elementsContent = [this._Image17_i(),this._Image18_i(),this._Image19_i(),this._Image20_i(),this._Image21_i(),this._Image22_i(),this._Image23_i(),this.achieve0_i(),this.achieve1_i(),this.achieve2_i()];
		return t;
	};
	_proto._Image17_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_txtbg";
		t.touchEnabled = false;
		t.x = 38;
		t.y = 28;
		return t;
	};
	_proto._Image18_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_txtbg";
		t.touchEnabled = false;
		t.x = 220;
		t.y = 28;
		return t;
	};
	_proto._Image19_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_txtbg";
		t.touchEnabled = false;
		t.x = 389;
		t.y = 28;
		return t;
	};
	_proto._Image20_i = function () {
		var t = new eui.Image();
		t.height = 100;
		t.scale9Grid = new egret.Rectangle(23,61,9,24);
		t.source = "dispelPk_json.dpk_arrowframe";
		t.touchEnabled = false;
		t.width = 559;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image21_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_shengli";
		t.touchEnabled = false;
		t.x = 30;
		t.y = 19;
		return t;
	};
	_proto._Image22_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_shibai";
		t.touchEnabled = false;
		t.x = 208;
		t.y = 16;
		return t;
	};
	_proto._Image23_i = function () {
		var t = new eui.Image();
		t.source = "dispelPk_json.dpk_shenglv";
		t.touchEnabled = false;
		t.x = 379;
		t.y = 19;
		return t;
	};
	_proto.achieve0_i = function () {
		var t = new eui.Label();
		this.achieve0 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.stroke = 2;
		t.text = "x300";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 111;
		t.x = 62;
		t.y = 34;
		return t;
	};
	_proto.achieve1_i = function () {
		var t = new eui.Label();
		this.achieve1 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.stroke = 2;
		t.text = "x300";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 111;
		t.x = 241;
		t.y = 32;
		return t;
	};
	_proto.achieve2_i = function () {
		var t = new eui.Label();
		this.achieve2 = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.scaleX = 1;
		t.scaleY = 1;
		t.stroke = 2;
		t.text = "x300";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 111;
		t.x = 409;
		t.y = 32;
		return t;
	};
	_proto._Image24_i = function () {
		var t = new eui.Image();
		t.bottom = 200;
		t.name = "friendBtn";
		t.right = 32;
		t.source = "dispelPk_json.dpk_friend";
		return t;
	};
	_proto._Image25_i = function () {
		var t = new eui.Image();
		t.bottom = 76;
		t.name = "recordBtn";
		t.right = 34;
		t.source = "dispelPk_json.dpk_zhanji";
		return t;
	};
	return PKMenuUISkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKResultUI.exml'] = window.PKResultUISkin = (function (_super) {
	__extends(PKResultUISkin, _super);
	function PKResultUISkin() {
		_super.call(this);
		this.skinParts = ["headImg1","headImg2","winnerImg","continueBtn","changeBtn","readyImg","homeBtn","maskRect1","maskRect2","rewardLabel","doubleFlag","addFriendBtn","scoreLabel","readyLabel","p1d1Txt","p1d2Txt","p1d3Txt","p1d4Txt","p1ScoreTxt","p2d1Txt","p2d2Txt","p2d3Txt","p2d4Txt","p2ScoreTxt","boxTipGroup"];
		
		this.width = 750;
		this.elementsContent = [this.headImg1_i(),this.headImg2_i(),this.winnerImg_i(),this.continueBtn_i(),this.changeBtn_i(),this.readyImg_i(),this.homeBtn_i(),this.maskRect1_i(),this.maskRect2_i(),this.rewardLabel_i(),this.doubleFlag_i(),this.addFriendBtn_i(),this.scoreLabel_i(),this.readyLabel_i(),this._Label1_i(),this._Group1_i(),this.boxTipGroup_i()];
	}
	var _proto = PKResultUISkin.prototype;

	_proto.headImg1_i = function () {
		var t = new eui.Image();
		this.headImg1 = t;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 174;
		t.y = 403;
		return t;
	};
	_proto.headImg2_i = function () {
		var t = new eui.Image();
		this.headImg2 = t;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 472;
		t.y = 404;
		return t;
	};
	_proto.winnerImg_i = function () {
		var t = new eui.Image();
		this.winnerImg = t;
		t.height = 90;
		t.source = "dispelPk_json.dpk_winner_icon";
		t.width = 90;
		t.x = 492;
		t.y = 348;
		return t;
	};
	_proto.continueBtn_i = function () {
		var t = new eui.Image();
		this.continueBtn = t;
		t.source = "dispelPk_json.dpk_btn_1";
		t.touchEnabled = true;
		t.x = 119;
		t.y = 929;
		return t;
	};
	_proto.changeBtn_i = function () {
		var t = new eui.Image();
		this.changeBtn = t;
		t.source = "dispelPk_json.dpk_btn_2";
		t.touchEnabled = true;
		t.x = 119;
		t.y = 1059;
		return t;
	};
	_proto.readyImg_i = function () {
		var t = new eui.Image();
		this.readyImg = t;
		t.anchorOffsetY = 40;
		t.source = "dispelPk_json.dpk_isready";
		t.x = 537;
		t.y = 424;
		return t;
	};
	_proto.homeBtn_i = function () {
		var t = new eui.Image();
		this.homeBtn = t;
		t.height = 88;
		t.source = "dispelPk_json.dpk_homebtn";
		t.width = 88;
		t.x = 18;
		t.y = 15;
		return t;
	};
	_proto.maskRect1_i = function () {
		var t = new eui.Rect();
		this.maskRect1 = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 180;
		t.y = 409;
		return t;
	};
	_proto.maskRect2_i = function () {
		var t = new eui.Rect();
		this.maskRect2 = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 479;
		t.y = 410;
		return t;
	};
	_proto.rewardLabel_i = function () {
		var t = new eui.Label();
		this.rewardLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 56;
		t.text = "+100金币";
		t.textAlign = "center";
		t.textColor = 0xffe548;
		t.width = 552;
		t.x = 99;
		t.y = 281;
		return t;
	};
	_proto.doubleFlag_i = function () {
		var t = new eui.Image();
		this.doubleFlag = t;
		t.source = "dispelPk_json.dpk_doubleflag";
		t.x = 500;
		t.y = 255;
		return t;
	};
	_proto.addFriendBtn_i = function () {
		var t = new eui.Image();
		this.addFriendBtn = t;
		t.source = "dispelPk_json.dpk_new_addfriend";
		t.x = 454;
		t.y = 479;
		return t;
	};
	_proto.scoreLabel_i = function () {
		var t = new eui.Label();
		this.scoreLabel = t;
		t.bold = true;
		t.size = 56;
		t.text = "1 : 0";
		t.textColor = 0xffffff;
		t.x = 319;
		t.y = 422;
		return t;
	};
	_proto.readyLabel_i = function () {
		var t = new eui.Label();
		this.readyLabel = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 36;
		t.text = "准备";
		t.textAlign = "center";
		t.textColor = 0x8d3f00;
		t.touchEnabled = false;
		t.width = 491;
		t.x = 130;
		t.y = 971;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 36;
		t.text = "更换对手";
		t.textColor = 0x1a3495;
		t.touchEnabled = false;
		t.x = 305;
		t.y = 1103;
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		t.cacheAsBitmap = true;
		t.x = 0;
		t.y = 527;
		t.elementsContent = [this._Image1_i(),this._Label2_i(),this._Rect1_i(),this._Label3_i(),this.p1d1Txt_i(),this._Label4_i(),this.p1d2Txt_i(),this._Label5_i(),this.p1d3Txt_i(),this._Label6_i(),this.p1d4Txt_i(),this._Label7_i(),this.p1ScoreTxt_i(),this._Label8_i(),this.p2d1Txt_i(),this._Label9_i(),this.p2d2Txt_i(),this._Label10_i(),this.p2d3Txt_i(),this._Label11_i(),this.p2d4Txt_i(),this._Label12_i(),this.p2ScoreTxt_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 244;
		t.scale9Grid = new egret.Rectangle(352,9,16,4);
		t.source = "dispelPk_json.dpk_bg_0";
		t.width = 750;
		t.x = 0;
		t.y = 58;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.size = 32;
		t.text = "对局详情";
		t.textColor = 0xffffff;
		t.x = 308;
		t.y = 0;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.alpha = 0.2;
		t.fillColor = 0x427ace;
		t.height = 200;
		t.strokeAlpha = 1;
		t.width = 2;
		t.x = 374;
		t.y = 79;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "连击数：";
		t.textColor = 0xffffff;
		t.x = 93;
		t.y = 80;
		return t;
	};
	_proto.p1d1Txt_i = function () {
		var t = new eui.Label();
		this.p1d1Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 202;
		t.y = 83;
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "消除得分：";
		t.textColor = 0xffffff;
		t.x = 92;
		t.y = 138;
		return t;
	};
	_proto.p1d2Txt_i = function () {
		var t = new eui.Label();
		this.p1d2Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 234;
		t.y = 141;
		return t;
	};
	_proto._Label5_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "道具：";
		t.textColor = 0xffffff;
		t.x = 92;
		t.y = 197;
		return t;
	};
	_proto.p1d3Txt_i = function () {
		var t = new eui.Label();
		this.p1d3Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 170;
		t.y = 197;
		return t;
	};
	_proto._Label6_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "额外得分：";
		t.textColor = 0xffffff;
		t.x = 92;
		t.y = 252;
		return t;
	};
	_proto.p1d4Txt_i = function () {
		var t = new eui.Label();
		this.p1d4Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 227;
		t.y = 255;
		return t;
	};
	_proto._Label7_i = function () {
		var t = new eui.Label();
		t.size = 30;
		t.text = "总得分：";
		t.textColor = 0xffffff;
		t.x = 92;
		t.y = 324;
		return t;
	};
	_proto.p1ScoreTxt_i = function () {
		var t = new eui.Label();
		this.p1ScoreTxt = t;
		t.bold = true;
		t.size = 34;
		t.text = "600";
		t.textColor = 0xffe548;
		t.x = 205;
		t.y = 322;
		return t;
	};
	_proto._Label8_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "连击数：";
		t.textColor = 0xffffff;
		t.x = 466;
		t.y = 80;
		return t;
	};
	_proto.p2d1Txt_i = function () {
		var t = new eui.Label();
		this.p2d1Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 575;
		t.y = 83;
		return t;
	};
	_proto._Label9_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "消除得分：";
		t.textColor = 0xffffff;
		t.x = 465;
		t.y = 138;
		return t;
	};
	_proto.p2d2Txt_i = function () {
		var t = new eui.Label();
		this.p2d2Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 606;
		t.y = 141;
		return t;
	};
	_proto._Label10_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "道具：";
		t.textColor = 0xffffff;
		t.x = 465;
		t.y = 197;
		return t;
	};
	_proto.p2d3Txt_i = function () {
		var t = new eui.Label();
		this.p2d3Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 546;
		t.y = 197;
		return t;
	};
	_proto._Label11_i = function () {
		var t = new eui.Label();
		t.size = 28;
		t.text = "额外得分：";
		t.textColor = 0xffffff;
		t.x = 465;
		t.y = 252;
		return t;
	};
	_proto.p2d4Txt_i = function () {
		var t = new eui.Label();
		this.p2d4Txt = t;
		t.size = 28;
		t.text = "83";
		t.textColor = 0x2ED8FF;
		t.x = 600;
		t.y = 255;
		return t;
	};
	_proto._Label12_i = function () {
		var t = new eui.Label();
		t.size = 30;
		t.text = "总得分：";
		t.textColor = 0xffffff;
		t.x = 466;
		t.y = 324;
		return t;
	};
	_proto.p2ScoreTxt_i = function () {
		var t = new eui.Label();
		this.p2ScoreTxt = t;
		t.bold = true;
		t.size = 34;
		t.text = "600";
		t.textColor = 0xffe548;
		t.x = 580;
		t.y = 322;
		return t;
	};
	_proto.boxTipGroup_i = function () {
		var t = new eui.Group();
		this.boxTipGroup = t;
		t.x = 524;
		t.y = 940;
		t.elementsContent = [this._Image2_i(),this._Image3_i(),this._Label13_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.scale9Grid = new egret.Rectangle(54,12,145,72);
		t.source = "dpk_recrewardbg_png";
		t.width = 283;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 50;
		t.anchorOffsetY = 100;
		t.name = "boxImg";
		t.source = "newbox_1_1";
		t.x = 54;
		t.y = 98;
		return t;
	};
	_proto._Label13_i = function () {
		var t = new eui.Label();
		t.anchorOffsetX = 0;
		t.height = 60;
		t.lineSpacing = 10;
		t.name = "condtionLbl";
		t.size = 24;
		t.text = "待领取";
		t.verticalAlign = "middle";
		t.x = 97;
		t.y = 19;
		return t;
	};
	return PKResultUISkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKTicketView.exml'] = window.PKTicketViewSkin = (function (_super) {
	__extends(PKTicketViewSkin, _super);
	function PKTicketViewSkin() {
		_super.call(this);
		this.skinParts = ["videoBtn","cancelTxt"];
		
		this.elementsContent = [this._Image1_i(),this.videoBtn_i(),this._Image2_i(),this._Label1_i(),this.cancelTxt_i(),this._Label2_i()];
		this._Image3_i();
		
		this.states = [
			new eui.State ("status_nohave",
				[
					new eui.AddItems("_Image3","",2,"_Label1"),
					new eui.SetProperty("videoBtn","x",290),
					new eui.SetProperty("cancelTxt","x",360.5),
					new eui.SetProperty("cancelTxt","y",451),
					new eui.SetProperty("_Label2","x",296),
					new eui.SetProperty("_Label2","text","亲爱的小主，您的入场券耗尽，需要补货啦！")
				])
			,
			new eui.State ("status_yeshave",
				[
					new eui.SetProperty("_Image1","width",660),
					new eui.SetProperty("_Image1","x",0),
					new eui.SetProperty("_Image1","y",0),
					new eui.SetProperty("videoBtn","y",223),
					new eui.SetProperty("videoBtn","x",161),
					new eui.SetProperty("_Image2","y",248),
					new eui.SetProperty("_Image2","x",414),
					new eui.SetProperty("_Label1","y",259),
					new eui.SetProperty("_Label1","x",198),
					new eui.SetProperty("cancelTxt","y",352),
					new eui.SetProperty("cancelTxt","x",232),
					new eui.SetProperty("_Label2","y",88),
					new eui.SetProperty("_Label2","text","亲爱的小主，通过观看小视频\n可以获取更多的入场券哦 "),
					new eui.SetProperty("_Label2","width",465),
					new eui.SetProperty("_Label2","x",98)
				])
		];
	}
	var _proto = PKTicketViewSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.height = 440;
		t.scale9Grid = new egret.Rectangle(31,29,61,64);
		t.source = "dispelPk_json.dpk_dlg_0";
		t.width = 517;
		t.x = 158;
		t.y = 97;
		return t;
	};
	_proto.videoBtn_i = function () {
		var t = new eui.Image();
		this.videoBtn = t;
		t.height = 114;
		t.scale9Grid = new egret.Rectangle(24,19,293,73);
		t.source = "dispelPk_json.dpk_btn_0";
		t.touchEnabled = true;
		t.width = 338;
		t.y = 324;
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		this._Image2 = t;
		t.height = 55;
		t.source = "dispelPk_json.dpk_video_0";
		t.touchEnabled = false;
		t.width = 57;
		t.x = 539;
		t.y = 349;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "dispelPk_json.dpk_figure_0";
		t.touchEnabled = false;
		t.x = 4;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		this._Label1 = t;
		t.bold = true;
		t.size = 42;
		t.text = "获取入场券";
		t.textColor = 0xffffff;
		t.touchEnabled = false;
		t.x = 323;
		t.y = 360;
		return t;
	};
	_proto.cancelTxt_i = function () {
		var t = new eui.Label();
		this.cancelTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 67;
		t.size = 30;
		t.text = "暂不需要";
		t.textAlign = "center";
		t.textColor = 0x999999;
		t.touchEnabled = true;
		t.verticalAlign = "middle";
		t.width = 197;
		t.y = 465;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 84;
		t.lineSpacing = 14;
		t.size = 34;
		t.text = "亲爱的小主，您的入场券 耗尽，需要补货啦！";
		t.textColor = 0x222222;
		t.width = 372;
		t.y = 180;
		return t;
	};
	return PKTicketViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/PKWord.exml'] = window.PKWordSkin = (function (_super) {
	__extends(PKWordSkin, _super);
	function PKWordSkin() {
		_super.call(this);
		this.skinParts = ["wordBg","wordTxt"];
		
		this.elementsContent = [this.wordBg_i(),this.wordTxt_i()];
	}
	var _proto = PKWordSkin.prototype;

	_proto.wordBg_i = function () {
		var t = new eui.Image();
		this.wordBg = t;
		t.scale9Grid = new egret.Rectangle(37,35,5,5);
		t.source = "dispelPk_json.dpk_wordbg1";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.wordTxt_i = function () {
		var t = new eui.Label();
		this.wordTxt = t;
		t.height = 100;
		t.size = 52;
		t.text = "䳹";
		t.textAlign = "center";
		t.textColor = 0x000000;
		t.verticalAlign = "middle";
		t.width = 100;
		t.x = 0;
		t.y = 0;
		return t;
	};
	return PKWordSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/RankItemRenderer.exml'] = window.RankItemRendererSkin = (function (_super) {
	__extends(RankItemRendererSkin, _super);
	function RankItemRendererSkin() {
		_super.call(this);
		this.skinParts = ["rankImg","headImg","maskRect","nameTxt","coinTxt","coinImg","rankTxt","levelTxt"];
		
		this.currentState = "level_status";
		this.width = 600;
		this.elementsContent = [this._Rect1_i(),this.rankImg_i(),this.headImg_i(),this.maskRect_i(),this.nameTxt_i(),this.rankTxt_i()];
		this.coinTxt_i();
		
		this.coinImg_i();
		
		this.levelTxt_i();
		
		this.states = [
			new eui.State ("level_status",
				[
					new eui.AddItems("levelTxt","",1,"")
				])
			,
			new eui.State ("coin_status",
				[
					new eui.AddItems("coinTxt","",2,"rankTxt"),
					new eui.AddItems("coinImg","",2,"rankTxt")
				])
		];
	}
	var _proto = RankItemRendererSkin.prototype;

	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.fillColor = 0xEED3B6;
		t.height = 1;
		t.width = 515;
		t.x = 43;
		t.y = 124;
		return t;
	};
	_proto.rankImg_i = function () {
		var t = new eui.Image();
		this.rankImg = t;
		t.source = "viewpage_json.rank_1";
		t.x = 24;
		t.y = 32;
		return t;
	};
	_proto.headImg_i = function () {
		var t = new eui.Image();
		this.headImg = t;
		t.anchorOffsetX = 45;
		t.anchorOffsetY = 45;
		t.height = 90;
		t.source = "menuover_json.headimg";
		t.width = 90;
		t.x = 137;
		t.y = 63;
		return t;
	};
	_proto.maskRect_i = function () {
		var t = new eui.Rect();
		this.maskRect = t;
		t.ellipseHeight = 78;
		t.ellipseWidth = 78;
		t.height = 78;
		t.width = 78;
		t.x = 98;
		t.y = 24;
		return t;
	};
	_proto.nameTxt_i = function () {
		var t = new eui.Label();
		this.nameTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.height = 40;
		t.maxChars = 6;
		t.multiline = false;
		t.text = "18516465685";
		t.textColor = 0x74411C;
		t.width = 186;
		t.x = 198;
		t.y = 48;
		return t;
	};
	_proto.coinTxt_i = function () {
		var t = new eui.Label();
		this.coinTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.text = "10000";
		t.textAlign = "right";
		t.textColor = 0xf39c3e;
		t.width = 174;
		t.x = 350;
		t.y = 48;
		return t;
	};
	_proto.coinImg_i = function () {
		var t = new eui.Image();
		this.coinImg = t;
		t.height = 38;
		t.source = "menuover_json.coin";
		t.width = 38;
		t.x = 535;
		t.y = 40;
		return t;
	};
	_proto.rankTxt_i = function () {
		var t = new eui.Label();
		this.rankTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 76;
		t.size = 40;
		t.text = "9999";
		t.textAlign = "center";
		t.textColor = 0xe0a650;
		t.verticalAlign = "middle";
		t.width = 105;
		t.x = 0;
		t.y = 25;
		return t;
	};
	_proto.levelTxt_i = function () {
		var t = new eui.Label();
		this.levelTxt = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.text = "第250关";
		t.textAlign = "right";
		t.textColor = 0xf9703b;
		t.width = 221;
		t.x = 350;
		t.y = 48;
		return t;
	};
	return RankItemRendererSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/RankViewSkin.exml'] = window.RankViewSkin = (function (_super) {
	__extends(RankViewSkin, _super);
	function RankViewSkin() {
		_super.call(this);
		this.skinParts = ["tabBtn2","tabBtn1","tabLabel1","tabLabel2","normalGrp","guessGrp","closeBtn","mainGrp","scroller"];
		
		this.currentState = "level_status";
		this.elementsContent = [this.mainGrp_i(),this.scroller_i(),this._Rect3_i()];
		this._Rect2_i();
		
		this.normalGrp_i();
		
		this.guessGrp_i();
		
		this._Label3_i();
		
		this.states = [
			new eui.State ("level_status",
				[
					new eui.AddItems("_Rect2","mainGrp",2,"tabBtn2"),
					new eui.AddItems("normalGrp","mainGrp",2,"closeBtn"),
					new eui.AddItems("guessGrp","mainGrp",2,"closeBtn"),
					new eui.SetProperty("tabBtn2","strokeWeight",2),
					new eui.SetProperty("tabBtn2","fillAlpha",0),
					new eui.SetProperty("tabBtn2","strokeColor",0xe0a650),
					new eui.SetProperty("tabBtn2","x",353),
					new eui.SetProperty("tabBtn2","y",30.99),
					new eui.SetProperty("tabBtn2","width",298),
					new eui.SetProperty("tabBtn1","y",30.99),
					new eui.SetProperty("tabBtn1","fillColor",0xefa74f),
					new eui.SetProperty("tabBtn1","width",298),
					new eui.SetProperty("tabLabel1","width",298),
					new eui.SetProperty("tabLabel2","x",355),
					new eui.SetProperty("tabLabel2","y",30.99),
					new eui.SetProperty("tabLabel2","textColor",0x8f5007),
					new eui.SetProperty("tabLabel2","width",298),
					new eui.SetProperty("scroller","y",197),
					new eui.SetProperty("scroller","height",580),
					new eui.SetProperty("_Rect3","x",36),
					new eui.SetProperty("_Rect3","width",632),
					new eui.SetProperty("_Rect3","y",777),
					new eui.SetProperty("_Rect3","height",125)
				])
			,
			new eui.State ("money_status",
				[
					new eui.AddItems("_Label3","mainGrp",1,""),
					new eui.SetProperty("tabBtn2","x",353),
					new eui.SetProperty("tabBtn2","y",30.99),
					new eui.SetProperty("tabBtn2","fillColor",0xefa74f),
					new eui.SetProperty("tabBtn2","width",298),
					new eui.SetProperty("tabBtn1","x",55),
					new eui.SetProperty("tabBtn1","y",30.99),
					new eui.SetProperty("tabBtn1","strokeWeight",2),
					new eui.SetProperty("tabBtn1","strokeColor",0xe0a650),
					new eui.SetProperty("tabBtn1","fillAlpha",0),
					new eui.SetProperty("tabBtn1","width",298),
					new eui.SetProperty("tabLabel1","y",30.99),
					new eui.SetProperty("tabLabel1","x",55),
					new eui.SetProperty("tabLabel1","anchorOffsetX",0),
					new eui.SetProperty("tabLabel1","anchorOffsetY",0),
					new eui.SetProperty("tabLabel1","height",66),
					new eui.SetProperty("tabLabel1","verticalAlign","middle"),
					new eui.SetProperty("tabLabel1","width",298),
					new eui.SetProperty("tabLabel1","textColor",0x8f5007),
					new eui.SetProperty("tabLabel2","y",30.99),
					new eui.SetProperty("tabLabel2","x",353),
					new eui.SetProperty("tabLabel2","anchorOffsetX",0),
					new eui.SetProperty("tabLabel2","anchorOffsetY",0),
					new eui.SetProperty("tabLabel2","height",66),
					new eui.SetProperty("tabLabel2","verticalAlign","middle"),
					new eui.SetProperty("tabLabel2","width",298),
					new eui.SetProperty("closeBtn","touchEnabled",true),
					new eui.SetProperty("_Label3","text","亲，财富排行数据每周日0点更新哦~"),
					new eui.SetProperty("scroller","y",114),
					new eui.SetProperty("scroller","height",666),
					new eui.SetProperty("scroller","scrollPolicyH","off"),
					new eui.SetProperty("scroller","scrollPolicyV","auto"),
					new eui.SetProperty("scroller","anchorOffsetY",0),
					new eui.SetProperty("_Rect3","y",777),
					new eui.SetProperty("_Rect3","height",125)
				])
		];
	}
	var _proto = RankViewSkin.prototype;

	_proto.mainGrp_i = function () {
		var t = new eui.Group();
		this.mainGrp = t;
		t.x = 0;
		t.y = 0;
		t.elementsContent = [this._Image1_i(),this._Rect1_i(),this.tabBtn2_i(),this.tabBtn1_i(),this.tabLabel1_i(),this.tabLabel2_i(),this.closeBtn_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 920;
		t.scale9Grid = new egret.Rectangle(32,30,3,4);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 32;
		t.y = 30;
		return t;
	};
	_proto._Rect1_i = function () {
		var t = new eui.Rect();
		t.ellipseWidth = 53;
		t.fillColor = 0xffd983;
		t.height = 100;
		t.width = 638;
		t.x = 33;
		t.y = 11.05;
		return t;
	};
	_proto._Rect2_i = function () {
		var t = new eui.Rect();
		this._Rect2 = t;
		t.fillColor = 0xffd983;
		t.height = 100;
		t.width = 631;
		t.x = 37;
		t.y = 80;
		return t;
	};
	_proto.tabBtn2_i = function () {
		var t = new eui.Rect();
		this.tabBtn2 = t;
		t.ellipseHeight = 16;
		t.ellipseWidth = 16;
		t.fillColor = 0xE0A650;
		t.height = 66;
		t.width = 300;
		t.x = 349;
		t.y = 30.99;
		return t;
	};
	_proto.tabBtn1_i = function () {
		var t = new eui.Rect();
		this.tabBtn1 = t;
		t.ellipseHeight = 16;
		t.ellipseWidth = 16;
		t.fillColor = 0xe0a650;
		t.height = 66;
		t.width = 300;
		t.x = 55;
		t.y = 30.99;
		return t;
	};
	_proto.tabLabel1_i = function () {
		var t = new eui.Label();
		this.tabLabel1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 66;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 30;
		t.text = "通关排行";
		t.textAlign = "center";
		t.textColor = 0xfef9e3;
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 300;
		t.x = 55;
		t.y = 30.99;
		return t;
	};
	_proto.tabLabel2_i = function () {
		var t = new eui.Label();
		this.tabLabel2 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 66;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 30;
		t.text = "财富排行";
		t.textAlign = "center";
		t.textColor = 0xfef9e3;
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.width = 300;
		t.x = 349;
		t.y = 30.99;
		return t;
	};
	_proto.normalGrp_i = function () {
		var t = new eui.Group();
		this.normalGrp = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 56;
		t.y = 106;
		t.elementsContent = [this._Image2_i(),this._Label1_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(96,35,9,28);
		t.source = "viewpage_json.mail_cur_tab_bg";
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.text = "成语接龙";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.width = 294;
		t.x = 0;
		t.y = 24;
		return t;
	};
	_proto.guessGrp_i = function () {
		var t = new eui.Group();
		this.guessGrp = t;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 349.48;
		t.y = 106;
		t.elementsContent = [this._Image3_i(),this._Label2_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(96,35,9,28);
		t.scaleX = 1;
		t.scaleY = 1;
		t.source = "viewpage_json.mail_cur_tab_bg";
		t.width = 300;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.text = "看图猜";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.width = 294;
		t.x = 0;
		t.y = 24;
		return t;
	};
	_proto.closeBtn_i = function () {
		var t = new eui.Image();
		this.closeBtn = t;
		t.source = "viewpage_json.closebtn";
		t.x = 613.06;
		t.y = -16;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.size = 22;
		t.text = "亲，财富排行数据每周一0点更新哦~";
		t.textAlign = "center";
		t.textColor = 0xab660d;
		t.touchEnabled = false;
		t.width = 703;
		t.x = 0;
		t.y = 912;
		return t;
	};
	_proto.scroller_i = function () {
		var t = new eui.Scroller();
		this.scroller = t;
		t.height = 616;
		t.touchEnabled = false;
		t.width = 600;
		t.x = 52;
		t.y = 184;
		t.viewport = this._Group1_i();
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		return t;
	};
	_proto._Rect3_i = function () {
		var t = new eui.Rect();
		this._Rect3 = t;
		t.fillColor = 0xffe6ad;
		t.height = 118;
		t.width = 631;
		t.x = 36;
		t.y = 793;
		return t;
	};
	return RankViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/RedBagViewSkin.exml'] = window.RedBagViewSkin = (function (_super) {
	__extends(RedBagViewSkin, _super);
	function RedBagViewSkin() {
		_super.call(this);
		this.skinParts = ["lightImg1","lightImg2","moneyLbl"];
		
		this.currentState = "open";
		this.width = 560;
		this.elementsContent = [this.lightImg1_i(),this.lightImg2_i(),this._Image1_i(),this._Group1_i(),this._Group3_i()];
		this.states = [
			new eui.State ("open",
				[
					new eui.SetProperty("_Group1","visible",true)
				])
			,
			new eui.State ("opened",
				[
					new eui.SetProperty("_Image1","source","newredeff_json.new_redbag1"),
					new eui.SetProperty("_Group1","visible",false),
					new eui.SetProperty("_Label2","x",148),
					new eui.SetProperty("_Label2","y",204),
					new eui.SetProperty("_Label3","bold",true),
					new eui.SetProperty("_Label4","bold",true),
					new eui.SetProperty("_Label4","size",38),
					new eui.SetProperty("_Group3","visible",true)
				])
		];
	}
	var _proto = RedBagViewSkin.prototype;

	_proto.lightImg1_i = function () {
		var t = new eui.Image();
		this.lightImg1 = t;
		t.anchorOffsetX = 213.5;
		t.anchorOffsetY = 193;
		t.scaleX = 0;
		t.scaleY = 0;
		t.source = "newredeff_json.new_lighteff";
		t.x = 280;
		t.y = 374;
		return t;
	};
	_proto.lightImg2_i = function () {
		var t = new eui.Image();
		this.lightImg2 = t;
		t.anchorOffsetX = 213.5;
		t.anchorOffsetY = 193;
		t.rotation = 180;
		t.scaleX = 0;
		t.scaleY = 0;
		t.source = "newredeff_json.new_lighteff";
		t.x = 280;
		t.y = 374;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		this._Image1 = t;
		t.source = "newredeff_json.new_redbag";
		return t;
	};
	_proto._Group1_i = function () {
		var t = new eui.Group();
		this._Group1 = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.height = 81;
		t.name = "closeBtn";
		t.touchChildren = false;
		t.width = 94;
		t.x = 472;
		t.y = -2;
		t.elementsContent = [this._Image2_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.source = "newredeff_json.new_redbag_close";
		t.x = 47;
		t.y = 22;
		return t;
	};
	_proto._Group3_i = function () {
		var t = new eui.Group();
		this._Group3 = t;
		t.visible = false;
		t.elementsContent = [this._Label1_i(),this.moneyLbl_i(),this._Label2_i(),this._Label3_i(),this._Group2_i()];
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 36;
		t.text = "恭喜获得现金";
		t.textColor = 0x8A4758;
		t.x = 173;
		t.y = 109;
		return t;
	};
	_proto.moneyLbl_i = function () {
		var t = new eui.Label();
		this.moneyLbl = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 80;
		t.text = "88.88";
		t.textAlign = "center";
		t.textColor = 0xF65049;
		t.width = 300;
		t.x = 147;
		t.y = 187;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		this._Label2 = t;
		t.bold = true;
		t.size = 48;
		t.text = "￥";
		t.textColor = 0xF65049;
		t.x = 143;
		t.y = 209;
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		this._Label3 = t;
		t.size = 30;
		t.text = "待存入现金账户";
		t.textColor = 0xFEE1B0;
		t.x = 177;
		t.y = 456;
		return t;
	};
	_proto._Group2_i = function () {
		var t = new eui.Group();
		t.name = "acceptBtn";
		t.touchChildren = false;
		t.x = 45;
		t.y = 534;
		t.elementsContent = [this._Image3_i(),this._Label4_i()];
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		t.source = "newredeff_json.new_redbag_collectbg";
		return t;
	};
	_proto._Label4_i = function () {
		var t = new eui.Label();
		this._Label4 = t;
		t.text = "收下";
		t.textColor = 0xF0493B;
		t.x = 199;
		t.y = 33;
		return t;
	};
	return RedBagViewSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/RobotITipItem.exml'] = window.RobotITipItemSkin = (function (_super) {
	__extends(RobotITipItemSkin, _super);
	function RobotITipItemSkin() {
		_super.call(this);
		this.skinParts = ["tipTxt","goStartBtn"];
		
		this.elementsContent = [this._Image1_i(),this.tipTxt_i(),this.goStartBtn_i(),this._Label1_i()];
	}
	var _proto = RobotITipItemSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.robotbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.tipTxt_i = function () {
		var t = new eui.Label();
		this.tipTxt = t;
		t.anchorOffsetY = 0;
		t.height = 120;
		t.lineSpacing = 10;
		t.size = 24;
		t.text = "小主，闯过成语接龙第2005关就可以升级新房子啦！";
		t.textColor = 0x914e00;
		t.width = 250;
		t.x = 61;
		t.y = 27;
		return t;
	};
	_proto.goStartBtn_i = function () {
		var t = new eui.Image();
		this.goStartBtn = t;
		t.height = 50;
		t.source = "viewpage_json.btnget";
		t.touchEnabled = true;
		t.width = 140;
		t.x = 166;
		t.y = 102;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 26;
		t.text = "前往";
		t.textAlign = "center";
		t.touchEnabled = false;
		t.width = 144;
		t.x = 166;
		t.y = 114;
		return t;
	};
	return RobotITipItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/SignItem.exml'] = window.SignItemSkin = (function (_super) {
	__extends(SignItemSkin, _super);
	function SignItemSkin() {
		_super.call(this);
		this.skinParts = ["cointTxt","signImg","timeTxt","boxGrp"];
		
		this.width = 70;
		this.elementsContent = [this.cointTxt_i(),this.signImg_i(),this.timeTxt_i(),this.boxGrp_i()];
	}
	var _proto = SignItemSkin.prototype;

	_proto.cointTxt_i = function () {
		var t = new eui.Label();
		this.cointTxt = t;
		t.bold = true;
		t.size = 22;
		t.text = "+50";
		t.textAlign = "center";
		t.textColor = 0xF8673B;
		t.width = 62;
		t.x = 4;
		t.y = 11;
		return t;
	};
	_proto.signImg_i = function () {
		var t = new eui.Image();
		this.signImg = t;
		t.anchorOffsetX = 30;
		t.anchorOffsetY = 30;
		t.height = 60;
		t.source = "viewpage_json.videoimg";
		t.width = 60;
		t.x = 35;
		t.y = 76;
		return t;
	};
	_proto.timeTxt_i = function () {
		var t = new eui.Label();
		this.timeTxt = t;
		t.bold = true;
		t.size = 24;
		t.text = "3天";
		t.textAlign = "center";
		t.textColor = 0x985300;
		t.width = 62;
		t.x = 4;
		t.y = 121;
		return t;
	};
	_proto.boxGrp_i = function () {
		var t = new eui.Group();
		this.boxGrp = t;
		t.x = 2;
		t.y = 2;
		t.elementsContent = [this._Image1_i(),this._Label1_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.fontbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 20;
		t.text = "宝箱";
		t.x = 13;
		t.y = 6;
		return t;
	};
	return SignItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/SoundDialog.exml'] = window.SoundDialogSkin = (function (_super) {
	__extends(SoundDialogSkin, _super);
	function SoundDialogSkin() {
		_super.call(this);
		this.skinParts = ["radioBtn1","radioBtn2"];
		
		this.elementsContent = [this._Image1_i(),this.radioBtn1_i(),this.radioBtn2_i(),this._Label1_i(),this._Label2_i()];
	}
	var _proto = SoundDialogSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.soundbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.radioBtn1_i = function () {
		var t = new eui.ToggleSwitch();
		this.radioBtn1 = t;
		t.label = "ToggleButton";
		t.x = 145;
		t.y = 35;
		return t;
	};
	_proto.radioBtn2_i = function () {
		var t = new eui.ToggleSwitch();
		this.radioBtn2 = t;
		t.label = "ToggleButton";
		t.x = 145;
		t.y = 104;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "背景音效";
		t.textColor = 0x5c7177;
		t.x = 26;
		t.y = 43;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 28;
		t.text = "游戏音效";
		t.textColor = 0x5C7177;
		t.x = 26;
		t.y = 112;
		return t;
	};
	return SoundDialogSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/StartItem.exml'] = window.StartItemSkin = (function (_super) {
	__extends(StartItemSkin, _super);
	function StartItemSkin() {
		_super.call(this);
		this.skinParts = ["lockTxt1","startBtn","lifeImg","startGrp","lockTxt2","cashGrp","videoBtn","btnLvlUp"];
		
		this.elementsContent = [this.lockTxt1_i(),this.startGrp_i(),this.cashGrp_i(),this.btnLvlUp_i()];
	}
	var _proto = StartItemSkin.prototype;

	_proto.lockTxt1_i = function () {
		var t = new eui.Label();
		this.lockTxt1 = t;
		t.fontFamily = "Arial";
		t.text = "还差2关解锁新房子";
		t.textAlign = "center";
		t.textColor = 0x925e2e;
		t.width = 400;
		t.x = 0;
		t.y = 56;
		return t;
	};
	_proto.startGrp_i = function () {
		var t = new eui.Group();
		this.startGrp = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.x = 73;
		t.y = 106;
		t.elementsContent = [this.startBtn_i(),this._Label1_i(),this.lifeImg_i()];
		return t;
	};
	_proto.startBtn_i = function () {
		var t = new eui.Image();
		this.startBtn = t;
		t.anchorOffsetX = 166;
		t.anchorOffsetY = 66;
		t.touchEnabled = true;
		t.x = 166;
		t.y = 66;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 52;
		t.text = "开始";
		t.touchEnabled = false;
		t.x = 89;
		t.y = 38;
		return t;
	};
	_proto.lifeImg_i = function () {
		var t = new eui.Image();
		this.lifeImg = t;
		t.source = "menuover_json.lifeA";
		t.touchEnabled = false;
		t.x = 206;
		t.y = 36;
		return t;
	};
	_proto.cashGrp_i = function () {
		var t = new eui.Group();
		this.cashGrp = t;
		t.x = 28;
		t.y = 241;
		t.elementsContent = [this._Image1_i(),this.lockTxt2_i()];
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.tipsbg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.lockTxt2_i = function () {
		var t = new eui.Label();
		this.lockTxt2 = t;
		t.fontFamily = "Arial";
		t.size = 24;
		t.text = "距离10000提现额度还差200";
		t.textAlign = "center";
		t.textColor = 0xd57d2f;
		t.width = 344;
		t.x = 0;
		t.y = 26;
		return t;
	};
	_proto.btnLvlUp_i = function () {
		var t = new eui.Group();
		this.btnLvlUp = t;
		t.anchorOffsetX = 160;
		t.anchorOffsetY = 49;
		t.touchChildren = false;
		t.touchEnabled = true;
		t.x = 192;
		t.y = 47;
		t.elementsContent = [this._Image2_i(),this._Label2_i(),this.videoBtn_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.anchorOffsetX = 0;
		t.scale9Grid = new egret.Rectangle(159,20,14,50);
		t.scaleX = -1;
		t.source = "menuover_json.levelup";
		t.touchEnabled = false;
		t.width = 337;
		t.x = 337;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.fontFamily = "Arial";
		t.size = 36;
		t.text = "升级";
		t.touchEnabled = false;
		t.x = 124;
		t.y = 31;
		return t;
	};
	_proto.videoBtn_i = function () {
		var t = new eui.Image();
		this.videoBtn = t;
		t.source = "guessgame_json.video4";
		t.visible = false;
		t.x = 72;
		t.y = 29;
		return t;
	};
	return StartItemSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/tip/IconBtnTipSkin.exml'] = window.IconBtnTipSkin = (function (_super) {
	__extends(IconBtnTipSkin, _super);
	function IconBtnTipSkin() {
		_super.call(this);
		this.skinParts = ["tipTxt"];
		
		this.height = 127;
		this.width = 251;
		this.elementsContent = [this._Image1_i(),this.tipTxt_i()];
	}
	var _proto = IconBtnTipSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.scale9Grid = new egret.Rectangle(33,21,129,72);
		t.source = "menuover_json.icontipbg";
		return t;
	};
	_proto.tipTxt_i = function () {
		var t = new eui.Label();
		this.tipTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 54;
		t.lineSpacing = 4;
		t.size = 24;
		t.text = "生词本\n搬到这了哦";
		t.textColor = 0xc36d13;
		t.width = 159;
		t.x = 38;
		t.y = 34;
		return t;
	};
	return IconBtnTipSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/tip/InvitePKTip.exml'] = window.InvitePKTipSkin = (function (_super) {
	__extends(InvitePKTipSkin, _super);
	function InvitePKTipSkin() {
		_super.call(this);
		this.skinParts = ["agreeBtn","ignoreBtn","downcountLbl","inviteTxt"];
		
		this.elementsContent = [this._Image1_i(),this.agreeBtn_i(),this.ignoreBtn_i(),this.downcountLbl_i(),this.inviteTxt_i()];
	}
	var _proto = InvitePKTipSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.height = 128;
		t.scale9Grid = new egret.Rectangle(33,30,4,6);
		t.source = "menuover_json.mo_thebg";
		t.width = 730;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto.agreeBtn_i = function () {
		var t = new eui.Image();
		this.agreeBtn = t;
		t.source = "menuover_json.mo_agree";
		t.x = 569;
		t.y = 31;
		return t;
	};
	_proto.ignoreBtn_i = function () {
		var t = new eui.Image();
		this.ignoreBtn = t;
		t.source = "menuover_json.mo_hulve";
		t.x = 462;
		t.y = 31;
		return t;
	};
	_proto.downcountLbl_i = function () {
		var t = new eui.Label();
		this.downcountLbl = t;
		t.anchorOffsetX = 0;
		t.bold = true;
		t.size = 32;
		t.text = "10s";
		t.textAlign = "center";
		t.textColor = 0x006E1A;
		t.width = 59;
		t.x = 652;
		t.y = 48;
		return t;
	};
	_proto.inviteTxt_i = function () {
		var t = new eui.Label();
		this.inviteTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.bold = true;
		t.height = 61;
		t.text = "你的好友邀请你一起玩消成语";
		t.textColor = 0x925e2e;
		t.verticalAlign = "middle";
		t.width = 445;
		t.x = 17;
		t.y = 35;
		return t;
	};
	return InvitePKTipSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/TreeGetDialog.exml'] = window.TreeGetDialogSkin = (function (_super) {
	__extends(TreeGetDialogSkin, _super);
	function TreeGetDialogSkin() {
		_super.call(this);
		this.skinParts = ["checkBoxGroup","getBtn1","getBtn2","leftTxt"];
		
		this.elementsContent = [this._Image1_i(),this.checkBoxGroup_i(),this.getBtn1_i(),this.getBtn2_i(),this.leftTxt_i()];
		this.states = [
			new eui.State ("mul",
				[
					new eui.SetProperty("_Image3","visible",true),
					new eui.SetProperty("getBtn1","visible",true)
				])
			,
			new eui.State ("normal",
				[
					new eui.SetProperty("getBtn2","visible",true)
				])
		];
	}
	var _proto = TreeGetDialogSkin.prototype;

	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.dtreebg";
		return t;
	};
	_proto.checkBoxGroup_i = function () {
		var t = new eui.Group();
		this.checkBoxGroup = t;
		t.touchChildren = false;
		t.x = 119;
		t.y = 158;
		t.elementsContent = [this._Image2_i(),this._Image3_i(),this._Label1_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 36;
		t.source = "dpk_checkboxbg_png";
		t.width = 36;
		return t;
	};
	_proto._Image3_i = function () {
		var t = new eui.Image();
		this._Image3 = t;
		t.source = "dpk_checkbox_png";
		t.visible = false;
		t.x = 1;
		t.y = 4;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.size = 24;
		t.text = "多倍领取";
		t.textColor = 0xB7B7B7;
		t.x = 44;
		t.y = 5;
		return t;
	};
	_proto.getBtn1_i = function () {
		var t = new eui.Group();
		this.getBtn1 = t;
		t.touchChildren = false;
		t.visible = false;
		t.x = 51;
		t.y = 23;
		t.elementsContent = [this._Image4_i(),this._Label2_i()];
		return t;
	};
	_proto._Image4_i = function () {
		var t = new eui.Image();
		t.source = "menuover_json.tdbget";
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 34;
		t.text = "多倍领取 (2~5倍）";
		t.x = 11;
		t.y = 29;
		return t;
	};
	_proto.getBtn2_i = function () {
		var t = new eui.Group();
		this.getBtn2 = t;
		t.touchChildren = false;
		t.visible = false;
		t.x = 51;
		t.y = 23;
		t.elementsContent = [this._Image5_i(),this._Label3_i()];
		return t;
	};
	_proto._Image5_i = function () {
		var t = new eui.Image();
		t.source = "dpk_greenbtnbg_png";
		return t;
	};
	_proto._Label3_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.size = 34;
		t.text = "普通领取";
		t.textColor = 0xffffff;
		t.x = 77;
		t.y = 29;
		return t;
	};
	_proto.leftTxt_i = function () {
		var t = new eui.Label();
		this.leftTxt = t;
		t.size = 22;
		t.text = "今日剩余领取次数：5";
		t.textColor = 0x666666;
		t.x = 51;
		t.y = 210;
		return t;
	};
	return TreeGetDialogSkin;
})(eui.Skin);generateEUI.paths['resource/game_skins/UpperLimit.exml'] = window.UpperLimitSkin = (function (_super) {
	__extends(UpperLimitSkin, _super);
	function UpperLimitSkin() {
		_super.call(this);
		this.skinParts = ["viewbg","descTxt","btnConfirm"];
		
		this.elementsContent = [this.viewbg_i(),this._Image1_i(),this._Label1_i(),this.descTxt_i(),this.btnConfirm_i()];
	}
	var _proto = UpperLimitSkin.prototype;

	_proto.viewbg_i = function () {
		var t = new eui.Image();
		this.viewbg = t;
		t.anchorOffsetY = 0;
		t.height = 420;
		t.scale9Grid = new egret.Rectangle(34,34,3,5);
		t.source = "viewpage_json.viewbg";
		t.width = 640;
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Image1_i = function () {
		var t = new eui.Image();
		t.source = "viewpage_json.common_title_bg";
		t.x = 0;
		t.y = 0;
		return t;
	};
	_proto._Label1_i = function () {
		var t = new eui.Label();
		t.bold = true;
		t.height = 55;
		t.scaleX = 1;
		t.scaleY = 1;
		t.size = 40;
		t.stroke = 3;
		t.strokeColor = 0xF9E9B5;
		t.text = "温馨提示";
		t.textAlign = "center";
		t.textColor = 0x8F5007;
		t.verticalAlign = "middle";
		t.x = 238;
		t.y = 29;
		return t;
	};
	_proto.descTxt_i = function () {
		var t = new eui.Label();
		this.descTxt = t;
		t.anchorOffsetX = 0;
		t.anchorOffsetY = 0;
		t.horizontalCenter = 1;
		t.lineSpacing = 14;
		t.size = 30;
		t.text = "适度游戏，今天已经玩了50关了，快去写作业吧~";
		t.textAlign = "center";
		t.textColor = 0x8f5007;
		t.width = 460;
		t.y = 163;
		return t;
	};
	_proto.btnConfirm_i = function () {
		var t = new eui.Group();
		this.btnConfirm = t;
		t.x = 160;
		t.y = 289;
		t.elementsContent = [this._Image2_i(),this._Label2_i()];
		return t;
	};
	_proto._Image2_i = function () {
		var t = new eui.Image();
		t.height = 90;
		t.horizontalCenter = 0;
		t.scale9Grid = new egret.Rectangle(30,28,275,47);
		t.source = "viewpage_json.commonbtn";
		t.touchEnabled = true;
		t.width = 320;
		t.y = 0;
		return t;
	};
	_proto._Label2_i = function () {
		var t = new eui.Label();
		t.height = 90;
		t.size = 34;
		t.text = "确定";
		t.touchEnabled = false;
		t.verticalAlign = "middle";
		t.x = 132;
		t.y = 0;
		return t;
	};
	return UpperLimitSkin;
})(eui.Skin);