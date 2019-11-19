<?php
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/session.php");
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/dbconn.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>인증번호 발급</title>
        <link rel="stylesheet" href="./style/master.css">
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html"); ?>
        <script>
            function ChkCheckbox(){
                var checkbox = document.getElementById("chk_manager");
                var numericBox = document.getElementById("numericBox");
                numericBox.value = "";
                
                if(checkbox.checked){
                    document.getElementById("rdoRoot").style.display = "";
                    numericBox.placeholder = "발급 개수(단위: 개)"
                }
                else{
                    document.getElementById("rdoRoot").style.display = "none";
                    numericBox.placeholder = "발급 개수(단위: 반)"
                }
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/top_nav.html"); ?>
        <div class='description'>
            <form action="./functions/AuthCodeGenerator.php" method="POST">
                <input type="checkbox" id="chk_manager" name="chk_manager" onchange="ChkCheckbox();"> 관리자 인증번호 발급
                <span id="rdoRoot" style="display:none;">
                    &nbsp;&nbsp;<input type="radio" name="rdo" value="0" checked> 학생 레벨&nbsp;<input type="radio" name="rdo" value="1"> 교사 레벨
                </span>
                <br>
                <input type="checkbox" name="chk_truncate"> 기존에 발급된 인증번호는 삭제<br>
                <input type="number" name="count" id="numericBox" placeholder="발급 개수(단위: 반)">&nbsp;
                <input type="submit" value="발급"><br>
            </form>
            <br>
            &nbsp;일반 모드에서는 WorkSheet당 인증번호 30개씩, 입력값 만큼의 WorkSheet가 만들어집니다.<br>
            &nbsp;관리자 인증번호 발급 모드에서는 한 WorkSheet에 입력값 만큼의 인증번호가 발급됩니다.<br>
            <br>
            <br>
            <button onclick="location.reload(true);">새로고침</button><br>
            <?php
                $sql = "SELECT COUNT(*) FROM auth_code";
                $num_users = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                $sql = "SELECT COUNT(*) FROM manager_auth_code WHERE root = 0";
                $num_st_managers = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                $sql = "SELECT COUNT(*) FROM manager_auth_code WHERE root = 1";
                $num_tc_managers = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                echo "- 미사용 인증번호 현황 -<br>";
                echo "<br>";
                echo "일반 사용자: $num_users<br>";
                echo "학생 관리자: $num_st_managers<br>";
                echo "교사 관리자: $num_tc_managers<br>";
                echo "<br><br>";

                $sql = "SELECT COUNT(*) FROM authed_user";
                $num_users = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                $sql = "SELECT COUNT(*) FROM sign_info WHERE root = 0";
                $num_st_managers = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                $sql = "SELECT COUNT(*) FROM sign_info WHERE root = 1";
                $num_tc_managers = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

                echo "- 인증된 사용자 현황 -<br>";
                echo "<br>";
                echo "일반 사용자: $num_users<br>";
                echo "학생 관리자: $num_st_managers<br>";
                echo "교사 관리자: $num_tc_managers<br>";     
            ?>
            <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/bug_report.html"); ?>
        </div>
    </body>
</html>
