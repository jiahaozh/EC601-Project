<!DOCTYPE html>
<html>
<head>
	<title>Register</title>
	<link rel="stylesheet" href="stylesheet.css">
</head>

<body>
	<h1>Stock Predictor</h1>
	<center>
		<h3>Registration Form</h3>
		<form action="connector.php" method="post"/>
		
		<b>First Name</b>*	<input type="text" name="first_name" required="req">
		
		<b>Last Name</b>*<input type="text" name="first_name" required="req1"><br><br>
		
		<b>Email Address</b>*<input type="email" name="first_name" required="req2">
		
		<b>Password</b>*<input type="password" name="password" required="req3" maxlength="20"><br><br>
		
		<b>Age</b>*<input type="text" name="age" required="req4">
		
		<b>Gender</b> <input type="radio" name="gender" value="male" > Male
  				<input type="radio" name="gender" value="female"> Female
 			 	<input type="radio" name="gender" value="other"> Other
 			 	<br><br><br>

 		<input type="submit" name="Register" id="Register" >
	</center>

</body>
</html>
