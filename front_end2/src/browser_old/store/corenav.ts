import { defineStore } from 'pinia'
// const utilsStore = useutilsStore()

export const usecorenavStore = defineStore('corenav', {
    // store state
    state: () => {

        return {
            asm: 'hg19',
            chrom: 'chr1',
            start: 1,
            end: 1,
            min: 1,
            max: 1,
            isLoaded: false,
            chromSizes: {},
            chromBands: {},
            minViewBpeif: 10,
        }
    },
    actions: {
        async getChromSizesAndBands() {
            console.log('isLoaded is:', this.isLoaded)
            const { chromSizes, chromBands } = await loadChromSizesAndBands()
            this.chromSizes = chromSizes
            this.chromBands = chromBands
            // this.isLoaded = true
            console.log('isLoaded is:', this.isLoaded)
        },
        setLocationAndRefresh(chrom, start, end) {
            // Full package
            this.setChromosome(chrom);
            this.setLocation(start, end);
            // emitter.emit(useconstantsStore().BASICEvent.NAV_REFRESH, "full");
        },
        setChromosome(chrom) {
            this.chrom = chrom;
        },
        setChromosomeAndSize(chrom, size) {
            this.chrom = chrom;
            this.max = size;
        },
        setLocation(start, end) {
            this.start = start;
            this.end = end;
        },
        // getLocation(callback) {
        //     callback($.extend({}, this.position));
        // },
        // refresh(type, param) {
        //     if (type == "full") {
        //         // notify server of new location on full refresh
        //         $.post(BASICService.COOKIE_SET, position);
        //         $.address.value('?' + $.param({ c: position.chrom, s: position.start, e: position.end }));
        //     }
        // },
        zoomTo(chrom, start, end) {
            if (chrom == null) {
                chrom = this.chrom
            } else {
                this.chrom = chrom
            }
            
            var size = this.chromSizes[chrom],
                s = Math.max(start, 1) || 1,
                e = Math.min(end, size) || size;

            this.start = Math.round(s)
            this.end = Math.round(e)
            
            console.log('zoomTo', this.chrom, this.start, this.end)
        },
        zoomIn() {
            const s = this.start,
                e = this.end,
                m = (s + e) / 2,
                x = (e - s + 1) / 4;
            this.zoomTo(this.chrom, Math.round(m - x), Math.round(m + x) - 1);
            // console.log('zoomIn', this.start, this.end)
        },
        zoomOut() {
            const s = this.start,
                e = this.end,
                m = (s + e) / 2,
                x = Math.max(1, e - s);
            this.zoomTo(this.chrom, Math.round(m - x), Math.round(m + x) + 1);
            // console.log('zoomOut', this.start, this.end)
        },
        shift(ev, direction){
            var span = this.end - this.start + 1,
                delta = ev.ctrlKey ? ev.shiftKey ? 0.95 : 0.475 : 0.1;
            console.log('shift', this.start, this.end, span, delta)
            delta *= direction * span;
           // $.publish(BASICEvent.NAV_ZOOM_TO, [loc.chrom, loc.start + delta, loc.end + delta]);
            this.zoomTo(this.chrom, this.start + delta, this.end + delta)
           //    start.value += delta
        //    end.value += delta
        // console.log(start.value + delta)
        //    emit('update:start', start.value + delta)
        //    emit('update:end', end.value + delta)  
    }
    }
}
)