<html>
    <head>
        <meta charset="utf-8"/>
        <title>챗봇 관리자 등록</title>
        <link rel="stylesheet" href="/style/signin.css">
        <script>
            function SetErrorMessage(msg){
                var chk_result = document.getElementById("pwd_chk_result");
                chk_result.style = "color:red;";
                chk_result.innerHTML = msg;
                document.getElementById("submit").style.display = "none";
            }

            function Pass(){
                var chk_result = document.getElementById("pwd_chk_result");
                chk_result.innerHTML = "";
                document.getElementById("submit").style.display = "";
            }

            function IsInfoValid(){
                var id = document.getElementById("id");
                var pwd = document.getElementById("pwd");
                var pwd_chk = document.getElementById("pwd_chk");

                var num = pwd.value.search(/[0-9]/g);
                var eng = pwd.value.search(/[a-z]/ig);

                var num_character_type = 0;

                if(num > -1){
                    num_character_type += 1;
                }
                if(eng > -1){
                    num_character_type += 1;
                }

                if(id.value.length == 0){
                    SetErrorMessage("아이디를 입력하셔야 합니다.");
                }
                else if(num_character_type < 2){
                    SetErrorMessage("패스워드는 영문과 숫자를 반드시 포함해야 합니다.");
                }
                else if(pwd.value.length < 6){
                    SetErrorMessage("패스워드가 너무 짧습니다.");
                }
                else if(pwd.value.search(/\s/) != -1){
                    SetErrorMessage("패스워드에 공백이 있습니다.");
                }
                else if(pwd.value != pwd_chk.value){
                    SetErrorMessage("패스워드 입력창의 값과 패스워드 확인 입력창의 값이 다릅니다.");
                }
                else if(document.getElementById("nickname").value.length == 0){
                    SetErrorMessage("닉네임을 정해주세요.");
                }
                else{
                    Pass();
                }
            }
        </script>
    </head>
    <body>
        <div class="login_form">
            <form action="functions/signin.php" method="POST">
                <input type="text" id="id" name="id" placeholder="아이디" onchange="IsInfoValid();"><br>
                <input type="password" id="pwd" name="pwd" placeholder="패스워드" onchange="IsInfoValid();"><br>
                <input type="password" id="pwd_chk" name="pwd_chk" placeholder="패스워드 확인" onchange="IsInfoValid();"><br>
                <input type="text" name="auth_code" placeholder="가입 인증번호"><br>
                <br>
                <input type="text" id="nickname" name="nickname" placeholder="닉네임" onchange="IsInfoValid();"><br>
                <input type="submit" id="submit" class="btn" value="가입" style="display:none;">
            </form>
            <strong><span id="pwd_chk_result"></span></strong>
        </div>
    </body>
</html>