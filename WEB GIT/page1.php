<html>
<head>
<style>
</style>
<body>
<h1>Hello</h1>
<form action="page2.php" method="POST">
Name<input type="text" name="name"><br><br>
College<input type="text" name="college"><br><br>
Number1<input type="text" name="fff"><br><br>
number2<input type="text" name="ggg"><br><br>
<button name="add">add</button>
<button name="sub">sub</button>

</form>



<?php
$name="EDVIN";
echo "<h2 style='color:red'>".$name."</h2>";
$address="Kovil vilai manali <br>Thuckalay <br> kanyakumari";
echo "<h2 style='color:blue'>".$address."</h2>";
$phonenumber="8940752414";
echo "<h3>$phonenumber<h3>";
$a=100;
$b=70;
$c=$a-$b;
echo "<h3>$c</h3>";
echo "The difference between ".$a." and".$b." is ".$c;
$d=0;
/*while($d<20)
{
	if($d%2==0)
	{
    echo "Even number print".$d."<br>";
	}
	else
	{
     echo "Odd number print".$d."<br>";
	}
    $d++;
	}
*/
for($e=0;$e<20;$e++)
	
	{
if($e%2==0 && $e<=10)
{
	echo "Even number".$e."<br>";
}
else if ($e%2!=0 && $e>=10) 
{
	echo "Odd number".$e."<br>";
}
	}
	$g=array("red","blue","green","yellow");
	echo $g[2]."<br>";
 foreach($g as $element)
 {
 echo $element."<br>";
 }
 $h=array("Name"=>"sarju","Roll no"=>"42","Age"=>"22");
  echo $h["Name"];
  foreach($h as $key=>$value)
  {
	  echo "$key is $value"."<br>";
  }

 ?>
 


</body>
</head>
</html>