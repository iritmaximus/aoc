use std::fs;
use std::iter::zip;
use std::collections::HashMap;

fn main() {
    println!("Hello, world!");
    let numbers: (Vec<i32>, Vec<i32>) = parse_input_file("./input.txt");

    let left = numbers.0;
    let right = numbers.1;

    let result1: u32 = solve_part1(&left, &right);
    println!("Result (part1): {}", result1);

    let result2: i32 = solve_part2(&left, &right);
    println!("Result (part2): {}", result2);
}

fn solve_part1(left_orig: &Vec<i32>, right_orig: &Vec<i32>) -> u32 {
    let mut left = left_orig.clone();
    let mut right: Vec<i32> = right_orig.clone();

    left.sort();
    right.sort();

    let mut result: u32 = 0;
    for (left_num, right_num) in zip(left, right) {
        result += left_num.abs_diff(right_num);
    }

    result
}

fn solve_part2(left_orig: &Vec<i32>, right_orig: &Vec<i32>) -> i32 {
    let mut result: i32 = 0;

    let mut num_counts: HashMap<i32, i32> = HashMap::new();

    let left: Vec<i32> = left_orig.clone();
    let right: Vec<i32> = right_orig.clone();

    for num in left.iter() {
        match num_counts.get(num) {
            Some(num_count) => {
                result += num * num_count
            }
            None => {
                let num_count = right.iter().filter(|r_num| *r_num == num).count();
                num_counts.insert(*num, num_count.try_into().unwrap());

                result += match num_counts.get(num) {
                    Some(num_count) => num * num_count,
                    None => 0
                }
            }
        }
    }


    result
}

fn parse_input_file(filename: &str) -> (Vec<i32>, Vec<i32>) {
    let contents = fs::read_to_string(filename).expect("Should have read the file");

    let mut numbers_left: Vec<i32> = Vec::new();
    let mut numbers_right: Vec<i32> = Vec::new();


    for item in contents.lines() {
        let right_left: Vec<&str> = item.split_whitespace().collect();
        let left: i32 = right_left[0].parse::<i32>().unwrap();
        let right: i32 = right_left[1].parse::<i32>().unwrap();

        numbers_left.push(left);
        numbers_right.push(right);
    }

    (numbers_left, numbers_right)
}
