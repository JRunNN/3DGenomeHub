import { defineComponent, ref, onMounted, reactive, watch } from 'vue';

import { usecorenavStore } from '../store/corenav'
import { storeToRefs } from 'pinia'

// export const useBaseRowTrack = defineComponent({
// })

const _intersects = (dim1, dim2, hpad = 10) => {
    var pad = hpad,
        p = dim1.start - pad,
        q = dim1.end + pad,
        m = dim2.start - pad,
        n = dim2.end + pad;
    return p < n && q >= m;
}

const _noIntersection = (dim, group) => {
    for (var i = 0; i < group.length; i++) {
        if (_intersects(group[i], dim)) return false;
    }
    return true;
}

const _createCanvas = (canvasEle, ParentEle, h, prepad, postpad, data) => {
    // var canvas = $(cvs_holder).data('canvas');

    // if (isCanvasBlank(cvs_holder)) {
    // avoid re-creating canvas if it's already present
    console.log(canvasEle)
    canvasEle.setAttribute('width', ParentEle.offsetWidth);
    canvasEle.setAttribute('height', (h.value + prepad + postpad) * data.length);

    // cvs_holder.scroll(function () { // must sync link layer with canvas scrolling
    //     var link_layer = cvs_holder.find(">div");
    //     link_layer.css({ top: canvas.position().top });
    // });

    // cvs_holder.value.addEventListener('scroll', function () { // must sync link layer with canvas scrolling
    //     var link_layer = cvs_holder.querySelector('>div');
    //     link_layer.style.top = canvas.offsetTop + 'px';
    // });
    // }

    // return canvas;
}

const _measureWidth = (canvas, w, scls, c, showLable) => {
    // determine which part of canvas will be used to draw given scls
    var ctx = canvas.getContext("2d"),
        cstart = Math.max(1, c(scls.start)),
        cend = Math.min(w, c(scls.end + 1)),
        actualWidth = Math.max(cend - cstart, showLable ? ctx.measureText(scls._text).width : 0);

    return { start: cstart, end: cstart + actualWidth };
}

const _determineRow = (dim, groups) => {
    for (var i = 0; i < groups.length; i++) {
        if (_noIntersection(dim, groups[i])) {
            groups[i].push(dim);
            return i;
        }
    }
    // must be placed in a new row
    groups.push([dim]);
    return groups.length - 1;
}

const _clearCanvas = (canvas, linklayer) => {
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.offsetWidth, canvas.offsetWidth);
    if (linklayer) {
        linklayer.css({
            height: canvas.offsetWidth,
            width: canvas.offsetWidth - 16
        }).empty();
    }
}

export const drawPlotX = (canvasEle, items, quick,ParentEle, h, prepad, postpad, showLabel, _drawItem, _measureWidth, start, end, color) => {
    console.log('drawPlotX BED file')
    // const corenavStore = usecorenavStore()
    console.log(items)

    // const { chrom, min, max, start, end, isLoaded, chromSizes, chromBands } = storeToRefs(corenavStore)

    const linklayer = null;

    var links = []; // returned at the end of function; so this plugin can't be chained
    
    const colors = color || reactive({ '_': "black" })
    console.log(colors)
    // colors = _.isObject(colors_)
    //     ? colors_ // if head/tail/line is missing, wildcard/default color will be used (see _getColor)
    //     : { _: colors_ }; // set wildcard if it's either string or function
    // console.log(items)

    // 设置canvas元素的宽和高，宽度设置成和父元素一致，高度设置成和items的长度一致
    _createCanvas(canvasEle, ParentEle, h, prepad, postpad, items)

    // cavas元素的宽度
    const w = canvasEle.getBoundingClientRect().width;
    console.log(h)
    // console.log(w)
    // check if quickdraw is requested
    // if (!quick) {
    //     if (clickable) {
    //         linklayer = data(cvs_holder, "linkLayer");
    //         if (!linklayer) {
    //             linklayer = _createLayer(cvs_holder);
    //             data(cvs_holder, { "linkLayer": linklayer });
    //         }
    //     }
    //     // reset item placement data, so that they'll be recalculated
    //     data(cvs_holder, { "rows": {} });
    // }

    const ratio = w / (end - start + 1)
    const _c = function (x1) { return (x1 - start) * ratio; }; // convert genome location to canvas coordinate

    let groups = []
    const rows = {}
    // stores mapping {item local ID -> row number}
    // let rows = data(cvs_holder.value, "rows")
    // used in quickdraw so that we don't need to recompute layout
    // cnv_elem = canvas.get(0);
    // cnv_elem = canvas
    // console.log(rows)
    canvasEle.style.display = "none";
    _clearCanvas(canvasEle, linklayer);

    var rowcount = 0, k = 0; // running number

    // determine layout
    for (var i = 0; i < items.length; i++, k++) {
        var item = items[i];
        if (rows[k] == null) {
            rows[k] = _determineRow(_measureWidth(canvasEle, w, item, _c, showLabel), groups);
        }
        if (rowcount < rows[k]) rowcount = rows[k];
    }

    // resize canvas and redraw
    // $(cnv_elem).attr({
    //     height: (h + prepad + postpad) * (rowcount + 2)
    // });
    canvasEle.setAttribute('height', (h + prepad + postpad) * (rowcount + 2));

    k = 0; // restart from 0
    for (var i = 0; i < items.length; i++, k++) {
        var item = items[i], r = rows[k];
        // console.log(r * (h + postpad) + prepad * (r + 1))
        _drawItem(canvasEle, 0, r * (h + postpad) + prepad * (r + 1), w, h, item, colors, _c, quick);
        // if (!quick && _addLinks) {
        //     var link = _addLinks(linklayer, cnv_elem, r * (h + postpad) + prepad * (r + 1), w, h.value, postpad, item, _c);
        //     links.push([item, link]);
        // }
    }
    // canvas.value.show();
    canvasEle.style.display = "block";


    return links;
}


