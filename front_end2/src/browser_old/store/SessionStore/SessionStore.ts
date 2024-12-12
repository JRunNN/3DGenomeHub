import { defineStore } from 'pinia'
import { useTrackStore } from '@/browser/store'
import type { CreateTrackType } from '../TrackStore/TrackStore'

export interface CreateSessionType {
    key: string
    trackIds: Array<string>
    sessionConfig: SessionConfigType
}

export interface SessionConfigType {
    width: number
    height: number
    type: string
    maxTrackNum: number
}

export const useSessionStore = defineStore({
    id: 'useSessionStore',
    state: () => ({
        sessionList: [] as CreateSessionType[],
        targetedSession: []
    }),
    getters: {
        getSessionList() {
           return this.sessionList
        },
        getTargtedSession() {
           return  this.sessionList.filter(session => this.targetedSession.includes(session.key));
        }
    },
    actions: {
        getTrackById(id: string): CreateTrackType | undefined {
            const trackStore = useTrackStore()
            // Assuming there is an array of tracks defined somewhere
            return trackStore.getTrackList.find((track) => track.key === id);
        },
        getSessionTracks(session: CreateSessionType): Array<CreateTrackType> {
            const tracks: Array<CreateTrackType> = [];
                for (const trackId of session.trackIds) {
                  const track = this.getTrackById(trackId);
                  if (track) {
                    tracks.push(track);
                  }
                }
                return tracks;
        },
        getSessionConfigs(sessionId: string): SessionConfigType {
            const session = this.sessionList.find(session => session.key === sessionId)
            if (session) {
                return session.sessionConfig
            }
            return {
                type: '',
                maxTrackNum: 0
            }
        },
        addSession(session: CreateSessionType) {
            this.sessionList.push(session)
        },
        removeSession(session: CreateSessionType): void {
            const index = this.sessionList.indexOf(session)
            if (index !== -1) {
                this.sessionList.splice(index, 1)
            }
        },
        addSessionTrack(session: CreateSessionType, trackId: string) {
            session.trackIds.push(trackId)
        },
        removeSessionTrack(sessionId, trackId: string) {
            const targetedSession = this.sessionList.find(session => session.key === sessionId)
            targetedSession.trackIds = targetedSession.trackIds.filter((id) => id != trackId)
        }
    }
})