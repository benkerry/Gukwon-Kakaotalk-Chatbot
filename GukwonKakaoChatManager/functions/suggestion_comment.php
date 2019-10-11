<?php
    include("session.php");
    include("dbconn.php");

    $handle = ((int)$_GET['handle']);

    if($handle == 0){
        $_GET['comment_description'] = htmlspecialchars('comment_description');
        $datetime = new DateTime("now");
        $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
        $str_datetime = $datetime->format("Y.m.d. H:i");

        $sql = "INSERT INTO suggestion_comments(sug_idx, description, commit_datetime) VALUES(".$_GET['sug_idx'].", '".$_GET['comment']."', '".$str_datetime."')";
        mysqli_query($conn, $sql);
        $sql = "UPDATE suggestion SET num_comments = num_comments + 1 WHERE idx = ".$_GET['sug_idx'];
        mysqli_query($conn, $sql);

        header("Location:../SuggestionViewer.php?idx=".$_GET['sug_idx']);
    }
    else if($handle == 1){
        $sql = "DELETE suggestion_comments WHERE idx = ".$_GET['idx'];
        mysqli_query($conn, $sql);
        $sql = "UPDATE suggestion SET num_comments = num_comments - 1 WHERE idx = ".$_GET['idx'];
        mysqli_query($conn, $sql);

        echo "<script>history.back();</script>";
    }
    else{
        echo "<script>alert(\"잘못된 접근입니다.\");history.back();</script>";
    }
?>