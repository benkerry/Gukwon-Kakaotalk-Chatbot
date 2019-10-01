<?php
    include("functions/dbconn.php");
    $hash = password_hash("test", PASSWORD_DEFAULT);
    $sql = "INSERT INTO sign_info VALUES('test', '".$hash."')";
    mysqli_query($conn, $sql);
?>