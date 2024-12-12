import { useSessionStore } from '@/browser/store/SessionStore/SessionStore'
const sessionStore = useSessionStore();
import { useTrackStore } from '@//browser/store/TrackStore/TrackStore'
const trackStore = useTrackStore();

const addTrack = (row) => {
    row.loadingStatus = 'loading';
    let type;
    switch (row.format) {
        case 'bedpe':
            if(row.display == 'basicCurve') {
                type = 'CurvTrack'
            } else if (row.display == 'flatCurve'){
                type = 'CurvTrack'
            } else if(row.display == 'block') {
                type = 'PclsTrack'
            } else if(row.display == 'interchrom') {
                type = 'InterChromCurvTrack'
            } else if(row.display == 'network') {
                type = 'NetworkTrack'
            }
            break;
        case 'hic':
            type = 'HicTrack'
            break;
        case 'bed':
            type = 'SclsTrack'
            break;
        case 'bigwig':
            type = 'LineGTrack'
            break;
        case 'heatmap':
            type = 'HeatmapGTrack'
            break;
        case 'fasta':
            type = 'SeqTrack'
            break;
    }
    const label = row.id
    const name = row.id

      UploadJsonFile([{
        id: row.id,
        name: name,
        label: label,
        type: type,
        url: row.url,
        style: row.display
    }])
    row.loadingStatus = 'loaded';
    console.log(row)
}



const UploadJsonFile = async (data) => {
    try {
        console.log(sessionStore.getSessionList)

        const promises = data.map(async (item, index) => {
            const trackComponentType = item.type;
            // item.uuid = uuid();
            console.log(item)
            // Make sure to uncomment these lines if necessary
            // await componentInstall(trackComponentType, fetchTrackComponent(item.type));
            // await componentInstall(`${trackComponentType}Config`, fetchConfigComponent(item.type));

            const newTrack = await createComponent(item.type);
            newTrack.key = String(item.id);
            newTrack.trackConfig.sessionId.push(sessionStore.getSessionList[0].key);
            newTrack.option.url = item.url;
            newTrack.option.style = item.style;
            newTrack.trackConfig.name = item.name;
            newTrack.trackConfig.label = item.label;
            // newTrack.trackConfig.order = index;
            console.log(newTrack)
            sessionStore.getSessionList[0].trackIds.push(item.id);

            return trackStore.addTrackList(newTrack, false, true);
        });

        await Promise.all(promises);

    } catch (error) {
        console.error(error);
    }
};

const modules = import.meta.glob('@/browser/tracks/*/config.ts', { eager: true })
const modulePaths = Object.keys(modules);
const createComponent = async (trackType) => {
    try {
        const modulePath = modulePaths.find(path => path.includes(`${trackType}`));
        const moduleImportFunction = await modules[modulePath];
        return new moduleImportFunction.default()
    } catch (error) {
        console.error(`Error while creating component of type ${trackType}: `, error);
        return null;
    }
}

export default addTrack