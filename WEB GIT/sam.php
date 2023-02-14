<?php
$con=new mysqli("localhost","root","","sarju");
if($con->connect_error)
{
  die("connection failed".$con->connect_error);
}
if(isset($_POST['submit']))
{
	$name=$_POST['name'];
	$hour1=$_POST['h1'];
	$hour2=$_POST['h2'];
	$sql="INSERT INTO attendance(name,h1,h2)VALUE('$name','$hour1','$hour2')";
$result=$con->query($sql);
  if($result==TRUE)
{
			echo "INSERTED SUCESSFULLY";
}
}
$eql="SELECT * from attendance";
$result=$con->query($eql);
echo '<table><tr><th>ROLLNO</th><th>NAME</th><tr>';
while($row=$result->fetch_assoc())
{
	echo'<tr><td>'.$row['rollno'].'</td><td>'.$row['name'].'</td></tr>';
	
}
echo '</table>';
?>
<form method="post">
NAME:<input type="text" name="name" id="name"><br><br>
HOUR1:<input type="text" name="h1" id="h1"><br><br>
HOUR2:<input type="text" name="h2" id="h2"><br><br>
<input type="submit" value="SUBMIT" name="submit" id="submit">
</form>