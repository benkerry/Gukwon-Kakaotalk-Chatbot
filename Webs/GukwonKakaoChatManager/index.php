<html>
    <head>
        <meta charset="utf-8"/>
        <title>국원고등학교 챗봇 관리자 페이지</title>
        <link rel="stylesheet" href="./style/index.css">
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html"); ?>
    </head>
    <body>
        <div class="login_form">
            <form action="./functions/login_auth.php" method="POST">
                <input type="text" name='id' placeholder='아이디'><br>
                <input type="password" name='pwd' placeholder='패스워드'><br>
                <input type="submit" class="btn" value='로그인'>
            </form>
            <button class="btn" onclick="location.href='signin.php';">관리자 회원가입</button>
        </div>
    </body>
</html>