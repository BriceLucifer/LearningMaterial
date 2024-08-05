use std::{
    io::Write, 
    net::{TcpListener, TcpStream},
    fs
};

fn main(){
    let listener = TcpListener::bind("127.0.0.1:7878");
    if let Ok(listen) = listener {
        // 处理stream
        for stream in listen.incoming(){
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

fn handle_connection(mut stream: TcpStream) {
    let buffer = [0; 1024];
    let get = b"GET / HTTP/1.1\r\n";

    let (status_line, filename) = if buffer.starts_with(get) {
        ("HTTP/1.1 200 OK", "./hello.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND", "./404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();

    let response = format!(
        "{}\r\nContent-Length: {}\r\n\r\n{}",
        status_line,
        contents.len(),
        contents
    );

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}
