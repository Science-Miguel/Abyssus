<html>
<head>
</head>
<body>
	<?php
	$user_curator = $_POST['fcurator'];
	$user_name = filter_var($_POST['fname']);
	$email = filter_var($_POST['femail']);
	$pas1 = filter_var($_POST['fpas1']);
	$pas2 = filter_var($_POST['fpas2']);
		if ($pas1 === $pas2){
			$servername = "tepeu.lcg.unam.mx";
			$username = "danielaf";
			$password = "f4l31n4d";
			$con = new mysqli($servername, $username, $password, "Abyssus");
			if ($con->connect_error){
				die ("Connection failed: " . $con->connect_error);
			}
			echo "<p>Connection successful</p>";
			$sql= "SELECT user_email FROM ACCOUNTS WHERE user_email = '$email';";
			$check = $con -> query($sql);
			if ($check->num_rows == 0){
				$id = "SELECT user_id FROM ACCOUNTS";
				$ids = $con -> query($id);
				$lastid = end($ids -> fetch_array());
				sscanf($lastid, "U_%d", $nextid_num);
				$nextid_num += 1;
				$nextid = implode(array("U_", $nextid_num), "");
				echo "<p> '$nextid' </p>";
				$Add = "INSERT INTO ACCOUNTS (user_id, user_name, user_email, user_password, user_curator, user_on) VALUES ('$nextid', '$user_name', '$email', '$pas1', '$user_curator', 1);";
				if ($con -> query($Add) === TRUE){
					echo "<p>Registro de usuario correcto.</p>";
					echo "<p>Thanks for registering, $user_name </p>";
				}else{
					"<p>Error: '$Add' <br> '$con->error' </p>";
				}
			}else{
				die ("El email ya está registrado en la base de datos.");
			}
			$con->close();
		} else {
			echo "<p>Las contraseñas no coinciden. Por favor, verifique los datos.</p>";

		}
	?>
</body>
</html>
