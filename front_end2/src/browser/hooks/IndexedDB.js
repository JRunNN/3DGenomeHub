import {openDB} from 'idb'


// export async function saveToIndexedDB(key, data, database = 'myDatabase', store = 'myObjectStore') {
//     // const db = await openDB('myDatabase', 1);
//     const db = await openDB(database, 1, {
//         upgrade(db) {
//             db.createObjectStore(store);
//         },
//     });
//     const tx = db.transaction(store, 'readwrite');
//     // console.log(tx)
//     tx.store.put(data, key);
//     await tx.done;
//     console.log('Data saved to IndexedDB:', data);
// }

export  function saveToIndexedDB(data, database, store) {
    // const db = await openDB(database, 1);
    // const tx = db.transaction(store, 'readwrite');
    // const objectStore = tx.objectStore(store);
    // objectStore.put(data, key);
    // await tx.done;
    // console.log('Data saved to IndexedDB:', data);
    const dbPromise = openDB(database, 1, function (upgradeDb) {
        if (!upgradeDb.objectStoreNames.contains(store)) {
            const store = upgradeDb.createObjectStore(store);
        }
    });

    dbPromise
    .then(function (db) {
      const tx = db.transaction(store, 'readwrite');
      const store = tx.objectStore(store);
      store.add(data);
      return tx.complete;
    })
    .then(function () {
      console.log('Item updated!');
    });

    return dbPromise;
}



export async function fetchFromIndexedDB(database,  store) {
    // console.log('Fetching data from IndexedDB:', key)
    const db = await openDB(database, 1);
    console.log('111')

    const tx = db.transaction(store, 'readonly');
    console.log('222')

    const result = await tx.store.getAll();
    console.log('333')
    console.log('Data retrieved from IndexedDB:', result);
    return result;
}