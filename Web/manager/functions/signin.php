<?php
    include("dbconn.php");

    $id = mysqli_real_escape_string($conn, htmlspecialchars($_POST['id']));
    $pwd = mysqli_real_escape_string($conn, htmlspecialchars($_POST['pwd']));
    $pwd_check = mysqli_real_escape_string($conn, htmlspecialchars($_POST['pwd_chk']));
    $nickname = mysqli_real_escape_string($conn, htmlspecialchars($_POST['nickname']));
    $authcode = mysqli_real_escape_string($conn, htmlspecialchars(strtoupper($_POST['auth_code'])));
    $email = mysqli_real_escape_string($conn, htmlspecialchars($_POST['email']));
    
    $sql = "SELECT COUNT(*) FROM sign_info WHERE id = '$id'";
    $id_count = mysqli_fetch_array(mysqli_query($conn, $sql))[0];
    $sql = "SELECT COUNT(*) FROM sign_info WHERE nickname = '$nickname'";
    $nick_count = mysqli_fetch_array(mysqli_query($conn, $sql))[0];
    
    if($id_count > 0){
        echo "<script>alert(\"이미 존재하는 아이디입니다.\");history.back();</script>";
    }
    else if($nick_count > 0){
        echo "<script>alert(\"이미 존재하는 닉네임입니다.\");history.back();</script>";
    }
    else{
        $sql = "SELECT root FROM manager_auth_code WHERE auth_code = '$authcode'";
        $result = mysqli_query($conn, $sql);
        $num_rows = mysqli_num_rows($result);
        $result = mysqli_fetch_assoc($result);

        if($num_rows == 0){
            echo "<script>alert(\"인증번호가 유효하지 않습니다.\");history.back();</script>";
        }
        else if(empty($id) || empty($nickname) || empty($email) || empty($pwd)){
            echo "<script>alert(\"모든 정보를 제대로 입력했는지 다시 확인해주세요.\");history.back();</script>";
        }
        else if(strlen($pwd) < 6){
            echo "<script>alert(\"패스워드가 너무 짧습니다.\");history.back();</script>";
        }
        else if($pwd != $pwd_check){
            echo "<script>alert(\"비밀번호를 다시 확인해주세요.\");history.back();</script>";
        }
        else{
            $pwd_hash = password_hash($pwd, PASSWORD_DEFAULT);
            $root = (string)$result['root'];

            $sql = "INSERT INTO sign_info VALUES('$id', '$pwd_hash', $root, '$nickname', '$email')";
            mysqli_query($conn, $sql);
            $sql = "DELETE FROM manager_auth_code WHERE auth_code='$authcode'";
            mysqli_query($conn, $sql);
            echo "<script>alert(\"가입 성공!\");location.href='../index.php';</script>";
        }
    }
?>