<html>
    <head>
        <meta charset='utf-8'>
        <title>인증번호 발급</title>
        <link rel="stylesheet" href="/style/master.css">
        <link rel="stylesheet" href="/style/generateAuthcode.css">
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $result = mysqli_query($conn, "SELECT COUNT(*) FROM auth_code");
        ?>
        <script>
            function ChkCheckbox(){
                var checkbox = document.getElementById("chk_manager");
                
                if(checkbox.checked){
                    document.getElementById("rdoRoot").style.display = "";
                }
                else{
                    document.getElementById("rdoRoot").style.display = "none";
                }
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <form action="functions/AuthCodeGenerator.php" method="POST">
                <input type="checkbox" id="chk_manager" name="chk_manager" onchange="ChkCheckbox();"> 관리자 인증번호 발급<br>
                <span id="rdoRoot" style="display:none;">
                    <input type="radio" name="rdo" value="0" checked> 학생 레벨&nbsp;<input type="radio" name="rdo" value="1"> 교사 레벨<br>
                </span>
                <br>
                <input type="checkbox" name="chk_truncate"> 기존에 발급된 인증번호는 삭제<br>
                <input type="number" name="count" placeholder="발급 개수">&nbsp;
                <input type="submit" value="발급" onclick="reload();"><br>
            </form>
            <?php
                $sql = "SELECT COUNT(*) FROM auth_code";
                $num_rows = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                echo "현재 미사용 인증번호는 ".$num_rows."개 입니다.<br>";
            ?>
            엑셀 파일을 열 때 오류가 발생할 수 있지만, 사용에는 문제가 없습니다.
        </div>
    </body>
</html>
