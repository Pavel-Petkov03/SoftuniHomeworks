# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter
# what and that is exactly what you are called to do for this problem.
# On the first line you will be given the population (numbers separated by comma and space ", ").
# On the second line you will be given the minimum wealth. You have to distribute the wealth, so that
# there is no part of the population that has less than the minimum wealth. To do that, you should always
# take wealth from the wealthiest part of the population. There will be cases, where the distribution will
# not be possible. In that case, print "No equal distribution possible"
population = [int(num) for num in input().split(", ")]
wealth_level = int(input())

if sum(population) < len(population) * wealth_level:
    print('No equal distribution possible')
else:
    poorest = min(population)

    while poorest < wealth_level:
        poorest_index = population.index(poorest)
        richest = max(population)
        richest_index = population.index(richest)

        needed = wealth_level - poorest
        can_take = richest - wealth_level
        redistributed_wealth = min(needed, can_take)
        population[poorest_index] += redistributed_wealth
        population[richest_index] -= redistributed_wealth

        poorest = min(population)

    print(population)




