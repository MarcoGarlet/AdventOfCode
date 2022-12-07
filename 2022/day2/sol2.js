const fs = require('fs')

let data = null;

try{
	data = fs.readFileSync('./inp.txt','utf8');
} catch(err){
	console.error(err);
}

const rps = {'A':'A','B':'B','C':'C'}
const win_rules = {'A':'B','B':'C','C':'A'}
const points = {'Z':6,'Y':3,'X':0}
const move_values = {'A':1,'B':2,'C':3}
const input = data.split('\n').filter(row=>row.length===3)


let score = 0 

for (let round of input){
	let opponent_move = round.split(' ')[0];
	let result = round.split(' ')[1]; 	
	let my_move;	
	if (result === 'Z'){
		my_move = win_rules[opponent_move];
	}
	else if (result === 'Y'){
		my_move = opponent_move;
	}
	else{
		my_move = Object.keys(rps).filter(move=>move!==opponent_move && move!= win_rules[opponent_move])[0]
	}

	score+=points[result]+move_values[my_move];
}

console.log(score)
