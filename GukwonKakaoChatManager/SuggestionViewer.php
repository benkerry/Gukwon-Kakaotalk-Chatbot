<html>
    <head>
        <meta charset='utf-8'>
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $raw_result = mysqli_query($conn, "SELECT * FROM suggestion WHERE idx = ".$_GET['idx']);
            $result['suggestion'] = mysqli_fetch_assoc($raw_result);

            echo "<title>#".$_GET['idx']."번 건의사항</title>";
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <div class='suggestion'>
                <?php
                    echo "<h3>등록일: ".$result['suggestion']['open_datetime']."</h3>";
                    if(((int)$result['suggestion']['closed']) == 0){
                        echo "<h3>닫힌 날짜: ".$result['suggestion']['close_datetime']."</h3>";
                    }
                    echo "<br><br>";
                    echo $result['suggestion']['description'];
                ?>
            </div>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comments WHERE sug_idx = ".$_GET['idx']);
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo "[".$row['commit_datetime']."]".$row['description'];
                        echo "</div>";
                    }
                ?>
                <form action="functions/suggestion_comment.php" method="POST">
                    <?php echo "<input type='hidden' name='sug_idx' value='".$_GET['idx']."'>"; ?>
                    <textarea name="comment_description" wrap="hard" cols="30" rows="10" placeholder="답글 남기기"></textarea>
                    <input type="submit" value="전송">
                </form>
            </div>
        </div>
    </body>
</html>
