# Protein-mRNA network Parameter Optimization

This projects fits the parameters of a regulatory network 

## Background Data

* mRNA levels can be measured in a variety of ways.
* The same methods can be applied to all sequences.
* Protein levels are much harder to measure
* Mutants give information 
* It is possible to determine where on the DNA a transcription factor binds. Likewise to determine if two proteins interact, etc.
* Mutations are useful to: reveal components involved in a system, indicate causality, hint at how things are regulated. 

## System Description 

* A/B/C form a loop.
* A activates transcription of B.
* B activates transcription of C.
* A represses B’s activation of C.
* C represses transcription of A. 
* C increases degradation of B (which is otherwise slow).
* Other components are degraded by dx/dt = -kx.
* D is regulated by A, B and/or C but the relationship is unknown 
* Hill coefficients in the system are small integers (1 or 2)

The network showed in the next figure

![system](system.png)

The equation system proposed is:

![equations](eqn_syst.png)


To solve it simmulated annealing and genetic algorithms were applied. An example of genetic algorithms can be found ![here](https://github.com/j-lazo/genetic_algoritm_example).

## Data

The Experimental data that needs to be fit is shown in the figures bellow:


![Experimental_1](results/Experimental_1.png)

When *mD* is not considered


![Experimental_2](results/Experimental_2.png)

When *mD* is considered

![Experimental_3](results/Experimental_3.png)

Overexpression mutants, transcription.

## Results

Using simulated annealing the results obtained are as follows:

![Comparison_1](results/Comparison_1.png)

![Comparison_2](results/Comparison_2.png)

![Comparison_3](results/Comparison_3.png)
