<?php
    if(!is_numeric($_POST['count'])){
        echo "<script>alert('숫자만 입력해주세요.');history.back();</script>";
        return;
    }
    else if($_POST['count'] <= 0){
        echo "<script>alert('1 이상의 수를 입력하셔야 합니다.');history.back();</script>";
        return;
    }
    else{
        include("session.php");
        require_once("./PHPExcel/PHPExcel.php");

        $pwd_hash = mysqli_real_escape_string($conn, $_SESSION['pwd_hash']);
        $id = mysqli_real_escape_string($conn, $_SESSION['id']);

        $sql = ("SELECT root FROM sign_info WHERE pwd = '$pwd_hash' AND id = '$id'");
    
        if((int)(mysqli_fetch_assoc(mysqli_query($conn, $sql))['root']) != 1){
            echo "<script>alert('권한이 없습니다.');history.back();</script>";
            return;
        }
        else{
            $mode = -1;
            $pri = "";

            if(isset($_POST['chk_manager'])){
                if($_POST['count'] > 500){
                    echo "<script>alert('값이 너무 큽니다. 500 이하의 값을 입력하세요.');history.back();</script>";
                    return;
                }
                else if($_POST['rdo'] == 0){
                    $priv = "학생 관리자";
                    $mode = 0;

                    if(isset($_POST['chk_truncate'])){
                        mysqli_query($conn, "DELETE FROM manager_auth_code WHERE root = 0");
                    }
                }
                else if($_POST['rdo'] == 1){
                    $priv = "교사 관리자";
                    $mode = 1;

                    if(isset($_POST['chk_truncate'])){
                        mysqli_query($conn, "DELETE FROM manager_auth_code WHERE root = 1");
                    }
                }
                else{
                    echo "<script>alert('잘못된 요청입니다.');history.back();</script>";
                    return;
                }
            }
            else{
                $priv = "일반 학생";

                if($_POST['count'] > 50){
                    echo "<script>alert('값이 너무 큽니다. 50 이하의 값을 입력하세요.');history.back();</script>";
                    return;
                }
                else if(isset($_POST['chk_truncate'])){
                    mysqli_query($conn, "TRUNCATE auth_code");
                }
            }

            $charpool = "ABCDEFGHIJKLMNOPQRSTUWXYZ0123456789";
            $authcodes = array();

            if($mode >= 0){   
                $sql = "INSERT INTO manager_auth_code VALUES";  
                $i = 0;  
                while($i < $_POST['count']){
                    $authcode = "";
                    for($k = 0; $k < 6; $k++){
                        $authcode .= $charpool[mt_rand(0, 34)];
                    }
    
                    if(array_search($authcode, $authcodes) == FALSE){
                        $authcodes[] = $authcode;
                        $sql .= "('$authcode', $mode), ";
                        $i++;
                    }
                }
                mysqli_query($conn, substr($sql, 0, -2));
            }
            else{
                $_POST['count'] = $_POST['count'] * 30;
                $sql = "INSERT INTO auth_code VALUES";
                $i = 0;
                while($i < $_POST['count']){
                    $authcode = "";
                    for($k = 0; $k < 6; $k++){
                        $authcode .= $charpool[mt_rand(0, 34)];
                    }
    
                    if(array_search($authcode, $authcodes) == FALSE){
                        $authcodes[] = $authcode;
                        $sql .= "('$authcode'), ";
                        $i++;
                    }
                }
                mysqli_query($conn, substr($sql, 0, -2));
            }

            $excel = new PHPExcel();
            $excel->getProperties()
                ->setCreator("Ben Kerry")
                ->setLastModifiedBy("Ben Kerry")
                ->setTitle("AuthCodes")
                ->setSubject("AuthCodes")
                ->setDescription("AuthCodes")
                ->setKeywords("Authcodes")
                ->setCategory("Authcodes");
            
            $last_idx = 0;
            $excel->removeSheetByIndex(0);

            for($i = 0; $i < $_POST['count']; $i++){
                $tmp = $i % 30;
                if($tmp == 0){
                    $last_idx = $i / 30;
                    $excel->createSheet($last_idx);
                    $excel->setActiveSheetIndex($last_idx);
                    $excel->getActiveSheet()
                        ->setCellValue("B2", "index")
                        ->setCellValue("C2", "인증번호")
                        ->setCellValue("D2", "권한");
                    $excel->getActiveSheet()->setTitle("sheet_".((string)($last_idx + 1)));
                }
                $ii = $tmp + 3;
                $excel->getActiveSheet()
                    ->setCellValue("B$ii", $ii - 2)
                    ->setCellValue("C$ii", $authcodes[$i])
                    ->setCellValue("D$ii", $priv);
                }

            if(($_POST['count'] + 1) % 30 == 0){
                $excel->removeSheetByIndex($last_idx);
            }

            $writer = PHPExcel_IOFactory::createWriter($excel, 'Excel2007');
            $hash_fname = md5((string)time()).".xlsx";
            $writer->save("./$hash_fname");

            echo "잠시만 기다려 주세요. 3초 후 원래 페이지로 돌아갑니다.";
            echo "<script>document.location.href=\"AuthCodeDownloader.php?fname=$hash_fname\"; setTimeout(function(){ history.back(); }, 3000);</script>";
        }
    }
?>
