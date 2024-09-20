#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>
#include <string.h>
int main ()
{   

  int nmol;
  int i,k;
  float x,y,z;
  char atom;
  FILE *output;
  FILE *input;
  FILE *fp;
  
  

       while (1)

        {

     while ((output=fopen("10.0.crd", "w"))==NULL)
       {
           {
            printf ("Can't open output file\n");
             exit(0);}

       }

          while ((input=fopen("10.0.xyz", "r"))==NULL)
       {
           {
            printf ("Can't open output file\n");
             exit(0);}

       }
           
          while ((fp=fopen("Molecule_Information", "r"))==NULL)
       {
           {
            printf ("Can't open molecule information\n");
             exit(0);}

       }


           fscanf(input,"%d\n",&nmol);
	   printf("atom numer is %d\n",nmol);
           
	   char t[60],tt[60];
	   char atype[nmol][60],residue[nmol][60];
	   int resid[nmol],residueid[nmol];
           for (k = 0;k < nmol;k++)
	   {
		   fscanf(fp,"%s %s %d %d\n",&atype[k][60],&residue[k][60],&resid[k],&residueid[k]);
		   strcpy(t ,&atype[k][60]);
		   strcpy(tt, &residue[k][60]);
		   //printf("%s %s\n",read_atype,read_residue);
		   
		   
	   }
	   int n_cation = 2;
	   int n_anion  = 2;
	   int a_cation = 1;
	   int a_anion  = 7;

	   fscanf(input,"\n");
           i = 2 ;
	   fprintf(output,"* GENERATED BY YNAN\n");
	   fprintf(output,"* DATE\n");
	   fprintf(output,"* \n");
	   fprintf(output,"%10d  EXT\n",nmol);
	   int count=1;
	   int hi=1;
	   float weighting=0.00;
	   k = nmol + 2;
           while ( i < k )
		{
           		fscanf(input,"%s  %f %f %f \n",&atom, &x, &y, &z);
                        fprintf(output,"%10d%10d  %-10s%-8s%20.10f%20.10f%20.10f  %-10s%d%27.10f\n",count,resid[i-2],&residue[i-2][60],&atype[i-2][60],x,y,z,&residue[i-2][60],residueid[i-2],weighting);
			i++;
			count++;
		}
           
      fclose(output);
      fclose(input);
      fclose(fp);
      return 0;
       
        }  //while 1


} // main