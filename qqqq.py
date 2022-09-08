import java.util:*;
public class Monte Carlo Simulation
{
Static scnner console = new scanner (system.in)
public static void main (string [] args)
{
int demandsize, predictionsize
demand probability, cummulative probabilitry, rangetop, rangebottom

system.out.print ("Enter the number of demands to be processed:");
demandsize = console.next Int();
system.out.printIn();
double [] demand = new double [demandSize];
double [] probability = new double [demand size];
double [] cummulative prob = new double [demand size];
double [] rangetop = new double [demand size];
double [] rangebottom = new double [demand size];
For (int i=0; i<demandsize; i++)
{
system.out.print ('Enter the demand on days", i+1); 
deemand [i] = console.nextDouble();
system.out.printIn();
system.out.print ("Enter coressponding probability;");
probability [i] = console.nextDouble();
if (i==0)
	cummulative probability [i] = probability [i]
	rangeTop[i] = rangeBottom [i] = (cum prob.[1]*100)-1
else
	cummulative prob [i] = probability [i] + probability [(i+1)]
	rangetop= [i] = (cummulative prob [(i+1)]*100)-1
	rangebottom = [i] (cummulative prob [i] * 100)-1
system.out.print ("Enter the number of days to be predicted;");
predictionsize = console.nextInt();
double[] random number = new double [ pediction size];
double[] result demand = new double [ pediction size];
for (int j = 0; j<predictionsize; j++)
{
system.out.print (Enter random day for day;",j);
randnumber [j] = console.nextDouble ();
for (int K=0; K<demandsize, K++)
{
if (rangeTop [k] > randnumber [i] < rangebottom [k]
resultdemand [j] = demand [k]
}
sum = sum + resultdemand [j]
}
averagedemand = sum/predictionsize
for (int i=0; i < demand size; i++)
{
system.out.print ("DD", "PROB", "CPROB", "RNRANGE");
for (int I=0; I < demandSize; I++)
{
system.out.print(demand [L], probability [L], cummulativeprob [L] rangetop [L], "-", rangebottom [L]);
}
system.out.printIn ();
for (int m = 0; M= prediction size; m++)
{
system.out.print ("days", "random Numbers", "result demand"),
for (int m=0; m<prediction size; m++)
{
system.out.print (m, randnumber, result demand);
}
system.out.printIn ();
system.out.print (" the average demand is : ", average demand);
