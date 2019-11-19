<?php
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/session.php");
    include($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/functions/dbconn.php");
?>
<html>
    <head>
        <meta charset='utf-8'>
        <title>건의사항 관리</title>
        <link rel="stylesheet" href="./style/master.css">
        <link rel="stylesheet" href="./style/suggestionList.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html");
            
            $result['staged'] = mysqli_query($conn, "SELECT idx, description, num_signs, open_datetime FROM suggestion WHERE status = 0");
            $result['open'] = mysqli_query($conn, "SELECT idx, description, num_signs, open_datetime FROM suggestion WHERE status = 1");
            $result['closed'] = mysqli_query($conn, "SELECT idx, description, status, num_signs, open_datetime FROM suggestion WHERE status = 2 or status = 4");
            $result['recycle'] = mysqli_query($conn, "SELECT idx, description, num_signs, open_datetime FROM suggestion WHERE status = 3");
        ?>
        <script>
            function setStaged(){
                document.getElementById('divStaged').style.display = "";
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = 'none';
                document.getElementById('divRecycle').style.display = 'none';
            }

            function setOpen(){
                document.getElementById('divStaged').style.display = "none";
                document.getElementById('divOpen').style.display = '';
                document.getElementById('divClosed').style.display = 'none';
                document.getElementById('divRecycle').style.display = 'none';
            }

            function setClosed(){
                document.getElementById('divStaged').style.display = "none";
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = '';
                document.getElementById('divRecycle').style.display = 'none';
            }

            function setRecycle(){
                document.getElementById('divStaged').style.display = "none";
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = 'none';
                document.getElementById('divRecycle').style.display = '';
            }

            function setPassedOnly(){
                var sections = document.getElementsByClassName("non-passed");

                if(document.getElementById('chkPassedOnly').checked){
                    for(var i = 0; i < sections.length; i++){
                        var item = sections.item(i);
                        item.style.display = "none";
                    }
                }
                else{
                    for(var i = 0; i < sections.length; i++){
                        var item = sections.item(i);
                        item.style.display = "";
                    }
                }
            }
        </script>
    </head>
    <body>
        <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/top_nav.html"); ?>
        <div class='description'>
            <input type="radio" name="rdo" id='rdoStaged' class='rdoBtn' onclick='setStaged()' checked> 발행 대기중인 제안&nbsp;&nbsp;
            <input type="radio" name="rdo" id='rdoOpen' class='rdoBtn' onclick='setOpen()'> 열린 제안&nbsp;&nbsp;
            <input type="radio" name="rdo" id='rdoClosed' class='rdoBtn' onclick='setClosed()'> 닫힌 제안&nbsp;&nbsp;
            <input type="radio" name="rdo" id='rdoRecycle' class='rdoBtn' onclick='setRecycle()'> 제안 휴지통
            <div id='divStaged' style='display:;'>
                <!-- Pushed Issues -->
                <h3>현재 승인을 기다리는 제안을 열람중입니다.</h3>
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
                <h3>현재 열린 제안을 열람중입니다.</h3>
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
                <h3>현재 닫힌 제안을 열람중입니다.</h3>
                <input type="checkbox" id="chkPassedOnly" onchange="setPassedOnly();"> 통과된 건의만 보기
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

                                if($row['status'] == 2){
                                    echo "<tr class='non-passed'>";
                                    echo "<td>".$row['idx']."</td>";
                                    echo "<td class='preview'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                    echo "<td>".$row['open_datetime']."</td>";
                                    echo "</tr>";
                                }
                                else{
                                    echo "<tr><strong>";
                                    echo "<td>".$row['idx']."</td>";
                                    echo "<td class='preview'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
                                    echo "<td>".$row['open_datetime']."</td>";
                                    echo "</strong></tr>";
                                }
                            }
                        ?>
                    </tbody>
                </table>
            </div>
            <div id='divRecycle' style='display:none;'>
                <!-- deleted Issues -->
                <h3>현재 삭제 대기중 건의를 열람중입니다.</h3>
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

                            while(($row = mysqli_fetch_assoc($result['recycle']))){        
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
            <?php echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/GukwonKakaoChatManager/templates/bug_report.html"); ?>
        </div>
    </body>
</html>
