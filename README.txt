To simulate the disease spread through a population, we will keep track of the condition of each person in the population. The idea behind our model is based on the commonly used SIR model (https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model). The possible conditions are:

- Susceptible (encoded as ‘S’). This means that the person is healthy, but does not have any immunity to the disease, so is susceptible to infection.
- Infected (encoded as ‘I’). This means that the person is currently infected with the disease. They can potentially infect others with the disease, and they can potentially recover from the disease.
- Recovered (encoded as ‘R’). This means that the person has recovered from the disease. We will assume that people who have recovered from the disease have immunity, and cannot be reinfected.

Our simulation will track the status of the population with a list of strings, where each string stores the current status of one person in the population. At the beginning of our simulation, only one person will be infected, and the rest will be infected. For example, if there are 8 people in the population, this list would start as

[‘I’, ‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘S’]

The simulation will run one day at a time. On each day, We record the number of people who are currently susceptible, infected, and recovered.
- Each infected person comes in contact with some other people in the population. Each of these people may become infected, based on a random chance.
- Each infected person may recover, based on random chance.

Our simulation will end once there is no longer anyone in the population who is infected. In addition to recording the counts of susceptible, infected, and recovered people for each day, we will also compute the peak number of infections during the course of the simulation. This peak infection value is important, since hospital resources are limited, and if many people are infected at the same time, those resources might be depleted.