import math
import random

"""Decides if an infection has occurred"""
def infect(infect_chance: float) -> bool:
    return random.random() < infect_chance

"""Decides if a recovery has occurred"""
def recover(recover_chance: float) -> bool:
    return random.random() < recover_chance

"""Decides which people come into contact with an infected person"""
def contact_indices(pop_size: int, source: int, contact_range: int) -> list:
    contact_list = []
    for index in range(source - contact_range, source + contact_range + 1):
        if 0 <= index < pop_size:
            contact_list.append(index)
    return contact_list

"""Decides whether or not the infected person recovers at a given day"""
def apply_recoveries(population: list, recover_chance: float) -> None:
    for index in range(len(population)):
        if population[index] == 'I' and recover(recover_chance):
            population[index] = 'R'

"""Simulates an infected person coming into contact with other people"""
def contact(population: list, source: int, contact_range: int, infect_chance: float) -> None:
    contact_list = contact_indices(len(population), source, contact_range)
    for index in contact_list:
        if population[index] == 'S' and infect(infect_chance):
            population[index] = 'I'

"""Simulates all of the infected people in the population coming into contact with other people"""
def apply_contacts(population: list, contact_range: int, infect_chance: float) -> None:
    infect_list = []
    for index in range(len(population)):
        if population[index] == 'I':
            infect_list.append(index)
            
    for index in infect_list:
        contact(population, index, contact_range, infect_chance)

"""Counts the number who are susceptible, infected, and recovered"""
def population_SIR_counts(population: list) -> dict:
    return {"susceptible": population.count('S'), "infected": population.count('I'), "recovered": population.count('R')}

"""Simulates one day in the progression of the disease"""
def simulate_day(population: list, contact_range: int, infect_chance: float, recover_chance: float):
    apply_recoveries(population, recover_chance)
    apply_contacts(population, contact_range, infect_chance)

"""Initializes the state of the population"""
def initialize_population(pop_size: int) -> list:
    population = ['S'] * pop_size # In day 1, the entire population is susceptible
    population[math.floor(random.random() * pop_size)] = 'I' # Except one random person, who is infected
    return population

"""Simulate each day in the progression of the disease"""
def simulate_disease(pop_size: int, contact_range: int, infect_chance: float, recover_chance: float) -> list:
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts] # This list contains the states of each day during the disease outbreak
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts

"""Finds the peak infection"""
def peak_infections(all_counts: list) -> int:
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections

"""Displays the state of each day in the progression of the disease"""     
def display_results(all_counts: list) -> None:
    num_days = len(all_counts)
    print("Day".rjust(14) + "Susceptible".rjust(14) + "Infected".rjust(14) + "Recovered".rjust(14)) # print the result in a table format
    for day in range(num_days):
        line = str(day).rjust(14)
        line += str(all_counts[day]["susceptible"]).rjust(14)
        line += str(all_counts[day]["infected"]).rjust(14)
        line += str(all_counts[day]["recovered"]).rjust(14)
        print(line)
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))


"""Trial run"""
counts = simulate_disease(100, 10, .2, .05)
display_results(counts)