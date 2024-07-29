class stack{
	constructor(){
		this.array = [];
		this.size = -1;
	}
	add(num){
		this.array.push(num);
		this.size += 1;
	}
	peek(){
		return this.array[this.size];	
	}
	size(){
		return this.size + 1;
	}
}

var temp = new stack();
temp.add(12);
temp.add(13);
temp.add(66666);
var size = temp.size();
console.log(size);
var top = temp.peek();
console.log(top);
