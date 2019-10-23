<?php
    include("dbconn.php");
    include("session.php");

    $sql = "";

    if($_GET['handle'] == "Open"){
        $sql = "UPDATE suggestion SET status = 1 WHERE idx = ".$_GET['idx'];
    }
    else{
        $sql = "UPDATE suggestion SET status = 2 WHERE idx = ".$_GET['idx'];
    }

    mysqli_query($conn, $sql);

    echo "<script>history.back();</script>";
?>