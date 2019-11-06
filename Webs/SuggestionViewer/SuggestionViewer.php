<html>
    <head>
        <meta charset='utf-8'>
        <link rel="stylesheet" href="/style/master.css">
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $raw_result = mysqli_query($conn, "SELECT * FROM suggestion WHERE idx = ".$_GET['idx']);
            $result['suggestion'] = mysqli_fetch_assoc($raw_result);

            echo "<title>#".$_GET['idx']."번 건의사항</title>";
        ?>
    </head>
    <body>
        <div class='description'>
            <div class='suggestion'>
                <?php
                    echo "<h4>등록일: ".$result['suggestion']['open_datetime']."</h4>";
                    echo $result['suggestion']['description'];
                ?>
            </div>
            <br>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comment WHERE sug_idx = ".$_GET['idx']);
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo "[".$row['commit_datetime']."]\n\n\n".$row['description'];
                        echo "<br>";
                        echo "</div>";
                    }
                ?>
                <br>
            </div>
            <button onclick="history.back();">뒤로가기</button>
        </div>
    </body>
</html>
