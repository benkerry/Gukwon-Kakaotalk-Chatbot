<html>
    <head>
        <meta charset='utf-8'>
        <title>건의사항 관리</title>
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <?php
                $sql = "SELECT * FROM ";

            // 하: Migrate 필요
            while( $row = mysqli_fetch_assoc($result)){
                $date = $row['dat'];
                echo '<tr><td>'.htmlspecialchars($row['idx']).'</td>';
                echo '<td><a href="http://localhost/tmps/grill/notice.php?id='.$row['idx'].'">'.htmlspecialchars($row['title']).'</a></td>';
                echo '<td>'.$date[2].$date[3].'.'.$date[5].$date[6].'.'.$date[8].$date[9].'. '.$date[11].$date[12].':'.$date[14].$date[15].':'.$date[17].$date[18].'</td>';
                if($_SESSION['level'] == '*C4E74DDDC9CC9E2FDCDB7F63B127FB638831262E' || $_SESSION['level'] == '*12033B78389744F3F39AC4CE4CCFCAD6960D8EA0'){
                    echo '<td>삭제</td></tr>';
                }
              }
            ?>
        </div>
    </body>
</html>
