import { defineStore } from 'pinia'

export const useutilsStore = defineStore('utils', {
    // Store 选项...
    state: () => {


        /* FOR DEBUGGING PURPOSES */
        // var _dump = function (obj, depth) {
        //     _fun = function (obj, depth) {
        //         if (obj == null) return 'null';
        //         if (!_.isObject(obj) || depth < 0) return obj;
        //         var out = '',
        //             comma = false;
        //         for (var i in obj) {
        //             if (comma) out += ", ";
        //             out += i + ": " + _fun(obj[i], depth - 1);
        //             comma = true;
        //         }
        //         return "{" + out + "}";
        //     };
        //     return _fun(obj, depth || 3);
        // };

        /* This function is invoked from the main template */
        // function BASIC_initialize(app_url, asm, chrom, start, end, print_friendly) {
        //     var shared = {};

        //     var ui_components = ['world', 'basic_navbar', 'select_chrom',
        //                          'left_panel', 'left_sep', 'left_panel_accord', 
        //                          'bottom_panel', 'bottom_sep', 'middle_panel', 
        //                          'control_panel', 'center_panel', 'track_holder', 'tab_holder', 
        //                          'full_chrom_view', 'part_chrom_view', 'acgt_view', 'awsum_bar'];

        //     // shared = {'left_panel': 对应的JQuery对象，‘left_sep’：对应的JQuery对象}
        //     // html页面上有以id为上述ui_components的元素
        //     // shared.ui_component就返回元素对应的JQuery对象
        //     for (var i in ui_components) {
        //       var id = ui_components[i];
        //       shared[id] = $('#' + id);
        //     }

        //     // assembly信息
        //     shared.asm = asm;

        //     shared.fun_bottom = function() {
        //       // to be called whenever the bottom panel is resized
        //       if (shared.bottom_panel.css('bottom')[0] === '-') {
        //         // panel is being hidden (its height not changed)
        //         h = shared.middle_panel.height()-shared.bottom_panel.offset().top + 17;
        //       } else {
        //         // panel is resized
        //         h = shared.bottom_panel.height() + 17; // magic number; don't ask me why it works
        //       }

        //       shared.tab_holder.css({ height: shared.bottom_panel.height()-6 });

        //       shared.tab_holder.find('.flexitab').css({
        //         height: shared.tab_holder.height()-shared.tab_holder.find('>ul').height()-15 // magic (see widget "tabby")
        //       });
        //     };

        //     shared.fun_left = function() {
        //       // to be called whenever the left panel is resized
        //       var w = shared.left_panel.offset().left + shared.left_panel.width();
        //       shared.middle_panel.css({ left: w, width: $(window).width()-w });
        //       shared.fun_bottom();
        //     };

        //     BASIC.initialize({ // will be passed to all the components during initialization
        //       // global里包含各种ui_components对应的JQuery object, fun_left,fun_bottom,asm
        //       global: shared,
        //       APP_URL: app_url,
        //       print_friendly: print_friendly,

        //       position: {
        //         asm: asm,
        //         chrom: chrom,
        //         start: start,
        //         end: end
        //       }
        //     });
        //   }

        /**
         * Core file for BASIC platform.
         * Requires pub/sub mechanism (default is using jQuery pub/sub plugin by Peter Higgins).
         */
        // 立即执行函数
        // 返回BASIC对象，内涵register和initialize两个属性
        // register是一个函数
        // initialize是一个函数
        // var BASIC = (function () {
        //     var _modules = {},       // { mod_id -> module (dictionary) }
        //         _deps_list = {},     // { mod_id -> [dependent modules] }
        //         _deps_count = {},    // { mod_id -> unsatisfied_count (zero means all clear) }
        //         _initialized = {}    // { mod_id -> True (if not inside, means not initialized yet) }
        //         ;

        //     function _refresh_dep(mod_id) {
        //         for (var i in _deps_list[mod_id]) {
        //             var dep_mod = _deps_list[mod_id][i];
        //             _deps_count[dep_mod]--;
        //         }
        //     };

        //     return {
        //         /**
        //          * Called by components/plugins
        //          */
        //         register: function (mod_id, module) {
        //             _modules[mod_id] = module; // modules['gis.basic.bootstrap'] = 自执行函数（产生闭包）。因此module是一个拥有闭包的对象

        //             // module is a dictionary; iterate each item in module
        //             for (var i in module) {
        //                 var item = module[i];
        //                 // 如果item是一个函数
        //                 if (_.isFunction(item)) {
        //                     // 就把item这个函数绑定到module对象上， When the function is called, the value of this will be the module object.
        //                     _.bind(item, module);
        //                     if (i[0] !== '_') { // 如果不是私有函数，就使用callback订阅这个函数
        //                         // methods that start with underscore are private
        //                         // if a pub is broadcast, we invoke the corresponding function in the module
        //                         $.subscribe(mod_id + '.' + i, function () {  // 如果不是私有函数，就使用callback订阅这个函数
        //                             var moo = mod_id;
        //                             if (!_initialized[moo]) {
        //                                 // console.warn('Service in module [' + moo + '] invoked but it is not (yet) loaded.');
        //                             }
        //                         });
        //                         // 让item注册“mod_id + '.' + i”这个主题
        //                         $.subscribe(mod_id + '.' + i, item); // 如果module的第i个成员不是私有函数，那么就用这个函数来监听
        //                     } else if (i === '__deps__') {
        //                         var deps = item(); // 返回一个如下的数组：['gis.basic.panel.left', 'gis.basic.panel.bottom', 'gis.basic.tracklist']
        //                         for (var j in deps) {
        //                             var d = deps[j]; // 'gis.basic.panel.left'
        //                             if (_deps_list[d] == null) _deps_list[d] = [];
        //                             _deps_list[d].push(mod_id); // _deps_list储存着依赖d的module名称
        //                         }
        //                         if (_deps_count[mod_id] == null) _deps_count[mod_id] = 0;
        //                         _deps_count[mod_id] += deps.length; // _deps_count储存着某个mod_id的依赖module的个数
        //                     }
        //                 }
        //             }

        //             $.publish('basic.platform.__reg__', [mod_id]);
        //         },

        //         /**
        //          * Called after document is ready
        //          */
        //         //  called from basic.main.js
        //         //  BASIC.initialize({ // will be passed to all the components during initialization
        //         //     global: shared,
        //         //     APP_URL: app_url,
        //         //     print_friendly: print_friendly,

        //         //     position: {
        //         //       asm: asm,
        //         //       chrom: chrom,
        //         //       start: start,
        //         //       end: end
        //         //     }
        //         //   })
        //         // The initialize function is called after the document is ready, and it initializes all the registered components in the right order according to their dependencies. 
        //         // The initialization process starts by putting all the components in a queue, then iterating through the queue, initializing components whose dependencies have been satisfied.
        //         initialize: function (args) {
        //             var queues = [];
        //             for (var mod_id in _modules) {
        //                 queues.push({ id: mod_id, module: _modules[mod_id] });
        //             }

        //             function _init_helper(inited_mod) {
        //                 _initialized[inited_mod] = true;
        //                 while (queues.length > 0) {
        //                     var q = queues.shift(), // The shift() method removes the first element from an array and returns that removed element. This method changes the length of the array.
        //                         mod_id = q.id,
        //                         module = q.module;

        //                     if (_deps_count[mod_id] > 0) {
        //                         // defer initialization
        //                         queues.push(q);
        //                         continue;
        //                     }

        //                     (function () {
        //                         var _mod_id = mod_id;
        //                         if (BASIC_DEBUG) console.log('Module [' + mod_id + '] init');
        //                         if (module.__init__ != null) {
        //                             // pass arguments from caller to each component
        //                             var def = module.__init__($.extend(args, {
        //                                 // also pass some platform-specific variables, if any
        //                             }));

        //                             var done_callback = function () {
        //                                 // callback function to be called by component after __init__ is done
        //                                 _refresh_dep(_mod_id);
        //                                 BASIC_log.info('Module [' + mod_id + '] loaded');
        //                                 if (BASIC_DEBUG) BASIC_log.debug('Module [' + mod_id + '] loaded');
        //                                 $.publish('basic.platform.__init__', [_mod_id]);
        //                             };

        //                             if (_.isUndefined(def)) {
        //                                 // if nothing is returned, we assume it's a sync operation
        //                                 done_callback();
        //                             } else {
        //                                 def.done(done_callback);
        //                             }
        //                         }
        //                     })();
        //                     break;
        //                 }
        //                 if (_modules.length === _initialized.length) {
        //                     $.publish('basic.platform.__done__');
        //                 }
        //             }

        //             $.subscribe('basic.platform.__init__', _init_helper);
        //             _init_helper();
        //         }
        //     };
        // })();



        const leftDragBound = function () {
            return this.BASIConst.flot.labelWidth + 17; // magic number
          }

        // const rightDragBound: function () {
        //     return this.options._content.width() + 5; // magic number
        //   }

        return {
            message: 'Hello World',
            _modules: {},       // { mod_id -> module (dictionary) }
            _deps_list: {},     // { mod_id -> [dependent modules] }
            _deps_count: {},    // { mod_id -> unsatisfied_count (zero means all clear) }
            _initialized: {}, // { mod_id -> True (if not inside, means not initialized yet) } 
            no_panel_op: false,
        }
    },
    actions: {
        // basic.platform.js
        _refresh_dep(mod_id) {
            for (var i in this._deps_list[mod_id]) {
                var dep_mod = this._deps_list[mod_id][i];
                this._deps_count[dep_mod]--;
            }
        },
        register(mod_id, module) {
            this._modules[mod_id] = module; // modules['gis.basic.bootstrap'] = 自执行函数（产生闭包）。因此module是一个拥有闭包的对象

            // module is a dictionary; iterate each item in module
            for (var i in module) {
                var item = module[i];
                // 如果item是一个函数
                if (_.isFunction(item)) {
                    // 就把item这个函数绑定到module对象上， When the function is called, the value of this will be the module object.
                    _.bind(item, module);
                    if (i[0] !== '_') { // 如果不是私有函数，就使用callback订阅这个函数
                        // methods that start with underscore are private
                        // if a pub is broadcast, we invoke the corresponding function in the module
                        $.subscribe(mod_id + '.' + i, function () {  // 如果不是私有函数，就使用callback订阅这个函数
                            var moo = mod_id;
                            if (!this._initialized[moo]) {
                                // console.warn('Service in module [' + moo + '] invoked but it is not (yet) loaded.');
                            }
                        });
                        // 让item注册“mod_id + '.' + i”这个主题
                        $.subscribe(mod_id + '.' + i, item); // 如果module的第i个成员不是私有函数，那么就用这个函数来监听
                    } else if (i === '__deps__') {
                        var deps = item(); // 返回一个如下的数组：['gis.basic.panel.left', 'gis.basic.panel.bottom', 'gis.basic.tracklist']
                        for (var j in deps) {
                            var d = deps[j]; // 'gis.basic.panel.left'
                            if (this._deps_list[d] == null) this._deps_list[d] = [];
                            this._deps_list[d].push(mod_id); // _deps_list储存着依赖d的module名称
                        }
                        if (this._deps_count[mod_id] == null) this._deps_count[mod_id] = 0;
                        this._deps_count[mod_id] += deps.length; // _deps_count储存着某个mod_id的依赖module的个数
                    }
                }
            }

            $.publish('basic.platform.__reg__', [mod_id]);
        },
        initialize(args) {
            var queues = [];
            for (var mod_id in this._modules) {
                queues.push({ id: mod_id, module: this._modules[mod_id] });
            }

            function _init_helper(inited_mod) {
                this._initialized[inited_mod] = true;
                while (queues.length > 0) {
                    var q = queues.shift(), // The shift() method removes the first element from an array and returns that removed element. This method changes the length of the array.
                        mod_id = q.id,
                        module = q.module;

                    if (this._deps_count[mod_id] > 0) {
                        // defer initialization
                        queues.push(q);
                        continue;
                    }

                    (function () {
                        var _mod_id = mod_id;
                        if (BASIC_DEBUG) console.log('Module [' + mod_id + '] init');
                        if (module.__init__ != null) {
                            // pass arguments from caller to each component
                            var def = module.__init__($.extend(args, {
                                // also pass some platform-specific variables, if any
                            }));

                            var done_callback = function () {
                                // callback function to be called by component after __init__ is done
                                this._refresh_dep(_mod_id);
                                BASIC_log.info('Module [' + mod_id + '] loaded');
                                if (BASIC_DEBUG) BASIC_log.debug('Module [' + mod_id + '] loaded');
                                $.publish('basic.platform.__init__', [_mod_id]);
                            };

                            if (_.isUndefined(def)) {
                                // if nothing is returned, we assume it's a sync operation
                                done_callback();
                            } else {
                                def.done(done_callback);
                            }
                        }
                    })();
                    break;
                }
                if (this._modules.length === this._initialized.length) {
                    $.publish('basic.platform.__done__');
                }
            }

            $.subscribe('basic.platform.__init__', _init_helper);
            _init_helper();
        },
        fun_left() {
            // to be called whenever the left panel is resizedns
            var w = $('#left_panel').offset().left + $('#left_panel').width();
            console.log(w)
            $('#middle_panel').css({ left: w, width: $(window).width() - w });
            // this.fun_bottom();
        },
        fun_bottom() {
            // to be called whenever the bottom panel is resized
            if ($('#bottom_panel').css('bottom')[0] === '-') {
                // panel is being hidden (its height not changed)
                const h = $('#middle_panel').height() - $('#bottom_panel').offset().top + 17;
            } else {
                // panel is resized
                const h = $('#bottom_panel').height() + 17; // magic number; don't ask me why it works
            }

            $('#tab_holder').css({ height: $('#bottom_panel').height() - 6 });

            $('#tab_holder').find('.flexitab').css({
                height: $('#tab_holder').height() - $('#tab_holder').find('>ul').height() - 15 // magic (see widget "tabby")
            });
        }
    }
});