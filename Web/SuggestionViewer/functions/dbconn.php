<?php
    include($_SERVER['DOCUMENT_ROOT']."/config.php");
    $conn = mysqli_connect($db_addr, $db_username, $db_pwd);
    mysqli_select_db($conn, $db_name);
?>
