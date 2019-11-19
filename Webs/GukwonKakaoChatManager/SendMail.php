<?php
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/session.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>개발자에게 메일 보내기</title>
        <link rel="stylesheet" href="./style/master.css">
        <link rel="stylesheet" href="./style/sendmail.css">
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html"); ?>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                setMode();
            }, false);

            function setMode(){
                var rdobtn = document.getElementById("standard");

                if(rdobtn.checked){
                    document.getElementById("mode").value = "send2developer";
                    document.getElementById("submit").value = "개발자에게 메일 보내기";
                }
                else{
                    document.getElementById("mode").value = "send2allmanagers";
                    document.getElementById("submit").value = "전체 관리자에게 메일 보내기";
                }
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/top_nav.html"); ?>
        <div class='description'>
            <input type="radio" name="rdo" id="standard" onchange="setMode();" checked>&nbsp;개발자에게 보내기&nbsp;<input type="radio" name="rdo" onchange="setMode();">&nbsp;전체 관리자에게 보내기 
            <br>
            <br>
            <form action="./functions/SendMail.php" method="POST">
                <input type="hidden" id="mode" name="mode" value="send2developer">
                <input type="text" class="title" name="title" placeholder="메일 제목"><br>
                <br>
                <strong>내용 작성</strong>
                <textarea name="description"></textarea><br>
                <input type="submit" id="submit" class="submit" value="개발자에게 메일 보내기">
            </form>
        </div>
    </body>
</html>
