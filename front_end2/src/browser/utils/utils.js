// BASIC_log = (function() {
//     EV = 'gis.basic.logger.log';
//     return {
//         error: function(text) { $.publish(EV, ['ERROR', 'red', text]); },
//         warn : function(text) { $.publish(EV, ['WARN', 'orange', text]); },
//         info : function(text) { $.publish(EV, ['INFO', 'blue', text]); },
//         debug: function(text) { console.log(text); }
//     };
// })();
export const BASIC_log = {
    error: function(text) { $.publish('gis.basic.logger.log', ['ERROR', 'red', text]); },
    warn : function(text) { $.publish('gis.basic.logger.log', ['WARN', 'orange', text]); },
    info : function(text) { $.publish('gis.basic.logger.log', ['INFO', 'blue', text]); },
    debug: function(text) { console.log(text); }
}
/**
 * Utility function to call multiple async functions
 * 
 * Arguments:
 * - funs:
 *       list of functions, each of which takes one callback function as argument
 *       the callback function must be called with the result of the corresponding function
 * - callback: 
 *       the ultimate callback function that will be called with one argument:
 *       a dictionary of results from all the functions (keys(funs) == keys(arg)) 
 */
export function BASIC_insync(funs, callback) {
    var counter = 0,
        result = {};
        
    function _callback(id, subresult) {
        counter--;
        result[id] = subresult;
        if (counter === 0) {
            callback(result);
        }
    }
    
    _.each(funs, function(f, id) {
        counter++;
        f(function(subresult) { _callback(id, subresult) });
    });
}

export function BASIC_getMultiJSON(urls, params) {
    if (urls == null || urls.length == 0) return;
    
    var funs = {};
    _.each(urls, function(url, id) {
        funs[id] = function(callback) {
            $.getJSON(url, params || {}).done(callback).fail(function() { callback(undefined) });
        };
    });
    
    return $.Deferred(function(def) {
        BASIC_insync(funs, function(result) {
            var ok = true;
            for (var i in result) {
                if (_.isUndefined(result[i])) { ok = false; break; }
            }
            def[ok ? 'resolve' : 'reject'](result);
        });
    }).promise();
}

if (!String.prototype.startsWith) {
    String.prototype.startsWith = function(prefix) {
        return this.substring(0, prefix.length) === prefix;
    };
}

if (!String.prototype.strip) {
    String.prototype.strip = function() {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

if (!String.prototype.endsWith) {
    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

/*
 * Performs recursive eval in case there's a function stored as string in the
 * expression
 */
export function BASIC_recurseval(expr) {
  
    if (expr === null) {
        return null;
    };
    
    var t = typeof(expr);
    if (t === 'string') {
        expr = expr.strip();
        // case #1: closure
        if (expr.startsWith('(function') && expr.endsWith(')()')) {
            return BASIC_recurseval(eval('(' + expr + ')'));
        }
        var lastChar = expr.length>0 ? expr[expr.length-1] : null;
        if (lastChar === '}') {
            // case #2: dictionary
            if (expr[0] === '{')
                return BASIC_recurseval(eval('(' + expr + ')'));
            // case #3: function
            if (expr.startsWith('function'))
                return eval('(' + expr + ')');
        } else if (lastChar === ']' && expr[0] == '[') {
            // case #4: list
            return BASIC_recurseval(eval('(' + expr + ')'));
        }
    } else if (t === 'object') {
        var newobj = {};
        for (var k in expr) {
            newobj[k] = BASIC_recurseval(expr[k]);
        }
        return newobj;
    }
    
    return expr; // returned as-is (e.g. function is returned unchanged)
}

export function BASIC_intComma(num) {
    var str = "";
    do {
        let q = "" + (num % 1000);
        num = Math.floor(num / 1000);
        if (num > 0) {
            while (q.length < 3) q = "0" + q;
            q = "," + q;
        }
        str = q + str;
    } while (num > 0);
    return str;
};

export function BASIC_sciNotation(num, prec) {
    // format number to scientific notation
    // with [prec] significant digits
    return new Number(num.toPrecision(prec)).toExponential();
}

/**
 * Retrieves/stores values from HTML5 session storage 
 */
export function BASIC_session(key, value) {
    if (value == undefined) {
        var v = sessionStorage.getItem(key);
        return v == null ? null : JSON.parse(v);
    } else {
        sessionStorage.setItem(key, JSON.stringify(value));
    }
}

/**
 * Retrieves/stores values from HTML5 local storage 
 */
export function BASIC_local(key, value) {
    if (value == undefined) {
        var v = localStorage.getItem(key);
        return v == null ? null : JSON.parse(v);
    } else {
        localStorage.setItem(key, JSON.stringify(value));
    }
}



export function formatBytes(bytes) {
    const kilobytes = bytes / 1000;
    if (kilobytes < 1) {
      return bytes + " B";
    }
    const megabytes = kilobytes / 1000;
    if (megabytes < 1) {
      return kilobytes.toFixed(2) + " KB";
    }
    return megabytes.toFixed(2) + " MB";
  }

// export { BASIC_log, BASIC_insync, BASIC_getMultiJSON, BASIC_recurseval, BASIC_intComma, BASIC_sciNotation, BASIC_session, BASIC_local}