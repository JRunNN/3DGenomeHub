import { thingDark } from 'naive-ui'
import { v4 as uuid} from 'uuid'
/**
 * A class for managing and allocating web workers.
 */
export class WebWorkerManager {
    /**
     * Creates a new WebWorkerManager instance.
     * @param {number} maxWorkers - The maximum number of workers to allocate.
     */
    constructor(maxWorkers) {
      /**
       * The maximum number of workers to allocate.
       * @type {number}
       */
      this.maxWorkers = maxWorkers
  
      /**
       * The array of workers currently allocated.
       * @type {Worker[]}
       */
      this.workers = []
  
      // /**
      //  * The array of workers waiting to be allocated.
      //  * @type {Object[]}
      //  */
      // this.workerQueue = []
  
      // /**
      //  * The map of worker results.
      //  * @type {Map<number, any>}
      //  */
      // this.workerResults = new Map()
  
      /**
       * The counter for worker IDs.
       * @type {number}
       */
      this.FreeWorkers = 4
      // this.workIdCounter = 0
    }
  
    /**
     * Adds a new worker to the workers array.
     * @param {string} workerScript - The URL of the worker script.
     */
    addWorker(worker: Worker, data, options, handler) {
      // const worker = new Worker(workerScript)
      const workerId = uuid()
      // Add the worker to the workers array.
      this.workers.push({
        workerId,
        worker,
        data,
        options
      })
      // Set up the onmessage event handler to handle messages from the worker.
      worker.onmessage = event => {
        const { workerId, result } = event.data
        // this.workerResults.set(workerId, result)
        // 拿到worker返回的数据，执行一些函数
        console.log("worker返回的数据", result)
        handler(result)
        // terminate this worker
        this.terminateWorker(workerId)
        this.allocateWorkerFromQueue()
      }

      this.allocateWorkerFromQueue()
    

    }
  
    /**
     * Allocates a worker from the worker queue.
     */
    allocateWorkerFromQueue() {
      // Check if there are workers waiting in the queue and if there are workers available.
      if (this.workers.length > 0 && this.FreeWorkers > 0) {
        this.FreeWorkers--

        // Get the next worker from the queue and the next available worker.
        const { workerId, worker, data, options } = this.workers.shift()
        // const worker = this.workers.shift()
        // console.log(options)

        // Send a message to the worker with the worker ID, data, and options.
        worker.postMessage({ workerId, data, options })
        console.log('message sent to worker')
      }
    }

    /**
     * Terminates a worker and removes it from the workers array.
     * @param {number} workerId - The ID of the worker to terminate.
     */
    terminateWorker(workerId) {
      // Find the worker in the workers array.
      const workerIndex = this.workers.findIndex(worker => worker.workerId === workerId)
  
      // If the worker is found, terminate it and remove it from the workers array.
      if (workerIndex !== -1) {
        const worker = this.workers[workerIndex]
        worker.terminate()
        this.workers.splice(workerIndex, 1)
  
        // Remove the worker from the worker queue and the worker results map.
        // this.workerQueue = this.workerQueue.filter(queueItem => queueItem.workerId !== workerId)
        // this.workerResults.delete(workerId)
  
        this.FreeWorkers++
      }
    }
  }