import { defineStore } from 'pinia'
import { CreateTrackType } from '../../components/index.d'
import { isString, isArray } from '../../utils/type'

class WebWorker {
    private worker: Worker

    constructor(workerPath: string) {
        this.worker = new Worker(workerPath)
    }

    postMessage(message: any) {
        this.worker.postMessage(message)
    }

    onMessage(callback: (event: MessageEvent) => void) {
        this.worker.onmessage = callback
    }

    terminate() {
        this.worker.terminate()
    }
}



import { WebWorker } from './WorkerStore'

// create a new instance of WebWorker
const worker = new WebWorker('/path/to/worker.js')

// send a message to the worker
worker.postMessage({ type: 'ping' })

// listen for messages from the worker
worker.onMessage((event) => {
    console.log('Received message from worker:', event.data)
})

// terminate the worker
worker.terminate()
