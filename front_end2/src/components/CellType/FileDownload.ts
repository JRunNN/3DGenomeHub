// import * as stream from 'stream';
// import { promisify } from 'util';
import axios from 'axios'

// const finished = promisify(stream.finished);
// export async function downloadFile(fileUrl: string, outputLocationPath: string): Promise<any> {
//   const writer = createWriteStream(outputLocationPath);
// return axios({
//     method: 'get',
//     url: fileUrl,
//     responseType: 'stream',
//   }).then(async response => {
//     response.data.pipe(writer);
//     return await finished(writer);
//   });
// }

export async function downloadFile(fileUrl: string, outputLocationPath: string) {
    const writer = createWriteStream(outputLocationPath);
  ​
    return axios({
      method: 'get',
      url: fileUrl,
      responseType: 'stream',
    }).then(response => {
      //ensure that the user can call `then()` only when the file has
      //been downloaded entirely.
      return new Promise((resolve, reject) => {
        response.data.pipe(writer);
        let error = null;
        writer.on('error', err => {
          error = err;
          writer.close();
          reject(err);
        });
        writer.on('close', () => {
          if (!error) {
            resolve(true);
          }
          //no need to call the reject here, as it will have been called in the
          //'error' stream;
        });
      });
    });
  }