import { get } from './base'
import axios from 'axios'

// export function getChromSizes() {
//   console.log('Get chrom sizes')
//   return get('http://localhost:8000/basic/services/genome/get_chrom_sizes/', { })
// }
// export function getChromSizes2(url) {
//   console.log('Get chrom sizes')
//   return get(url, { })
// }
// export function getChromBands() {
//   console.log('Get chrom bands')
//   return get('http://localhost:8000/basic/services/genome/get_chrom_bands/', {  })
// }

// export function loadChromSizesAndBands(SizesUrl, BandsUrl) {
//   console.log('Get chrom sizes and bands')
//   return axios.all([axios.get('http://localhost:8000/basic/services/genome/get_chrom_sizes/'), axios.get('http://localhost:8000/basic/services/genome/get_chrom_bands/')])
//     .then(
//       axios.spread((res1, res2) => {
//         const chromSizes = res1.data
//         const chromBands = res2.data
//         console.log(chromBands, chromSizes)
//         return { chromSizes, chromBands }
//       }
//       )).catch(error => {
//         console.log(error)
//         return { chromSizes: {}, chromBands: {} }
//       })
// }
