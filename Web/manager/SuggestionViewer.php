<?php
    include($_SERVER['DOCUMENT_ROOT']."/manager/functions/session.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>건의 열람</title>
        <link rel="stylesheet" href="./style/master.css">
        <link rel="stylesheet" href="./style/suggestionViewer.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html"); 

            $idx = mysqli_real_escape_string($conn, htmlspecialchars($_GET['idx']));
            $result = mysqli_fetch_assoc(mysqli_query($conn, "SELECT * FROM suggestion WHERE idx=$idx"));
            $num_authed = (int)(mysqli_fetch_array(mysqli_query($conn, "SELECT COUNT(*) FROM authed_user"))[0] * 0.15);

            echo "<title>#".$idx."번 건의사항[".$result['num_signs']." / $num_authed]</title>";
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/manager/templates/top_nav.html"); ?>
        <div class='description'>
            <div class='suggestion'>
                <?php
                    echo "<h4>등록일: ".$result['open_datetime']."</h4>";
                    if($result['status'] == 3){
                        echo "<h4>삭제일: ".$result['deleted_datetime']."</h4>";
                    }
                    
                    if(!empty($result['handler_nickname'])){
                        echo "<h4>최근 제안 상태를 바꾼 관리자: ".$result['handler_nickname']."</h4>";
                    }

                    $sql = "SELECT COUNT(*) FROM authed_user WHERE user_val = '".$result['user_val']."'";

                    if(((int)(mysqli_fetch_array(mysqli_query($conn, $sql))[0])) > 0){
                        echo "<button onclick='location.href=\"./functions/deprive.php?idx=$idx&user_val=".$result['user_val']."\";'>건의 권한 박탈하기</button>";
                    }
                    else{
                        echo "<strong>건의 권한이 박탈된 사용자가 남긴 건의입니다.</strong>";
                    }
                    echo "<br><br>";

                    if($result['status'] == 1){
                        echo "<button onclick='location.href=\"./functions/ChangeIssueStatus.php?handle=Close&idx=$idx\";'>건의 닫기</button>&nbsp;";
                    }
                    else if($result['status'] != 4){
                        echo "<button onclick='location.href=\"./functions/ChangeIssueStatus.php?handle=Open&idx=$idx\";'>건의 열기</button>&nbsp;";
                    }

                    if($result['status'] == 0 || $result['status'] == 2){
                        echo "<button onclick='location.href=\"./functions/ChangeIssueStatus.php?handle=Delete&idx=$idx\";'>삭제</button>";
                    }
                    else if($result['status'] == 3){
                        echo "<button onclick='location.href=\"./functions/ChangeIssueStatus.php?handle=Restore&idx=$idx\";'>복원</button>";
                    }
                    echo "<br><br>";
                    echo "<div class='sug_description'>";
                    echo $result['description'];
                    echo "</div>";
                ?>
            </div>
            <br>
            <button id="back" onclick="location.href='SuggestionList.php';" style="background-color:EBEBEB;">목록으로 돌아가기</button><br>
            <br>
            <div class="write_comment">
                <form action="./functions/suggestion_comment.php" method="GET">
                    <input type="hidden" name="handle" value="0">
                    <?php 
                        echo "<input type=\"hidden\" name=\"sug_idx\" value=\"$idx\">";
                    ?>
                    <textarea name="description" placeholder="코멘트 남기기"></textarea><br>
		    <input type="submit" value="입력 완료">
                </form>
            </div>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comment WHERE sug_idx = $idx");
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo $row['description']."<br><br>";
                        echo "<span>by ".$row['nickname']."<br>[".$row['commit_datetime']."]<a href='./functions/suggestion_comment.php?handle=1&idx=$idx&cmt_idx=".$row['idx']."'><strong>[삭제]</strong></a></span>";
                        echo "<br>";
                        echo "</div><br>";
                    }
                ?>
                <br>
            </div>
            <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/manager/templates/bug_report.html"); ?>
        </div>
    </body>
</html>
