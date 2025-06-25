#! /usr/bin/perl


open (DATA, "./data/db.dat");
@data = <DATA>;
close DATA;

srand(time ^ $$);
$num = rand(@data);

($name, $path) = split(/::/, $data[$num]);

chomp($path);


open (DATA, "./data/$path/db.dat");
@image = <DATA>;
close DATA;

srand(time ^ $$);
$numb = rand(@image);

print "Location: http://www.eqguilded.com/freefire/gallery/$path/$image[$numb]\n\n";
