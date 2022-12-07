const fs = require('fs');
const fname = './inp.txt';


const base_lower = 1;
const base_upper = 27;
let data = null;

try{
	data=fs.readFileSync(fname,'utf-8');
}catch (error){
	console.error(error);
	process.exit();
}

let input = data.split('\n').filter(line=>line.length>0);

result = 0;

for (let row of input){
	let item1 = [... new Set(row.substr(0,row.length/2>>0))], item2 = [...new Set(row.substr(row.length/2>>0))];
	
	let tot_items = [...item1, ...item2];
	tot_items =tot_items.filter(c=>(item1.includes(c)&&item2.includes(c)))[0];
	
	basec = (tot_items === tot_items.toUpperCase())?'A':'a';
	base = (tot_items === tot_items.toUpperCase())?base_upper:base_lower;
	result +=  base + (tot_items.charCodeAt(0)-basec.charCodeAt(0));
}

console.log(result)




