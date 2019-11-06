<?php
    if(!is_numeric($_POST['count'])){
        echo "<script>alert('숫자만 입력해주세요.');location.href=\"../index.php\";</script>";
    }
    else{
        include("dbconn.php");
        include("session.php");

        $sql = "SELECT root FROM sign_info WHERE pwd = '".$_SESSION['pwd_hash']."' AND id = '".$_SESSION['id']."'";
    
        if((int)(mysqli_fetch_assoc(mysqli_query($conn, $sql))['root']) != 1){
            echo "<script>alert('권한이 없습니다.');history.back();</script>";
        }
        else{
            $root = 0;

            if(isset($_POST['chk_truncate'])){
                mysqli_query($conn, "TRUNCATE auth_code");
            }
            if(isset($_POST['chk_manager'])){
                $root = "1";
            }
            else{
                $root = "0";
            }

            header( "Content-type: application/vnd.ms-excel");
            header( "Content-type: application/vnd.ms-excel; charset=utf-8");
            header( "Content-Disposition: attachment; filename = auth_codes.xls" );
            header( "Content-Description: PHP4 Generated Data" );

            $charpool = "ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789";
            
            $sql = "INSERT INTO auth_code VALUES";

            $EXCEL_FILE = "
            <table border='1'>
                <tr><td>인증번호</td></tr>
            ";

            $authcodes = array();
            for($i = 0; $i < $_POST['count']; $i++){
                $authcode = "";
                for($k = 0; $k < 6; $k++){
                    $authcode .= $charpool[mt_rand(0, 34)];
                }

                if(array_search($authcode, $authcodes) == FALSE){
                    $authcodes[] = $authcode;

                    $sql .= "('".$authcode."', ".$root."), ";
                    $EXCEL_FILE .= "<tr><td>".$authcode."<td/></tr>";
                }
            }
            $sql = substr($sql, 0, -2);
            $EXCEL_FILE .= "</table>";

            mysqli_query($conn, $sql);

            echo "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>";
            echo $EXCEL_FILE;
        }
    }
?>