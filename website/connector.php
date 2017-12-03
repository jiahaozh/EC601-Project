<?php 

define('DB_NAME', 'Login');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_HOST', 'localhost');
$link = mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
if (!$link) {
	die('Could not connect: ' . mysql_error());
}
$db_selected = mysql_select_db(DB_NAME, $link);
if (!$db_selected) {
	die('Can\'t use ' . DB_NAME . ': ' . mysql_error());
}
$value1 = $_POST['first_name'];
$value2 = $_POST['last_name'];
$value3 = $_POST['email_add'];
$value4 = $_POST['password'];
$value5 = $_POST['age'];
$value6 = $_POST['gender'];
$sql = "INSERT INTO demo (first_name,last_name,email_add,password,age,gender) VALUES ('$value1', '$value2','$value3','$value4','$value5','$value6')";
if (!mysql_query($sql)) {
	die('Error: ' . mysql_error());
}
mysql_close();
?>
