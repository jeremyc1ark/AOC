use std::fs::File;
use std::io::{BufRead, BufReader};

#[allow(dead_code)]
pub fn part_1() -> i32 {
    let file: File = File::open("input.txt").expect("Failed to open file.");
    let reader: BufReader<File> = BufReader::new(file);

    let mut highest_elf: i32 = 0;
    let mut current_elf: i32 = 0;

    for line in reader.lines() {
        if let Ok(s) = line {
            if s.trim().is_empty() {
                highest_elf = if current_elf > highest_elf {current_elf} else {highest_elf};
                current_elf = 0;
            } else {
                let meal: i32 = s.parse::<i32>().unwrap();
                current_elf += meal;
            }
        }
    }
    highest_elf = if current_elf > highest_elf {current_elf} else {highest_elf};
    highest_elf
}
