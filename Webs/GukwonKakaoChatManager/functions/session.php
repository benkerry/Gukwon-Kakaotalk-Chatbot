<?php
    session_start();
    include("dbconn.php");

    if(!isset($_SESSION['id']) || !isset($_SESSION['pwd_hash'])){
        $_SESSION['request_addr'] = $_SERVER['REQUEST_URI'];
        echo "<script>alert('올바르지 못한 세션입니다.');if(document.location.href.includes('functions')) location.href=\"../index.php\"; else location.href=\"index.php\"</script>";
    }
    else{
        $id = mysqli_real_escape_string($conn, $_SESSION['id']);
        $pwd_hash = mysqli_real_escape_string($conn, $_SESSION['pwd_hash']);
        $nickname = mysqli_real_escape_string($conn, $_SESSION['nickname']);

        $sql = "SELECT COUNT(*) FROM sign_info WHERE id = '$id' AND pwd = '$pwd_hash' AND nickname='$nickname'";
        $num_row = mysqli_fetch_array(mysqli_query($conn, $sql))[0];
        if($num_row == 0){
            echo "<script>alert('올바르지 못한 세션입니다.');if(document.location.href.includes('functions')) location.href=\"../index.php\"; else location.href=\"index.php\"</script>";
        }
    }
?>