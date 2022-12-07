const fs = require('fs')

let data = null;

try{
	data = fs.readFileSync('./inp.txt','utf8');
} catch(err){
	console.error(err);
}

const rps = {'A':'X','B':'Y','C':'Z'}
const win_rules = {'A':'Y','B':'Z','C':'X'}
const points = {'win':6,'draw':3,'loose':0}
const move_values = {'X':1,'Y':2,'Z':3}
const input = data.split('\n').filter(row=>row.length===3)


let score = 0 

for (let round of input){
	let opponent_move = round.split(' ')[0];
	let my_move = round.split(' ')[1]; 	
	
	if (win_rules[opponent_move] === my_move){
		score+=move_values[my_move]+points['win']
	}
	else if (rps[opponent_move] === my_move){
		score+=move_values[my_move]+points['draw']
	}
	else{
		score+=move_values[my_move]+points['loose']
	}
}

console.log(score)
