<?php
    include("session.php");
    include($_SERVER['DOCUMENT_ROOT']."/config.php");
    require_once("./PHPMailer/PHPMailerAutoload.php");

    if(isset($_POST['mode'])){
        $id = mysqli_real_escape_string($conn, $_SESSION['id']);
        $sql = "SELECT email FROM sign_info WHERE id = '$id'";  
        $source_email = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

        $title = htmlspecialchars($_POST['title']);
        $description = htmlspecialchars($_POST['description']);

        $mailer = new PHPMailer();
        $mailer->isSMTP();
        $mailer->SMTPSecure = "tls";
        $mailer->SMTPAuth = true;
        $mailer->Host = $smtp_server;
        $mailer->Port = $tls_port;
        $mailer->Username = $mail;
        $mailer->Password = $mail_pwd;
        $mailer->CharSet = "UTF-8";
        $mailer->From = "developerkerry@gmail.com";
        $mailer->FromName = htmlspecialchars($_SESSION['nickname']);
        $mailer->Subject = "[Chatbot Manager] $title";
        $mailer->AltBody = "";
        $mailer->msgHTML(nl2br($description));

        if($_POST['mode'] == "send2developer"){
            $mailer->addAddress($developer_mail);
            if($mailer->send()){
                echo "<script>alert('전송 완료!');history.back();</script>";
            }
            else{
                echo "<script>alert('전송 실패');history.back();</script>";
            }
        }
        else if($_POST['mode'] == "send2allmanagers"){
            $sql = "SELECT root FROM sign_info WHERE id = '$id'";
            $root = mysqli_fetch_array(mysqli_query($conn, $sql))[0];

            if($root == 1){
                $sql = "SELECT email FROM sign_info";
                $result = mysqli_query($conn, $sql);

                while(($destination_email = mysqli_fetch_assoc($result))){
                    $mailer->addAddress($destination_email['email']);
                }

                if($mailer->send()){
                    echo "<script>alert('전송 완료!');history.back();</script>";
                }
                else{
                    echo "<script>alert('전송 실패');history.back();</script>";
                }
            }
            else{
                echo "<script>alert('권한이 없습니다. 전체 메일 전송은 교사만 가능합니다.');history.back();</script>";
            }
        }
    }
    else{
        echo "<script>alert('잘못된 요청입니다.');history.back();</script>";
    }
?>
