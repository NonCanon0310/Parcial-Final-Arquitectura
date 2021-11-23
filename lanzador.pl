#!/usr/bin/perl

#fichero especializado para la ejecucuión en lotes ejecutables

$path="/home/ubuntu/Descargas/PARCIA_ARQ/Python";

@Ejecutables=("MMPython.py");

@VectorSize= ("200","400","600","800","1000");

$repeticiones=2;

foreach $exe (@Ejecutables)
{
    foreach $ves (@VectorSize)
    {
        $file = "$path/"."$exe"."-Size-"."$ves".".txt";
        #print "$file \n"; #este es el nombre del archivo vale!! 
        for($i=0; $i<$repeticiones;  $i++)
        {
            system("python3 $exe $ves >> $file");
            # print "python3 $exe $ves \n";
        }
    }
}