<?php
    include("session.php");

    $id = mysqli_real_escape_string($conn, $_SESSION['id']);
    $pwd_hash = mysqli_real_escape_string($conn, $_SESSION['pwd_hash']);

    $sql = "SELECT root FROM sign_info WHERE id = '$id' AND pwd='$pwd_hash'";
    
    if((int)(mysqli_fetch_assoc(mysqli_query($conn, $sql))['root']) != 1){
        echo "<script>alert('권한이 없습니다.');history.back();</script>";
    }
    else{
        $sql = "DELETE FROM sign_info WHERE id = '$id'";
        mysqli_query($conn, $sql);
        echo "<script>alert('삭제 완료!');location.href='../ManagerManager.php';</script>";
    }
?>