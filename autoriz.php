<?php
	echo '<script language="javascript">';
	echo 'alert("Вы вошли как: Tester")';
	echo '</script>';

	if ( !empty($_REQUEST['password']) and !empty($_REQUEST['login']) and $_POST['token']) {
		
		$Login = $_REQUEST['login'];
		$Password = hash('sha3-256' , $_REQUEST['password']);
		$file = $_POST['token'];
		
		$query = 'SELECT * FROM `aut` WHERE Login="'.$Login.'" AND L="'.$L.'" AND x.y="'.$Q.'" AND q="'.$q.'"';
		$result = mysqli_query($link, $query)
		
		$array = Array (
			"0" => Array (
				"1" => $L, 
				"2" => $Q, 
				"3" => $q
			)
		);
		$json = json_encode(array('data' => $array));
		file_put_contents("data.json", $json)
		
		$f = fopen($file, 'r');
		$line = fgets($f);
		fclose($f);
		
		$res = sell_exec('python Aut.py ' . escapeshellarg(json_encode($line))); 
		$resultData = json_decode($res);
		
		$query = 'SELECT `Login`, `Password` FROM `users` WHERE Login="'.$Login.'" AND Password="'.$Password.'" AND User_name="'.$User_name.'"';
		$result = mysqli_query($link, $query);
		$user = mysqli_fetch_assoc($result);
		
		if (!empty($user)) {
			session_start(); 
			$_SESSION['auth'] = true;
			$_SESSION['login'] = $user['login']; 
			echo "<script>alert('$resultData $User_name')</script>";
		} else {
			echo "<script>alert('$resultData')</script>";
		}
	}
echo '<a href="test.html" style="text-decoration: none; font-size: 18px;"><p>Главная</p></a>';
?>