<html>
    <head>
        <meta charset='utf-8'>
        <title>건의 열람</title>
        <link rel="stylesheet" href="/style/master.css">
        <link rel="stylesheet" href="/style/suggestionViewer.css">
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

                    $sql = "SELECT COUNT(*) FROM authed_user WHERE user_val = '".$result['suggestion']['user_val']."'";

                    if(((int)(mysqli_fetch_array(mysqli_query($conn, $sql))[0])) > 0){
                        echo "<button action='functions/deprive.php?user_val=".$result['suggestion']['user_val']."'>건의 권한 박탈하기</button>";
                    }
                    else{
                        echo "<strong>건의 권한이 박탈된 사용자가 남긴 건의입니다.</strong>";
                    }
                    echo "<br><br>";

                    if((int)$result['suggestion']['status'] == 1){
                        echo "<button onclick='location.href=\"functions/ToggleIssueStatus.php?handle=Close&idx=".$_GET['idx']."\";'>건의 닫기</button>";
                    }
                    else{
                        echo "<button onclick='location.href=\"functions/ToggleIssueStatus.php?handle=Open&idx=".$_GET['idx']."\";'>건의 열기</button>";
                    }
                    echo "<br><br>";

                    echo $result['suggestion']['description'];
                ?>
            </div>
            <br>
            <button onclick="location.href='../SuggestionList.php';">뒤로가기</button><br>
            <br>
            <div class="write_comment">
                <form action="/functions/suggestion_comment.php" method="GET">
                    <input type="hidden" name="handle" value="0">
                    <?php 
                        echo "<input type=\"hidden\" name=\"sug_idx\" value=\"".$_GET['idx']."\">";
                    ?>
                    <textarea name="description" placeholder="코멘트 남기기"></textarea><br>
                    <input type="submit">
                </form>
            </div>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comment WHERE sug_idx = ".$_GET['idx']);
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo $row['description']."<br><br>";
                        echo "<span>by ".$row['nickname']."<br>[".$row['commit_datetime']."]<a href='functions/suggestion_comment.php?handle=1&idx=".$row['idx']."'><strong>[삭제]</strong></a></span>";
                        echo "<br>";
                        echo "</div><br>";
                    }
                ?>
                <br>
            </div>
        </div>
    </body>
</html>
