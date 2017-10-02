# 42 US - Silicon Valley

## Walking Marvin

### Who is Marvin?

Marvin, the Paranoid Android, is a fictional character in
The Hitchhiker's Guide to the Galaxy series by Douglas Adams.
Marvin is the ship's robot aboard the starship Heart of Gold.

### Goals

This is a python project, that uses OpenAI Gym with an environment called Marvin.
The goal is to train Marvin to walk, having the training and walking process.
The total reward for each episode after training is bigger than 100. During the
development, we learned how to use neural networks to help Marvin
get back on his feet, without using any libraries that do the goal of the
project for us, like Evostra or Tensorflow.

![Walking Process](resources/walking_process.gif)

### Usage

**Basic form:**

`python marvin.py`

The program display log for each episode.

**Advanced options:**

| Flags               | Description                                                                                   |
| :------------------ |:--------------------------------------------------------------------------------------------- |
| `–-walk (-w)`       | Display only walking process.                                                                 |
| `–-video (-v)`      | Saves videos of the walking process.                                                          |
| `–-name (-n)`       | Display the name of the game (environment).                                                   |
| `--generation (-g)` | Change the maximum number of generations.                                                     |
| `--population (-p)` | Count of the population between each generation.                                              |
| `--rate (-r)`       | Mutation rate (recommended values in the range of decimals).                                  |
| `--movement (-m)`   | umber of steps (movement) between each episode.                                               |
| `–-load (-l)`       | Load weights for Marvin agent from a file. Skip training process if this option is specified. |
| `–-save (-s)`       | Save weights to a file after running the program.                                             |
| `–-quiet (-q)`      | Hide the program's log between each episode.                                                  |
| `–-help (-h)`       | Display available commands and exit.                                                          |
| `–-log`             | Save a log of each generation to a file. Expects a path.                                      |
| `–-version`         | Show program's version number and exit.                                                       |

*If the program launches without arguments, display training process and walking
process.*

### Setup

Use `sh setup.sh` to setup and build all the dependencies.

*All the dependencies will be installed to the user by running the script...*

### TODO

* Make use of the average fitness of a generation, so it doesn't deviate from the parent.
* Check if by changing code from the source file can interfere with loading the file (of a different version
of the program). If it does, create some kind of flag to validate the version.

### Resources

The following sources helped us during the development of this project:

* [OpenAI Gym documentation](https://gym.openai.com/docs)
* [NEAT Super Mario World](https://www.youtube.com/watch?v=qv6UVOQ0F44) (to understand what we have to do):
* [OpenAI-NEAT Project example](https://github.com/HackerHouseYT/OpenAI-NEAT)
* [OpenAI Gym bipedal walker](https://gym.openai.com/evaluations/eval_ujFWHmoqSniDh8cErKCVpA)
* [Neuroevolution - Wikipedia Article](https://en.wikipedia.org/wiki/Neuroevolution)
* [Artificial Neural Network - Wikipedia Article](https://en.wikipedia.org/wiki/Artificial_neural_network)
* [Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf) (Kenneth O. Stanley and Risto Miikkulainen)

## Contributors

* [JR Aleman](https://github.com/jraleman/)
* [Gerardo Solis](https://github.com/corezip/)

## License

This project is under the MIT License;
