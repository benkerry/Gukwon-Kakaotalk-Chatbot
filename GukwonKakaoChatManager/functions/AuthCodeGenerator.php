<?php
    if(!is_numeric($_POST['count'])){
        echo "<script>alert('숫자만 입력해주세요.');location.href=\"../index.php\";</script>";
    }
    else{
        include("dbconn.php");
        include("session.php");

        $sql = "SELECT root FROM sign_info WHERE pwd = '".$_SESSION['pwd_hash']."' AND id = '".$_SESSION['id']."'";

        if((int)(mysqli_fetch_assoc(mysqli_query($conn, $sql))['root']) != 1){
            echo "<script>alert('권한이 없습니다.');location.href=\"../index.php\";</script>";
        }
        else{
            if(isset($_POST['chk_truncate'])){
                system("python AuthCodeGenerator.py 1 ".$_POST['count']);
            }
            else{
                system("python AuthCodeGenerator.py 0 ".$_POST['count']);
            }

            $filename = "authcodes.xlsx";
            $reail_filename = urldecode($filename);
        
            header('Content-Type: application/x-octetstream');
            header('Content-Length: '.filesize($filename));
            header('Content-Disposition: attachment; filename='.$filename);
            header('Content-Transfer-Encoding: binary');
        
            $fp = fopen($filename, "r");
            fpassthru($fp);
            fclose($fp);

            header("Location:../GenerateAuthCode.php");
        }
    }
?>