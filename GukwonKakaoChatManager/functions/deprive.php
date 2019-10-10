<?php
    include("dbconn.php");
    include("session.php");

    $sql = "DELETE FROM authed_user WHERE user_val = '".$_GET['user_val']."'";
    mysqli_query($conn, $sql);

    echo "<script>alert('유저번호: ".$_GET['user_val']."\n건의 권한 박탈되었습니다.');history.back();</script>";
?>