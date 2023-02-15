<?php
	require_once "Connect.php";
    if($conn->connect_error){
        echo("Ошибка: " . $conn->connect_error);
    }
	$sql = "SELECT * FROM `aut`;";
	$result = mysqli_query($conn, $sql);
	
	json_decode(shell_exec('Regist.py' . base64_encode(json_encode($User_name))));
	$string = file_get_contents("datas.json");
	$json_a = json_decode($string, true);
	$path1 = $json_a['path1'];
	$path2 = $json_a['path2'];
	$path3 = $json_a['path3'];
	$path4 = $json_a['path4'];
	
	$file = $_POST['token'];
    $fh = fopen($file, 'w');
    fwrite($fh, 'Test.6301913719');
    fclose($fh);
	
	$sql = "INSERT INTO `Aut`(`User_name`, `L`, `x.y`, `q`) VALUES ('$User_name', '$path1', '$path2', '$path3')";
    if($conn->query($sql)){
        echo "Данные успешно добавлены</br>";
    } else{
        echo "Ошибка: " . $conn->error;}
?>