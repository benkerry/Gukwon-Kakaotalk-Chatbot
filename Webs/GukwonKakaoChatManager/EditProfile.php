<?php
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/session.php");
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/dbconn.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>내 정보 수정</title>
        <link rel="stylesheet" href="./style/master.css">
        <link rel="stylesheet" href="./style/editprofile.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html");
            $id = mysqli_real_escape_string($conn, htmlspecialchars($_SESSION['id']));
            $email = mysqli_fetch_array(mysqli_query($conn, "SELECT email FROM sign_info WHERE id='$id'"))[0];
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/top_nav.html"); ?>
        <div class='description'>
            <h4>이메일 변경</h4>
            <?php echo "현재 이메일은 '$email'입니다.<br>"; ?>
            <br>
            <form action="functions/EditProfile.php" method="POST">
                <input type="hidden" name="req_type" value="change_email">
                <input type="email" name="email" placeholder="변경할 이메일 입력"><br>
                <input type="password" name="password" placeholder="비밀번호 입력"><br>
                <input type="submit" value="변경하기">
            </form>
            <br>
            <h4>닉네임 변경</h4>
            <?php echo "현재 닉네임은 '".$_SESSION['nickname']."'입니다.<br>"; ?>
            <br>
            <form action="functions/EditProfile.php" method="POST">
                <input type="hidden" name="req_type" value="change_nickname">
                <input type="nickname" name="nickname" placeholder="변경할 닉네임 입력"><br>
                <input type="password" name="password" placeholder="비밀번호 입력"><br>
                <input type="submit" value="변경하기">
            </form>
            <br>
            <h4>패스워드 변경</h4>
            <form action="functions/EditProfile.php" method="POST">
                <input type="hidden" name="req_type" value="change_password">
                <input type="password" name="next_password" placeholder="변경할 패스워드 입력"><br>
                <input type="password" name="next_password_chk" placeholder="변경할 패스워드 확인"><br>
                <input type="password" name="password" placeholder="현재 패스워드 입력"><br>
                <input type="submit" value="변경하기">                
            </form>
            <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/bug_report.html"); ?>
        </div>
    </body>
</html>
