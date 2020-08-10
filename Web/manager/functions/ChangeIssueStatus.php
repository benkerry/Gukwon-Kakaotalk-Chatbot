<?php
    include("session.php");

    $sql = "";
    $nickname = mysqli_real_escape_string($conn, htmlspecialchars(htmlspecialchars_decode($_SESSION['nickname'])));
    $idx = mysqli_real_escape_string($conn, $_GET['idx']);

    if($_GET['handle'] == "Open"){
        $datetime = new DateTime("now");
        $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
        $str_datetime = $datetime->format("Y-m-d");

        $sql = "UPDATE suggestion SET status = 1, open_datetime = '$str_datetime', handler_nickname = '$nickname' WHERE idx = $idx";
        echo "<script>alert('제안을 열었습니다!');</script>";
    }
    else if($_GET['handle'] == "Close"){
        $sql = "UPDATE suggestion SET status = 2, handler_nickname = '$nickname' WHERE idx = $idx";
        echo "<script>alert('제안을 닫았습니다.');</script>";
    }
    else if($_GET['handle'] == "Delete"){
        $datetime = new DateTime("now");
        $datetime->setTimezone(new DateTimeZone("Asia/Seoul"));
        $str_datetime = $datetime->format("Y-m-d");
        
        $sql = "UPDATE suggestion SET status = 3, deleted_datetime = '$str_datetime', handler_nickname = '$nickname' WHERE idx = $idx";
        echo "<script>alert('제안을 휴지통으로 옮겼습니다. 15일 후 삭제됩니다.');</script>";
    }
    else if($_GET['handle'] == "Restore"){
        $sql = "UPDATE suggestion SET status = 0, handler_nickname = '$nickname' WHERE idx = $idx";
        echo "<script>alert('제안을 \'승인 대기중 제안\'으로 복원했습니다.');</script>";
    }

    if($sql != ""){
        mysqli_query($conn, $sql);
    }
    
    echo "<script>location.href='../SuggestionViewer.php?idx=$idx';</script>";
?>
