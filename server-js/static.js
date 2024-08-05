class Liuyunxiang{
    static age=100000;
    static logt(){
        return  "love❤";
    }
    year = 2004;
    yearprint(){
        return ++this.year;
    }
}
console.log(Liuyunxiang.age);
console.log(Liuyunxiang.logt());

const a = new Liuyunxiang();
console.log(a.year);
console.log(a.yearprint());
console.log(Liuyunxiang.year);