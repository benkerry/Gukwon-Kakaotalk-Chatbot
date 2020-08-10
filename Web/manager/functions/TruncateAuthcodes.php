<?php
    include("session.php");

    if(mysqli_fetch_array(mysqli_query($conn, "SELECT root FROM sign_info WHERE id='".$_SESSION['id']."'"))[0] == 1){
        mysqli_query($conn, "TRUNCATE auth_code");
        mysqli_query($conn, "TRUNCATE manager_auth_code");
        echo "<script>alert('초기화 성공!');history.back();</script>";
    }
    else{
        echo "<script>alert('권한이 없습니다.');history.back();</script>";
    }
?>