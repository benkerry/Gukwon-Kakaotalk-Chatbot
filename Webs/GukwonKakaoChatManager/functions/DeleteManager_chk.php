<?php
    include("session.php");

    echo htmlspecialchars($_GET['nickname'])."님의 관리자 권한이 제거됩니다. 진행하시겠습니까? <a href='./DeleteManager?nickname=".htmlspecialchars($_GET['nickname'])."&id=".htmlspecialchars($_GET['id'])."'>진행</a>";
?>