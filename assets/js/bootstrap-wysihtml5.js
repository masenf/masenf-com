!function($, wysi) {
	"use strict"
	
	var templates = {
		"font-styles": "<li class='dropdown'>" +
							"<a class='btn dropdown-toggle' data-toggle='dropdown' href='#'>" +
								"<i class='icon-font'></i>&nbsp;<span class='current-font'>Normal text</span>&nbsp;<b class='caret'></b>" +
							"</a>" +
						    "<ul class='dropdown-menu'>" +
						      	"<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='div'>Normal text</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h1'>Heading 1</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h2'>Heading 2</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h3'>Heading 3</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h4'>Heading 4</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h5'>Heading 5</a></li>" +
					            "<li><a data-wysihtml5-command='formatBlock' data-wysihtml5-command-value='h6'>Heading 6</a></li>" +
						    "</ul>" +
						"</li>",
		"emphasis":     "<li>" +
							"<div class='btn-group'>" +		
							    "<a class='btn' data-wysihtml5-command='bold' title='CTRL+B'>Bold</a>" +
							    "<a class='btn' data-wysihtml5-command='italic' title='CTRL+I'>Italic</a>" +
							"</div>" +
						"</li>",
		"lists": 		"<li>" +
							"<div class='btn-group'>" +
						    	"<a class='btn' data-wysihtml5-command='insertUnorderedList'><i class='icon-list'></i></a>" +
							    "<a class='btn' data-wysihtml5-command='insertOrderedList'><i class='icon-th-list'></i></a>" +		
							"</div>" +
						"</li>",
        "misc":         "<li>" +
                            "<div class='btn-group'>" +
                                "<a class='btn' data-wysihtml5-action='change_view' data-toggle='button'>source</a>" +
                            "</div>" +
                        "</li>"
	};
	
	var defaultOptions = {
		"font-styles": true,
		"emphasis": true,
		"lists": true,
        "misc": true
	};

	var parserRules = {
        classes: {
            "white_rounded":1,
            "well":1,
            "row":1,
            "label":1,
            "label-success":1,
            "label-important":1,
            "label-warning":1,
            "label-info":1,
            "label-inverse":1,
            "span1":1,
            "span2":1,
            "span3":1,
            "span4":1,
            "span5":1,
            "span6":1,
            "span7":1,
            "span8":1,
            "span9":1,
            "span10":1,
            "span11":1,
            "span12":1,
            "inline":1,
            "pointer":1,
            "float-right":1,
            "float-left":1 },
		tags: {
			b:  {},
			i:  {},
			br: {},
			ol: {},
			ul: {},
			li: {},
			h1: {},
			h2: {},
			h3: {},
			h4: {},
			h5: {},
			h6: {},
            p: {},
            pre: {},
            center: {},
            div: {},
            iframe: {
                "check_attributes": {
                    "src":"url",
                    "width":"numbers",
                    "height":"numbers"                
                },
                "set_attributes":{
                    "frameborder":"0",             
                }
            },
            img: {
                "check_attributes": {
                    "width": "numbers",
                    "alt": "alt",
                    "src": "text",
                    "height": "numbers"
                }
            },
			a:  {
				set_attributes: {
					target: "_blank",
					rel:    "nofollow"
				},
				check_attributes: {
					href:   "url" // important to avoid XSS
				}
			}
		}
	};

	var Wysihtml5 = function(el, options) {
		this.el = el;
		this.toolbar = this.createToolbar(el, options || defaultOptions);
		this.editor =  new wysi.Editor(this.el.attr('id'), {
    		toolbar: this.toolbar.attr('id'),
		    parserRules: parserRules,
            stylesheets: ['/css/bootstrap.css','/css/bootstrap-responsive.css','/css/masenf.css']
  		});
  		
  		$('iframe.wysihtml5-sandbox').each(function(i, el){
			$(el.contentWindow).off('focus.wysihtml5').on({
			  'focus.wysihtml5' : function(){
			     $('li.dropdown').removeClass('open');
			   }
			});
		});
	};

	Wysihtml5.prototype = {
		constructor: Wysihtml5,
		
		createToolbar: function(el, options) {
			var toolbar = $("<ul/>", {
					id : el.attr('id') + "-wysihtml5-toolbar",
					class : "wysihtml5-toolbar",
					style: "display:none"
				});

			for(var key in defaultOptions) {
				var value;
				
				if(options[key] != undefined) {
					if(options[key] == true) {
						value = true;
					}
				} else {
					value = defaultOptions[key];
				}
				
				if(value == true) {
					toolbar.append(templates[key]);
				}
			}
			
			var self = this;
			
			toolbar.find("a[data-wysihtml5-command='formatBlock']").click(function(e) {
				var el = $(e.srcElement);
				self.toolbar.find('.current-font').text(el.html())
			});
			
			this.el.before(toolbar);
			
			return toolbar;
		}
	};

	$.fn.wysihtml5 = function (options) {
		return this.each(function () {
			var $this = $(this);
	      	$this.data('wysihtml5', new Wysihtml5($this, options));
	    })
  	};

  	$.fn.wysihtml5.Constructor = Wysihtml5;

}(window.jQuery, window.wysihtml5);
