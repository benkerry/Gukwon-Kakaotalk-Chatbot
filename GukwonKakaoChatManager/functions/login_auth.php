<?php
    include('dbconn.php');

    $sql = "SELECT * FROM sign_info WHERE id = '".$_POST['id']."'";
    echo $sql;
    $result = mysqli_fetch_assoc(mysqli_query($conn, $sql));
    $is_authed = false;

    if(isset($result['id'])){
        if(password_verify($_POST['pwd'], $result['pwd'])){
            session_start();

            $is_authed = true;
            $_SESSION['id'] = $_POST['id'];
            $_SESSION['pwd_hash'] = $result['pwd'];
        }
    }

    if(!$is_authed){
        echo $result['pwd'];
        //echo "<script>alert('Login Data is not valid');location.href=\"../index.php\";</script>";
    }
    else{
        header("Location:../GenerateAuthCode.php");
    }
?>