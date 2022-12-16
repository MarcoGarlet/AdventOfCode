const fs = require('fs');
const fname = './inp.txt';


let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
}catch (err){
	console.log('Error in reading file');
	process.exit(1);
}

[last,...input] = [... data.split('\n')].reverse();
input.reverse();

let pos = input.indexOf('');

let stacks = input.slice(0,pos);
let moves = input.slice(pos+1)

stacks = stacks.map((line) => { return [... Array(line.length).keys()].filter(element=>element===2||(element-2)%4===0).map(pos=>line[pos-1])});

[piles,...stacks] = [... stacks].reverse()
stacks.reverse()
let res = 0;

piles_dict = {} 

t = [... Array(piles.length).keys()].map(element=>piles_dict[parseInt(element)]=stacks.map(el=>el[element]).filter(el=>el!==' '))

for (let move of moves){
	quantity = parseInt(move.split(' ')[1]);
	from = parseInt(move.split(' ')[3])-1;
	to = parseInt(move.split(' ')[5])-1;
	moved_item = piles_dict[from].slice(0,quantity)
	piles_dict[from] = piles_dict[from].slice(quantity);
	piles_dict[to] = [...moved_item, ...piles_dict[to]]
}

res = ''
for (let k in Object.keys(piles_dict)){
	res+=piles_dict[k][0]
}
console.log(res)









