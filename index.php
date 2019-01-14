<html>
<?php
#########################程序简介##########################
# Spam Message Classifiers
# time 2018.12.20
# author: liangfh
?>
<head>
    <title>垃圾短信识别</title>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
        body {background:#EAEDED;}
        ul {padding:0; margin:0;}
        li {list-style:none;}
        #container {margin: 0 auto; width: 80%;}
        a {color:#146fdf; text-decoration: none}
        a:hover {color: black; text-decoration: underline}
        #g_list {margin-top:60px; background:#fff;border-radius:4px}
        #g_u,#g_p {position:relative}
        #g_u {border-bottom:1px solid #eaeaea}
        .inputstyle {text-align:center;-webkit-tap-highlight-color:rgba(255,255,255,0); width:100%; height:100px;color:#000;border:2px solid #3366CC; background:0; font-size:24px;-webkit-appearance:none;line-height:normal; /* for non-ie */}
        #cjsubmit {margin-top:40px;margin-left:435px; width:200px; height:50px; color:#BC8F8F}
        .button {border:0px; width:200px; height:50px;color:white; background:#D94600; border-radius:4px; font-size:22px;}
        #notice {text-align:center; margin-top:60px; color:#246183; line-height:14px; font-size:14px; padding:15px 10px}
		
		#title {color:#146fdf;font-size:25px; text-align:center; font-family:"YouYuan"; font-weight:bold;margin-top:20px;margin-bottom:5px;}
		#closewindos {margin-top:60px; width:30%; height:30px; color:#146fdf}
		table {border:1px solid #eaeaed;}
		td {font-size:20px;border-bottom:1px solid #eaeaed; color:#246183}
	   .footer{position:absolute;bottom:10px;width:100%;height:10px;font-size:10px;}
    </style>
</head>
<body>
    <div id="container">
        <div id="title">垃圾短信识别</div>  
            <form method=post name="cf" target="" onSubmit=javascript:chkfs()>
                <ul  id="g_list">
                    <li  id="g_u">
                        <div  id="del_touch"  class="del_touch">
                            <span  id="del_u"  class="del_u"  style="display: none;"></span>
                        </div>
                        <textarea  id="u"  class="inputstyle"  name="pmessage"  autocomplete="off" ></textarea>
                    </li>
                </ul>
				</br>
            <center><input type=submit value=识别 id="shibie" class="button"><center></br>
            <script language=javascript>  
                function chkfs(){ 
                var frm = document.forms['cf']; 
				var ue=document.getElementById('shibie');
				ue.setAttribute("disabled", true);
				ue.value="识别中...";
				ue.style="background:#9D9D9D;";
                frm.action="";
                return true;  
                }
            </script>
        </form>
    </div>
	
	
	<div id="container">
        <center>
      
        <?php
        error_reporting(0);  //禁用错误报告
        #var_dump($_POST);
        if($_POST[pmessage]=="") 
			echo '</br> No Message'; 
        else{
            $output = shell_exec('python ./SPAM_CLASSIFY_online/Message_Classify.py'.' '.$_POST[pmessage]);
			//$output2 = shell_exec('python ./SPAM_CLASSIFY_online/Message_Classify.py'.' '.$_POST[pmessage]);
			echo "<font size=4 weight=bolder>短信内容:</font> $_POST[pmessage] </br></br>";  
			echo "$output";
			//$output2 = shell_exec('python3 ./SPAM_CLASSIFY_online/luoning.py'.' '.'哈哈哈');  
			//echo "$output2";
			//shell_exec("echo $output2 fgd >> mytext.txt");
			//echo "<font size=6 weight=700>GBDT: </font> <font color=#D2691E size=6 weight=700>$output2</font>"; 
        }
        ?>
		
      
        </center>
    </div>
	
	<div class="footer" align="center">Copyright @2018 liangfh</div>
</body>
</html>