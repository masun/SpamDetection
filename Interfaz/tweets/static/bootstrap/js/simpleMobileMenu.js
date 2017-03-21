!function(n){

	n.fn.smplmnu=function(o){

	var s=n.extend({background:"#222",speed:"0.5s",textColor:"#fff"},o)
		,r=n(this),
		l=r.next("ul"),
		e=(r.next("ul li a"),'<div class="overally"></div>');

	return  r.addClass("inrwrpr"),
			l.addClass("inrwrpr"),
		n(".inrwrpr").wrapAll("<div class='navwrp'>"),
	l.prepend('<a href="javascript:void(0)" class="mnuclose ion-close-round"><span>X</span></a>'),
	n("body").prepend(e),
	r.click(function(o){
	r.next("ul").addClass("mobimenu")
	,n(".mobimenu").addClass("mnuopn")
	,n(".mnuopn").css({
	"z-index":"9999","background-color":
	s.background,transition:s.speed})
	,n(".mnuopn a").css({color:s.textColor}),
	n(".overally").addClass("ovrActv")}),
	n(".mnuclose").click(function(o){
		r.next("ul").removeClass("mnuopn"),
		n(".overally").removeClass("ovrActv")}),
	n(".overally").click(function(o){
		l.removeClass("mnuopn"),
		n(this).removeClass("ovrActv")}),
	this
	}

}(jQuery);