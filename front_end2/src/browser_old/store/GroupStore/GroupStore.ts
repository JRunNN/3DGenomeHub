import { defineStore } from 'pinia'

export const useGroupStore = defineStore({
    id: 'useGroupStore',
    state: () => ({
        GroupList: []
    
    }),
    getters: {
        getGroupList() {
            return this.GroupList
        }
    },
    actions: {

    }
})