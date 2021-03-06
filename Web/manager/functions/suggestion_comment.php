<?php
    include("session.php");

    $handle = $_GET['handle'];

    if($handle == 0){
        if(empty($_GET['description'])){
            echo "<script>alert(\"아무것도 입력하지 않으셨습니다.\");history.back();</script>";
        }
        else{
            $sug_idx = mysqli_real_escape_string($conn, htmlspecialchars($_GET['sug_idx']));
            $description = mysqli_real_escape_string($conn, nl2br(htmlspecialchars($_GET['description'])));
            $nickname = mysqli_real_escape_string($conn, htmlspecialchars($_SESSION['nickname']));

            $datetime = new DateTime("now");
            $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
            $str_datetime = $datetime->format("Y-m-d, H:i");

            $sql = "INSERT INTO suggestion_comment(sug_idx, description, nickname, commit_datetime) VALUES($sug_idx, '$description', '$nickname', '$str_datetime')";
            mysqli_query($conn, $sql);

            header("Location:../SuggestionViewer.php?idx=".$_GET['sug_idx']);
        }
    }
    else if($handle == 1){
        $idx = mysqli_real_escape_string($conn, $_GET['cmt_idx']);
        $sql = "DELETE FROM suggestion_comment WHERE idx = $idx and nickname='".$_SESSION['nickname']."'";
        mysqli_query($conn, $sql);
        
        header("Location:../SuggestionViewer.php?idx=".$_GET['idx']);
    } 
    else{
        echo "<script>alert(\"잘못된 접근입니다.\");history.back();</script>";
    }
?>
