<?php
    include($_SERVER['DOCUMENT_ROOT']."/manager/functions/session.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>관리자 관리</title>
        <link rel="stylesheet" href="./style/master.css">
        <link rel="stylesheet" href="./style/managermanage.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html");
            $id = mysqli_real_escape_string($conn, $_SESSION['id']);
            $pwd_hash = mysqli_real_escape_string($conn, $_SESSION['pwd_hash']);

            $result = mysqli_query($conn, "SELECT root FROM sign_info WHERE id = '$id' and pwd = '$pwd_hash'");
        ?>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/manager/templates/top_nav.html"); ?>
        <div class='description'>
            <table>
                <thead>
                    <tr>
                        <th class='nickname'>닉네임</th>
                        <th class='del'>관리자 권한 박탈</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                        if(mysqli_fetch_array($result)[0] != 1){
                            echo "<script>alert(\"권한이 없습니다.\");history.back();</script>";
                        }
                        else{
                            $sql = "SELECT nickname, id FROM sign_info";
                            $result = mysqli_query($conn, $sql);

                            while(($row = mysqli_fetch_assoc($result))){        
                                echo "<tr>";
                                echo "<td>".$row['nickname']."</td>";
                                echo "<td><a href='./functions/DeleteManager_chk.php?nickname=".$row['nickname']."&id=".$row['id']."'>권한 박탈</a></td>";
                                echo "</tr>";
                            }
                        }
                    ?>
                </tbody>
            </table>
            <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/manager/templates/bug_report.html"); ?>
        </div>
    </body>
</html>
