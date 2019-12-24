# Valentin Macé
# valentin.mace@kedgebs.com
# Developed for fun
# Feel free to use this code as you wish as long as you quote me as author

"""
main.py
~~~~~~~~~~

Main file for this project

Here I provide some examples for you to run easily,
you just need ton uncomment the part you want and comment what you don't want,
each part is independent of others
"""

from game import*
from genetic_algorithm import *

"""
Use this to run a saved player and add a row to the result file
Use d isplay= False to make a tournament between the saved players
Use display = True (default) to actually watch the saved player play.
"""
def loadPlayer(name='', display=True, result_file='result.csv'):
    net.load(filename_weights='saved/'+ name + '_weights.npy', filename_biases='saved/'+ name + '_biases.npy')
    game.player_name = name.capitalize()
    score = game.start(display = display, neural_net=net)
    with open(result_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name.capitalize(), score])
            file.close

"""
Watch games of snake played by my best neural nets !

Only 3 games are played here but you can load more networks from the saved folder if you wish
"""
net = NeuralNetwork()
game = Game()

#Tournement
for i in range(100):
    loadPlayer('joseph')
    loadPlayer('GSO-Gen13-LongCubeFoisAge')
    loadPlayer('GSO-NokiaScore_Gen24')
    loadPlayer('joseph')
    loadPlayer('valentin')
    loadPlayer('larry')
    loadPlayer('adam')
    loadPlayer('jason')
    loadPlayer('juan')
    loadPlayer('kevin')


#Mine
#loadPlayer('GSO-Gen13-LongCubeFoisAge')
#loadPlayer('GSO-NokiaScore_Gen24')

# Joseph is the funniest to watch, he always does something cool
#loadPlayer('joseph')

# Valentin is safe and precise
#loadPlayer('valentin')

# Larry is very very safe but also my best network, don't hesitate to run him a few times if he's doing loops
#loadPlayer('larry')

#the others
#loadPlayer('adam')
#loadPlayer('jason')
#loadPlayer('juan')
#loadPlayer('kevin')


"""
Play a game of snake !

I do not recommend it as it is in first person and not that fun
But if you want, you can
"""
#game = Game()
#game.start(playable=True, display=True, speed=10)


"""
Train your own snakes !

Starts the genetic algorithm with parameters that I've already tested
Best snake of each generation is saved in current folder
The training speed depend a lot on your CPU and its cores number

Contact me if you know how to make it run on GPU
"""
#gen = GeneticAlgorithm(population_size=1000, crossover_method='neuron', mutation_method='weight')
#gen.start()











# Hey pssst, you, yes you.. Sometimes I boost training by making the snake already huge at the begining
# Also don't hesitate to put a iteration limit in the game loop (see game.py)