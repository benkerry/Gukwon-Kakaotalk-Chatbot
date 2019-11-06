<?php
    include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");
    session_start();

    if(!isset($_SESSION['id']) || !isset($_SESSION['pwd_hash'])){
        echo "<script>alert('올바르지 못한 세션입니다.');location.href=\"../index.php\";</script>";
    }
    else{
        $sql = "SELECT COUNT(*) FROM sign_info WHERE id = '".$_SESSION['id']."' AND pwd = '".$_SESSION['pwd_hash']."'";
        $num_row = mysqli_fetch_array(mysqli_query($conn, $sql))[0];
        if($num_row == 0){
            echo "<script>alert('올바르지 못한 세션입니다.');location.href=\"../index.php\";</script>";
        }
    }
?>