<?php
    include("session.php");
    include("dbconn.php");

    $handle = $_GET['handle'];

    if($handle == 0){
        if(empty($_GET['description'])){
            echo "<script>alert(\"아무것도 입력하지 않으셨습니다.\");history.back();</script>";
        }
        else{
            $_GET['description'] = nl2br(htmlspecialchars($_GET['description']));
            $datetime = new DateTime("now");
            $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
            $str_datetime = $datetime->format("Y-m-d, H:i");

            $sql = "INSERT INTO suggestion_comment(sug_idx, description, nickname, commit_datetime) VALUES(".$_GET['sug_idx'].", '".$_GET['description']."', '".$_SESSION['nickname']."', '".$str_datetime."')";
            mysqli_query($conn, $sql);

            header("Location:../SuggestionViewer.php?idx=".$_GET['sug_idx']);
        }
    }
    else if($handle == 1){
        $sql = "DELETE FROM suggestion_comment WHERE idx = ".$_GET['idx'];
        mysqli_query($conn, $sql);
        
        echo "<script>history.back();</script>";
    }
    else{
        echo "<script>alert(\"잘못된 접근입니다.\");history.back();</script>";
    }
?>