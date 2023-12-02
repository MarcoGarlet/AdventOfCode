const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
        data = fs.readFileSync(fname,'utf-8');
} catch(err){
        console.log('Error in reading file');
        process.exit(1);
}


data = data.split('\n').filter(line=>line.length>0);
const limits = {'red':12,'green':13,'blue':14}


function getSetConfiguration(set){
	const colors = set.split(',');
	const count = {'red':0,'green':0,'blue':0};
	for(let color of colors){
		color = color.trim();
		color_name = color.split(' ')[1];
		color_count = Number(color.split(' ')[0]);
		count[color_name]+=color_count;	
	}
	return Object.keys(count).map(k => count[k]<=limits[k]).reduce((acc,v)=>acc&&v,true);
}

let response = 0;
for (let game of data){
	let game_number = Number(game.split(':')[0].trim().split(' ')[1]);
	let sets = game.split(':')[1].trim();
	let possible = true;
	for(let set of sets.split(';')){
		possible&&=getSetConfiguration(set.trim());
	}
	if(possible===true){
		response+=game_number;
	}
}


console.log(response);
