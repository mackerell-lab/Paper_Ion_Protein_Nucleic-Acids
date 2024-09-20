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

     while ((output=fopen("10.0.pdb", "w"))==NULL)
       {
           {
            printf ("Can't open output file\n");
             exit(0);}

       }

          while ((input=fopen("10.0.xyz", "r"))==NULL)
       {
           {
            printf ("Can't open intput file\n");
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
	   int last = nmol - 1;
	   k = nmol + 2 ;
	   fscanf(input,"\n");
           i = 2 ;
	   fprintf(output,"REMARK CREATED BY YNAN\n");
	   fprintf(output,"REMARK\n");
	   int count=1;
           while ( i < k )
		{
           		fscanf(input,"%s  %f %f %f \n",&atom, &x, &y, &z);
                        fprintf(output,"ATOM%7d  %-4s%-8s%d    %8.3f%8.3f%8.3f  1.00  0.00      %s\n",count,&atype[i-2][60],&residue[i-2][60],residueid[i-2],x,y,z,&residue[i-2][60]);
			i++;
			count++;
		}
           int hi=2;
	   count++;
	   fprintf(output,"TER%8d      %s%6d\n",count,&residue[last][60],hi);
	   fprintf(output,"END");

           
      fclose(output);
      fclose(input);
      fclose(fp);
      return 0;
       
        }  //while 1


} // main
