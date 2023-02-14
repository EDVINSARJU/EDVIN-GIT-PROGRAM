<h1>This is my hegde </h1>
<?php
 $a=$_POST["name"];
 $b=$_POST["college"];
 $c=$_POST["fff"];
 $d=$_POST["ggg"];
 if(isset ($_POST["add"]))
 {
	 $e=$c+$d;
	 echo $e;
 }
 if(isset ($_POST["sub"]))
 {
	 $e=$c-$d;
	 echo $e;
 }
 echo "$a<br> Welcome to $b <br>";
?>