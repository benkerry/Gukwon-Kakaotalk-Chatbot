<?php
    $filepath = "./".$_GET['fname'];
    $filesize = filesize($filepath);
    $path_parts = pathinfo($filepath);
    $filename = $path_parts['basename'];
    $extension = $path_parts['extension'];

    header("Pragma: public");
    header("Expires: 0");
    header("Content-Type: application/octet-stream");
    header("Content-Disposition: attachment; filename=authcodes.xlsx");
    header("Content-Transfer-Encoding: binary");
    header("Content-Length: $filesize");

    ob_clean();
    flush();
    readfile($filepath);
    unlink($filepath);
    
//    echo "Tlqjf";  
///    print("<meta http-equiv='refresh' content='0; URL='https://gukwonchatbot.tk/manager/GenerateAuthCode.php''>");
//echo "<script>document.location.href=\"https://gukwonchatbot.tk/manager/GenerateAuthCode.php\";</script>";
?>
