<?php
    include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

    $_POST['id'] = htmlspecialchars($_POST['id']);
    $_POST['pwd'] = htmlspecialchars($_POST['pwd']);

    $sql = "SELECT * FROM sign_info WHERE id = '".$_POST['id']."'";
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
        //echo "<script>alert('로그인 정보가 틀립니다.');location.href=\"../index.php\";</script>";
    }
    else{
        header("Location:../GenerateAuthCode.php");
    }
?>