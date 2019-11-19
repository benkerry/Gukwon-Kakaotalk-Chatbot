<html>
    <head>
        <meta charset='utf-8'>
        <link rel="stylesheet" href="./style/master.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html");
            include($_SERVER['DOCUMENT_ROOT']."/SuggestionViewer/functions/dbconn.php");

            $idx = mysqli_real_escape_string($conn, htmlspecialchars($_GET['idx']));
            $raw_result = mysqli_query($conn, "SELECT * FROM suggestion WHERE idx = $idx");
            $result = mysqli_fetch_assoc($raw_result);
            $num_authed = (int)(mysqli_fetch_array(mysqli_query($conn, "SELECT COUNT(*) FROM authed_user"))[0] * 0.15);
            
            echo "<title>#".$idx."번 건의사항[".$result['num_signs']." / $num_authed]</title>";
        ?>
    </head>
    <body>
        <div class='description'>
            <div class='suggestion'>
                <?php
                    if($result['status'] != 0 && $result['status'] != 3){
                        echo "<h4>등록일: ".$result['open_datetime']."</h4>";
                        echo $result['description'];
                    }
                    else{
                        echo "<script>alert('접근 권한이 없습니다.');history.back();</script>";
                    }
                ?>
            </div>
            <br>
            <div class="comments">
                <?php
                    $raw_result = mysqli_query($conn, "SELECT * FROM suggestion_comment WHERE sug_idx = $idx");
                    
                    while(($row = mysqli_fetch_assoc($raw_result))){
                        echo "<div class='comment'>";
                        echo "[".$row['commit_datetime']."]\n\n\n".$row['description'];
                        echo "<br>";
                        echo "</div>";
                    }
                ?>
                <br>
            </div>
            <button onclick="location.href='index.php';">뒤로가기</button>
        </div>
    </body>
</html>
