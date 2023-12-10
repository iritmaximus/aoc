use std::fs::File;
use std::io::{self, BufRead, BufReader};

const PATH: &str = "./input.txt";

fn main() {
    // 1. read file
    // 2. loop line by line
    // 3. count all values
    // 4. if \n, check sum

    let mut highest_sum: i32 = 0;
    let mut new_sum: i32 = 0;

    let mut highest_sums: Vec<i32> = Vec::new();

    let lines = read_lines(PATH);
    for result in lines {
        let line = result.unwrap();

        if line == "" {
            highest_sum = check_highest_sum(&new_sum, &highest_sum);
            new_sum = 0;
        } else {
            new_sum += line.parse::<i32>().unwrap();
            check_3_highest(&new_sum, &mut highest_sums);
        }
    }

    println!("1. RESULT: {}", highest_sum);
    println!("2. RESULT {:?}", calc_final_result(highest_sums));
}

fn check_highest_sum(new_sum: &i32, highest_sum: &i32) -> i32 {
    if *new_sum > *highest_sum {
        *new_sum
    } else {
        *highest_sum
    }
}

fn check_3_highest(new_sum: &i32, highest_sums: &mut Vec<i32>) {
    if highest_sums.len() < 3 {
        highest_sums.push(*new_sum);
        return;
    }

    highest_sums.sort();
    highest_sums.reverse();

    println!(
        "{} > {} = {}",
        *new_sum,
        *highest_sums.last().unwrap(),
        *new_sum > highest_sums[0]
    );

    if *new_sum > *highest_sums.last().unwrap() {
        highest_sums.pop();
        highest_sums.push(*new_sum);
    }
    println!("{:?}", highest_sums);
}

fn calc_final_result(sum: Vec<i32>) -> i32 {
    sum.iter().sum()
}

fn read_lines(filename: &str) -> io::Lines<BufReader<File>> {
    let file = File::open(filename).unwrap();
    return io::BufReader::new(file).lines();
}
