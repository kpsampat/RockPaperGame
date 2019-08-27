#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: kishan
"""

def play():
    continue_playing = True
    while continue_playing:  
        p_choice_1 = raw_input("What do you choose?")
        # You need to validate user input too
        while p_choice_1 not in ("Rock", "Paper", "Scissors"):
            print("Please try again")
            p_choice_1 = raw_input("What do you choose?")
        p_choice_2 = raw_input("What do you choose?")
        while p_choice_2 not in ("Rock", "Paper", "Scissors"):
            print("Please try again")
            p_choice_2 = raw_input("What do you choose?")
        if p_choice_1 == p_choice_2:
            print("Tie!")
        elif p_choice_1 == "Rock" and p_choice_2 == "Paper":
            print("You Lose!")
        elif p_choice_1 == "Rock" and p_choice_2 == "Scissors":
            print("You Win!")
        elif p_choice_1 == "Paper" and p_choice_2 == "Scissors":
            print("You Lose!")
        elif p_choice_1 == "Paper" and p_choice_2 == "Rock":
            print("You Win!")
        elif p_choice_1 == "Scissors" and p_choice_2 == "Rock":
            print("You Lose!")
        elif p_choice_1 == "Scissors" and p_choice_2 == "Paper":
            print("You Win!")
        play_again = raw_input("Play again?")
        while play_again not in ("Yes", "No"): 
            print("Please try again")
            play_again = raw_input("Play again?")
        if play_again == "No":
            print("Game Over")
            continue_playing = False

def main():
    while True:
        begin = raw_input("Would you like to play Rock, Paper, Scissors?")
        if begin == "Yes":
            play()
        elif begin == "No":
            print("Game Over")
        else:
            print("Please try again")
        break

