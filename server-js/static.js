class aaa{
    static age=100000;
    static logt(){
        return  "love❤";
    }
    year = 2004;
    yearprint(){
        return ++this.year;
    }
}
console.log(aaa.age);
console.log(aaa.logt());

const a = new aaa();
console.log(a.year);
console.log(a.yearprint());
console.log(aaa.year);