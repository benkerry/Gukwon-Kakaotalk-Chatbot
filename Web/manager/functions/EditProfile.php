<?php
    include("session.php");

    if(isset($_POST['req_type'])){
        if(password_verify(htmlspecialchars($_POST['password']), $_SESSION['pwd_hash'])){
            $id = mysqli_real_escape_string($conn, htmlspecialchars($_SESSION['id']));
            
            if($_POST['req_type'] == "change_email"){
                $email = mysqli_real_escape_string($conn, htmlspecialchars($_POST['email']));

                $sql = "UPDATE sign_info SET email = '$email' WHERE id = '$id'";
                mysqli_query($conn, $sql);
            }
            else if($_POST['req_type'] == "change_nickname"){
                $nickname = mysqli_real_escape_string($conn, htmlspecialchars($_POST['nickname']));
                $sql = "SELECT COUNT(*) FROM sign_info WHERE nickname='$nickname'";
                $nick_cnt = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                if($nick_cnt == 0){
                    $_SESSION['nickname'] = $nickname;

                    $sql = "UPDATE sign_info SET nickname = '$nickname' WHERE id = '$id'";
                    mysqli_query($conn, $sql);
                }
                else{
                    echo "<script>alert('이미 존재하는 닉네임입니다.');history.back();</script>";
                }
            }
            else if($_POST['req_type'] == "change_password"){
                if($_POST['next_password'] == $_POST['next_password_chk']){
                    $next_password = mysqli_real_escape_string($conn, htmlspecialchars($_POST['next_password']));
                    $pwd_hash = password_hash($next_password, PASSWORD_DEFAULT);
                    $_SESSION['pwd_hash'] = $pwd_hash;

                    $sql = "UPDATE sign_info SET pwd = '$pwd_hash' WHERE id = '$id'";
                    mysqli_query($conn, $sql);
                }
                else{
                    echo "<script>alert('변경할 패스워드를 다시 확인해주세요.');history.bach();</script>";
                }
            }
            echo "<script>alert('정보변경 성공!');location.href='../EditProfile.php';</script>";
        }
        else{
            echo "<script>alert('패스워드가 틀렸습니다.');history.back();</script>";
        }   
    }
    else{
        echo "<script>alert('잘못된 요청입니다.');history.back();</script>";
    }
?>
