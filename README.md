# linear_equations

This program solves a system of equations for any number of unknown varaibles,
 as long as there are the same number of equations as there are variables.

The equations have to be formated like this: 'ax +by +cz +... =d'. 
There has to be one space between each termand each term must be connected to the '+' or '=' in front of it. 
If you want to write 'ax -by =c', you have to write 'ax +-by =c'. You cannot write 'x +y =-2', 
you have to write '1x +1y =-2' 

Also the equations has to be in the file 'equations.txt' with a new equation on each row and no extra rows
 and each equation has to include all of the terms in the same order, just set the coefficients to zero in front of the variables you do not want in the equation. 
 For example you cannot write '3x =3' if you have two equations, write '3x +0y =3'.
