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
	return count;
}

let response = [];
for (let game of data){
	let game_number = Number(game.split(':')[0].trim().split(' ')[1]);
	let sets = game.split(':')[1].trim();
	const min_cubes = {'red':0,'green':0,'blue':0}
	for(let set of sets.split(';')){
		count=getSetConfiguration(set.trim());
		Object.keys(min_cubes).map(color => min_cubes[color]=Math.max(min_cubes[color],count[color]));
	}
	response.push(Object.keys(min_cubes).map(color=>min_cubes[color]).reduce((acc,v)=>acc*v,1));
}


console.log(response.reduce((acc,v)=>acc+v,0));
