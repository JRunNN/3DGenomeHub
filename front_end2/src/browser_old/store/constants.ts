import { defineStore } from 'pinia'

export const useconstantsStore = defineStore('constants', {
    state: () => {
        /**
        * CONSTANTS REFERRED TO BY BASIC'S SCRIPTS
        */
        var BASIC_DEBUG = true;

        var BASIConst = {
            flot: {
                labelWidth: 80 // passed as parameter FLOT when plotting; other tracks that don't use FLOT must put this value into account when plotting (i.e. as padding size)
            },

            LIMITS: { // max number of entries retrieved via JSON service for a particular track
                'default': 1000, // used if limit is not defined for a particular track, e.g. pcls, scls, snp, etc
                'snp': 150,
                'gene': 1000,
                'ptag': 2500,
                'stag': 2500,
                'curv': 20000 // this track can handle big entries
            },

            TRACK_AUTO_REFRESH_INTERVAL: 500 // millisecond
        };

        var BASICService = {
            /* BASIC MODULES */

            // user
            USER_CHANGE_PASSWD: '/basic/services/user/passwd/',

            // cookies
            COOKIE_SET: '/basic/services/cookies/set/',

            // genome
            CHROME_SIZES: '/basic/services/genome/get_chrom_sizes/',
            CHROME_BANDS: '/basic/services/genome/get_chrom_bands/',
            CHROME_ACGT: '/basic/services/genome/get_refseq/',
            GENOME_LOCATION_PARSER: '/basic/services/genome/parse_location/',

            // library
            LIBRARY_STATS: '/basic/services/library/view_stats/',

            // tables
            TABLE_EXPLORE: '/basic/services/tables/explore/',
            TABLE_DOWNLOAD: '/basic/services/tables/download/',

            // tracks
            TRACK_CONFIG_GET: '/basic/services/tracks/get_config/',
            TRACK_CONFIG_SET: '/basic/services/tracks/set_config/',
            TRACK_DEFS: '/basic/services/tracks/defs/',
            TRACK_LIST: '/basic/services/tracks/list/',

            // genes
            GENE_AUTOCOMPLETE: '/basic/services/genes/autocomplete/',

            // misc  
            PROJ_LIST: '/basic/services/misc/list_projects/',
            TECH_LIST: '/basic/services/misc/list_techs/',
            CELL_LIST: '/basic/services/misc/list_cells/',
            TARGET_LIST: '/basic/services/misc/list_tfactors/'
        };

        /*
         * Names of events subscribed to/published by UI components and BASIC modules
         */
        var BASICEvent = {
            TRACK_ALLOW_SLIDE: '/track/allow-slide',
            TRACK_CHANGE: '/track/change',
            TRACK_SLIDE: '/track/slide',
            TRACK_HRESIZE: '/track/h-resize',
            TRACK_VRESIZE: '/track/v-resize',
            TRACK_CONFIG: '/track/config',

            WIN_RESIZE: '/window/resize',

            GOTO_GENE: '/goto/gene',

            // --------------------------------------------

            NAV_ZOOM_TO: 'gis.basic.corenav.zoomTo',
            NAV_ZOOM_IN: 'gis.basic.corenav.zoomIn',
            NAV_ZOOM_OUT: 'gis.basic.corenav.zoomOut',

            NAV_SET_CHROM: 'gis.basic.corenav.setChromosome',
            NAV_SET_CHROM_AND_SIZE: 'gis.basic.corenav.setChromosomeAndSize',
            NAV_SET_LOCATION: 'gis.basic.corenav.setLocation',
            NAV_GET_LOCATION: 'gis.basic.corenav.getLocation',

            NAV_REFRESH: 'gis.basic.corenav.refresh',

            TRACK_MGR_GET_TRACKLIST: 'gis.basic.trackmanager.getTrackList',
            TRACK_MGR_ADD: 'gis.basic.trackmanager.add',
            TRACK_MGR_REMOVE: 'gis.basic.trackmanager.remove',
            TRACK_MGR_RELOAD: 'gis.basic.trackmanager.reload',

            TRACK_OPEN: 'gis.basic.tracklist.openTrack',
            TRACK_CLOSE: 'gis.basic.tracklist.closeTrack',

            TABLE_VIEW: 'gis.basic.tableview.viewTable',

            PANEL_LEFT_ADD: 'gis.basic.panel.left.addTab',
            PANEL_LEFT_SHOW: 'gis.basic.panel.left.show',
            PANEL_LEFT_HIDE: 'gis.basic.panel.left.hide',
            PANEL_LEFT_TOGGLE: 'gis.basic.panel.left.toggle',

            PANEL_BOTTOM_SHOW: 'gis.basic.panel.bottom.show',
            PANEL_BOTTOM_HIDE: 'gis.basic.panel.bottom.hide',
            PANEL_BOTTOM_TOGGLE: 'gis.basic.panel.bottom.toggle'
        };

        /*
         * Names of variables stored in Local/Session storage
         */
        var BASICStorage = {
            TRACK_ACTIVE_PREFIX: '/track/list/active/',
            TRACK_ACTIVE_GROUP: '/track/list/group/',
            ACCORD_ACTIVE_IDX: '/accordion/tab/active',

            PANEL_BOTTOM_HIDDEN: '/panel/bottom/hidden',
            PANEL_BOTTOM_HEIGHT: '/panel/bottom/height',
            PANEL_LEFT_HIDDEN: '/panel/left/hidden',
            PANEL_LEFT_WIDTH: '/panel/left/width'
        };


        return {
            BASIC_DEBUG,
            BASIConst,
            BASICService,
            BASICEvent,
            BASICStorage,
        }
    }
})