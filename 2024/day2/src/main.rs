use std::fs;

fn main() {
    println!("Hello, world!");
    let contents = parse_input_file("./input.txt");

    let result1 = solve_part1(&contents);
    println!("Result part1: {}", result1);

    let result2 = solve_part2(&contents);
    println!("Result part2: {}", result2);
}

fn count_results(reports: &Vec<Vec<i32>>, selector: &dyn Fn(&Vec<i32>, i32) -> bool) -> i32 {
    let mut result: i32 = 0;

    for report in reports {
        result += match selector(&report, 0) {
            true => 1,
            false => 0,
        }
    }

    result
}

fn solve_part1(reports: &Vec<Vec<i32>>) -> i32 {
    count_results(&reports, &is_monotonic_and_properly_gapped)
}

fn solve_part2(reports: &Vec<Vec<i32>>) -> i32 {
    count_results(&reports, &is_monotonic_and_properly_gapped_with_errors)
}

fn is_monotonic_and_properly_gapped(line: &Vec<i32>, _depth: i32) -> bool {
    let is_previous_increasing: bool = (line[0] - line[1]) > 0;
    for idx in 0..(line.len() - 1) {
        let difference: i32 = line[idx] - line[idx + 1];

        if difference.abs() > 3 || 1 > difference.abs() {
            return false;
        }

        if difference > 0 && is_previous_increasing != true {
            return false;
        }
        if difference < 0 && is_previous_increasing == true {
            return false;
        }
    }
    true
}

fn is_monotonic_and_properly_gapped_with_errors(line: &Vec<i32>, depth: i32) -> bool {
    if line.len() < 2 {
        return false;
    }

    let is_previous_increasing: bool = (line[0] - line[1]) > 0;
    for idx in 0..(line.len() - 1) {
        let difference: i32 = line[idx] - line[idx + 1];

        if difference.abs() > 3 || 1 > difference.abs() {
            for idx_i in 0..(line.len() - 1) {
                let mut without_index: Vec<i32> = line.to_owned();
                without_index.remove(idx_i);
                if depth >= 0 && is_monotonic_and_properly_gapped_with_errors(&without_index, depth - 1) {
                    return true;
                };
            }
            return false;
        }

        if difference > 0 && is_previous_increasing != true {
            for idx_i in 0..(line.len() - 1) {
                let mut without_index: Vec<i32> = line.to_owned();
                without_index.remove(idx_i);
                if depth >= 0 && is_monotonic_and_properly_gapped_with_errors(&without_index, depth - 1) {
                    return true;
                };
            }
            return false;
        }
        if difference < 0 && is_previous_increasing == true {
            for idx_i in 0..(line.len() - 1) {
                let mut without_index: Vec<i32> = line.to_owned();
                without_index.remove(idx_i);
                if depth >= 0 && is_monotonic_and_properly_gapped_with_errors(&without_index, depth - 1) {
                    return true;
                };
            }
            return false;
        }
    }
    true
}

fn parse_input_file(filename: &str) -> Vec<Vec<i32>> {
    let mut reports: Vec<Vec<i32>> = Vec::new();
    let file = fs::read_to_string(filename).expect("Should open the file");

    for line in file.lines() {
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        reports.push(numbers);
    }

    reports
}
