/* This function is invoked from the main template */
function BASIC_initialize(app_url, asm, chrom, start, end, print_friendly) {
  var shared = {};
  
  var ui_components = ['world', 'basic_navbar', 'select_chrom',
                       'left_panel', 'left_sep', 'left_panel_accord', 
                       'bottom_panel', 'bottom_sep', 'middle_panel', 
                       'control_panel', 'center_panel', 'track_holder', 'tab_holder', 
                       'full_chrom_view', 'part_chrom_view', 'acgt_view', 'awsum_bar'];
  
  // shared = {'left_panel': 对应的JQuery对象，‘left_sep’：对应的JQuery对象}
  // html页面上有以id为上述ui_components的元素
  // shared.ui_component就返回元素对应的JQuery对象
  for (var i in ui_components) {
    var id = ui_components[i];
    shared[id] = $('#' + id);
  }

  // assembly信息
  shared.asm = asm;

  shared.fun_bottom = function() {
    // to be called whenever the bottom panel is resized
    if (shared.bottom_panel.css('bottom')[0] === '-') {
      // panel is being hidden (its height not changed)
      h = shared.middle_panel.height()-shared.bottom_panel.offset().top + 17;
    } else {
      // panel is resized
      h = shared.bottom_panel.height() + 17; // magic number; don't ask me why it works
    }
    
    shared.tab_holder.css({ height: shared.bottom_panel.height()-6 });
    
    shared.tab_holder.find('.flexitab').css({
      height: shared.tab_holder.height()-shared.tab_holder.find('>ul').height()-15 // magic (see widget "tabby")
    });
  };
      
  shared.fun_left = function() {
    // to be called whenever the left panel is resized
    var w = shared.left_panel.offset().left + shared.left_panel.width();
    shared.middle_panel.css({ left: w, width: $(window).width()-w });
    shared.fun_bottom();
  };

  BASIC.initialize({ // will be passed to all the components during initialization
    // global里包含各种ui_components对应的JQuery object, fun_left,fun_bottom,asm
    global: shared,
    APP_URL: app_url,
    print_friendly: print_friendly,
    
    position: {
      asm: asm,
      chrom: chrom,
      start: start,
      end: end
    }
  });
}

export { BASIC_initialize }