<?php
    include("dbconn.php");
    include("session.php");

    $sql = "";

    if($_GET['handle'] == "Close"){
        $sql = "UPDATE suggestion SET closed = 1 WHERE idx = ".$_GET['idx'];
    }
    else{
        // $_GET['handle'] == "Open"에 대한 처리
        $sql = "UPDATE suggestion SET closed = 0 WHERE idx = ".$_GET['idx'];
    }

    mysqli_query($conn, $sql);

    echo "<script>history.back();</script>";
?>