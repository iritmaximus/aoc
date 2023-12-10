use std::fs::File;
use std::io::{self, BufRead, BufReader};


fn parse_rpc_str(rpc_string: &str) -> Result<i32, &str> {
    match rpc_string {
        "A" | "X" => return Ok(1), // Rock
        "B" | "Y" => return Ok(2), // Paper
        "C" | "Z" => return Ok(3), // Scissors
        _ => Err("Incorrect value :D"), // error lol
    }
}

fn game_result(p1: &str, p2: &str) -> i32 {
    let p1_score = parse_rpc_str(p1).unwrap();
    let p2_score = parse_rpc_str(p2).unwrap();

    // RPC
    // Rock     1
    // Paper    2
    // Scissors 3


    // lol the problem wasn't even the calculations
    match p1_score {
        1 => {
            if p2_score == 1 {
                return 3 + p1_score;
            }
            if p2_score == 2 {
                return 0 + p1_score;
            }
            if p2_score == 3 {
                return 6 + p1_score;
            }
        },
        2 => {
            if p2_score == 1 {
                return 6 + p1_score;
            }
            if p2_score == 2 {
                return 3 + p1_score;
            }
            if p2_score == 3 {
                return 0 + p1_score;
            }
        },
        3 => {
            if p2_score == 1 {
                return 0 + p1_score;
            }
            if p2_score == 2 {
                return 6 + p1_score;
            }
            if p2_score == 3 {
                return 3 + p1_score;
            }
        },
        _ => return 8000,
    }

    println!("No result from here: {}, {}", p1_score, p2_score);
    return 8000;
}
fn part2_game_result(p1: &str, p2: &str) -> i32 {
    let p1_score = parse_rpc_str(p1).unwrap();
    let p2_score = parse_rpc_str(p2).unwrap();

    match p1_score {
        1 => return 0 + if p2_score == 1 {3} else {p2_score - 1},
        2 => return 3 + p2_score,
        3 => return 6 + if p2_score == 3 {1} else {p2_score + 1},
        _ => return 8000,
    }
}


fn main() {
    let mut result: i32 = 0;
    let mut p2_result: i32 = 0;
    let lines = read_lines("input.txt".to_string());
    for line in lines {
        let chars_str = line.as_ref().unwrap();
        let chars: Vec<&str> = chars_str.split(" ").collect();

        if chars.len() != 2 {
            println!("Fake result?: {}", result);
            return;
        }

        // lol the players were the other way around
        result += game_result(chars[1], chars[0]);
        p2_result += part2_game_result(chars[1], chars[0])
    }
    println!("{}", result);
    println!("{}", p2_result);

    let mut test_result: i32 = 0;
    test_result += game_result("A", "Y");
    test_result += game_result("B", "X");
    test_result += game_result("C", "Z");
    test_result += game_result("C", "C");

    println!("{}", test_result);
}

fn read_lines(filename: String) -> io::Lines<BufReader<File>> {
    let file = File::open(filename).unwrap();
    return io::BufReader::new(file).lines();
}
