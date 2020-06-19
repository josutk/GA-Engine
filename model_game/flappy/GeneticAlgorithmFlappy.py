from genetic_model.GeneticAlgorithm import GeneticAlgorithmTemplate
from tensorflow.keras import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
import random

class GeneticAlgorithmFlappy(GeneticAlgorithmTemplate):

    def __init__(self, neurais_network):
        self.population_size = len(neurais_network)
        self.generation = []
        self.indexs = None
        self.neurais_network = neurais_network

    def template(self, scores):
        self.population()
        self.fitness(scores)
        select_individuals = self.generation[self.indexs]
        for idx in range(0, len(select_individuals), 2):
            self.crossover(idx, idx+1)

        for model in select_individuals:
            mutates_weights = []
            weights = model.get_weights()
            weights_mutate1 = self.mutation(weights[0])
            weights_mutate2 = self.mutation(weights[2])
            mutates_weights.append(weights_mutate1)
            mutates_weights.append(weights[1])
            mutates_weights.append(weights_mutate2)
            mutates_weights.append(weights[3])
            model.set_weights(mutates_weights)

    def population(self):
        for nn in self.neurais_network:
           self.generation = np.append(self.generation, nn)

    def fitness(self, scores):
        np_scores = np.array(scores)
        self.indexs = np_scores.argsort()[-(int(self.population_size/2)):][::-1]

    def crossover(self, idx1, idx2):
        weights1 = self.generation[idx1].get_weights()
        weights2 = self.generation[idx2].get_weights()
        newWeight1 = weights2 
        newWeight2 = weights1
        weights1[0] = newWeight1[0]
        weights2[0] = newWeight2[0]
        self.generation[idx1].set_weights(weights1)
        self.generation[idx2].set_weights(weights1)

    def mutation(self, weights):
        for i in range(len(weights)):
            for j in range(len(list(weights[i]))):
                if random.random() > 0.7:
                    if random.randint(0, 5000) % 2 == 0:
                        mutation = random.uniform(-0.8, 0.8)
                        weights[i][j] += mutation
                    else:
                        mutation = random.uniform(-0.8, 0.8)
                        weights[i][j] -= mutation
        return weights

    def new_population(self, birds):
        new_generation = self.generation[self.indexs]
        for bird in birds:
            model = bird.get_neural_network()
            new_generation = np.append(new_generation, model)
        self.generation = new_generation
    
    def save(self):
        idx = 1 
        for model in self.generation:
            model.save_weights("models/model" + str(idx)+ ".keras")
            idx+=1