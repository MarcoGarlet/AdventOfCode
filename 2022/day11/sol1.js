const fs = require('fs');
const fname = './inp.txt';

let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
}catch(e){
	console.error('Error in reading ',fname);
	process.exit(1);
}


let monkeys = [];

function parseMonkeys(lines){
	let monkeyIndex = -1;
	for(let i=0;i<lines.length;i++){
		if(i%6===0){
			monkeyIndex+=1;
			monkeys.push({})
		}
		else{
			let line = lines[i];
			let att = line.split(' ')[2].replaceAll(':','');
			switch(att){
				case 'Starting':
					monkeys[monkeyIndex].items = line.split(' ').slice(4).map(number=>parseInt(number.replaceAll(',','')));
				break;
				case 'Operation':
					monkeys[monkeyIndex].operation = new Function('o','return '+(line.split(' ').slice(5).map(w=>(w==='old'||w==='new')?w[0]:w).reverse().reduce((noun,exp='')=>{return exp+=' '+noun})));  

				break;				
				case 'Test':
					monkeys[monkeyIndex].test = (val)=>(val%parseInt(line.split(' ')[5]))===0;
				break;
				default:
					switch(line.split(' ')[5].replaceAll(':','')){
						case 'true':	
							monkeys[monkeyIndex].true = parseInt(line.split(' ')[9])
						break;
						case 'false':
							monkeys[monkeyIndex].false = parseInt(line.split(' ')[9])
						break;
					}
				break;
		
			}
		
		}

	}

}

data = data.split('\n').filter(line=>line.length>0);
parseMonkeys(data);
monkeys.map(monkey=>monkey.n_items = 0)

for(let round = 0;round<20;round++){
	for (let monkey of monkeys){
		for(let [i,item] of monkey.items.entries()){
			let w = item;
			w=monkey.operation(w)
			w = Math.floor(w/3);
			monkeys[monkey[monkey.test(w)]].items.push(w);
			monkey.n_items+=1
		}

			monkey.items = [];

	}

}

result = monkeys.map(monkey=>monkey.n_items).sort((a,b)=>{return b-a}).slice(0,2).reduce((el,acc=1)=>{return acc*el} )
console.log(result)





