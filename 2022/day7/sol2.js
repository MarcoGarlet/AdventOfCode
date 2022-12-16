const fs = require('fs');
const fname = 'inp.txt';


let data = undefined;

try{
	data = fs.readFileSync(fname, 'utf-8');
} catch(err){
	console.log('Error in reading file');
	process.exit(1);
}



class Dir{
	name;
	adj;
	parentNode;
	size;
	constructor(name, parentNode=null, adj=[]){
		this.name = name;
		this.adj = adj;
		this.parentNode = parentNode;
		this.size = -1;
	}

	setSize(){
		let size=0;
		for (let node of this.adj){
			size+=node.setSize();
		}	

		this.size = size;
		return size;
	}

}

class File{
	constructor(name,size){
		this.name = name;
		this.size = parseInt(size);
	}

	setSize(){
		return this.size;
	}
}



data = data.split('\n').filter(row=>row.length>0);
let command = []

for (let i=0;i<data.length;){
	let comm,out;
	comm = data[i];
	out = [];
	i++;
	while (i<data.length&&data[i][0]!=='$'){
		out.push(data[i]);
		i++;
	} 

	command.push({'command':comm,'output':out});
}



let current_node = new Dir('/');
let dirs = [current_node];
for (let c of command){
	let comm = c['command'].split(' ').slice(1);
	let out = c['output'];
	switch(comm[0]){
		case 'cd':
			switch(comm[1]){
				case '/':
					while (current_node.parentNode!==null)
						current_node = current_node.parentNode;
					break;

				case '..':
					current_node = current_node.parentNode;
					break;

				default:
					current_node = current_node.adj.filter(node=>node.name===comm[1])[0];
					break;
			}
				
		break;
		case 'ls':
			for (let line of out){
				let p = line.split(' ');
				new_node = (p[0]==='dir')? new Dir(p[1],current_node):new File(p[1],p[0]);
				if(p[0]==='dir')
					dirs.push(new_node)
				current_node.adj.push(new_node);
				
			}	
		
		break;
		default:
		break;
	}

}


while(current_node.parentNode!==null)
	current_node=current_node.parentNode;

current_node.setSize()


const totSpace = 70000000;
let freeSpace =  totSpace - dirs[0].size;
const bound = 30000000;
let space2free = bound-freeSpace;



console.log(Math.min(... dirs.filter(dir=>dir.size>=space2free).map(dir=>dir.size) ))

