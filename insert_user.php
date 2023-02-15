<?php
	require_once "Connect.php";
    if($conn->connect_error){
        echo("Ошибка: " . $conn->connect_error);
    }
	
	$sql = "SELECT * FROM `User_db`;";
	$result = mysqli_query($conn, $sql);
	
if (isset($_POST["User_name"]) && isset($_POST["Login"]) && isset($_POST["Password"]) && isset($_POST["token"])) {
    
	$User_name = $conn->real_escape_string($_POST["User_name"]);
    $Login = $conn->real_escape_string($_POST["Login"]);
	$Password = $conn->real_escape_string(hash('sha3-256' , ($_POST["Password"])));
    $sql = "INSERT INTO `users` (`User_name`, `Login`, `Password`) VALUES ('$User_name', '$Login', '$Password')";
    if($conn->query($sql)){
        echo "Данные успешно добавлены</br>";
    } else{
        echo "Ошибка: " . $conn->error;
    }
	
	include('insert_token.php');
	echo '<a href="test.html" style="text-decoration: none; font-size: 18px;"><p>Главная</p></a>';
	$conn->close();
}
?>