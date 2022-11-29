#!/usr/bin/perl
#######################################################################
# Rich's vote.cgi program
#
#	This program takes votes for peoples favorite Robert Cray
#	Albums.  It will keep the voting results in a text file.
#	Thats about it!  Cheers!
#
#
#
#  These are the settings that you need to change for your site.
#	$VoterInfo 	Log file for storing visitor browser info
#	$results	Vote results


require "cgi-lib.pl";

MAIN:
{
$VoterInfo = "vote.log";
$results = "votes.txt";
########################################################################################################
#  This line is need on all HTML
  print &PrintHeader;
  &ReadParse(*input);




# Count the votes!
if ($input{'name'} =~ /Who's Been Talking/)
	{
	$results="who.txt";
	}
#   <OPTION>Too Many Cooks

if ($input{'name'} =~ /Too Many Cooks/)
	{
	$results="too.txt";
	}

#   <OPTION>Bad Influence
if ($input{'name'} =~ /Bad Influence/)
	{
	$results="bad.txt";
	}

#   <OPTION>False Accusations
if ($input{'name'} =~ /False Accusations/)
	{
	$results="false.txt";
	}

#   <OPTION>Strong Persuader
if ($input{'name'} =~ /Strong Persuader/)
	{
	$results="strong.txt";
	}

#   <OPTION>Don't Be Afraid of the Dark
if ($input{'name'} =~ /Don't Be Afraid of the Dark/)
	{
	$results="dont.txt";
	}
#   <OPTION>Midnight Stroll
if ($input{'name'} =~ /Midnight Stroll/)
	{
	$results="mid.txt";
	}
#   <OPTION>I Was Warned
if ($input{'name'} =~ /I Was Warned/)
	{
	$results="warn.txt";
	}
#   <OPTION>Shame + A Sin
if ($input{'name'} =~ /Shame/)
	{ 
	$results="shame.txt";
	}
#   <OPTION>Some Rainy Morning
if ($input{'name'} =~ /Some Rainy Morning/)
	{
	$results="some.txt";
	}
#   <OPTION>Sweet Potato Pie
if ($input{'name'} =~ /Sweet Potato Pie/)
	{
	$results="pie.txt";
	}
#
if ($input{'name'} =~ /Take Your Shoes Off/)
	{
	$results="shoes.txt";
	}

#   <OPTION>Heavy Picks
if ($input{'name'} =~ /Heavy Picks/)
        {
        $results="heavy.txt";
        }

#   <OPTION>Shoulda Been Home
if ($input{'name'} =~ /Shoulda Been Home/)
	{
	$results="home.txt";
	}

#   <OPTION>Time Will Tell
if ($input{'name'} =~ /Time Will Tell/)
	{
	$results="tell.txt";
	}
#
unless (open (VOTEFILE, $results)) {
        die ("cannot open vote file");
	}
$votes=<VOTEFILE>;
close(VOTEFILE);
$votes++;
unless (open (VOTEFILE, ">$results")) {
        die ("cannot open vote file");
	}
print VOTEFILE "$votes";
close(VOTEFILE);

open (LOGFILE, ">>$VoterInfo")|| die ("Oops error on if");
# Select the Log file for output and print to it.
print LOGFILE "$ENV{'REMOTE_HOST'},$ENV{'HTTP_REFERER'},$ENV{'HTTP_USER_AGENT'} $date $input{'name'}\n";
close (LOGFILE);
print "<head><title>Thanks</title></head><BODY>\n";
print "<H1> Thanks! </H1>\n";
print "<HR>\n";
print "Your vote: $input{'name'}<P>";
print "<P>";
print " <A HREF=\"index.cgi\">Go back to the results page</A><BR>\n";
print "</BODY></HTML>\n";

}
