<html>
    <head>
        <meta charset='utf-8'>
        <title>인증번호 발급</title>
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $result = mysqli_query($conn, "SELECT * FROM auth_code");
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <form action="functions/AuthCodeGenerator.php" method="POST">
                <input type="checkbox" name="chk_truncate"> 기존에 발급된 인증번호는 삭제<br>
                <input type="number" name="count"> 발급 개수<br>
                <input type="submit" value="발급"><br>
            </form>
            <?php
                echo "현재 미사용 인증번호는 ".(string)(mysqli_num_rows($result))."개 입니다.<br>";
            ?>
        </div>
    </body>
</html>
