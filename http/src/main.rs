fn main(){
    let ipstr = String::new();
    let args = std::env::args();
    if args.len() != 2{
        eprintln!("Usage: showip hostname\n");
        return ;
    }

    // 查找addrinfo hints, *res, *p
}