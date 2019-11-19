<?php
    include("session.php");

    $user_val = mysqli_real_escape_string($conn, htmlspecialchars($_GET['user_val']));
    $sql = "DELETE FROM authed_user WHERE user_val = '$user_val'";
    mysqli_query($conn, $sql);

    echo "<script>alert('유저번호: $user_val 건의 권한 박탈되었습니다.');history.back();</script>";
?>