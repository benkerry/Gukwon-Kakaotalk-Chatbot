<?php
    include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");
    
    $sql = "SELECT COUNT(*) FROM sign_info WHERE id = '".$_POST['id']."'";
    $count = mysqli_fetch_array(mysqli_query($conn, $sql))[0];
    
    if($count > 0){
        echo "<script>alert(\"이미 존재하는 아이디입니다.\");history.back();</script>";
    }
    else{
        $sql = "SELECT root FROM auth_code WHERE auth_code = '".strtoupper($_POST['auth_code'])."'";
        $result = mysqli_query($conn, $sql);
        $num_rows = mysqli_num_rows($result);

        if($num_rows == 0){
            echo "<script>alert(\"인증번호가 유효하지 않습니다.\");history.back();</script>";
        }
        else if(($result = mysqli_fetch_array($result))[0] == 0){
            echo "<script>alert(\"가입 권한이 없는 인증번호입니다.\");history.back();</script>";
        }
        else{
            $sql = "INSERT INTO sign_info VALUES('".htmlspecialchars($_POST['id'])."', '".htmlspecialchars($_POST['id'])."', ".$_POST['rdo'].", '".htmlspecialchars($_POST['nickname'])."')";
            mysqli_query($conn, $sql);
            echo "<script>alert(\"가입 성공!\");location.href='index.php';</script>";
        }
    }
?>