<?php
setcookie("dangnhap", "", time() - (86400 * 10),"/");
header('Location: index.php?page=login');
exit;
?>