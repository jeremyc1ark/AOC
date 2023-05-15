use std::fs::File;
use std::io::{BufRead, BufReader};


fn get_elf_list() -> Vec<i32> {
    let file: File = File::open("input.txt").expect("Failed to open file.");
    let reader: BufReader<File> = BufReader::new(file);

    let mut elf_list: Vec<i32> = Vec::new();
    let mut current_elf: i32 = 0;

    for line in reader.lines() {
        if let Ok(s) = line {
            if s.trim().is_empty() {
                elf_list.push(current_elf);
                current_elf = 0;
            } else {
                let meal: i32 = s.parse::<i32>().unwrap();
                current_elf += meal;
            }
        }
    }
    elf_list.push(current_elf);

    elf_list
}

#[allow(dead_code)]
pub fn part_1() -> i32 {
    let elf_list: Vec<i32> = get_elf_list();
    let mut highest_elf: i32 = 0;

    for elf in elf_list {
        if elf > highest_elf {
            highest_elf = elf;
        }
    }
    highest_elf
}

/*
Takes a list of elves and a new elf. Adds the new elf to the list if
it's greater than any of its elements.
 */
fn prioritize_elves(top_elves: &mut Vec<i32>, new_elf: &i32) {
    top_elves.push(*new_elf);
    top_elves.sort_by(|a, b| b.cmp(a));
    top_elves.pop();
}

#[allow(dead_code)]
pub fn part_2() -> i32 {
    let elf_list: Vec<i32> = get_elf_list();
    let mut top_elves: Vec<i32> = elf_list[0..=2].to_vec();

    for elf in &elf_list[3..] {
      prioritize_elves(&mut top_elves, elf);
    }

    top_elves.iter().sum()
}