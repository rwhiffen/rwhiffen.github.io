#!/usr/bin/perl
#######################################################################
# Rich's index.cgi program
#
# 	This one displays the results of the Robert Cray voting
#
#
#
#
#  These are the settings that you need to change for your site.
#	$FileName 	Log file for storing visitor browser info

require "cgi-lib.pl";

MAIN:
{

########################################################################################################
#  This line is need on all HTML
  print &PrintHeader;

$Total_Votes = 0;
#  Open the above text files

print "<HEAD>\n";
print "  <TITLE>Voting Booth</TITLE>\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=\"#FFFFFF\">\n";

print "<H1>Rich Whiffen's <I>Favorite Robert Cray Albums</I> Voting booth</H1>\n";

print "<P>\n";
print "<HR>\n";
print "This is the place! Cast your vote for your favorite all time Robert
Cray Album. I know it can be an agonizing proposition. Depending on
my mood, any album can be my favorite, but you can only pick one!
Choose carefully!</P>\n";


print "<P>Here are the results so far:</P>\n";

print "Who's Been Talking: \n";

$results="who.txt";
unless (open (VOTEFILE, $results)) {
        die ("cannot open vote file");
	}
$votes=<VOTEFILE>;
close(VOTEFILE);
print "<b>$votes</b><BR>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../cooks.html\">Too Many Cooks ( Tomato Records)</A>: \n";
	$results="too.txt";
	unless (open (VOTEFILE, $results)) {
       	 die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../bad.html\">Bad Influence (1983, Hightone Records)</A>: \n";

	$results="bad.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../false.html\">False Accusations (1985, Hightone Records)</A>: \n";
	$results="false.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../strong.html\">Strong Persuader (1986, PolyGram Records)</A>: \n";
	$results="strong.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../dark.html\">Don't Be Afraid of the Dark (1988, PolyGram Records)</A>: \n";
	$results="dont.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../stroll.html\">Midnight Stroll (1990, PolyGram Records)</A>: \n";
	$results="mid.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../warned.html\">I Was Warned (1992, PolyGram Records)</A>: \n";
	$results="warn.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../shame.html\">Shame + A Sin (1993, PolyGram Records)</A>: \n";
	$results="shame.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><BR>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../rainy.html\">Some Rainy Morning (1995, PolyGram Records)</A>: \n";
	$results="some.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../pie.html\">Sweet Potato Pie (1997, Mercury Records)</A>: \n";
	$results="pie.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../shoes.html\">Take Your Shoes Off (1999, Rykodisc)</A>: \n";
	$results="shoes.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../picks.html\">Heavy Picks - The Robert Cray Band Collection (1999, Mercury Records)</A>: \n";
	$results="heavy.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../home.html\">Shoulda Been Home (2001, Rykodisc)</A>: \n";
	$results="home.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<A HREF=\"../tell.html\">Time Will Tell (2003, Sanctuary)</A>: \n";
	$results="tell.txt";
	unless (open (VOTEFILE, $results)) {
        	die ("cannot open vote file");
		}
	$votes=<VOTEFILE>;
	close(VOTEFILE);
	print "<b>$votes</b><br>\n";
$Total_Votes = $Total_Votes + $votes;
print "<P>&nbsp;</P>\n";
print " There are $Total_Votes so far!  Keep them comming!<BR>\n";
print "<H3><A HREF=\"vote.html\">Cast your vote!</A></H3>\n";

print "<P>&nbsp;</P>\n";


print "<P>\n";
print "<HR>\n";
print "<A HREF=\"http://www.claris.com/\"><IMG SRC=\"../Images/chpmade.gif\"
WIDTH=117 HEIGHT=33 X-SAS-UseImageWidth X-SAS-UseImageHeight BORDER=0
ALIGN=bottom></A> <A HREF=\"http://www.apple.com/\"><IMG
SRC=\"../Images/macmade.gif\" WIDTH=88 HEIGHT=31 X-SAS-UseImageWidth
X-SAS-UseImageHeight BORDER=0 ALIGN=bottom></A>\n";
print "<HR>\n";
print "Created: 3/3/97<BR>\n";

print "Mod: 7/17/03<BR>\n";

print "By: rwhiffen<BR>\n";

print "</P>\n";
print "</BODY>\n";
print "</HTML>\n";

}
