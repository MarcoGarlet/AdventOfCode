const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
} catch(err){
	console.log('Error in reading file');
	process.exit(1);
}


data = data.split('\n')[0];

console.log(data)

let l = 14;

for (i=l-1;i<data.length;i++){
	let seq = [... data.slice(i-(l-1),i+1)];
	if (seq.length === [... new Set(seq)].length){
		console.log(i+1);
		break;
	}
	
}



