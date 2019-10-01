<?php
    include('dbconn.php');
    session_start();

    $sql = "SELECT COUNT(*) FROM sign_info WHERE id = '".$_SESSION['id']."' AND pwd = '.$_SESSION['pwd'].'";
    $num_row = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

    if($num_row == 0){
        session_destroy();
        echo "<script>alert('올바르지 못한 세션입니다.');location.href=\"../index.php\";</script>";
    }
?>