<html>
    <head>
        <meta charset='utf-8'>
        <title>건의 뷰어</title>
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $result = mysqli_query($conn, "SELECT * FROM auth_code");
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            
        </div>
    </body>
</html>
