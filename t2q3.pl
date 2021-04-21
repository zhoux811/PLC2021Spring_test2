use String::Random;
use Data::Dumper;


$iteration_n = 9999;

%names_n_ages;   #define hash
my $name_gen = String::Random->new;


my $start = time; #timer1 start!
my $counter = 0;
while( $counter < $iteration_n )
{
    $name = $name_gen->randregex('[A-Z]{5}');
    if (exists $names_n_ages{$name}) 
    {
        #do nothing
    }
    else 
    {
        $names_n_ages{$name} = $age = int(rand(100));
        $counter ++;
    }
	#print("\n$counter", ":", "$name" ,"\,", "$age" );
}
my $end = time;   #end timer1

#print "\n",Dumper(\%names_n_ages);
print "\nhash length:", $size = keys %names_n_ages, " , time lapsed: ",  $end - $start;

sleep(1);

my $start = time(); #timer2 start!
my @array;        #define array
my $counter = 0;
while( $counter < $iteration_n )
{
    $name = $name_gen->randregex('[A-Z]{5}');
    if (not grep( /^$name$/, @array[0] ) )  
    {
        $array[0][$counter] = $name;
        $array[1][$counter] = $age = int(rand(100));
        $counter ++;
    }
	#print("\n$counter", ":", "$name" ,"\,", "$age" );
}
my $end = time();   #end timer2
#print "\n",Dumper(\@array[0]) ,  Dumper(\@array[1]);
print "\narray[1] and [2] length: ", scalar(@{ $array[1] })," and ", scalar(@{ $array[0] }) ," time lapsed: ",  $end - $start;;