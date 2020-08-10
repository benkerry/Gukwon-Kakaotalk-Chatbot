<?php
    include("dbconn.php");

    $id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['id']));
    $pwd = mysqli_real_escape_string($conn, htmlspecialchars($_POST['pwd']));

    $sql = "SELECT * FROM sign_info WHERE id = '$id'";
    $result = mysqli_fetch_assoc(mysqli_query($conn, $sql));
    $is_authed = false;

    if(isset($result['id'])){
        if(password_verify($pwd, $result['pwd'])){
            session_start();

            $is_authed = true;
            $_SESSION['id'] = $result['id'];
            $_SESSION['pwd_hash'] = $result['pwd'];
            $_SESSION['nickname'] = $result['nickname'];
        }
    }

    session_start();

    if(!$is_authed){
        echo "<script>alert('로그인 정보가 틀립니다.');location.href=\"../index.php\";</script>";
    }
    else if(isset($_SESSION['request_addr'])){
        $addr = $_SESSION['reqeust_addr'];
        unset($_SESSION['request_addr']);

        header("Location:$addr");
    }
    else{
        header("Location:../GenerateAuthCode.php");
    }
?>