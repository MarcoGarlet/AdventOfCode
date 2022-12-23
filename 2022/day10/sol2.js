const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
}catch(e){
	console.error('Error in reading ', fname);
	process.exit(1);
}

prog = data.split('\n').filter(line=>line.length>0)

let clock = [];
let sprite_pos = [];
let v = 1;


function sol(){
	let res='';
	for (let i=0;i<clock.length;i++){
		let i1 = i%40;
		if(sprite_pos[i][1][i1+1]==='#')
			res+='#'
		else
			res+='.'
	}
	return res;
}



let sprite = [... Array(40).keys()].map(p=>'.');
sprite[0]='#';
sprite[1]='#';
sprite[2]='#';

for (let line of prog){
	let inst = line.split(' ')[0];
	switch(inst){
		case 'addx':
			let arg = parseInt(line.split(' ')[1]);
			clock.push([v,v,v]);
			sprite_pos.push([sprite,sprite,sprite]);
			clock.push([v,v,v+arg]);
			sprite_upd = [... Array(40).keys()].map(p=>'.');
			sprite_upd[v+arg] = '#';
			sprite_upd[v+arg+1] = '#';
			sprite_upd[v+arg+2] = '#';
	
			sprite_pos.push([sprite,sprite,sprite_upd]);	
			sprite = [...sprite_upd]
			v+=arg;
		break;
		case 'noop':
			clock.push([v,v,v]);
			sprite_pos.push([sprite,sprite,sprite]);
		
		break;	
	
		default:
		break;
	}

}

res = sol();

for (let i=0;i<res.length/40;i++){
	console.log(res.slice(i*40,i*40+40))	
}


