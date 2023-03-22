use std::fs::File;
use std::io::{self, BufRead, BufReader};

// template
enum RPC {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

enum ABC {
    A = 1,
    B = 2,
    C = 3,
}

enum XYZ {
    Y = 1,
    X = 2,
    Z = 3,
}

fn main() {
    println!("Hello, world!");
    let result: i32 = 0;
    let lines = read_lines("input.txt".to_string());
    for line in lines {
	let chars_str = line.as_ref().unwrap();
	let chars: Vec<&str> = chars_str.split(" ").collect();
	if chars.len() != 2 {
	    println!("{}", result);
	    return;
	}
    }
}

fn read_lines(filename: String) -> io::Lines<BufReader<File>> {
    let file = File::open(filename).unwrap();
    return io::BufReader::new(file).lines();
}
