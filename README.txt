These are supplementally files for "Differential, Linear and Meet-in-the-middle attacks on the lightweight block cipher RBFK"

1. sbox
 1.1 main_differential_probability_sbox.c
 1.2 main_linear_probability_sbox.c
 These files are used to calculate DP or LP for S-box.
 They are written by c.
 
2. Differential
 2.1 Rbfk_DCP_functions.py
 2.2 Rbfk_lp.py
  These two files are used to generate lp-file for gurobi.
  When we execute "Rbfk_lp.py", the lp-file named "rbfk.lp" is generated.
 2.3 main.py
 2.4 rbfk.py
  These two files are used to execute "rbfk.lp".
 2.5 print_characteristics.py
  This file is used to print characteristic and the number of active s-box.
  
3. Linear
 All files are same as Differential.
