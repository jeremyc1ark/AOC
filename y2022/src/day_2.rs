use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn _parse_input() -> [Vec<char>; 2] {
    let file: File = File::open("input.txt").expect("Failed to open file.");
    let reader: BufReader<File> = BufReader::new(file);

    let mut opponent_moves: Vec<char> = Vec::new();
    let mut response_moves: Vec<char> = Vec::new();

    for line in reader.lines() {
        if let Ok(s) = line {
            let opponent_move: char = s.chars().nth(0).unwrap();
            let response_move: char = s.chars().nth(2).unwrap();
            opponent_moves.push(opponent_move);
            response_moves.push(response_move);
        }
    }
    [opponent_moves, response_moves]
}

fn _did_you_win(opponent: &str, response: &str) -> i32 {
    if opponent == response {
        return 0;
    }
    let domination_map: HashMap<&str, &str> = HashMap::from([
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock")
    ]);
    let opponent_won: bool = domination_map[opponent] == response;
    if opponent_won {
        return -1;
    }
    1
}

fn _calculate_score(response: &str, outcome: i32) -> i32 {
    let response_to_score_map: HashMap<&str, i32> = HashMap::from([
        ("rock", 1),
        ("paper", 2),
        ("scissors", 3)
    ]);
    let outcome_to_score_map: HashMap<i32, i32> = HashMap::from([
        (-1, 0),
        (0, 3),
        (1, 6)
    ]);
    response_to_score_map[response] + outcome_to_score_map[&outcome]
}

#[allow(dead_code)]
pub fn part_1() -> i32 {
    let code_to_shape_map: HashMap<char, &str> = HashMap::from([
        ('A', "rock"),
        ('B', "paper"),
        ('C', "scissors"),
        ('X', "rock"),
        ('Y', "paper"),
        ('Z', "scissors")
    ]);

    let input = _parse_input();
    let opponent_moves = &input[0];
    let response_moves = &input[1];

    let mut total_score: i32 = 0;

    for i in 0..opponent_moves.len() {
        let opponent_move: &str = code_to_shape_map[&opponent_moves[i]];
        let response_move: &str = code_to_shape_map[&response_moves[i]];
        let outcome: i32 = _did_you_win(opponent_move, response_move);
        let round_score: i32 = _calculate_score(response_move, outcome);
        total_score += round_score;
    }
    total_score
}
