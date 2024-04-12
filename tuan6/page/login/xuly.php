<?php
$email = $_POST["email"];
$password = $_POST["password"];
$id_user = $obj->kiemtradangnhap($email, $password);
if ($id_user != 0) 
{
    setcookie("dangnhap",$id_user, time() + (86400 * 10), "/");
    $user_name=$obj->tentaikhoan($id_user);
    echo '<script>alert("Chúc mừng '.$user_name.' đăng nhập thành công !");setTimeout(function(){window.location.href = "index.php?page=trangchu";}, 0);</script>';}
else
    echo "<script>alert('Sai email hoặc mật khẩu!')</script>";
?>

