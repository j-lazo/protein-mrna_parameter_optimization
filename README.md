# Protein-mRNA network Parameter Optimization

This projects fits the parameters of the regulatory network showed in the next figure

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
