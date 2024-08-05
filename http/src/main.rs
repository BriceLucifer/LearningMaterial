use std::{
    fs, io::{BufRead, BufReader, Write}, net::{TcpListener, TcpStream}
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
    // request_line
    let request_line = bufreader.lines().next().unwrap().unwrap();

    let (status_line, filename) = if request_line == "GET / HTTP/1.1" {
        ("HTTP/1.1 200 OK", "hello.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND", "404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response =
        format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");

    stream.write_all(response.as_bytes()).unwrap();

    // if request_line == "GET / HTTP/1.1"{
    //     let status_line = "HTTP/1.1 200 OK\r\n\r\n";
    //     let contents = fs::read_to_string("hello.html").unwrap();
    //     let length = contents.len();

    //     let response = format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");
    //     stream.write_all(response.as_bytes()).unwrap();
    // }else {
    //     let status_line = "HTTP/1.1 404 NOT FOUND";
    //     let contents = fs::read_to_string("404.html").unwrap();
    //     let length = contents.len();

    //     let response = format!(
    //         "{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}"
    //     );

    //     stream.write_all(response.as_bytes()).unwrap();
    // }

    // 请求信息 
    // let _http_request:Vec<_> = bufreader
    //             .lines()
    //             .map(|x|{
    //                 if let Ok(buffer) = x {
    //                     return buffer;
    //                 }else {
    //                     eprintln!("error bufreader");
    //                     return String::new();
    //                 }
    //             })
    //             .take_while(|line| !line.is_empty())
    //             .collect();

    //println!("Request: {:#?}",http_request);
    // let status_line = "HTTP/1.1 200 OK\r\n\r\n";
    // write a website
    // let contents = fs::read_to_string("hello.html");
    // if let Ok(content) = contents {
        // let length = content.len();
        // let response = format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{content}");
        // stream.write_all(response.as_bytes()).unwrap();
    //}else {
    //     eprintln!("error read_to_string")
    // }
    //stream.write_all(response.as_bytes()).unwrap();
}