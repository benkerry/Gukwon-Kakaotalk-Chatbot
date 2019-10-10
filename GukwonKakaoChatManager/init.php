<?php
    include("functions/dbconn.php");
    $hash = password_hash(htmlspecialchars("test_0"), PASSWORD_DEFAULT);
    $sql = "INSERT INTO sign_info VALUES('".htmlspecialchars("test_0")."', '".$hash."', 0)";
    mysqli_query($conn, $sql);
    $hash = password_hash(htmlspecialchars("test_1"), PASSWORD_DEFAULT);
    $sql = "INSERT INTO sign_info VALUES('".htmlspecialchars("test_1")."', '".$hash."', 1)";
    mysqli_query($conn, $sql);
?>