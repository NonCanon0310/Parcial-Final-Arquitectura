#!/usr/bin/perl

#Fichero especializad para la ejecucion en lotes ejecutables
$path= "/home/ubuntu/Descargas/PARCIA_ARQ/Ejecuciones";

@Ejecutables=("MMcpp", "MM1c");

@VectorSize= ("200","400","600","800","1000");


$repeticiones = 2;

foreach $exe (@Ejecutables)
{
      foreach $ves (@VectorSize)
      {
            $file = "$path/"."$exe"."-Size-"."$ves".".txt";
            #print "$file \n"; #este es el nombre del archivo vale!! 
            for($i=0; $i<$repeticiones; $i++)
            {
                  system("$path/$exe $ves >> $file");
                  #print "$path/$exe $ves \n";                  
            }
      }
}    
