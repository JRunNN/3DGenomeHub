import axios from 'axios'

export default function () {
    const getJsonData = async function (file) {
        try {
            const responseData = await axios.get(file);
            let data = responseData.data;
            // if (pos.chrom === '') {
                        
            //     // no info found in cookie
            //     for (var i in data.csize) {
            //         pos.chrom = i;
            //         pos.start = 1;
            //         pos.end = data.csize[i];
            //     }
            // }
            
            // chrom_sizes = data.csize;
            // chrom_bands = data.cband;
            return data 
        } catch (error) {
            console.log(error);
        }
    }

    return { 
        getJsonData 
    };
}