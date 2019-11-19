<html>
    <head>
        <meta charset='utf-8'>
        <title>건의사항 관리</title>
        <link rel="stylesheet" href="./style/master.css">
        <?php
            echo file_get_contents($_SERVER['DOCUMENT_ROOT']."/default.html");
            include($_SERVER['DOCUMENT_ROOT']."/SuggestionViewer/functions/dbconn.php");

            $result['open'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 1");
            $result['closed'] = mysqli_query($conn, "SELECT * FROM suggestion WHERE status = 2 OR status = 4");
        ?>
        <script>
            function setOpen(){
                document.getElementById('divOpen').style.display = '';
                document.getElementById('divClosed').style.display = 'none';

                document.getElementById('btnOpen').style.display = 'none';
                document.getElementById('btnClose').style.display = '';
            }

            function setClosed(){
                document.getElementById('divOpen').style.display = 'none';
                document.getElementById('divClosed').style.display = '';

                document.getElementById('btnOpen').style.display = '';
                document.getElementById('btnClose').style.display = 'none';
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
        <div class='description'>
            <button class='toggleIssue' id='btnOpen' onclick='setOpen()' style='display:none;'> 열린 제안</button>
            <button class='toggleIssue' id="btnClose" onclick='setClosed()'> 닫힌 제안</button>
            <div id='divOpen'>
                <!-- Open Issues -->
                <h3>현재 열려있는 제안을 열람중입니다.</h3>
                <table>
                    <thead>
                        <tr>
                            <th class="idx">번호</th>
                            <th class="preView">내용 미리보기</th>
                            <th class="datetime">등록일</th>
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
                                echo "<td class='previewDescription'><a href='SuggestionViewer.php?idx=".$row['idx']."'>".$title."[".$row['num_signs']."]</a></td>";
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
                            <th class="idx">번호</th>
                            <th class="preview">내용 미리보기</th>
                            <th class="datetime">등록일</th>
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
        </div>
    </body>
</html>
