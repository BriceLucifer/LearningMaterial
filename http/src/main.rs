use std::{
    io::{BufRead, BufReader, Write}, 
    net::{TcpListener, TcpStream}
};

fn main(){
    let listener = TcpListener::bind("127.0.0.1:7878");
    if let Ok(Listen) = listener {
        // 处理stream
        for stream in Listen.incoming(){
            if let Ok(success) = stream {
                println!("Connect successfully");
                handle_connection(success);
            }else {
                println!("Connect Error")
            }
        }
    }else {
        println!("bind error")
    }
}

fn handle_connection(mut stream:TcpStream){
    
    // 缓存区
    let bufreader = BufReader::new(&mut stream);
    // 请求信息 
    let _http_request:Vec<_> = bufreader
                .lines()
                .map(|x|{
                    if let Ok(buffer) = x {
                        return buffer;
                    }else {
                        eprintln!("error bufreader");
                        return String::new();
                    }
                })
                .take_while(|line| !line.is_empty())
                .collect();

    //println!("Request: {:#?}",http_request);
    let response = "HTTP/1.1 200 OK\r\n\r\n";
    // write a website
                
    //stream.write_all(response.as_bytes()).unwrap();
}