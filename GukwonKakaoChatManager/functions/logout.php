<?php
    session_destroy();
    header($_SERVER['DOCUMENT_ROOT']."/index.php");
?>