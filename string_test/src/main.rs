
fn main() {
    let name = "hello world";
    let b = name.as_ptr();
    // let temp = unsafe {
    //     *b
    // };
    
    // for i in 0..name.len(){
    //     let mut temp = unsafe {
    //         *b.wrapping_add(i)
    //     };
    //     println!("{:#},{:#?}",temp,char::from(temp));
    // }
    let  inter = vec![0,1,2,3,4,5,6].iter().map(|x|{
        let mut temp = unsafe {
            *b.wrapping_add(*x)
        };
        println!("{:#},{:#?}",temp,char::from(temp));
    });

    println!("Hello, world!,{:#?},{:#?}",unsafe {   
        *b
    },unsafe {
        *b.wrapping_add(1)
    });
    
        let data = vec![vec![1, 2], vec![3, 4], vec![5, 6, 7, 8]];
        let new_data :Vec<usize>= data.iter().flat_map(|v| v.clone()).collect(); //Flat_map类型
        println!("new_data :{:?}", new_data);
        for v in new_data.iter() {
            println!("v:{:?}", v);
        }

}
