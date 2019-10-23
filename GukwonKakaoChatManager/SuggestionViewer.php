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
                    echo "<h4>등록일: ".$result['suggestion']['open_datetime']."</h4>";
                    if(((int)$result['suggestion']['closed']) == 1){
                        echo "<h4>닫힌 날짜: ".$result['suggestion']['close_datetime']."</h4>";
                        echo "<button onclick='location.href=\"functions/ToggleIssueStatus.php?handle=Open&idx=".$_GET['idx']."\";'>건의 열기</button>";
                    }
                    else{
                        echo "<button onclick='location.href=\"functions/ToggleIssueStatus.php?handle=Close&idx=".$_GET['idx']."\";'>건의 닫기</button>";
                    }

                    echo "<br>";

                    $sql = "SELECT COUNT(*) FROM authed_user WHERE user_val = '".$result['suggestion']['user_val']."'";

                    if(((int)(mysqli_fetch_array(mysqli_query($conn, $sql))[0])) > 0){
                        echo "<button action='functions/deprive.php?user_val=".$result['suggestion']['user_val']."'>건의 권한 박탈하기</button>";
                    }
                    else{
                        echo "<strong>건의 권한이 박탈된 사용자가 남긴 건의입니다.</strong>";
                    }

                    echo "<br><br>";
                    echo $result['suggestion']['description'];
                ?>
            </div>
            <br>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comment WHERE sug_idx = ".$_GET['idx']);
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo "[".$row['commit_datetime']."]\n\n\n".$row['description']."<a href='functions/suggestion_comment.php?handle=1&idx=".$row['idx']."'>-삭제-</a>";
                        echo "</div>";
                    }
                ?>
                <br>
            </div>
        </div>
    </body>
</html>
