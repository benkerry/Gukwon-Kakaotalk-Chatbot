<?php
    include("session.php");
    include("dbconn.php");

    $_POST['comment_description'] = htmlspecialchars('comment_description');
    $datetime = new DataTime("now");
    $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
    $str_datetime = $datetime->format("Y.m.d. H:i");

    $sql = "INSERT INTO suggestion_comments VALUES(".$_POST['sug_idx'].", '".$_POST['comment_description']."', '".$str_datetime."')";
    mysqli_query($conn, $sql);

    echo "<script>history.back();</script>";
?>