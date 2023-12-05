const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
        data = fs.readFileSync(fname,'utf-8');
} catch(err){
        console.log('Error in reading file');
        process.exit(1);
}


data = data.split('\n\n').filter(line=>line.length>0);


const seeds = data[0].split(':')[1].trim().split(' ').map(seed=>Number(seed));
data = data.slice(1);

const mapDict = {};

function getDestination(source, mapList){
        let destination = source;
        for (let list of mapList){
                let destinationMap = list[0];
                let sourceMap = list[1];
                let lengthMap = list[list.length-1];

                let limitSourceMap = sourceMap+lengthMap;
                if(source>=sourceMap && source<=limitSourceMap){
                        destination = destinationMap + (source - sourceMap);
                        break;
                }
        }
        return destination;
}

let sources = [...seeds];
let seedMaps = {};

seeds.map((seed,index)=>{seedMaps[index]=[seed]})
for (let map of data){
        let mapName = map.split(' ')[0].trim();
        mapDict[mapName] = map.split(':')[1].trim().split('\n').map(rangeValue=>rangeValue.split(' ').map(number=>Number(number)));
        let destinations = [];
        let i = 0;
        for (let seed of sources){
                let destination = getDestination(seed,mapDict[mapName]);
                destinations.push(destination);
                seedMaps[i].push(destination);
                i+=1;
        }

        sources = [...destinations];

}


let minDest = Math.min(...sources);
console.log(minDest);
