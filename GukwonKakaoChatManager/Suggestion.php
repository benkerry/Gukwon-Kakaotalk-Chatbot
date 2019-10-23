<html>
    <head>
        <meta charset='utf-8'>
        <title>건의사항 관리</title>
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $result['req_review'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 0");
            $result['open'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 1");
            $result['closed'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 2");
        ?>
        <script>
            function setOpen(){
                document.getElementById('divOpen').style.display = '';
                document.getElementById('divClosed').style.display = 'none';
            }

            function setClosed(){
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = '';
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <input type="radio" name="issue_status"> 등록 대기중인 제안 
            <input type="radio" name="issue_status"> 열린 제안
            <input type="radio" name="issue_status"> 닫힌 제안
            <button id='btnClosed' onclick='setClosed()' style='display:;'>닫힌 제안</button>
            <div id='divOpen' style='display:;'>
                <!-- Wating Issues -->
                <table>
                    <thead>
                        <tr>
                            <th>번호</th>
                            <th>내용 미리보기</th>
                            <th>등록일</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                            $title = "";

                            while(($row = mysqli_fetch_assoc($result['req_review']))){        
                                if(strlen($row['description']) >= 30){
                                    $title = substr($row['description'], 0, 24)."......";
                                }
                                else{
                                    $title = $row['description'];
                                }

                                echo "<tr>";
                                echo "<td>".$row['idx']."</td>";
                                echo "<td><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                echo "<td>".$row['open_datetime']."</td>";
                                echo "</tr>";
                            }
                        ?>
                    </tbody>
                </table>
            </div>
            <div id='divOpen' style='display:;'>
                <!-- Open Issues -->
                <table>
                    <thead>
                        <tr>
                            <th>번호</th>
                            <th>내용 미리보기</th>
                            <th>등록일</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                            $title = "";

                            while(($row = mysqli_fetch_assoc($result['open']))){        
                                if(strlen($row['description']) >= 30){
                                    $title = substr($row['description'], 0, 24)."......";
                                }
                                else{
                                    $title = $row['description'];
                                }

                                echo "<tr>";
                                echo "<td>".$row['idx']."</td>";
                                echo "<td><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                echo "<td>".$row['open_datetime']."</td>";
                                echo "</tr>";
                            }
                        ?>
                    </tbody>
                </table>
            </div>
            <div id='divClosed' style='display:none;'>
                <!-- Closed Issues -->
                <table>
                    <thead>
                        <tr>
                            <th>번호</th>
                            <th>내용 미리보기</th>
                            <th>등록일</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                            while(($row = mysqli_fetch_assoc($result['closed']))){
                                if(strlen($row['description']) >= 30){
                                    $title = substr($row['description'], 0, 24)."......";
                                }
                                else{
                                    $title = $row['description'];
                                }

                                echo "<tr>";
                                echo "<td>".$row['idx']."</td>";
                                echo "<td><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                echo "<td>".$row['open_datetime']."</td>";
                                echo "</tr>";
                            }
                        ?>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>
