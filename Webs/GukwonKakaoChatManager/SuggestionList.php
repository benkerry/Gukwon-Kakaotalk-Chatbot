<html>
    <head>
        <meta charset='utf-8'>
        <title>건의사항 관리</title>
        <link rel="stylesheet" href="/style/master.css">
        <link rel="stylesheet" href="/style/suggestionList.css">
        <?php
            include($_SERVER['DOCUMENT_ROOT']."/functions/session.php");
            include($_SERVER['DOCUMENT_ROOT']."/functions/dbconn.php");

            $result['staged'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 0");
            $result['open'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 1");
            $result['closed'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 2");
        ?>
        <script>
            function setStaged(){
                document.getElementById('divStaged').style.display = "";
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = 'none';
            }

            function setOpen(){
                document.getElementById('divStaged').style.display = "none";
                document.getElementById('divOpen').style.display = '';
                document.getElementById('divClosed').style.display = 'none';
            }

            function setClosed(){
                document.getElementById('divStaged').style.display = "none";
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = '';
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/templates/top_nav.html"); ?>
        <div class='description'>
            <input type="radio" name="rdo" id='rdoStaged' class='rdoBtn' onclick='setStaged()' checked> 발행 대기중인 제안&nbsp;&nbsp;
            <input type="radio" name="rdo" id='rdoOpen' class='rdoBtn' onclick='setOpen()'> 열린 제안&nbsp;&nbsp;
            <input type="radio" name="rdo" id='rdoClosed' class='rdoBtn' onclick='setClosed()'> 닫힌 제안
            <div id='divStaged' style='display:;'>
                <!-- Pushed Issues -->
                <table>
                    <thead>
                        <tr>
                            <th class='index'>번호</th>
                            <th class='preview'>내용 미리보기</th>
                            <th class='datetime'>등록일</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                            $title = "";

                            while(($row = mysqli_fetch_assoc($result['staged']))){        
                                if(strlen($row['description']) >= 30){
                                    $title = substr($row['description'], 0, 24)."......";
                                }
                                else{
                                    $title = $row['description'];
                                }

                                echo "<tr>";
                                echo "<td>".$row['idx']."</td>";
                                echo "<td class='preview'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                echo "<td>".$row['open_datetime']."</td>";
                                echo "</tr>";
                            }
                        ?>
                    </tbody>
                </table>
            </div>
            <div id='divOpen' style='display:none;'>
                <!-- Open Issues -->
                <table>
                    <thead>
                        <tr>
                            <th class='index'>번호</th>
                            <th class='preview'>내용 미리보기</th>
                            <th class='datetime'>등록일</th>
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
                                echo "<td class='preview'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
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
                            <th class='index'>번호</th>
                            <th class='preview'>내용 미리보기</th>
                            <th class='datetime'>등록일</th>
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
                                echo "<td class='preview'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
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
